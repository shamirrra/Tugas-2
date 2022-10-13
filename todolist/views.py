from email import message
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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
@csrf_exempt
def task_status(request, status_key):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=status_key, user=request.user)
        task.is_finished = not task.is_finished
        task.save()
        return JsonResponse({'error': False})
    #task = Task.objects.get(
        #user = request.user,
        #pk = status_key
        #)
    #task.is_finished = not task.is_finished
    #task.save()
    #return redirect(
    #    'todolist:show_todolist'

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_task(request, delete_key):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=delete_key, user=request.user)
        task.is_finished = not task.is_finished
        task.delete()
        return JsonResponse({'error': False})
    #task = Task.objects.get(
    #    user = request.user,
    #    pk = delete_key
    #    )
    #task.delete()
    #return redirect(
    #    'todolist:show_todolist'
    #    )

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data = Task.objects.filter( user=request.user ).order_by('id')
    return HttpResponse(serializers.serialize('json', data),
        content_type = 'application/json')

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task_ajax(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task_item = Task.objects.create(
            user=request.user, 
            title=title, 
            description=description,
        )
        task_item.save()
        return JsonResponse(
                {"instance": "Task successfully added!"}, status=200
        )