from webui import * # Add WebUI to your imports
from flask import Flask, render_template, request

app = Flask(__name__)
ui = WebUI(app, debug=False) # Create a WebUI instance


#open html files
indexfile = file.read(open('index.html'))
stylesht = file.read(open('static/stylesheets/styles.css'))
mejs = file.read(open('js/medium-editor.js'))
mecss = file.read(open('css/medium-editor.css'))
methm = file.read(open('css/themes/default.css'))
#/js/medium-editor.js


@app.route("/")
def index():
    return indexfile

@app.route("/static/stylesheets/styles.css")
def styles():
    return stylesht

@app.route("/js/medium-editor.js")
def mediumjs():
    return mejs

@app.route("/css/medium-editor.css")
def mediumcss():
    return mecss

@app.route("/css/themes/default.css")
def mediumtheme():
    return methm


if __name__ == '__main__':
  ui.run() #replace app.run() with ui.run(), and that's it
