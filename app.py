from flask import Flask, render_template, request, jsonify
from nLocation import getInfo
from model import predict_seaice_extent_from_date,predict_seaice_extent_from_temp, predict_panic_temp, predict_panic_year

app = Flask(__name__)

mylist = ["index","Glacier ID","Political Unit","Continent", "Basin Code","Location Code","Glacier Code","Latitude","Longitude","Primary Class","Minimum Elevation","Mean Elevation","Maximum Elevation","Accumulation Orientation","Ablation Orientation","Topographic Map Year","Topographic Map Scale"]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.htm')

@app.route('/map')
def map():
    return render_template('map.htm', title="Map")

@app.route('/info', methods=['GET','POST'])
def info():
    if request.method == 'POST':
        lat = request.form['lat']
        lng = request.form['lng']
        df = getInfo(float(lat), float(lng))
        return render_template('info.htm', cryosphere=df.values, mylist=mylist, lat=lat, lng=lng, title="Info")
    else:
        return render_template('map.htm', title="Map")

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        valuetype = int(request.form['type'])
        if(valuetype == 1):
            result = predict_seaice_extent_from_date(float(request.form['inputValue']))
            result_10_year = predict_panic_year(float(request.form['inputValue']))
            result_10_temp = predict_panic_temp(60)
        if(valuetype == 2):
            result = predict_seaice_extent_from_temp(float(request.form['inputValue']))
            result_10_year = predict_panic_year(2020)
            result_10_temp = predict_panic_temp(float(request.form['inputValue']))
        return render_template('prediction.htm', title="Prediction", result=result, result_10_year=result_10_year, result_10_temp=result_10_temp, value=request.form['inputValue'])
    else:
        return "Pred"


