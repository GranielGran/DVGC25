from flask import Flask
from datetime import datetime
from sqlalchemy import Column, Date, Integer, String, ForeignKey, DateTime, Float, Squence
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


""" Tabel Definitons """
class DataEntry(Base):
    __tablename__   = 'SensorData'
    id              = Column(Integer, primary_key = True)
    sensorID        = Column(Integer, nullable = False)
    output          = Column(Integer, nullable = False)
    timestamp       = Column(Integer, nullable = False)
    
class Sensor(Base):
    __tablename__   = 'Sensor'
    id              = Column(Integer, primary_key = True)
    nodeID          = Column(Integer, nullable = False)
    dataID          = Column(Integer, nullable = False)
    name            = Column(String(20), nullable = False, unique = True)

class Node(Base):
    __tablename__   = 'node'
    id              = Column(Integer, primary_key = True)
    name            = Column(String(20), nullable = False)


""" If this file is run separetly we want """
if __name__ == '__main__':
    engine = create_engine('sqlite:///database/relationless.db', echo=True)

    #If we can't find a the .db file, we create one at the given path
    if not database_exists(engine.url): create_database(engine.url) 
    
    Base.metadata.create_all(engine)