
from django.http import HttpResponse
# Create your views here.
def index(resquest):
    return HttpResponse("Index page")

def hello(request, id):
    result= id+33*5
    print(type(result))
    return HttpResponse("<h1> %s is the best programmer in the world!</h1>" %result)

def about(request):
    return HttpResponse("About")
