# blog-app-with-user-captcha-verification-in-django
    
    This is simple blogging aplication where user can apply CRUD operation on his blogs and can see other user's blogs. 

## Project look:

<p align="center" width="100%">
    <img src="https://github.com/dwipalshrirao/blog-app-with-user-captcha-verification-in-django/blob/main/project_look.gif"> 
</p>

## Features of project:


1. **Register user with captcha verification**. user need to solve arithematic captcha before get Register.
<p align="center" width="100%">
    <img src="https://github.com/dwipalshrirao/blog-app-with-user-captcha-verification-in-django/blob/main/screenshot.png"> 
</p>

2. **CRUD operation on blogs**. user can create, update, delete and view his own blogs.

3. **Search other users**. user can search other users and can see thier blog which are in 'public' status.

4. **hide blogs from other users**. if user make blog status to 'private' then other users can't see these blogs.


  ## Technology Used:

  #### Backend

  * Python, Django
  * SQLite3
  #### Frontend
  * HTML
  * CSS

  ### Run the following commands to get started your project:

  1. download project

  ```
  git clone https://github.com/dwipalshrirao/blog-app-with-user-captcha-verification-in-django.git

  cd blog-app-with-user-captcha-verification-in-django
  ```


  2. run command below

  ```python
  python3 manage.py makemigrations

  python3 manage.py migrate

  python3 manage.py runserver
  ```

  if you are using windows then:
  
  ```python
  python manage.py makemigrations

  python manage.py migrate

  python manage.py runserver
```

  if this is helpful please give star to repo. 
  thank you.
