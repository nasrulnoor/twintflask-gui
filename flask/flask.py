from flask import Flask , render_template,redirect,url_for
from waitress import serve
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   #app.run(debug = True) // Uncomment if you want to use in Development Environment 
   serve(app, host='0.0.0.0', port=5001) #For Production Environment 
