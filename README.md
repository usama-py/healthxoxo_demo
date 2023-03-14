# healthxoxo_demo

video link of running app:

https://drive.google.com/file/d/1IVwOEhA833bvtVVqqpSsI3qJ9JOF9nx1/view?usp=share_link

production link of running app:

usama98.pythonanywhere.com


Health xoxo assignment app

Health xoxo demo app for assignment

Navigate to the project directory:

Open the terminal/command prompt and navigate to the directory where the project has been cloned. You can use the cd command to change directories.

Create a virtual environment:
P.S. NO NEED TO CREATE VIRTUAL ENV IF MY GIT ENV WORKS PROPERLY, FIRST TRY ACTIVATING THE ENV WHICH COMES WITH THIS PROJECT
python -m venv env

Activate the virtual environment:

If you're on Windows, use the following command instead:

use this command exactly, this is my env: myenv\Scripts\activate.bat
if this doesn't work then create your own env with: python -m venv env

To activate the virtual environment ON MAC, run the following command:

source myenv/bin/activate


Install dependencies:

Once the virtual environment is activated, install the project's dependencies by running the following command:

pip install -r requirements.txt

This will install all the required packages and libraries that the project needs.

Run the project:

Once the dependencies are installed, you can run the project by running the following command:

python manage.py runserver

This will start the development server at http://127.0.0.1:8000/.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

WORKING LINKS ARE:

HOME PAGE:
TRIED TO IMPLEMENT EXACTLY
http://127.0.0.1:8000/

DIET CHART:
MADE FOR REFERENCE TO OTHER PAGES
http://127.0.0.1:8000/dietChart/

FOOD TRACKER:
UPADTES USER FOOD INTAKE INFO TO DB
http://127.0.0.1:8000/food_tracker/

MONITOR FASTING:
TAKES USER TIME AND CALCULATES IT TILL USER CLICKS THE BUTTON ONCE AGAIN TO RECORD FASTING TIME
http://127.0.0.1:8000/monitorFast/

EXPERT TALK:
GETS USER INFO AND DESCRIPTION OF PROBLEM TO BE ABLE TO CONTACT AN EXPERT ON IT
http://127.0.0.1:8000/expertTalk/

HEALTHY HABITS:
TAKES THE USER FOOD INFO AND GIVES THE VALUES OF THE NUTRIENTS WITH THE HELP OF AN ONLINE "USDA Food Composition Databases API", CAN HELP IN INTAKE OF HEALTHY FOOD
http://127.0.0.1:8000/healthyHabits/
