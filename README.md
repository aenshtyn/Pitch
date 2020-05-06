# Project Name
## 1MPitch (https://onemp.herokuapp.com)/


#### Built by

Mohamed Abdullahi  

## Description

This is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application.

## User Story
* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on s pitch they have viwed by giving it a upvote or a downvote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
*  Submit a pitch to a specific category of their choice.



## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

## Setup/Installation Requirements

* python3.7
* pip
* virtualenv


## Cloning
* In your terminal:

  $ git clone https://github.com/aenshtyn/Pitch/

  $ cd Pitch

## Running the Application
* Creating the virtual environment

        $ python3.7 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.7 -m pip install Flask
        $ python3.7 -m pip install Flask-Bootstrap
        $ python3.7 -m pip install Flask-Script

* To run the application, in your terminal:

        python3.7 manage.py server

## Testing the Application
* To run the tests for the class files:

        $ python3.7 manage.py tests


## Known Bugs

The pitches arent loading


## Technologies Used

* Python 3.7
* Flask
* Heroku

## Support and contact details

If you have any issues or questions you can contact me at demahom93@gmail.com

###### LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
