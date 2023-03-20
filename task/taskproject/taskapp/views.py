from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import District, branch


# Create your views here.
def getdata(request):
    deptcontext = District.objects.all()
    branchcontext = branch.objects.all()
    if request.method == 'POST':

        return redirect('/completed')

    return render(request, "personprofile.html", {'District': deptcontext, 'branch': branchcontext})


def home(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/getdata')
        else:
            messages.info(request, 'invalid login')
            return redirect('/loginn')

    return render(request, 'loginn.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password1']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('/registerr')

            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save
                return redirect('/loginn')

        else:
            messages.info(request, 'password miss match')
            return redirect('/registerr')
        return redirect('/loginn')

    return render(request, "registerr.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def completed(request):
    return render(request, "completed.html")
