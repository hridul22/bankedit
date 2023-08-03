from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import NewPageForm, RegistrationForm

from bank_app.models import District, Reginfo


def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})

# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#
#         if user is not None:
#             auth.login(request,user)
#             return redirect('bank_app:get_form')
#         else:
#             messages.info(request,"invalid entry")
#             return redirect('login')
#     return render(request,"login.html")
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         if username and password:  # Check if the fields are not empty
#             user = auth.authenticate(username=username, password=password)
#
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('/')
#             else:
#                 messages.error(request, 'Invalid username or password.')
#
#     return render(request, 'login.html')




# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             return redirect('bank_app:login')
#
#     else:
#         form = RegistrationForm()
#
#     return render(request, 'register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect('bank_app:register')

            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('bank_app:login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('bank_app:get')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Username and password are required.')

    return render(request, 'login.html')







def new_page(request):
    districts = District.objects.all()

    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted.')
            return redirect('bank_app:new_page')
        else:
            return redirect('bank_app:new_page')
    return render(request, 'new_page.html', {'districts': districts})


def logout(request):
    return redirect('bank_app:home')


def get(request):
    return render(request,'get_form.html')

def success(request):
    return render(request,'success.html')