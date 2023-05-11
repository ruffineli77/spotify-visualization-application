
import os
from pathlib import Path
from spotify_app import app, db
from spotify_app.forms import ContactForm
from spotify_app.models import *
from spotify_app.functions import *
from flask import url_for, render_template, redirect, flash, abort, request
from flask_sqlalchemy import Pagination
from sqlalchemy import func
# from essential_generators import DocumentGenerator


def insert_videos(video_directories):
  db.create_all()
  root_dir = Path(video_directories)
  file_location = root_dir.stem

  if root_dir:  # replace conditional with exceptions?
    sel_videos = one_folder(video_directories)
    # print(sel_videos)
    for dir_tuple in sel_videos.items():
        # print(str(Path(root_dir, dir_tuple[0])))
        # print(dir_tuple)
        for video in dir_tuple[1]:
            # print(video)
            video_record = Video(file_name=f"{video}.mp4", folder_name=f"{dir_tuple[0]}")
            # print(video_record.folder_name)

            exists = Video.query.filter_by(file_name=f"{video}.mp4").first()
            if not exists:
                db.session.add(video_record)


    db.session.commit()


insert_videos("spotify_app/static/images")


# main route. layout.html is used for the general skeleton of all pages.
@app.route('/')
def home():
    title = "Spotify Visualizations"


    return render_template('home.html', title=title)


@app.route('/contact')
def contact():
    title = "Contact"
    about_sections = {"use": "This is a blog photo gallery combo",
                      "pages": ["Account", "Blog", "Gallery"],
                      "info": "I am the creator Eli"}


    return render_template('contact.html', title=title, 
                           about_sections=about_sections)


@app.route('/faqs')
def faqs():
    title = "FAQs"
    faq_sections = {"use": "This is a blog photo gallery combo",
                      "search": ["Account", "Blog", "Gallery"],
                      "categories": "I am the creator Eli"}


    return render_template('faqs.html', title=title, 
                           faq_sections=faq_sections)


@app.route('/profile')
def profile():
    title = "Profile"

    return render_template('profile.html', title=title)


@app.route('/explore/<string:vid_fold>')
def explore(vid_fold=""):
    title = "Explore Albums"

    # return render_template('explore.html', title=title)

    page_num = request.args.get('page', 1, type=int)
    videos = Video.query.filter_by(folder_name=f"{vid_fold}")
    videos_pages = videos.paginate(per_page=10, page=page_num)

    # print(videos)
    # print(videos_pages.items)


    return render_template('explore.html', title=title,
                            videos=videos_pages, vid_fold=vid_fold)