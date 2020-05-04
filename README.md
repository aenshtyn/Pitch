# Project Name
## 1MPitch
 https://onemp.herokuapp.com


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
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

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

finalizing on the app before deployment


## Technologies Used

* Python 3.7
* Flask
* Heroku

## Support and contact details

If you have any issues or questions you can contact me at demahom93@gmail.com

###### LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
