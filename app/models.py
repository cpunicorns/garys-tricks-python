import uuid
import time
import datetime
from app import db

ts = time.time()


class Tricks(db.Model):
    id = db.Column(models.UUIDField(_(uuid.uuid4())), primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    progress = db.Column(db.String(120), index=True)
    state = db.Column(db.String(128))
    added_on = db.Column(datetime.datetime.fromtimestamp(
        ts).strftime('%Y-%m-%d %H:%M:%S'))
