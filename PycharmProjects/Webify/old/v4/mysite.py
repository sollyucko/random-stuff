from __future__ import annotations

from dataclasses import field
from enum import Enum

from webify.orm.datatypes import Email, Password

# noinspection PyArgumentList
PermissionType = Enum('PermissionType', 'READ, READ_WRITE, ALL', module=__name__, qualname='PermissionType')

# noinspection PyArgumentList
ActionType = Enum('ActionType', 'READ, WRITE, CREATE', module=__name__, qualname='ActionType')


class TaskTracker(WebApp, db='sqlite:///db.sqlite'):
    class User:
        username: str
        password: Password
        confirmed_email: Optional[Email]
        current_email: Email
        
        def __check_access__(self, action: Action, context: Context) -> Union[bool, Type[NotImplemented]]:
            if context.user is not None and context.user.access_level == AccessLevel.ADMIN:
                return True
            
            if context.user == self:
                return True
            
            return {
                ActionType.CREATE: True,
                ActionType.READ: False,
                ActionType.WRITE: False,
            }.get(action.type, NotImplemented)
    
    auth = Auth(User)
    
    class Task:
        id: int
        title: str
        owner: User
        
        is_complete: bool
        
        def __check_access__(self, action: Action, context: Context) -> Union[bool, Type[NotImplemented]]:
            if context.user is not None and context.user.access_level == AccessLevel.ADMIN:
                return True
            
            if context.user == self.owner:
                return True
            
            return {
                ActionType.CREATE: False,
                ActionType.READ: False,
                ActionType.WRITE: False
            }.get(action.type, NotImplemented)
    
    class TaskAccessLevel:
        user: User = field(metadata={'primary_key': True})
        task: Task = field(metadata={'primary_key': True})
        permission_type: PermissionType
        indirection_level: int = 0
