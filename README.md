# quiz-app
It is simple django based quiz app.

## Snaps of project
![1](https://imgur.com/a/uqGnF7R)
![2](https://imgur.com/a/iV8M8su)
![3](https://imgur.com/a/qVU5Npa)
![4](https://imgur.com/a/iyo7BQ2)
![5](https://imgur.com/a/ntcPJwl)

# Instructions
1) ### Installations
  Make sure to have python version 3 install on you pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `https://github.com/Thposbsmt/quiz-app.git`<br>
  `cd quiz_app`
  
2) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`
  
3) ### Create superuser
  To create super user run. <br>
  `python manage.py createsuperuser` <br>
  After running this command it will ask for username, password.
  You can access admin panel from `localhost:8000/admin/`

4) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 
