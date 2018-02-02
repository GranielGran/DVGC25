from bottle         import route, run, template
from datetime       import datetime
from AlchemyTest    import *    

@route('/<moduleName>/<sensorName>/readings/')
def sensorReading(moduleName, sensorName):
    return template('<b>Sensor Reading -> {{reading}}', reading = getValueByTime(datetime.now, moduleName, sensorName))

