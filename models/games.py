class Game():
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