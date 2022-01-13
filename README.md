Purpose:

I created this repo to serve as a reproducable starter template to accelerate the development process for standard
websites and to serve as a base template for more complex websites and web applications. The aim was to include as many
production ready configurations as possible. Alongside that, I have made use of best practices regarding seperation of
concerns, security, project structure and naming conventions.

Requirements:

This template makes use of python 3 and has been tested for usage with python 3.8 to 3.10. While
Docker is not strictly required, it is strongly recommended as it allows for reproducable results in both development
and production environments. All further dependencies are installed through the install.py file.

Getting Started:

1) clone repository
2) Run install.sh

Install

1) create virtual environment
2) install all dependencies
3) run setup.py which will set environment variables for development and create an ENV for django-secret_key
4) run the standard make migrations to create database tables
5) migrate those changes to your database tables
6) run the create superuser script

Settings

- Create base settings file which will import the settings from either production or development depending on the
  ENV_NAME.

Views

- using class based views