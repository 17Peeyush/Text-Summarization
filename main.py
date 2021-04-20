import textsummarize
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

#Inheritance concept
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    userText = request.form['usertext']
    num=int(request.form['numsen'])
    result,usertext=textsummarize.textSummarize(userText,num)
    return render_template('index.html',sumtext=result)
    # return render_template('index2.html', sumtext=result, usertext=usertext)

if __name__=="__main__":
    app.run()