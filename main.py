from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG']= True

header = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      form{
          background-color: #eee;
          padding: 20px;
          margin: 0 auto;
          width: 540px;
          font: 16px sans-serif;
          border-radius:10px;
      }
      textarea{{
          margin: 10px o;
          width: 1000px;
          height: 300px;
      }}
    </style>
  </head>
  <body>
  """
form = """
    <form action="/encrypt" method="POST">
      <label for="rot">Rotate by:
        <input id="rot" name="rot" type="text" value="0" />
      </label>
      <br>
      <textarea id="text" name="text">{0}</textarea>
      <input type="submit" value="Submit Query" />
    </form>
"""
footer = """  
  </body>
</html>
"""

@app.route("/")
def index():

  return header + form.format("") + footer

@app.route("/encrypt", methods=["POST"])
def encrypt():
    rotate = int(request.form['rot'])
    text = request.form['text']
    text_rotated = rotate_string(text,rotate)

    
    return header + form.format(text_rotated) + footer

app.run()