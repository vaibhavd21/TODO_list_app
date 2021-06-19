from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as LogIn,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import TODOForm
from .models import TODOModel


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        all_todos = TODOModel.objects.filter(user = user).order_by('-created')
        incomplete_todo = all_todos.filter(status = 'P').count()
        return render(request,'index.html',context={'form':form,'todos':all_todos,'incomplete':incomplete_todo})
    else:
        return redirect('login')

def login(request):
    if request.method == 'GET':
        auth_form = AuthenticationForm()
        data = {
            'form' : auth_form
        }
        print("in get")
        return render(request,'login.html',data)
    else:
        print("in post")
        auth_form = AuthenticationForm(data = request.POST)   #takes kargs as parameter
        data = {
            'form' : auth_form
        }
        if auth_form.is_valid():
            username = auth_form.cleaned_data.get('username')
            password = auth_form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            print("valid user found")
            print(user)
            if user is not None:
                LogIn(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',data)
        else:
            print("invadid form found")
            return render(request,'login.html',data)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        data = {
            "form" : form
        }
        
        return render(request,'signup.html',context = data)

    else:
        form_values = UserCreationForm(request.POST)
        data = {
            "form" : form_values 
            }
        if form_values.is_valid():
            user = form_values.save()
            if user is not None:
                return redirect('home')
            #return HttpResponse("Valid")
        else:
            return render(request,'signup.html',context = data)



def LogOut(request):
    logout(request)
    return redirect('login')



def AddTodo(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user = request.user

        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request,'index.html',context={'form':form})
    else:
        return redirect('login')



def delete_todo(request, id_of_todo):
    TODOModel.objects.get(pk = id_of_todo).delete()
    return redirect('home')


def ChangeStatus(request, id_of_todo, update_status_mark):
    print(update_status_mark)
    todo_to_change = TODOModel.objects.get(pk = id_of_todo)
    todo_to_change.status = update_status_mark
    todo_to_change.save()
    return redirect('home')