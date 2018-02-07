from sqlalchemy         import create_engine, MetaData, Table
from sqlalchemy.orm     import mapper, sessionmaker

engine = create_engine('sqlite:///database/datalog.db')
connection = engine.connect()

result = connection.execute("select moduleName from Modules")


with connection.begin() as transaction:
    r1 = connection.execute(Modules.select())
    connection.execute(Modules.insert(), col1 = "Totoro")
    transaction.commit()

print(result)
for row in result:
    print("moduleName: {0}").format(row['moduleName'])

connection.close()

'''
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


def addSensorType(moduleName, sensorName):
    #TODO add a sensor tabel to corresponding moduleName
    pass

def AddSensorModule(moduleName):
    #TODO create new entry in the module table with moduleName 
    db.session.add(Modules()) 
    pass
'''