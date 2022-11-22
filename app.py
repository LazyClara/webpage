import os

from flask import Flask, flash, jsonify, redirect, render_template, request
import json

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/home")
@app.route("/")
def home():
        return render_template("home.html")

@app.route("/cakes", methods=["GET", "POST"])
def cakes():
    if request.method == "POST":
        flash("Respond sent")
        return redirect("/")
    else:
        return render_template("cakes.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Respond sent")
        return redirect("/contact")
    else:
        return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/special")
def special():
    return render_template("special.html")

@app.route("/flavoured")
def flavoured():
    return render_template("flavoured.html")

@app.route("/cheesecakes")
def cheesecakes():
    return render_template("cheesecakes.html")

@app.route("/brownies")
def brownies():
    return render_template("brownies.html")

@app.route("/cupcakes")
def cupcakes():
    return render_template("cupcakes.html")

@app.route("/macarons")
def macarons():
    return render_template("macarons.html")

