from django.http import HttpResponse

def users_view(request):
    return HttpResponse("Hello, users!")