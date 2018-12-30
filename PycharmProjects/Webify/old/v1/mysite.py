from attr import dataclass
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from webify import BranchEndpoint, HtmlEndpoint, RestEndpoint

application: BranchEndpoint = BranchEndpoint()
api: BranchEndpoint = application.endpoint('api')(BranchEndpoint())

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


@dataclass
class Task(Base):
    id: int
    title: str
    description: str
    is_complete: bool
    
    __tablename__ = 'tasks'


application.endpoint('tasks')(HtmlEndpoint(Task))
api.endpoint('tasks')(RestEndpoint(Task))
