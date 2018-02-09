from sqlalchemy     import create_engine, MetaData, Table
from AlchemyDB      import Node
from AlchemyDB      import Sensor
from sqlalchemy.orm import sessionmaker
from datetime       import datetime, timedelta
""" Establish Connection to the database """
engine      = create_engine('sqlite:///database/datalog.db')
connection  = engine.connect()


""" Create a session object and bind it """
initSession = sessionmaker(bind = engine) #Create session object
session     = initSession() #Bind session object


""" Auxiallary Functions """
#Returns the timestamp closests to the input <timestamp> from the input <timestamps>
def __ClosestTimestamp(timestamp, timestamps):
    return min(timestamps, key=lambda x:timedelta(x-timestamp))


""" Private database functions """
#Create a new "Sensor" entry for a given Node <Node> with name <sensor>
def __addSensor(nodeName, sensorName, initReading, readTime):
    newSensor = Sensor(reading = initReading, timestamp = readTime, name = sensorName)
    session.add(newSensor)
    __getNode(nodeName).sensorID = newSensor.id
    session.commit()

#Create a new "Node" entry with the give name input
def __addNode(nodeName): 
    session.add(Node(name = nodeName))
    session.commit() 

#Get a "Node" entry with the given name <Node>
def __getNode(nodeName):
    return session.query(Node).filter_by(name = nodeName).first()

#Get a "Sensor" entry from a given Node <Node> with the given name <sensor>
def __getSensor(nodeName, sensorName):
    return session.query(Node.sensor).filter_by(name = sensorName).first()

""" Public database Functions """
def GetLatestSensorReading(timestamp, nodeName, sensorName):
    latestTimestamp = __ClosestTimestamp(__getSensor(nodeName, sensorName).timestamp, timestamp)
    latestReading = session.query(Node.sensor).filter_by(timestamp = latestTimestamp).first()
    return latestReading

    #TODO
        #Fetch sensor reading table
        #Compare database timestamp with call timestmap
        #return value
    pass

def postSensorReading(Node, sensor, readTime, reading):
    sessSensor = __getSensor(__getNode(Node), sensor).first()
    session.execute(sessSensor.insert(), {'reading': reading, 'timestamp': readTime})



def getConnectedSensor(Node):
    #TODO
        #getNode(Node) find the Node entry
        #Get Sensor from the return
        #return sensor list
    pass


def getReadingsByType(sensorType):
    #TODO return the readings of every sensor of type<sensorType> 
    pass

__addNode("testNode#1")
__addSensor('testNode#1', 'testSensor#1', 34.235, datetime.now())

#postSensorReading('testNode#1', 'testSesnor#1', datetime.now(), 24.235)


