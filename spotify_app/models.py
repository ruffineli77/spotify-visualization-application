
from datetime import datetime
from spotify_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    header_image = db.Column(db.String(80), nullable=False)
    profile_image = db.Column(db.String(80), nullable=False)
    bio_info = db.Column(db.String(80), nullable=False)
    posts = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Video('{self.username}', '{self.header_image}', '{self.profile_image}', '{self.bio_info}', '{self.posts}')"


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(80), nullable=False)
    artist_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Video('{self.track_name}', '{self.artist_name}')"
