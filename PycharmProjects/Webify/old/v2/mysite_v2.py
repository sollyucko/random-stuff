from dataclasses import field

from webify_v2 import *


class TaskTracker(Application, db='sqlite:///db.sqlite'):
    class User:
        username: str = field(metadata=dict(primary_key=True))
        password: Password
        email: Email

        def __check_permission__(self, permission_type: AccessType, permission_field: str, ctx: Context) -> bool:
            return (permission_type == AccessType.READ or permission_field != 'username') and ctx.user == self

    log_in, sign_up = LoginSignup(User)
    
    class Task:
        id: int = field(metadata=dict(primary_key=True, autoincrement=True))
        title: str
        description: Optional[str]
        is_complete: bool
        user: User
        
        def __check_permission__(self, permission_type: AccessType, permission_field: str, ctx: Context) -> bool:
            return ctx.user == self.user


application = TaskTracker()
