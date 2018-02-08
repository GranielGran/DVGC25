from sqlalchemy import create_engine, MetaData, Table
from AlchemyDB import Modules
from AlchemyDB import Sensors
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///database/datalog.db')
connection = engine.connect()

initSession = sessionmaker(bind = engine) #Create session object
session = initSession() #Bind session object

"""
Private Functions
"""

#Returns the timestamp closests to the input <timestamp> from the input <timestamps>
def __getClosestTimestamp(timestamp, timestamps):
    min(timestamps, key=lambda x:timedelta(x-timestmap))

#Get a "Modules" entry with the given name <module>
def __getModule(module):
    return session.query(Modules).filter_by(moduleName = module).first()

#Get a "Sensors" entry from a given module <module> with the given name <sensor>
def __getSensor(module, sensor):
    return session.query(Modules.sensorConnections).filter_by(sensorName = sensor, __getModule(module).id).first()

"""
Public Functions
"""

#Create a new "Sensors" entry for a given module <module> with name <sensor>
def AddSensor(module, sensor):
    session.add(Sensors(
                moduleID = getModule(module).id, 
                reading = 12.34, 
                sensorName = sensor))
    session.commit()

#Create a new "Modules" entry with the give name input
def AddModule(name): 
    session.add(Modules(moduleName = name))
    session.commit()

def GetLatestSensorReading(timestamp, module, sensor):
    latestTimestamp = __getClosestTimestamp(getSensor(module, sensor).timestamp, timestamp)
    session.query()


    #TODO
        #Fetch sensor reading table
        #Compare database timestamp with call timestmap
        #return value
    pass

def getConnectedSensors(moduleName):
    #TODO
        #getModule(moduleName) find the module entry
        #Get sensors from the return
        #return sensor list
    pass


#Takes a name and searches the DB for a Module entry with the corresponding moduleName field
def getModule(moduleName):
    #TODO return the DB object corresponding the moduleName parameter

    Modules.query.find()
    pass

#Queries the DB for all module entries and returns them as a Array
def getModules():
    instances = []
    for instance in Modules.query.Find_all():
        instances.append(instance)
    
    return instances

def getReadingsByType(sensorType):
    #TODO return the readings of every sensor of type<sensorType> 
    for modules in getModules():
        modules.query()
    pass


def postSensorReading(timestamp, module, sensor, reading)
    #TODO
        #write parameters timestamp and reading
        #too their respective module and sensor

    pass
'''
