from functools import wraps

# Define some roles
ROLES = ['admin', 'editor', 'viewer']

# Simple User class with roles
class User:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles  # list of roles assigned to the user

# Decorator to enforce role access
def requires_role(required_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not isinstance(required_roles, list):
                roles_to_check = [required_roles]
            else:
                roles_to_check = required_roles

            # Check if user has any of the required roles
            if any(role in user.roles for role in roles_to_check):
                return func(user, *args, **kwargs)
            else:
                return f"Access denied for user '{user.username}'. Required role(s): {roles_to_check}"
        return wrapper
    return decorator

# Example functions with role restrictions

@requires_role('admin')
def delete_user(user, username_to_delete):
    return f"User '{username_to_delete}' deleted by '{user.username}'."

@requires_role(['admin', 'editor'])
def edit_article(user, article_id):
    return f"User '{user.username}' edited article {article_id}."

@requires_role(['admin', 'editor', 'viewer'])
def view_article(user, article_id):
    return f"User '{user.username}' viewed article {article_id}."

# Example usage
if __name__ == "__main__":
    admin_user = User("alice", ["admin"])
    editor_user = User("bob", ["editor"])
    viewer_user = User("charlie", ["viewer"])
    guest_user = User("eve", [])

    print(delete_user(admin_user, "bob"))       # Allowed
    print(delete_user(editor_user, "charlie"))  # Denied
    print(edit_article(editor_user, 123))       # Allowed
    print(edit_article(viewer_user, 123))       # Denied
    print(view_article(viewer_user, 123))       # Allowed
    print(view_article(guest_user, 123))        # Denied
