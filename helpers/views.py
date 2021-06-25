from django.shortcuts import render








# function for 404 errors
def handle_not_found(request, exception):
    return (render(request, 'not-found.html'))

def handle_server_error(request):
    return (render(request, 'server-error.html'))