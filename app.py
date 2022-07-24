from flask import Flask
import housing
from housing.logger import logging
from housing import exception
import sys
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = exception.HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "Starting MAchine Learning Project"


if __name__=="__main__":
    app.run(debug=True)


