from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from contacts.models import Contact
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials. Try again.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
def logout(request):
    if request.method =="POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect('index')
    else:
        messages.error(request, "You have to login first")
        return redirect("login")
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username is taken!")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email is being used!")
                    return redirect('register')
                else:
                    newuser = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    newuser.save()
                    messages.success(request,"You are now registered and can now log in")
                    return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    user_inquiries = Contact.objects.order_by('contact_date').filter(user_id=request.user.id)
    context = {
        'inquiries': user_inquiries
    }
    return render(request, 'accounts/dashboard.html', context)