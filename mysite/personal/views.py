from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {"contents":["If u like to contact me, please send a mail at ", "himanshus096@gmail.com"]})
