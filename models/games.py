from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer

db = SQLAlchemy()

class Game(db.Model):
  name = db.Column(db.String(100), primary_key=True,)
  category = db.Column(db.String(40), nullable=False)
  year = db.Column(Integer, nullable=False)

  def __init__(self, name, category, year):
    self.name = name
    self.category = category
    self.year = year

  def to_dict(self):
    return {
      'name': self.name,
      'category': self.category,
      'year': self.year
    }
