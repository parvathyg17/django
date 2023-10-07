from flask import Flask
from flask import render_template
app=Flask(__name__)


@app.route('/ad')
def hello_world():
    return 'Hello World'

    
@app.route('/')
def home():
    d="Kevin"
    return render_template('home.html',n=d)

@app.route('/prm2')
def prm2():
    x=[1,2,3,4,5]
    y={'name':'Ann','Age':'21','Place':'kochi'}
    return render_template('prm2.html',n=x,s=y)

if __name__=='__main__':
    app.run()