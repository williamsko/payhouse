# Payhouse #

Readme of Payhouse project.

## Prerequisites ##

- docker (Install Docker according to your system Mac or Linux)

You can use the script at https://get.docker.com/ to download and install docker

```
curl https://get.docker.com/ >> install_docker.sh
sudo systemctl start docker
```

- Install and start Docker compose
```
sudo pip install docker-compose
```

## Project setup ##

###Please follow this instructions to setup the project locally in a docker container

- Clone the project on your the server on your local machine
```
- git clone https://github.com/williamsko/payhouse.git
- cd payhouse

```

- First Build of the project with docker
```
- docker build .
```

- Create necessary tables and migrate database
```
- docker-compose run web python /code/manage.py migrate --noinput
```

- Run test to assure everything is OK
```
- docker-compose run web python /code/manage.py test
```

- Collect static files in order to serve statics with nginx
```
- docker-compose run web python /code/manage.py collectstatic --noinput
```

- Create a superuser in order to access Django admin IHM
```
- docker-compose run web python /code/manage.py superuser --username root --password liverpool --noinput --email 'admin@email.com'
```

- Build again project and up with docker-compose in detached mode. You can remove ```-d``` option
```
- docker-compose up -d --build
```

### You can use instead this 2 steps below
run  deploy.sh script to deploy
```
- git clone https://github.com/williamsko/payhouse.git
- cd payhouse
- sudo chmod +x deploy.sh
- sudo ./deploy.sh
```
