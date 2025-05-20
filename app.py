from flask import Flask, request, jsonify
from models.games import Game
import os

app = Flask(__name__)

games = []

@app.route('/')
def get_header():
  headers = request.headers
  return dict(request.headers)

@app.route('/create', methods = ['POST'])
def create_game():
  data = request.json
  game = Game(data['name'] , data['category'], data['year'])
  games.append(game)

  return jsonify({'message': 'Game criado com sucesso!', 'game': game.to_dict()}), 201

@app.route('/listall', methods = ['GET'])
def get_all_games():
   return jsonify([game.to_dict() for game in games])

@app.route('/update/<string:id_name>', methods = ['PUT'])
def update_game(id_name):   
  for i in range(len(games)):
    if(games[i].name == id_name):
      data = request.json 
      games[i].name = data['name']
      games[i].category = data['category']
      games[i].year = data['year']

      return jsonify({'message': 'O Game foi atualizado com sucesso', 'Game': games[i].to_dict()}), 200
  return jsonify({'message': 'Game não encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=True)



















@app.route('/games/<name>', methods=['GET'])
def get_game_name(name):
    for game in games:
        if game.name.lower() == name.lower():
            return jsonify(game.to_dict())
    return jsonify({'error': 'Game não encontrado'}), 404



if __name__ == '__main__':
    app.run(debug=True)
