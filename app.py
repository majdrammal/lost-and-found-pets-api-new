from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Best19462005!@localhost/lost_and_found_pets" 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://rjhglancelwqph:324e568e3fdf61161274b78b02d572ce2e288dd869421a8c4213d08b3610e178@ec2-18-209-78-11.compute-1.amazonaws.com:5432/d5nuo2uksvc5vq" 
db = SQLAlchemy(app) 

class Missing(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.Text, nullable = False)
    name = db.Column(db.Text, nullable = False)
    breed = db.Column(db.Text, nullable = False)
    gender = db.Column(db.Text, nullable = False)
    age = db.Column(db.Text, nullable = False)
    lastSeenIn = db.Column(db.Text, nullable = False)
    lastSeenOn = db.Column(db.Text, nullable = False)
    phoneNumber = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = True)
    image = db.Column(db.Text, nullable = False)

    def __str__(self):
        return f'{self.id} {self.lastSeenIn} {self.lastSeenOn} {self.type} {self.name} {self.breed} {self.gender} {self.age} {self.phoneNumber} {self.description} {self.image}' 

def missing_serializer(missing):
    return {
        'id': missing.id,
        'type': missing.type,
        'name': missing.name,
        'breed': missing.breed,
        'gender': missing.gender,
        'age': missing.age,
        'lastSeenIn': missing.lastSeenIn,
        'lastSeenOn': missing.lastSeenOn,
        'phoneNumber': missing.phoneNumber,
        'description': missing.description,
        'image': missing.image,
    }

class Found(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.Text, nullable = False)
    breed = db.Column(db.Text, nullable = True)
    gender = db.Column(db.Text, nullable = True)
    ageRange = db.Column(db.Text, nullable = True)
    FoundIn = db.Column(db.Text, nullable = False)
    FoundOn = db.Column(db.Text, nullable = False)
    phoneNumber = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    image = db.Column(db.Text, nullable = True)

    def __str__(self):
        return f'{self.id} {self.FoundIn} {self.FoundOn} {self.type} {self.breed} {self.gender} {self.ageRange} {self.phoneNumber} {self.description} {self.image}' 

def found_serializer(found):
    return {
        'id': found.id,
        'type': found.type,
        'breed': found.breed,
        'gender': found.gender,
        'ageRange': found.ageRange,
        'FoundIn': found.FoundIn,
        'FoundOn': found.FoundOn,
        'phoneNumber': found.phoneNumber,
        'description': found.description,
        'image': found.image
    }

@app.route('/', methods = ['GET'])
def home():
    return "Nothing on this page"

# missing

@app.route('/missing', methods = ['GET'])
def indexMissing(): 
    return jsonify([*map(missing_serializer, Missing.query.all())])

@app.route('/missing/create', methods = ['POST'])
def createMissing():
    request_data = json.loads(request.data)
    missing = Missing(lastSeenIn = request_data['lastSeenIn'], lastSeenOn = request_data['lastSeenOn'], type = request_data['type'], name = request_data['name'], breed = request_data['breed'], gender = request_data['gender'], age = request_data['age'], phoneNumber = request_data['phoneNumber'], description = request_data['description'], image = request_data['image'])

    db.session.add(missing)
    db.session.commit()

    return {'201': 'missing created successfully'}

@app.route('/missing/<int:id>')
def showMissing(id):
    return jsonify([*map(missing_serializer, Missing.query.filter_by(id=id))])

@app.route('/missing/<int:id>', methods = ['POST'])
def deleteMissing(id):
    request_data = json.loads(request.data)
    Missing.query.filter_by(id=request_data['id']).delete()
    db.session.commit()

    return {'204': 'Deleted successfully'}

# found

@app.route('/found', methods = ['GET'])
def indexFound(): 
    return jsonify([*map(found_serializer, Found.query.all())])

@app.route('/found/create', methods = ['POST'])
def createFound():
    request_data = json.loads(request.data)
    found = Found(FoundIn = request_data['FoundIn'], FoundOn = request_data['FoundOn'], type = request_data['type'], breed = request_data['breed'], gender = request_data['gender'], ageRange = request_data['ageRange'], phoneNumber = request_data['phoneNumber'], description = request_data['description'], image = request_data['image'])

    db.session.add(found)
    db.session.commit()

    return {'201': 'found created successfully'}

@app.route('/found/<int:id>')
def showFound(id):
    return jsonify([*map(found_serializer, Found.query.filter_by(id=id))])

@app.route('/found/<int:id>', methods = ['POST'])
def deleteFound(id):
    request_data = json.loads(request.data)
    Found.query.filter_by(id=request_data['id']).delete()
    db.session.commit()

    return {'204': 'Deleted successfully'}

if __name__ == '__main__':
    app.run(debug=False)