from AlchemyTest import db
from AlchemyTest import Modules
from AlchemyTest import Sensors
 
sensor1     = Modules(moduleName = 'slave#1')
sensorType1 = Sensors(reading = 123, sensorName = 'DHT-011')

sensor1.sensorConnections.append(sensorType1)
db.session.add(sensorType1)

print('sensor1 connections: {}').format(sensor1.sensorConnections)


data = Table('SensorConnection', meta, autoload = True, autoload_with = engine)
print 'reading' in meta.tables


dbConnection = create_engine('sqlite:////tmp/test.db')
class SensorReadings(Resource)
    def get(self):
        connection = dbConnection.connect()
        query = conn.execute('select * from Modules')


















