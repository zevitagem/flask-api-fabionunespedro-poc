from flask import Flask, request, jsonify
from models.games import Game
import os

app = Flask(__name__)

list_games = []

@app.route('/create', methods = ['POST'])
def create_game():
  data = request.json
  game = Game(data['name'] , data['category'], data['year'])
  list_games.append(game)
  return jsonify({'message': 'Game criado com sucesso!', 'game': game.to_dict()}), 201

@app.route('/listall', methods = ['GET'])
def get_all_games():
   return jsonify([game.to_dict() for game in list_games])

@app.route('/games/<name>', methods=['GET'])
def get_game_name(name):
    for game in list_games:
        if game.name.lower() == name.lower():
            return jsonify(game.to_dict())
    return jsonify({'error': 'Game não encontrado'}), 404

@app.route('/update/<string:id_name>', methods = ['PUT'])
def update_game(id_name):   
  for i in range(len(list_games)):
    if(list_games[i].name == id_name):
      data = request.json 
      list_games[i].name = data['name']
      list_games[i].category = data['category']
      list_games[i].year = data['year']
      return jsonify({'message': 'O Game foi atualizado com sucesso', 'Game': list_games[i].to_dict()}), 200
  return jsonify({'message': 'Game não encontrado'}), 404

@app.route('/delete/<string:id_name>', methods = ['DELETE'])
def delete_game(id_name):
  for i in range(len(list_games)):
    if(list_games[i].name == id_name):
      list_games.pop(i)
      if len(list_games) != 0:
        return jsonify({'message': 'O Game foi removido com sucesso', 'Game': list_games[i].to_dict()}), 200
      else:
        return jsonify({'message': 'O Game foi removido com sucesso, você não possui nenhum game em sua lista'}), 200
  return jsonify({'message': 'Game não encontrado'}), 4


if __name__ == '__main__':
    app.run(debug=True)
