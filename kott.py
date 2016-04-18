from webui import * # Add WebUI to your imports
from flask import Flask, render_template, request

app = Flask(__name__)
ui = WebUI(app, debug=False) # Create a WebUI instance


#open html files
indexfile = file.read(open('index.html'))

@app.route("/")
def index():
    return indexfile


if __name__ == '__main__':
  ui.run() #replace app.run() with ui.run(), and that's it
