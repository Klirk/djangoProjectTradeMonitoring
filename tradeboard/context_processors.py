def get_user(request):
    if request.user.is_authenticated:
        return {
            'username': request.user.username,
            'avatar': 'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y',
        }
    return {}
