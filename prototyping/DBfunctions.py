from AlchemyDB.py import *

def getSensorReading(timestamp, module, sensor):
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


def getModule(moduleName):
    #TODO return the DB object corresponding the moduleName parameter
    pass

def getModules():
    #TODO return all Modules in the DB
    pass

def getReadingsByType(sensorType):
    #TODO return the readings of every sensor of type<sensorType> 
    pass


def postSensorReading(timestamp, module, sensor, reading)
    #TODO
        #write parameters timestamp and reading
        #too their respective module and sensor

    pass


def addSensorType(moduleName, sensorName):
    #TODO add a sensor tabel to corresponding moduleName
    pass

def AddSensorModule(moduleName):
    #TODO create new entry in the module table with moduleName 
    db.session.add(Modules()) 
    pass
