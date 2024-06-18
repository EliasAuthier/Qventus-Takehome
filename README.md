# Qventus-Takehome
Elías Authier's approach to Qventu's take home challenge, as part of their interview process.

Steps to run the project:

Create and move to a directory for our project. In my case I will be using /home/eauthier/qventus

> mkdir /home/eauthier
> mkdir /home/eauthier/qventus
> cd /home/eauthier/qventus


Create a Database Server for our API to use. In this case, I have chosen a 
simple Dockerized MariaDB.

> docker run --name mariadb-server -e MYSQL_ROOT_PASSWORD=r00t -e MYSQL_USER=eauthier -e MYSQL_PASSWORD=eauthier -v /home/eauthier/qventus/docker_volume:/var/lib/mysql -p 3306:3306 -d docker.io/library/mariadb:10.3

Create a Database for the API to use. In this case I have chosen a basic one named "qventus"

> docker exec -it mariadb-server mariadb -u eauthier -peauthier
> CREATE DATABASE qventus;
> exit;

Let's also install the mariadb-cli, needed by Django in order to stablish sessions with the DATABASE

> sudo apt install mariadb-client-core-10.6

Create and activate a Virtual Environment to run the project, using Python 3.11.

>  virtualenv -p=python3.11 venv
> . venv/bin/activate

Note: More installations might be needed to run the application depending on your OS. Feel free to install them as required.

Now, clone the repository with the project

> git clone https://github.com/EliasAuthier/qventus-takehome.git

This should have created a qventus_takehome directory. Lets move inside it.

> cd qventus_takehome

A .env file has been created, in order to import configurations. You can easily create a new one by creating a .env from the .env.sample file in the same location

> cp qventus_takehome/.env.sample qventus_takehome/.env

Note: You will see that the .env file determines the DB user. If you have trouble reaching the DB with a different user like I did, feel free
to switch to the root user (root:r00t)

Now, install the VENV requirements

> pip install -r requirements.txt

Run the migrations so that the DB is ready

> python manage.py migrate
> python manage.py migrate parts

And run the API on localhost, port 8000

> python manage.py runserver

The "Parts" CRUD can be tested by performing HTTP requests at 

> http://localhost/api/parts/

> http://localhost/api/parts/{id}

And the "Top words on Parts description" functionality can be tested on 
> http://localhost/api/parts/top_description_words

If you want to run the tests, you can do so by running the following command:
> python manage.py test