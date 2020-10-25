from flask import Flask, request, render_template, jsonify
import localData
import utils
import requests
from bs4 import BeautifulSoup as bs


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/good')
def good():
    statusGoodL = utils.statusGoodL(localData.getGoodL("20200828_good.db"))
    return render_template('good.html', goodL=statusGoodL)


@app.route('/candidate')
def candidate():
    return render_template('candidate.html')


@app.route('/screener')
def screener():
    return render_template('screener.html')


@app.route('/screener_input')
def screener_input():
    args = request.args
    name = args['name']
    name = str(int(name) * 10)
    return name


@app.route('/screener_fund')
def screener_fund():
    # 이거 페이지 32페이지 까지 있음
    dataL = utils.crawlingSise()
    return jsonify(dataL=dataL)


@app.route('/change_status')
def change_status():
    args = request.args
    code = args['code']
    status = args['status']
    newStatus = localData.changeStatus(code, status)
    if newStatus == "Having":
        buttonName = "매도"
        removeClass = "btn-warning"
        addClass = "btn-success"
    else:
        buttonName = "매수"
        removeClass = "btn-success"
        addClass = "btn-warning"
    return jsonify(newStatus=newStatus, buttonName=buttonName, removeClass=removeClass, addClass=addClass)


if __name__ == '__main__':
    localData.dataUpdate("")
