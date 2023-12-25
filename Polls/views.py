from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,User
from .form import UserCreateForm
# Create your views here.
def index(request):
    obj=Question.objects.get(id=4)
    context={
        'question':obj,
    }
    return render(request,'html/index.html',context)
def user(request):
    if request.method=="POST":
        form=UserCreateForm(request.POST)
        if form.is_valid(): 
            user_name=form.cleaned_data['name']
            user_email=form.cleaned_data['email']
            user_password=form.cleaned_data['password']

            print(user_name + user_email+user_password)
            check_email=User.objects.filter(email=user_email)
            # print(type(check_email))
            if(check_email.exists()):
                # print("Exits")
                return HttpResponse("Email already used")
            else: 
                new_user=User.objects.create(name=user_name,email=user_email,password=user_password)
                new_user.save()
                return HttpResponse('Student Created')


    context={
        "form":UserCreateForm()
    }
    return render(request,'html/note.html',context)