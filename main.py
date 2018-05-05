from flask import Flask, render_template
from data.games import Games

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', games = Games())

@app.route('/game/<int:id>/')
def game(id):
    games = Games()
    if id > len(games) or id < 1:
        return render_template('index.html', games = games)
    else:
        return render_template('game.html', games = games, id = id - 1)

if __name__ == '__main__':
    app.run(debug=True)