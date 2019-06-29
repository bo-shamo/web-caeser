from flask import Flask, request
    #TODO: Add Caesar rotate string


app = Flask(__name__)
app.config['DEBUG']= True

form = """
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
      textarea{
          margin: 10px o;
          width: 540px;
          height: 120px;
      }
    </style>
  </head>
  <body>
    <form action="/encrypt" method="POST">
      <label for="rot">Rotate by:
        <input id="rot" name="rot" type="text" value="0" />
      </label>
      <textarea id="text" name="text">
      </textarea>
      <input type="submit" value="Submit Query" />
    </form>
  </body>
</html>
"""

@app.route("/")
def index():
  return form

@app.route("/encrypt", methods=["POST"])
def encrypt():
    rotate = request.form['rot']
    text = request.form['text']


    #TODO:apply encrypting to the submitted text

app.run()