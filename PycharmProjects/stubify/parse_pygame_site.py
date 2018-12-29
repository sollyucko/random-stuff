from typing import Iterable

from lxml import etree

from generate_stub_file import generate_stub, Named, Function
from requests import get


def load_page(page_name: str) -> str:
    return get(f'https://www.pygame.org/docs/ref/{page_name}.html').text


def parse_signature(signature: str):
    return signature


def parse_page(page_data: str) -> Iterable[Named]:
    tree = etree.fromstring(page_data)
    title_nodes = tree.xpath('//dt[@title]')
    print(title_nodes)

    properties = (
        (
            title_node.xpath('./[@class="descname"]')[0].text,
            (
                signature_node.text
                for signature_node
                in title_node.xpath('.//[class="signature"]')
            )
        )
        for title_node
        in title_nodes
    )

    return (
        (
            Function(title, map(parse_signature, signatures))
        )
        for title, signatures
        in properties
    )


def generate_pygame_stub(page: str) -> str:
    return generate_stub(parse_page(load_page(page)))


def create_pygame_stub(page: str) -> None:
    with open(page + '.py', 'w') as f:
        f.write(generate_pygame_stub(page))


if __name__ == '__main__':
    create_pygame_stub('color')
