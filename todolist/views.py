from email import message
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from todolist.forms import InputForm
import datetime

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Register succesful!'
                )
            return redirect('todolist:login')

    context = { 'form':form }
    return render(
        request,
        'register.html',
        context
        )

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username = username,
            password = password
            )

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse('todolist:show_todolist')
                )
            response.set_cookie(
                'username',
                username
            )
            response.set_cookie(
                'last_login',
                str(datetime.datetime.now())
                )
            return response

        else:
            messages.info(
                request,
                'Invalid username or password'
                )

    return render(
        request,
        'login.html',
        {}
        )

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(
        reverse('todolist:login')
        )
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user = request.user)
    context = {
        'username': request.COOKIES['username'],
        'to_do_list': data,
        'last_login': request.COOKIES['last_login']
        }

    return render(
        request,
        "todolist.html",
        context
        )

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = InputForm()

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return HttpResponseRedirect(
                reverse('todolist:show_todolist')
                )
        else:
            message.info(
                request,
                'Oops! Something went wrong.'
            )

    context = { 'form':form }
    return render(
        request,
        'create_task.html',
        context
        )

@login_required(login_url='/todolist/login/')
def task_status(request, status_key):
    task = Task.objects.get(
        user = request.user,
        pk = status_key
        )
    task.is_finished = not task.is_finished
    task.save()
    return redirect(
        'todolist:show_todolist'
        )

@login_required(login_url='/todolist/login/')
def delete_task(request, delete_key):
    task = Task.objects.get(
        user = request.user,
        pk = delete_key
        )
    task.delete()
    return redirect(
        'todolist:show_todolist'
        )