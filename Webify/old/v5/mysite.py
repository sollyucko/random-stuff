from __future__ import annotations

from dataclasses import field
from enum import Enum
from sys import argv
from typing import Optional, Type, Union
from wsgiref.simple_server import make_server

from webify import Action, Context, CreateAction, ReadAction, WebApp, WriteAction, create_auth
from webify.db import DBRow
from webify.db.types import Email, Password

# noinspection PyArgumentList
PermissionType = Enum('PermissionType', 'READ, READ_WRITE, ALL', module=__name__, qualname='PermissionType')
# noinspection PyArgumentList
ActionType = Enum('ActionType', 'READ, WRITE, CREATE', module=__name__, qualname='ActionType')
# noinspection PyArgumentList
AccessLevel = Enum('AccessLevel', 'NORMAL, ADMIN')


class TaskTracker(WebApp, db='sqlite:///db.sqlite'):
    class User(BaseUser, DBRow):
        confirmed_email: Optional[Email]
        current_email: Email
        
        def __check_access__(self, action: Action, context: Context) -> Union[bool, Type[NotImplemented]]:
            if context.user is not None and context.user.access_level == AccessLevel.ADMIN:
                return True
            
            if context.user == self:
                return True
            
            if isinstance(action, ReadAction):
                return False
            elif isinstance(action, WriteAction):
                return False
            elif isinstance(action, CreateAction):
                return True
            else:
                return NotImplemented
    
    log_in, sign_up = create_auth(User)
    
    class Task(DBRow):
        id: int
        title: str
        owner: TaskTracker.User
        is_complete: bool
        
        def __check_access__(self, action: Action, context: Context) -> Union[bool, Type[NotImplemented]]:
            if context.user is not None and context.user.access_level == AccessLevel.ADMIN:
                return True
            
            if context.user == self.owner:
                return True
            
            if isinstance(action, ReadAction):
                return False
            elif isinstance(action, WriteAction):
                return False
            elif isinstance(action, CreateAction):
                return False
            else:
                return NotImplemented
    
    class TaskAccessLevel(DBRow, multiple_primary_keys=True):
        user: TaskTracker.User = field(metadata={'primary_key': True})
        task: TaskTracker.Task = field(metadata={'primary_key': True})
        permission_type: PermissionType
        indirection_level: int = 0


def main():
    host, port = argv[1].split(':')
    
    with make_server(host, int(port), TaskTracker()) as server:
        server.serve_forever()


if __name__ == '__main__':
    main()
