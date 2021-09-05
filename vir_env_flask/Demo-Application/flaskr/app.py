from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__,template_folder="../templates")

@app.route("/")
def landing_menu():
    return render_template('landing_menu.html')

@app.route("/service")
def render_service():
    """""This gets the service docs forms for a particular asset"""
    return render_template('render_service.html')

@app.route("/report")
def render_asset_report():
    """""This gets a general report over the asset"""
    return render_template('render_asset_report.html')

@app.route("/safety")
def render_site_safety_report():
    """""This gets the site safety plan"""
    return render_template('render_asset_report.html')