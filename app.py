from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from models import db, PizzaReview

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'


# Initialize SQLAlchemy with app context
db.init_app(app)

# Create the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    items = PizzaReview.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    data = request.json

    if not data:
        response = {
            "status": "error",
            "message": "No data provided"
        }
        return jsonify(response), 400


    name = data.get('name')
    score = data.get('score')
    location = data.get('location')

    if not name or not score or not location:
        response = {
            "status":"error",
            "message":"Missing required fields: 'name', 'score', and/or 'location"
        }
        return jsonify(response), 400

    new_item = PizzaReview(name=name, score=score, location=location)

    db.session.add(new_item)
    db.session.commit()
    response = {
        "status": "success",
        "message": "Item added successfully!",
        "data": {
            "id": new_item.id,
            "name": new_item.name,
            "score": new_item.score,
            "location": new_item.location,
        }
    }

    return jsonify(response), 201



@app.route('/delete/<int:id>', methods=['GET'])
def delete_item(id):
    item = PizzaReview.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return "Item deleted...", 201

if __name__ == '__main__':
    app.run(port='6969', debug=True)
