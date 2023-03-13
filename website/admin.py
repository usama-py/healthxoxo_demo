from django.contrib import admin
# Register your models here.
# Importing the required models for the admin panel
from .models import UserTime, Patient1, FoodTracker

# Defining the UserTimeAdmin class for customizing the UserTime model in the admin panel
class UserTimeAdmin(admin.ModelAdmin):
    # Specifying the fields to display in the UserTime model list
    list_display = ('user_id', 'current_time')

# Registering the FoodTracker model with the admin panel
admin.site.register(FoodTracker)

# Registering the UserTime model with the admin panel and applying the UserTimeAdmin class customization
admin.site.register(UserTime, UserTimeAdmin)

# Registering the Patient1 model with the admin panel
admin.site.register(Patient1)
