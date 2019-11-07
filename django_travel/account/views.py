from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect(reverse('travel:index'))
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('travel:index'))
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # print("Username already taken")
                messages.error(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
                
        else:
            print('Password not matching')
            messages.warning(request,'PASSWORD NOT MATCHING')
            # messages.error()
            return redirect('register')
        return redirect('/travel')
    else:
        return render(request,'register.html')