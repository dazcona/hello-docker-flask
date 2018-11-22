# Notes

* http://containertutorials.com/docker-compose/flask-simple-app.html
* https://codefresh.io/docker-tutorial/hello-whale-getting-started-docker-flask/
$ docker build -t flask-sample:latest .
$ docker run -d -p 5000:5000 flask-sample:latest

* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers
$ docker run -d -p 5000:5000 flask-gunicorn:latest
$ docker run --name hello -d -p 8000:5000 --rm flask-unicorn:latest
