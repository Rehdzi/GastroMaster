from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pathlib import Path
from sys import argv

# from util.db import *

app = Flask(__name__)

script_dir = Path(argv[0]).parent.resolve()
db_path = script_dir / 'db' / 'database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/rehdzi/ucheba/schweiton/GastroMaster/db/database.db"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    profile_image = db.Column(db.String(20), unique=False, nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_image}', '{self.password}')"


class OrgInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(45), unique=True, nullable=False, default='My Restraunt')
    org_image = db.Column(db.String(20), unique=False, nullable=False, default='default_org.jpg')
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.org_name}', '{self.org_image}', '{self.creation_date}')"


app.app_context().push()
db.create_all()


@app.route("/")
def index():
    guestData = [
        ("18.12.2023", 156),
        ("19.12.2023", 234),
        ("20.12.2023", 245),
        ("21.12.2023", 262),
        ("22.12.2023", 345),
        ("23.12.2023", 453),
        ("24.12.2023", 243)
    ]

    orgName = "Funny Restraunt"
    orgPic = "/static/img/EverlastingSummer-Background.webp"

    guestLabels = [row[0] for row in guestData]
    guestValues = [row[1] for row in guestData]

    # orgName = [row[0] for row in orgInformation]
    # orgPic = [row[1] for row in orgInformation]

    return render_template('dashboard.html',
                           guestLabels=guestLabels,
                           guestValues=guestValues,
                           orgPic=orgPic,
                           orgName=orgName)


if __name__ == "__main__":
    app.run()
