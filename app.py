from flask import Flask, render_template, request
import twint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']
        
        c = twint.Config()
        c.Search = search_term
        c.Limit = 10
        c.Store_object = True
        twint.run.Search(c)
        
        tweets = twint.output.tweets_list
        return render_template('index.html', tweets=tweets, search_term=search_term)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
