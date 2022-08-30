# PythonPersonalProject

# Introduction

This python repo is to learn to scrape data from a website

---

> Be sure to add that lovely star 😀 and fork it for your own copy

---

# Objectives

- A first try at learning how to scrape a website using python

---

# Who is this for?

- It's for anyone who wants to try web scraping in python

---

# Before using this repo fork and clone [Link](https://github.com/meera-ramesh19/PersonalProject)

- follow the instructions in that particular repo for deployment

---

# Packages/Dependencies used

bs4, requests, pandas, sqlalchemy, psycopg2

---

# Install all the dependencies or python or pip used for development via Terminal

downlaod python from python.org

---

# Things to add

- Create a `requirements.txt` file to add all the dependencies/packages needed for heroku deployment

  - pip freeze > requirements.txt
    pip freeze outputs the package and its version installed in the current environment in the form of a configuration file that can be used with pip install -r.

  -Create a `runtime.txt` file to specify the version of python installed for heroku deployment

  - python-(your version of python)

  It specifies the python version for all the packages incase there is some descrepency in the packages used

  - Add a `Procfile` to specify the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, including: Your app's web server. Multiple types of worker processes.

  - Deploy the app on heroku following this [link](https://devcenter.heroku.com/articles/getting-started-with-python)

  - Once it is deployed follow these steps to connect to a database

  - To connect python to a node db

    - heroku addons:attach <postgres_instance_name> -a <python_app_name>

  - To run python script

    - heroku ps:scale web=1

  - To check database has data
    - heroku pr:psql <database_url>
    - select \* from historical_data(table name)

  ***

Have fun testing and improving it! 😎
