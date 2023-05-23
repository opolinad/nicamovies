# Nicamovies

## Install

### Virtual environment

To install the project (from scratch), the first thing to do is to create a virtual environment. This is like a small computer within the system and it is done in order to prevent any interference with what will be worked on and installed. To create this environment, you should go to the directory where you want to work and execute the following command:

    python -m venv virtualEnvironmentName

By default, the virtual environment is named **env**, so the command would be:

    python -m venv env

### Activate virtual envioronment

From the folder where the virtual environment was created, execute the following command:

    source virtualEnvironmentName/Scripts/activate

Given that in this example the virtual environment was named env, the command would be:

    source env/Scripts/activate

If the virtual environment is active, you should see (env) above the directory name.

For further information on how to create and activate virtual environments in differents OS, please visit [Creation of virtual environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

### Install dependencies

To install all the components of this project (once the virtual environment is active), you can make use of the requirements.txt file (which contains all the dependencies and their versions). To do this, you should run the following command:

    pip install -r requirements.txt

## Run migrations

For the project to work correctly, it is necessary to run migrations. To do this, execute the following command:

    python manage.py migrate

This command generates the models in the database.

*In this case the DB is already in the directory and is preloaded with some information (user: test@mail.com, password:1234578Aa), so migrations must NOT be run*

## Starting the Server

The program runs on a server, so in order for the program to run, it is necessary to start the server (this is known as starting the server). In Django, the server is started as follows (this command needs to be executed from the same directory where the manage.py file is located, in this case, it is inside the backend/nicamovies folder, so you need to navigate to that directory to run it):

    python manage.py runserver