# Instagram clone

 The instagram clone is an implementation of a close feel of the Instagram application, by the flow of the functionality.
#### By **Derrick** created on, May 19th 2018 

## Description
The application allows users to register to the application and once they are authenticated, they can post their wanted photo posts followed by small description, the user also gains a free profile
whereby he/she can view all the posts made, he can view the people following or them he is following, 
The user can also edit his profile and do basic authentication management like changing the password etc.

## Behaviour

### Authentication
+ The authentication system is build using django core library.
+ The user visits the application via the link in any browser or phone and is redirected to register or login.
+ If the user din't have the account, A registration form has to be filled out and then redirected to login.
+ After successfully login, the user is again redirected to the dashboard where he can view all the posts.

### Profile
+ The user has a profile where he/she can view all the posts he/she made and the people following or them he's following.
+ The user also can edit the profile as wished.
+ The user can also change his credentials.

### Post and Commenting system
+ Each photo post has a comment form where the user can comment.
+ Each post shows the number of likes and comments.
+ Once a post is clicked, a modal popsup with more details about that photo.


## Development and Setup.

### prerequisites

+ Python 3.6 should be installed
+ django 1.11
+ install other packages ```provided in the requirements.txt file```

### Running the application.
+ Visit this link to view on any browser.

### Installation.
+ Ensure python3.6 is installed.
+ Clone the repository  ```git clone <repo url>  ```
+ create a virtual environment ```virtualenv <envname>``` and activate ```source <envname>/bin/activate```
+ Install the required packages ``` pip3 install -r requirements.txt```
+ Create a postgresql database.
- open the psql terminal by typing ```psql -h localhost -U <username>```
- Once on the psql terminal create the database ```CREATE DATABASE <dbname>``
- Quit the shell ```\q```
+ Once the database is setup, make migrations, this creates database schemas for the application  ```python manage.py makemigrations```
+ Then create the actual database tables by ```python manage.py migrate```
+ Start the application by ```python manage.py runserver ``` and open ```http://127.0.0.1:8000``` in the browser.

## Technology Used
+ Python3.6
+ Django 1.11
+ git version control
+ heroku cli

## Test Driven Development
Testing was done using python inbuild test tool called **unittest** to test database and form models.


## Further help
To get Further help you can visit the official [python](https://www.python.org/) and [django](http://djangoproject.com/ ) documentation.

## Licence
MIT (c) 2017 [muriithi derrick](https://github.com/muriithiderro)