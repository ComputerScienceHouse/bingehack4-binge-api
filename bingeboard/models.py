from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import String

from bingeboard import db

class BingeEntry(db.Model):
    __tablename__ = 'bingeboard'
    gid = Column(ForeignKey('games.gid'), primary_key=True)
    level = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    max_hp = Column(Integer, nullable=False)
    gold = Column(Integer, nullable=False)
    moves = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    max_energy = Column(Integer, nullable=False)
    attrib_str = Column(Integer, nullable=False)
    attrib_int = Column(Integer, nullable=False)
    attrib_wis = Column(Integer, nullable=False)
    attrib_dex = Column(Integer, nullable=False)
    attrib_con = Column(Integer, nullable=False)
    attrib_cha = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)

class Game(db.Model):
    __tablename__ = 'games'
    gid = Column(Integer, primary_key=True)
    filename = Column(Text, nullable=False)
    plname = Column(Text, nullable=False)
    role = Column(Text, nullable=False)
    race = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    alignment = Column(Text, nullable=False)
    mode = Column(Integer, nullable=False)
    moves = Column(Integer, nullable=False)
    depth = Column(Integer, nullable=False)
    level_desc = Column(Integer, nullable=False)
    done = Column(Boolean, nullable=False)
    owner = Column(ForeignKey('users.uid'), nullable=False)
    ts = Column(DateTime, nullable=False)
    start_ts = Column(DateTime, nullable=False)

class User(db.Model):
    __tablename__ = "users"
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
