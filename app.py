from flask import Flask, request, render_template
from models import db, PizzaReview

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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
