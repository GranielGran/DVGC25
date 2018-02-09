""" Operates towards the database without relations """

""" Imports """
from sqlalchemy         import create_engine, MetaData, Table
from relationlessDB     import Node
from relationlessDB     import Sensor
from sqlalchemy.orm     import *
from datetime           import datetime, timedelta

""" Establish Connection to the database """
engine      = create_engine('sqlite:///database/relationless.db')
connection  = engine.connect()

""" Create a session object and bind it """
initSession = sessionmaker(bind = engine) #Create session object
session     = initSession() #Bind session object

DEBUG = True

""" Auxiallary Functions """
#Returns the timestamp closests to the input <timestamp> from the input <timestamps>
def _ClosestTimestamp(timestamp, timestamps):
    return min(timestamps, key=lambda x:timedelta(x-timestamp))


""" Private database functions """
#Create a new "Sensor" entry for a given Node <Node> with name <sensor>
def addDataEntry(sensorName, initReading, readTime):
    
def _addSensor(nodeName, sensorName, initReading, readTime):
    #if DEBUG: print('Adding Sensor: name: {0} , reading: {1}, timestamp: {2} --> node: {3}').format(sensorName, initReading, readTime, nodeName)
    session.add(Sensor(
        nodeID = _getNode(nodeName).id,
        dataID = _getDataEntry().id, 
        name = sensorName
    ))

    session.commit()

#Create a new "Node" entry with the give name input
def _addNode(nodeName): 
    session.add(Node(name = nodeName))
    session.commit() 


def _getDataEntry(entrySensor, time):
    return session.query(Sensor).filter_by(Sensor.id = entrySensor.id, timestamp = time).first()
#Get a "Node" entry with the given name <Node>
def _getNode(nodeName):
    return session.query(Node).filter_by(name = nodeName).first()
#Get a "Sensor" entry from a given Node <Node> with the given name <sensor>
def _getSensor(nodeName, sensorName):
    return session.query(Sensor).filter_by(nodeID = _getNode(nodeName).id, name = sensorName).first()

""" Public database Functions """
def GetLatestSensorReading(timestamp, nodeName, sensorName):
    latestTimestamp = _ClosestTimestamp(_getSensor(nodeName, sensorName).timestamp, timestamp)
    latestReading = session.query(Sensor).filter_by(timestamp = latestTimestamp).first()
    return latestReading

    #TODO
        #Fetch sensor reading table
        #Compare database timestamp with call timestmap
        #return value
    pass

def postSensorReading(sessSensor, readTime, temp):
    Sensor.insert().where(Sensor.id == sessSensor.id).values(reading = temp, timestamp = readTime)
    #session.query(Sensor).filter(Sensor.id == sessSensor.id).add({"reading": temp})
    #session.query(Sensor).filter(Sensor.id == sessSensor.id).add({"timestamp": readTime})
    session.commit()



def getConnectedSensor(Node):
    #TODO
        #getNode(Node) find the Node entry
        #Get Sensor from the return
        #return sensor list
    pass


def getReadingsByType(sensorType):
    #TODO return the readings of every sensor of type<sensorType> 
    pass




if __name__ == '__main__':
    #_addNode("testNode#1")
    #_addSensor('testNode#1', 'testSensor#1', 34.235, datetime.now())

    print _getNode('testNode#1').name
    print _getNode('testNode#1').id
    print _getSensor('testNode#1', 'testSensor#1').reading

    postSensorReading(_getSensor('testNode#1', 'testSensor#1'), datetime.now(), 12.235)

    print _getSensor('testNode#1', 'testSensor#1').reading

#postSensorReading('testNode#1', 'testSesnor#1', datetime.now(), 24.235)


