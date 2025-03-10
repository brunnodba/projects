from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'Meu Hotel'}

api.add_resource(Hoteis, '/hoteis')     

if __name__ == '__main__' :
   app.run(debug=True)
    
# if __name__ == '__main__':
#     app.run(debug=True, port=5001)