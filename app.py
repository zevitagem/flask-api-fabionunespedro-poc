from flask import Flask, request, jsonify
from models.games import Game

app = Flask(__name__)

games = []

@app.route('/create', methods = ['POST'])
def create_game():
  data = request.json
  game = Game(data['name'], data['category'], data['year'])
  games.append(game)
  return jsonify({'message': 'Game criado com sucesso!', 'game': game.to_dict()}), 201

@app.route('/listall', methods = ['GET'])
def get_all_games():
   return jsonify([game.to_dict() for game in games])

if __name__ == '__main__':
    app.run(debug=True)
