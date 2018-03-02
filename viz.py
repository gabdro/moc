from flask import Flask
from flask import render_template

app = Flask(__name__)


def c3_format(tags,result):
    columns = []
    tag_db = [score for i,score in enumerate(result.T.values)]
    for i,tag in enumerate(tags):
        tag = i
        columns.append([tag]+list(tag_db[i]))
    return columns


@app.route("/")
def index():
    return "Hello, World"

@app.route("/graph")
def gen_graph():
    import pandas as pd
    fpath = "data/result_10.json"
    result = pd.read_json(fpath)
    tags = [col.strip() for col in result.columns] #['2ch','3DS',....,'GG']
    columns= c3_format(tags,result)
    return render_template("index.html",columns=columns[:100])

if __name__=="__main__":
    app.run(host="0.0.0.0", port=9999)
