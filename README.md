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

### Latest Games Cataloged

Displays last **n** games, according *catalog.ini* properties.

Path: `/latest.json`

Result:
```json
[
  {
    "created_at": "Wed, 28 Jun 2017 23:41:51 GMT", 
    "id": 10, 
    "name": "Counter-Strike: Global Offensive", 
    "views": 14
  }
]
```

### Top 10 Games

Lists top 10 most visualized games, from all categories.

Path: `/top10.json`

Result:
```json

[
  {
    "created_at": "Sun, 25 Jun 2017 19:55:50 GMT", 
    "id": 8, 
    "name": "The Long Dark", 
    "views": 51
  }
]
```

### Category Listing

Lists all categories and information about their games.

Path: `/category.json`

Result:
```json
[
  {
    "games": {
      "available_titles": [
        {
          "link": "/game/8.json", 
          "name": "The Long Dark"
        }
      ], 
      "quantity": 1
    }, 
    "id": 3, 
    "link": "/category/3", 
    "name": "Atmospheric"
  }
]
```

### Category Details

Show details about a category specified by it **id**.

Path: `/category/<int:cid>.json`

Result:
```json
{
  "description": "FPS (First-Person Shooter) games are a sub-genre of Shooting games that became immensely popular. They are basically Shooting games played from the protagonist's perspective, allowing for a higher degree of immersion and realism. Military FPS games are extremely popular, but these games may also take place in fantasy or sci-fi settings. FPS games may also incorporate an optional third-person perspective, limited melee combat, or narrative elements of Action-Adventures. Online multi-player FPS games are also particularly popular.\n", 
  "games": {
    "available_titles": [
      {
        "link": "/game/10.json", 
        "name": "Counter-Strike: Global Offensive"
      }
    ], 
    "quantity": 1
  }, 
  "id": 4, 
  "link": "/category/4", 
  "name": "FPS"
}
```

### Game Listing

Lists all games.

Path: `/game.json`

Result:
```json
[
  {
    "created_at": "Sun, 25 Jun 2017 15:30:07 GMT", 
    "id": 4, 
    "name": "Age of Empires: Definitive Edition", 
    "synopsis": "A refreshed version of Age of Empires, a real-time strategy game that debuted in 1997. Microsoft, th...", 
    "views": 16
  }, 
```

### Game Details

Show details about a game specified by it **id**.

Path: `/game/<int:gid>.json`

Result:
```json

{
  "category": {
    "id": 9, 
    "link": "/category/9", 
    "name": "Strategy"
  }, 
  "created_at": "Sun, 25 Jun 2017 15:30:07 GMT", 
  "developer": "Ensemble Studios", 
  "id": 4, 
  "link": "/game/4", 
  "name": "Age of Empires: Definitive Edition", 
  "platform": [
    "PC"
  ], 
  "publisher": "Microsoft Games", 
  "sent_by": {
    "email": "diogosilverio@yahoo.com.br", 
    "id": 1, 
    "name": "Diogo Silv\u00e9rio"
  }, 
  "synopsis": "A refreshed version of Age of Empires, a real-time strategy game that debuted in 1997. Microsoft, the company responsible for the new version, focused not only on improving the graphics so that they now support 4K resolution, but on recording a new version of the symphonic soundtrack as well. \r\n\r\nThe title contains the content of the basic version of the original game and of the Rise of Rome expansion pack. The singleplayer scenarios were expanded with new narrative features. In Age of Empires: Definitive Edition the player is leading civilizations from various areas of the world to war. The gameplay is focused on expanding the base, obtaining resources, recruiting army and participating in dynamical battles. \r\n\r\nA modernized interface makes controlling the battlefield easier. In addition to singleplayer modes, the title offers multiplayer mode based on Xbox Live.", 
  "thumb": "http://www.gry-online.pl/galeria/gry13/433152235.jpg", 
  "views": 15
}

```
