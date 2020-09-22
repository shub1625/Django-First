from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def relative(request):
    con_dict = {'text': 'hello world'}
    return render(request, 'relative.html', con_dict)


def other_page(request):
    return render(request, 'other_page.html')
