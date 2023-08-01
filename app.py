from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('./flask-crud-9cffe-1b467a0a4d77.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)  # creates Flask class instance
if __name__ == '__main__':  # starts the flask server
    app.run(use_reloader=True)


@app.route("/test", methods=['GET'])
def test():
    doc_ref = db.collection("users").document("alovelace")
    doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
    return jsonify({"Message": "Added the document"})


@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    print(data)
     
    dataDB = {"book_title": data['book_title'], "book_author": data['book_author'], "book_publicatin": data['book_publication'],
              "Description": data['Description']}
         
    doc_ref = db.collection("books")
    doc_ref.add(dataDB)
    return jsonify({"Message": "Added the document"})


@app.route("/get",methods=['GET'])
def get():
    docs = db.collection("books").stream()
    data={}
    for doc in docs:
        print(doc.to_dict())
        data.update(doc.to_dict())
    
    print(data)
    return data

@app.route("/health", methods=['GET'])
def give_status():
    return jsonify({"Message": "Healthy"})
