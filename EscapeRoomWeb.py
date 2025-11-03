from flask import Flask, jsonify, make_response, render_template, request, abort
from EscapeRoomGame import EscapeRoomGame
import os
import string
import random
import time
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()

app = Flask("")

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

game = EscapeRoomGame()


@app.route('/')
def index():
    game.reset()
    return render_template('escape.html')


@app.route('/rooms/<string:name>', methods=['POST'])
def load_room(name):
    response = jsonify({"success": True, "room_name": name})
    game.load_room(name, response)

    return response


@app.route('/rooms', methods=['POST'])
def load_all_rooms():
    game.load_all_rooms()
    return jsonify({"success": True})


@app.route('/rooms/available')
def get_available_rooms():
    return jsonify(game.find_rooms())


@app.route('/rooms')
def get_loaded_rooms():
    room_names = [room.get_name() for room in game.get_rooms()]
    return jsonify({"count": len(room_names), "room_names": room_names})


@app.route('/rooms/<int:room_nr>')
def get_room(room_nr):
    if (len(game.get_rooms()) <= room_nr):
        # print(f"Room {room_nr} does not exist (yet)")
        abort(404)
    else:
        return jsonify(game.get_room(room_nr).get_metadata())


@app.route('/rooms/<int:room_nr>/levels')
def get_levels(room_nr):
    return jsonify({"count": len(game.get_rooms()[room_nr].get_levels())})


@app.route('/rooms/<int:room_nr>/levels/<int:level_nr>')
def get_level(room_nr, level_nr):
    room = game.get_rooms()[room_nr]
    levels = room.get_levels()
    if level_nr < len(levels):
        level = room.get_levels()[level_nr]
        return jsonify({"gamename": level["gamename"], "tasks": level["task_messages"], "hints": level["hints"]})
    else:
        # print("Invalid level.")
        abort(404)


@app.route('/rooms/<int:room_nr>/levels/<int:level_nr>/solve', methods=['POST'])
def post_solve_level(room_nr, level_nr):
    room = game.get_rooms()[room_nr]
    level = room.get_levels()[level_nr]
    file = request.files['file']
    filename = ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=7))
    file.save(filename+".py")
    try:
        solution = room.check_solution(
            filename, level["solution_function"], level["data"])
    finally:
        os.remove(filename+".py")
    return jsonify(solution)


@app.route("/.env")
def env_debug():
    return jsonify(dict(os.environ))


# app.run(host='0.0.0.0', port=5000, debug=True)app.run(debug=True)
app.run(host='0.0.0.0', port=5001, debug=True)
