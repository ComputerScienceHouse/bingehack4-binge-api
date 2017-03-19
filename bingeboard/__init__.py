import operator
import os
import subprocess

from flask import Flask
from flask import current_app
from flask import jsonify
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from flask import session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False


if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

db = SQLAlchemy(app)

app.config["GIT_REVISION"] = subprocess.check_output(['git',
                                                      'rev-parse',
                                                      '--short',
                                                      'HEAD']).decode('utf-8').rstrip()

# pylint: disable=C0413
from bingeboard.models import BingeEntry
from bingeboard.models import Game
from bingeboard.models import User

@app.route("/api")
def index():
    return redirect("/api/get/10")

@app.route("/api/get/<int:num_entries>")
def get_bingeboard(num_entries):
    num_entries = int(num_entries)

    filter_complete = True
    if 'filter_complete' in request.args:
        filter_complete = strtobool(request.args.get('filter_complete'))

    binges = [get_binge_info(binge, filter_complete=filter_complete)
                for binge in BingeEntry.query.all()]

    # filter out Falsy types
    binges = [binge for binge in binges if binge]

    # sort by score
    binges.sort(key=operator.itemgetter('score'), reverse=True)

    # truncate to num_entries
    del binges[num_entries:]

    return jsonify(binges), 200

def get_binge_info(binge_entry, filter_complete=True):
    game_entry = Game.query.filter(Game.gid == binge_entry.gid).first()
    game_user = User.query.filter(User.uid == game_entry.owner).first()

    if filter_complete and game_entry.done:
        return None

    if game_entry and game_user:
        return {
                "username": game_user.name,
                "character_name": game_entry.plname,
                "role": game_entry.role,
                "race": game_entry.race,
                "gender": game_entry.gender,
                "alignment": game_entry.alignment,
                "depth": binge_entry.level,
                "hp": binge_entry.hp,
                "max_hp": binge_entry.max_hp,
                "gold": binge_entry.gold,
                "moves": binge_entry.moves,
                "energy": binge_entry.energy,
                "max_energy": binge_entry.max_energy,
                "strength": binge_entry.attrib_str,
                "intelligence": binge_entry.attrib_int,
                "wisdom": binge_entry.attrib_wis,
                "dexterity": binge_entry.attrib_dex,
                "constitution": binge_entry.attrib_con,
                "charisma": binge_entry.attrib_cha,
                "score": binge_entry.score
            }

    return None

def strtobool(string):
    return string.lower() in ['true', 't', '1']
