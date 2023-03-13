from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login
from datetime import datetime
from .models import UserTime
from django.http import HttpResponse
from .forms import PatientForm1
from .models import FoodTracker
import requests

# Define a function to Nutrient values from the api
def healthyHabits(request):
    if request.method == 'GET': #if request for 
        # API endpoint URL
        url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

        # API parameters
        api_key = '4cRkA9p31eDotiYwTWszYqbu8ww4a34KEPDlO4tf'# my api key
        query = request.GET.get('query')  # get the user's search query
        params = {
            'api_key': api_key,
            'generalSearchInput': query,
            'pageSize': 1,  # retrieve only the top search result
            'includeNutrition': True  # retrieve nutrient data
        }

        # make the API request
        response = requests.get(url, params=params)

        # parse the JSON response
        data = response.json()

        # extract the nutrient data
        nutrients = data['foods'][0]['foodNutrients']

        # pass the nutrient data to the template
        return render(request, 'website/healthyHabits.html', {'nutrients': nutrients})
    else:
        return render(request, 'website/healthyHabits.html')#call this if page is loaded without method
    

# Define a function to add a food item in the FoodTracker model
def add_food_item(request):
    if request.method == 'POST':
        user = request.POST['user']
        food_item = request.POST['food_item']
        food_tracker = FoodTracker(user=user, food_item=food_item)
        food_tracker.save()
        return redirect('food_tracker') # Redirect to the same page after food item added successfully
    else:
        return render(request, 'website/food_tracker.html')#same for this but food item is not updated
# Define a function to add user time in the UserTime model
def add_user_time(user_id):
    current_time = datetime.now()#get curent time
    new_user_time = UserTime(user_id=user_id, current_time=current_time)#update time in user time model
    new_user_time.save()#save time in db

def get_and_delete_user_time(request):
    user_id = request.user.username # get current user name
    user_time = UserTime.objects.filter(user_id=user_id).first() # find the usertime object in db
    if not user_time:#if not found update it now
        add_user_time(user_id=user_id)
        return HttpResponse('Tracking Started')# repose to start tracking of the fasting user
    saved_time = user_time.current_time #if found that means the user was already fasting so find the current time and return the total time fasted, can be implemented later
    user_time.delete()#delete the current user time object as the fast ended
    return saved_time #return the time

# Define a function to sign up a new user
def signup(request):
    if request.method == 'POST':#if form is submitted the check it
        form = UserRegisterForm(request.POST)#form extracted and saved in register model
        if form.is_valid():#check form validation
            form.save()#form saved in db 
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])#saving  new user info for authentication
            login(request,new_user)#login function t automate new user login
            return redirect("/")# goes to home page
    else:
        form = UserRegisterForm()# if signup page is loaded

    return render(request, 'registration/signup.html', {'form': form})# goes to signup page

# Define a function to get patient request and their probelm decription
def expertTalk(request):
    if request.method == 'POST':# if form is submitted 
        form = PatientForm1(request.POST)# form model is initiated
        if form.is_valid():#form is validated
            form.save() #form saved in db
            return redirect('expertTalk')#go back to orignal page
    else:
        form = PatientForm1()
    return render(request, 'website/expertTalk.html', {'form': form})#render normal page 

# Define a function to render home page
def welcome(request):
    return render(request,'website/home.html')
# Define a function to render diet chart page
def dietChart(request):
    return render(request,'website/dietChart.html')
# Define a function to show normal page wihout fasting or not logged in user
def monitorFast(request):
    return render(request,'website/monitorFast.html')
