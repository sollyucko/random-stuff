from typing import NamedTuple, Type, TypeVar

from numpy import cos, matrix, pi, sin

tau = 2 * pi

T = TypeVar('T', bound='Point')


class Point(NamedTuple):
    x: float
    y: float
    z: float
    
    def to_matrix(self) -> matrix:
        return matrix([[self.x, self.y, self.z]])
    
    @classmethod
    def from_matrix(cls: Type[T], mat: matrix) -> T:
        return cls(*mat.flatten().tolist()[0])
    
    def apply_matrix(self, mat: matrix) -> 'Point':
        return self.from_matrix(self.to_matrix() * mat)
    
    def rotate_x(self, radians: float) -> 'Point':
        return self.apply_matrix(matrix([[1, 0, 0],
                                         [0, cos(radians), -sin(radians)],
                                         [0, sin(radians), cos(radians)]]))
    
    def rotate_y(self, radians: float):
        return self.apply_matrix(matrix([[cos(radians), 0, sin(radians)],
                                         [0, 1, 0],
                                         [-sin(radians), 0, cos(radians)]]))
    
    def rotate_z(self, radians: float):
        return self.apply_matrix(matrix([[cos(radians), -sin(radians), 0],
                                         [sin(radians), cos(radians), 0],
                                         [0, 0, 1]]))


if __name__ == '__main__':
    print(Point(1, 2, 3).rotate_z(1).rotate_x(2))
    print(Point(1, 2, 3).rotate_x(2).rotate_z(1))
    print(Point(1, 2, 3).rotate_x(1).rotate_y(1).rotate_x(-1).rotate_y(-1))
    print(Point(1, 2, 3).rotate_x(1).rotate_x(-1))
