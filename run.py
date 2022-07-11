import os
from flask import Flask
import psycopg2
from squlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) #REMEMBER TO CHANGE TO DEBUG=FALSE BEFORE SUBMITTING!!#
