from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def some_url(request):
    return HttpResponse("Some_url 구현하기")