from flask import Flask, render_template

ob = Flask(__name__)


@ob.route('/')
def glavnstr():
    return render_template('index.html')



if __name__=='__main__':
    ob.run(debug=True)