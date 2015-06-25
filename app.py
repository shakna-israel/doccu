from flask import Flask, render_template, jsonify
import glob
try:
    import cpickle
except ImportError:
    import pickle

app = Flask(__name__,static_folder='static')

@app.route("/")
@app.route("/<name>/")
def hello(name=None):
    return render_template('index.html',dicto={'some':'dict','other':'dict'})

@app.route("/category/<name>/")
def show_category(name):
    databases = glob.glob('*.db')
    in_category = []
    in_category_url = []
    for database in databases:
        document = pickle.load(open(database, "rb"))
        if name in document['category']:
            in_category.append(document['title'])
            in_category_url.append(database.replace(".db",''))
    return render_template('category.html',name=name, in_category=in_category,url=in_category_url)

@app.route("/document/<name>/")
def document_fetch(name):
    document_name = str(name) + ".db"
    document = pickle.load(open(document_name, "rb"))
    title = document['title']
    date = document['date']
    renew_date = document['date-renew']
    version = document['version']
    category = document['category']
    descriptor = document['descriptor']
    preamble = document['preamble']
    content = document['content']
    return render_template('document.html',title=title,date=date,renew_date=renew_date,version=version,category=category,content=content,descriptor=descriptor,preamble=preamble,file=name)

@app.route("/document/<name>/json/")
def json_fetch(name=None):
    document_name = str(name) + ".db"
    document = pickle.load(open(document_name, "rb"))
    title = document['title']
    date = document['date']
    renew_date = document['date-renew']
    version = document['version']
    category = document['category']
    descriptor = document['descriptor']
    preamble = document['preamble']
    content = document['content']
    return jsonify(title=title,date=date,renew_date=renew_date,version=version,category=category,content=content,descriptor=descriptor,preamble=preamble,file=name)

@app.route("/document/new/<name>/")
def document_new(name):
    return "Not Yet Implemented"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
