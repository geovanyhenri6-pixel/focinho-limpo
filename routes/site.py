from flask import Blueprint, render_template, request, redirect, url_for

site = Blueprint("site", __name__)

@site.route("/")
def home():
    return render_template("site/home.html")