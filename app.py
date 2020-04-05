from boggle import Boggle
from flask import Flask, request, session, render_template, redirect, Response
from flask import jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"
app.debug = True

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def get_homepage():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('game_board.html', board=board)


@app.route('/validate', methods=["POST"])
def check_word():
    response = request.get_json()
    word = response['word']
    board = session['board']
    rlt = boggle_game.check_valid_word(board, word)
    return jsonify(result=rlt)


times_played = 0


@app.route('/stats', methods=['POST'])
def save_stats():
    global times_played
    response = request.get_json()
    score = response['score']
    times_played += 1
    session['scores'].append(score)
    session['times_played'] = times_played
    return jsonify(succes='succes')
