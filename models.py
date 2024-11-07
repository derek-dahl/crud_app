from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define a simple model
class PizzaReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"*** PizzaReview(name='{self.name}', score={self.score}, location='{self.location}') ***"
