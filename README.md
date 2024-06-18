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
Note: More installations might be needed to run the application depending on your OS. Feel free to install them as required.

Now, clone 

Create and run a Virtual Environment to run the project, using Python 3.11.

>  virtualenv -p=python3.11 venv
> . venv/bin/activate
