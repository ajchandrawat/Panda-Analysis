import discovery
import tweets
from flask import Flask, render_template, request , jsonify

app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def index():
  return render_template('data.html')

@app.route('/key',methods = ['POST', 'GET'])
def key():
  search = request.args.get('search' , '')
  key = discovery.getkey(search)
  return jsonify(key = key)

@app.route('/sent',methods = ['POST', 'GET'])
def sent():
  search = request.args.get('search' , '')
  sent = discovery.getsent(search)
  return jsonify(sent = sent)

@app.route('/ent',methods = ['POST', 'GET'])
def ent():
  search = request.args.get('search' , '')
  ent = discovery.getent(search)
  return jsonify(ent = ent)

@app.route('/stor',methods = ['POST', 'GET'])
def stor():
  search = request.args.get('search' , '')
  stor = discovery.getstor(search)
  return jsonify(stor = stor)

@app.route('/tweet',methods = ['POST', 'GET'])
def tweet():
  search = request.args.get('search' , '')
  tweet = tweets.gettweets(search)
  return jsonify(tweet = tweet)

if __name__ == '__main__':
   app.run(debug = True)