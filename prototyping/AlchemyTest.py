from flask                      import Flask
from flask_sqlalchemy           import SQLAlchemy
from sqlalchemy.orm             import relationship
from datetime                   import datetime
##########################################################################################
#Config and Instansiation                                                                #
##########################################################################################
app = Flask(__name__)
#Errors if not set
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#Assign Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

##########################################################################################
#Tabel Creation                                                                         #
##########################################################################################
class Sensors(db.Model):
    __tablename__   = 'sensors'
    id              = db.Column(db.Integer, primary_key = True)
    moduleID        = db.Column(db.Integer, db.ForeignKey('module.id'), nullable = False)
    reading         = db.Column(db.Integer, nullable = False)
    timestamp       = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    sensorName      = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return '<Sensor %r>' % self.sensorName

class Modules(db.Model):
    __tablename__        = 'modules'
    id                   = db.Column(db.Integer, primary_key = True)
    moduleName           = db.Column(db.String(10), nullable = False)
    sensorConnections    = relationship('Sensor')
    
    def __repr__(self):
        return 'Module %r' % self.moduleName


