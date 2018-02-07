from flask                          import Flask
from sqlalchemy                     import Column, Date, Integer, String, ForeignKey
from sqlalchemy                     import create_engine
from sqlalchemy.ext.declarative     import declarative_base
from sqlalchemy_utils               import database_exists, create_database
from sqlalchemy.orm                 import relationship
from datetime                       import datetime
##########################################################################################
#Config and Instansiation                                                                #
##########################################################################################

engine = create_engine('sqlite:///database/datalog.db', echo=True)
if not database_exists(engine.url): create_database(engine.url) 

Base = declarative_base()

##########################################################################################
#Tabel Creation                                                                         #
##########################################################################################
class Sensors(Base):
    __tablename__   = 'sensors'
    id              = Column(Integer, primary_key = True)
    moduleID        = Column(Integer, ForeignKey('modules.id'), nullable = False)
    reading         = Column(Integer, nullable = False)
    timestamp       = Column(Integer, nullable = False, default = datetime.utcnow)
    sensorName      = Column(String(10), nullable = False)

    def __repr__(self): 
        return '<Sensor %r>' % self.sensorName

class Modules(Base):
    __tablename__        = 'modules'
    id                   = Column(Integer, primary_key = True)
    moduleName           = Column(String(10), nullable = False)
    sensorConnections    = relationship('Sensor')
    
    def __repr__(self):
        return 'Module %r' % self.moduleName

Base.metadata.create_all(engine)


