from flask import Flask, render_template
import rdflib

app = Flask(__name__)

g = rdflib.Graph()
g.parse("upliftedDataset.ttl", format='turtle')


@app.route("/")
def editor():
    results = []
    return render_template("index.html", results=results, path='/')


@app.route("/query/1")
def query_one():
    question = "Surface of road types Electoral division (DED)wise"
    with open('sparql/1.txt','r') as queryData:
        results = g.query(queryData)

    return render_template("index.html", results=results, question=question, path='/query/1')


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
