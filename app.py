from flask import Flask, request, jsonify
from models.games import Game, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:games.db' 

db.init_app(app)

with app.app_context():
   db.create_all()

@app.route('/create', methods = ['POST'])
def create_game():
  data = request.json
  game = Game(data['name'] , data['category'], int(data['year']))
  db.session.add(game)
  db.session.commit()
  return jsonify({'message': 'Game criado com sucesso!', 'game': game.to_dict()}), 201

@app.route('/listall', methods = ['GET'])
def get_all_games():
  games = Game.query.all()
  print('Todos Games [')
  for game in games:
     print(f'{game.to_dict()}') 
  print('];')
  return jsonify([game.to_dict() for game in games])

@app.route('/games/<name>', methods=['GET'])
def get_game_name(name):
    for game in Game.query.all():
        if game.name.lower() == name.lower():           
            print(f'Game encontrado: {game.to_dict()}\n') 
            return jsonify(game.to_dict())
    return jsonify({'error': 'Game não encontrado'}), 404

@app.route('/update/<string:id_name>', methods = ['PUT'])
def update_game(id_name):   
  game = Game.query.session.get(Game, id_name)
  if(game):
    data = request.json
    game.name = data['name']
    game.category = data['category']
    game.year = data['year'] 
    db.session.commit()
    return jsonify({'message': 'O game foi atualizado com sucesso', 'Game': game.to_dict()}), 200
  return jsonify({'message': 'Game não encontrado'}), 404

@app.route('/delete/<string:id_name>', methods = ['DELETE'])
def delete_game(id_name):
  game = Game.query.session.get(Game, id_name)
  if(game):
    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'O Game foi removido com sucesso'}), 200
  return jsonify({'message': 'Game não encontrado'}), 4

if __name__ == '__main__':
    app.run(debug=True)
