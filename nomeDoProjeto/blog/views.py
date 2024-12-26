from django.http import HttpResponse
from blog.data import posts
#from django.shortcuts import render

# Create your views here.
def home(request, id):
    print('post', id)

    context = {
        #'text': 'Olá blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )