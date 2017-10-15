from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,'app2/app2main.html')


def other (request):
    return render(request,'app2/other.html')


def relative (request):
    return render(request,'app2/relitave_url_templates.html')
