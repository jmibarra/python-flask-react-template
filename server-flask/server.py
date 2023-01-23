from flask import Flask

app = Flask(__name__)

#Data API Route

@app.route("/members")
def members():
    return {"members": ["data1","data2","data3"]}

if __name__ == "__main__":
    app.run(debug=True)