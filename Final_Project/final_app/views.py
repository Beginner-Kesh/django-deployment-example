from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<em> Welcome!!</em>" )

def next(request):
    user_dict = {'insert_users':'Thanks for your patience!'}
    return render(request,'final_app/users1.html',context = user_dict)
