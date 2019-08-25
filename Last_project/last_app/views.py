from django.shortcuts import render
from last_app.models import User

# Create your views here.

def index(request):
    return render(request,'last_app/user_list.html')


def users(request):

    user_list = User.objects.order_by('first_name')
    userdict = {'users_range':user_list}
    return render(request,'last_app/new_users.html',context= userdict)
