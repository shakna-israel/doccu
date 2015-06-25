import pickle

def gen_db():
    db = {"title":"Important Documentation","preamble":"This is a preamble paragraph.","descriptor":"This is a policy descriptor. Short and sweet.","version":"24","date":"2015-06-24","date-renew":"2016-06-24","category":["testdocs","testing"],"content":["Some content","is better","than none."]}
    pickle.dump(db,open("document.db","wb"))

if __name__ == "__main__":
    gen_db()
