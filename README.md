# Game Catalog Project

This project was developed in fulfillment of **Full-Stack Web Developer Nanodegree** *Build an Item Catalog* module.

## Requirements

The following technologies were applied in the development of this project:
* [Python 2.7](https://www.python.org/downloads/)
* [SQLite3](https://www.sqlite.org/)
* [Flask 0.12](http://flask.pocoo.org/)
* [SQLAlchemy 1.1](http://www.sqlalchemy.org/)

### Configuration

### Docker

Running this project as a container is very simple.

Run `user:~/$ docker-image/builder.sh`, and your Game Catalog instance will be readily online on port **5000**. The build process will take care of everything needed to run correctly this project.

### Standalone

Running Game Catalog demands Python 2.X and few modules to be installed by user.

Install Python 2 and Pip from your prefered package manager, i.e, `sudo apt-get install python2.7 python-pip` for Ubuntu/Debian.

Issue the following command to install required python modules: `sudo pip install flask sqlalchemy`

Run `FLASK_APP=catalog flask run` at root path to start. Project will be online on port **5000**

For debugging purposes, add `FLASK_DEBUG=true` while starting Flask.

## Api Endpoints

* /latest.json
* /top10.json
* /category.json
* /category/<int:cid>.json
* /game.json
* /game/<int:gid>.json
