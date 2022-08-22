# Using flask to make an api
# import necessary libraries and functions
from pickle import TRUE
from sre_constants import SUCCESS
from flask import Flask, jsonify, render_template, request
from flask_validate_json import validate_json

import sqlite3
  
# creating a Flask app
app = Flask(__name__)


@app.route('/api/weather/stats/', methods = ['GET'])
def get_stats():
    with sqlite3.connect('./temp.db') as db:
        db.row_factory = sqlite3.Row  
        arguments = request.args
        clauses = []
        if 'station' in arguments:
            station = arguments["station"]
            clauses.append(f"station='{station}'")
        if 'year' in arguments:
        	dparam = arguments["year"]
        	clauses.append(f"year='{dparam}'")
        clause = ""
        if len(clauses):
        	clause =" where " + " and ".join(clauses)
        
        cursor_obj = db.cursor()
        cursor_obj.execute(f'SELECT * FROM WEATHER_DATA_STATS {clause}')
        data = cursor_obj.fetchall()
        data = [ list(row) for row in data ]
        return to_json(data);

@app.route('/api/weather/', methods = ['GET'])
def get_weather():
    with sqlite3.connect('./temp.db') as db:
        db.row_factory = sqlite3.Row  
        arguments = request.args
        clauses = []
        if 'station' in arguments:
            station = arguments["station"]
            clauses.append(f"station='{station}'")
        if 'date' in arguments:
        	date_param = arguments["date"]
        	clauses.append(f"row_date='{date_param}'")   
        clause = ""
        if len(clauses):
        	clause =" where " + " and ".join(clauses)
        
        cursor_obj = db.cursor()
        cursor_obj.execute(f'SELECT * FROM WEATHER {clause}')
        data = cursor_obj.fetchall()
        data = [ list(row) for row in data ]
        return to_json(data);

@app.route('/api/yield/', methods = ['GET'])
def get_yield():
    with sqlite3.connect('./temp.db') as db:
        db.row_factory = sqlite3.Row  
        arguments = request.args
        clauses = []
        if 'station' in arguments:
            station = arguments["station"]
            clauses.append(f"station='{station}'")
        if 'year' in arguments:
        	date_param = arguments["year"]
        	clauses.append(f"year='{date_param}'") 
        where_clause = ""
        if len(clauses):
        	where_clause =" where " + " and ".join(clauses)
        
        cursor_obj = db.cursor()
        cursor_obj.execute(f'SELECT * FROM YIELD {where_clause}')
        data = cursor_obj.fetchall()
        data = [ list(row) for row in data ]
        return to_json(data);


def to_json(data):
    response =  jsonify({
        "success": True,
        "data": data,
        "message": "success"
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
  
    return response 

# driver function
if __name__ == '__main__':
  
    app.run(debug = True)