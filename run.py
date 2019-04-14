#!/usr/bin/python3
# 2019-04-12 arrivato alla fine del pdf
from flask import Flask, render_template
import datetime
from flask import request
import platform

app = Flask(__name__)

@app.template_filter("datetimefilter")
def datetimefilter(value, format='%Y-%m-%d %02H:%02M:%02S'):
  """Convert a datetime to a differentformat."""
  return value.strftime(format)

#app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route("/")
def root():
  return render_template(
    'template.html',
    my_string="root page", 
    my_list=['a','b','c','d','e','f'],
    current_time=datetime.datetime.now(),
    title="/",
    pyVer=platform.python_version()
  )

@app.route("/home")
def home():
  return render_template(
    'template.html',
    my_string="home page",
    my_list=[0,1,2,3,4,5],
    current_time=datetime.datetime.now(),
    title="Home"
  )

@app.route("/about")
def about():
  return render_template(
    'template.html',
    my_string="about page",
    my_list=['alfa','beta','gamma','delta'],
    current_time=datetime.datetime.now(),
    title="About"
  )

@app.route("/contact")
def contact():
  return render_template(
    'template.html',
    my_string="contact page",
    my_list=[0,'b','alfa','#'],
    current_time=datetime.datetime.now(),
    title="Contact Us"
  )

@app.route("/search", methods=['GET', 'POST'])
def search():
  if request.method == 'GET':
    return 'no get method, only post'
  else:
    keyword = request.form['keyword']
    return render_template(
      'template.html',
      my_string=keyword,
      my_list=[keyword, keyword + '1', keyword + '2', keyword + '3'],
      current_time=datetime.datetime.now(),
      title=keyword
  )

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'python ' + platform.python_version() + ' by by ...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
      raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
  app.run(debug=True)
