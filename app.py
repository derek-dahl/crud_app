from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a simple model
class PizzaReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = PizzaReview.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    score = request.form['score']
    location = request.form['location']
    new_item = PizzaReview(name=name, score=score, location=location)
    db.session.add(new_item)
    db.session.commit()
    return 'Item Added!'

@app.route('/delete/<int:id>', methods=['GET'])
def delete_item(id):
    item = PizzaReview.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return 'Item Deleted!'

if __name__ == '__main__':
    app.run(port='6969', debug=True)
