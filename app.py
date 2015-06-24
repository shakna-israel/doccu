from flask import Flask, render_template, jsonify
import pickle

app = Flask(__name__,static_folder='static')

@app.route("/")
@app.route("/<name>/")
def hello(name=None):
    return render_template('index.html',dicto={'some':'dict','other':'dict'})

@app.route("/document/<name>/")
def document_test(name):
    document_name = str(name) + ".db"
    document = pickle.load(open(document_name, "rb"))
    title = document['title']
    date = document['date']
    renew_date = document['date-renew']
    category = document['category']
    content = document['content']
    return render_template('document.html',title=title,date=date,renew_date=renew_date,category=category,content=content)

@app.route("/document/<name>/json/")
def json_test(name=None):
    document_name = str(name) + ".db"
    document = pickle.load(open(document_name, "rb"))
    title = document['title']
    date = document['date']
    renew_date = document['date-renew']
    category = document['category']
    content = document['content']
    return jsonify(title=title,date=date,renew_date=renew_date,category=category,content=content)

app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
