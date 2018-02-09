from flask                      import Flask
from datetime                   import datetime
from sqlalchemy                 import Column, Date, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils           import database_exists, create_database
from sqlalchemy.orm             import relationship



Base = declarative_base()

'''
Here we define the tables that are going into the database
'''
class Sensor(Base):
    __tablename__   = 'sensor'
    id              = Column(Integer,    primary_key = True)
    reading         = Column(Float,      nullable    = False)
    timestamp       = Column(DateTime,   nullable    = False)
    name            = Column(String(20), nullable    = False)

    def __repr__(self): 
        return '<Sensor %r>' % self.sensorName

class Node(Base):
    __tablename__   = 'node'
    id              = Column(Integer,        primary_key = True)
    name            = Column(String(20),     nullable    = False)
    sensorID        = Column(Integer,        ForeignKey('sensor.id'))
    sensor          = relationship('Sensor')
    
    def __repr__(self):
        return 'Node %r' % self.NodeName


"""
If this file is run separetly we want
"""
if __name__ == '__main__':
    engine = create_engine('sqlite:///database/datalog.db', echo=True)

    #If we can't find a the .db file, we create one at the given path
    if not database_exists(engine.url): create_database(engine.url) 
    
    Base.metadata.create_all(engine)
    


