from django.http import HttpResponse
def index(request):
    return HttpResponse("<a href="www.google.com">Google</a>
<a href="www.youtube.com">Youtube</a>")

def about(request):
    return HttpResponse("about this webpage")

def home(request):
    return HttpResponse("Welcome to the home page of this website")