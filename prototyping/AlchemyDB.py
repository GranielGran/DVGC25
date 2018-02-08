from flask import Flask
from datetime import datetime
from sqlalchemy import Column, Date, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///database/datalog.db', echo=True)

#If we can't find a the .db file, we create one at the given path
if not database_exists(engine.url): create_database(engine.url) 

Base = declarative_base()

'''
Here we define the tables that are going into the database
'''
class Sensor(Base):
    __tablename__   = 'Sensor'
    id              = Column(Integer, primary_key = True)
    moduleID        = Column(Integer, ForeignKey('Module.id'), nullable = False)
    reading         = Column(Float, nullable = False)
    timestamp       = Column(DateTime, nullable = False, default = datetime)
    sensorName      = Column(String(10), nullable = False)

    def __repr__(self): 
        return '<Sensor %r>' % self.sensorName

class Module(Base):
    __tablename__   = 'Module'
    id              = Column(Integer, primary_key = True)
    moduleName      = Column(String(10), nullable = False)
    Connections     = relationship('Sensor')
    
    def __repr__(self):
        return 'Module %r' % self.moduleName

Base.metadata.create_all(engine)


