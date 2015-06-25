# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
import glob
try:
    import cpickle
except ImportError:
    import pickle

app = Flask(__name__,static_folder='static')

@app.route("/")
@app.route("/<name>/")
def hello(name=None):
    databases = glob.glob('*.db')
    policy_title = []
    policy_url = []
    for database in databases:
        document = pickle.load(open(database, "rb"))
        policy_title.append(document['title'])
        policy_url.append(database.replace(".db",''))
    return render_template('index.html',policies=policy_title,policy_url=policy_url)

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
    descriptor = document['descriptor'].replace('\r\n',' ')
    descriptor_json = document['descriptor'].replace('\r\n',' ').replace("'","\\'")
    preamble = document['preamble'].replace('\r\n',' ')
    preamble_json = document['preamble'].replace('\r\n',' ').replace("'","\\'")
    content = document['content']
    content_json = document['content']
    for item in content_json:
        item = item.replace("'","\\'")
    return render_template('document.html',title=title,date=date,renew_date=renew_date,version=version,category=category,content=content,descriptor=descriptor,preamble=preamble,descriptor_json=descriptor_json,preamble_json=preamble_json,content_json=content_json,file=name)

@app.route("/document/<name>/json/")
def json_fetch(name=None):
    document_name = str(name) + ".db"
    document = pickle.load(open(document_name, "rb"))
    title = document['title']
    date = document['date']
    renew_date = document['date-renew']
    version = document['version']
    category = document['category']
    descriptor = document['descriptor'].replace('\r\n',' ').replace("'","\\'")
    preamble = document['preamble'].replace('\r\n',' ').replace("'","\\'")
    content = document['content']
    for item in content:
        item = item.replace("'","\\'")
    return jsonify(title=title,date=date,renew_date=renew_date,version=version,category=category,content=content,descriptor=descriptor,preamble=preamble,file=name)

@app.route("/document/new/<name>/", methods=['GET','POST'])
def document_new(name):
    if request.method == 'GET':
        return render_template('new_document.html',title=name)
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        renew_date = request.form['date-renew']
        categories = request.form['category']
        category = categories.split(',')
        descriptor = request.form['descriptor']
        preamble = request.form['preamble']
        proper = request.form['document-proper']
        content = []
        for line in proper.split('\n'):
            line = line.replace('\r','')
            content.append(line)
        dict_to_store = {'title':title,'date':date,'date-renew':renew_date,'category':category,'descriptor':descriptor,'preamble':preamble,'content':content,'version':0}
        filename = str(name) + ".db"
        pickle.dump(dict_to_store,open(filename,"wb"))
        return render_template('new_document_submitted.html',title=title,filename=str(name))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
