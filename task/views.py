from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Employee, Task, User

# Create your views here.


def index(request):
    return HttpResponse('index')


def login_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'task/login.html')
    return render(request, 'task/login.html')


def logout_out(request):
    logout(request)
    return redirect('login')
    # return HttpResponse("success")


def create_employee(request):
    task_list = Task.objects.all()
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
        )
        Employee.objects.create(
            user=user,
            name=user.username,
            designation=request.POST['designation'],
            task=request.POST['task'],
        )
        return HttpResponse('Employee Created')
    return render(request, 'task/create-employee.html', {'task_list': task_list})


@login_required(login_url='login')
def give_task(request):
    user = request.user
    employee = Employee.objects.get(name=user.username)
    employee_list = Employee.objects.filter(designation='employee')
    task_list = Task.objects.exclude(status='Done')

    if employee.designation == 'TL':
        if request.method == 'POST':
            worker = request.POST['employee']
            # import ipdb; ipdb.set_trace()
            worker = Employee.objects.get(id=worker)
            print(worker.designation)
            task = Task.objects.get(id=request.POST['task'])

            worker.task = task
            worker.save()
            # print(worker)
            return HttpResponseRedirect(reverse('sample', args=(worker.id, )))
        return render(request, 'task/give-task.html', {'employee': employee, 'employee_list': employee_list, 'task_list': task_list})
    return HttpResponseRedirect(reverse('employee_task'))


def sample(request, worker_id):
    employee = Employee.objects.get(id=worker_id)
    return render(request, 'task/employeetaskdetails.html', {'employee': employee})


def employee_task(request):
    employee = Employee.objects.get(name=request.user.username)
    task = employee.task
    if request.method == 'POST':
        task.status = request.POST['status']
        
        task.save()
        return HttpResponseRedirect(reverse('employee_task'))
    return render(request, 'task/employeetask.html', {'employee': employee, 'task': task})
