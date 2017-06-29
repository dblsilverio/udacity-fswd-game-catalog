from datetime import datetime
from catalog.infra.db_factory import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Game(Base):
    """ An entity to map a single game. """
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False, unique=True)
    developer = Column(String(30), nullable=False)
    publisher = Column(String(30), nullable=False)
    platform = Column(String(10), nullable=False) #need table
    thumb = Column(String(500), nullable=True)
    synopsis = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", backref="games", lazy="joined")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref="games", lazy="joined")
    created = Column(DateTime, default=datetime.now())
    views = Column(Integer, default=0)

    def reset(self):
        self.id = 0
        self.name = ''
        self.developer = ''
        self.publisher = ''
        self.platform = ''
        self.thumb = ''
        self.synopsis = ''
        self.category_id = 0
        self.category = None
        self.user_id = 0
        self.user = None
        self.created = None
        self.views = 0

        return self

    def platforms(self):
        plat_str = Game.plat_array(self.platform)
        plat_arr = []

        for plat in plat_str:
            if plat == 'pc':
                plat_arr.append('PC')
            elif plat == 'xo':
                plat_arr.append('Xbox One')
            elif plat == 'ps':
                plat_arr.append('PS4')

        return plat_arr

    def has_platform(self, name):
        return name in Game.plat_array(self.platform)

    @staticmethod
    def plat_array(plat_str):
        return plat_str.split('|')
