from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""


    return '<!doctype html><html>Hi! This is the home page.<a href="/hello">Go to Hello</a><html>'

@app.route('/diss')
def say_insult():
  """ returns insults """

  player = request.args.get("person")
  insult = request.args.get("insultttype")


  return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, insult)

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          Compliment:
          <select name="complementtype">
            <option value= "awesome" >Awesome</option>
            <option value= "terrific" >Terrific</option>
            <option value= "fantastic" >Fantastic</option>
          </select><br>
          <input type="submit">
        </form>
        <form action="/diss">
          # <label>What's your name? <input type="text" name="person"></label><br>
          Insult:
          <select name="insultttype">
            <option value= "silly" >Silly</option>
            <option value= "dumb" >Dumb</option>
            <option value= "stupid" >Stupid</option>
          </select><br>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    my_compliment = request.args.get("complementtype")

    compliment = choice(AWESOMENESS)
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, my_compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
