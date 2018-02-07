from flask import Flask, request
from flask_restful import resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify


dbConnection    = create_engine('sqlite:////tmp/test.db')
app             = Flask(__name__)
api             = Api(app)


class Sensors(Resource)
    def get(self):
        connection  = dbConnection.connect()
        query       = connection.execute('select * from sensors')
        return {'Sensors': [i[0] for i in query.cursor.fetchall()]}
    
class Modules(Resource):
    #TODO
    pass
