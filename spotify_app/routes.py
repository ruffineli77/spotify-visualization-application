
import os
# from PIL import Image
from pathlib import Path
from spotify_app import app, db
from spotify_app.forms import ContactForm
from spotify_app.models import User
from flask import url_for, render_template, redirect, flash, abort, request
from flask_sqlalchemy import Pagination
from sqlalchemy import func
# from essential_generators import DocumentGenerator

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

