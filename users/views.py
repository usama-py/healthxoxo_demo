from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
# Define a function to login and authenticate user
def login_user(request):
    if request.method == 'POST':#if form is posted
        username= request.POST['username']#get username
        password = request.POST['password']#get password
        user = authenticate(username=username,password=password)#django authenticaton module
        if user is not None:# if existing user
            login(request,user)#login the user
            return redirect("/")#go to home page
        else:
            messages.success(request,("There was an error logging in"))#show error, might not work correctly
            return redirect('authenticate/login.html')# redirect to login page again
    else:
        return render(request,'authenticate/login.html')# normal login page 
# Define a function to add logout current user only available when a user is logged in
def logout_user(request):
    logout(request)#logout modeule of django is called
    messages.success(request,("You were logged out"))
    return redirect('home')#goes to home page