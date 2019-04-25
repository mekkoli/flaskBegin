from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "index or root web publish file"

if __name__ == '__main__':
  app.run(debug=True)
# flask on all interfaces
# app.run(debug=True, host='0.0.0.0')
 
# flask on other port > 1024
# app.run(debug=True, port=5555)

