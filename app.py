from flask import Flask, render_template, jsonify
import pickledb

app = Flask(__name__)

@app.route("/")
@app.route("/<name>/")
def hello(name=None):
    return render_template('index.html',dicto={'some':'dict','other':'dict'})

@app.route("/document/<name>/")
def document_test(name):
    document_name = str(name) + ".db"
    document_db = pickledb.load(document_name, False)
    title = document_db.get('title')
    date = document_db.get('date')
    renew_date = document_db.get('date-renew')
    category = document_db.get('category')
    content = document_db.get('content')
    return render_template('document.html',title=title,date=date,renew_date=renew_date,category=category,content=content)

@app.route("/document/<name>/json/")
def json_test(name=None):
    document_name = str(name) + ".db"
    document_db = pickledb.load(document_name, False)
    title = document_db.get('title')
    date = document_db.get('date')
    renew_date = document_db.get('date-renew')
    category = document_db.get('category')
    content = document_db.get('content')
    return jsonify(title=title,date=date,renew_date=renew_date,category=category,content=content)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
