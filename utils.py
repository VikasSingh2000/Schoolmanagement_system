def is_admin(user):
    return user.is_authenticated and user.is_superuser

def is_teacher(user):
    return user.is_authenticated and hasattr(user, 'teacherextra')

def is_student(user):
    return user.is_authenticated and hasattr(user, 'studentextra')
