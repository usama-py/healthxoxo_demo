from django.db import models
# Create your models here.
# Defining the UserTime model with two fields, user_id and current_time
class UserTime(models.Model):
    user_id = models.CharField(max_length=50)
    current_time = models.DateTimeField(auto_now_add=True)

# Defining the Patient model with four fields, full name, email, phone, and desc
class Patient1(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)

    # Method to return a string representation of the model instance
    def __str__(self):
        return self.full_name

# Defining the FoodTracker model with three fields, user, food_item, and date_added
class FoodTracker(models.Model):
    user = models.CharField(max_length=50)
    food_item = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    # Method to return a string representation of the model instance
    def __str__(self):
        return f"{self.user} - {self.food_item}"
