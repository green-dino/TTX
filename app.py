from flask import Flask, render_template, request
from utils.dread import RiskAssessment
from utils.risk import RiskAssessmentTool  # Import RiskAssessmentTool from risk.py
from utils.brr import RiskMatrix
from utils.disaster_recovery import steps,roles,functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', dread_result=None, risk_result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    damage = float(request.form['damage'])
    reproducibility = float(request.form['reproducibility'])
    exploitability = float(request.form['exploitability'])
    affected_users = float(request.form['affected_users'])
    discoverability = float(request.form['discoverability'])

    assessment = RiskAssessment(damage, reproducibility, exploitability, affected_users, discoverability)
    dread_result = {
        'damage': damage,
        'reproducibility': reproducibility,
        'exploitability': exploitability,
        'affected_users': affected_users,
        'discoverability': discoverability,
        'risk_value': assessment.calculate_dread_risk(),
        'risk_level': assessment.determine_risk_level(assessment.calculate_dread_risk())
    }

    return render_template('index.html', dread_result=dread_result, risk_result=None)

@app.route('/calculate_risk', methods=['POST'])
def calculate_risk():
    tp = float(request.form['tp'])
    vp = float(request.form['vp'])
    c = float(request.form['c'])
    i = float(request.form['i'])

    risk_tool = RiskAssessmentTool()
    risk_result = {
        'tp': tp,
        'vp': vp,
        'c': c,
        'i': i,
        'risk': risk_tool.calculate_risk(tp, vp, c, i)
    }

    return render_template('index.html', dread_result=None, risk_result=risk_result)

@app.route('/brr')
def brr():
    risk_tool = RiskMatrix()
    return render_template('index.html', risk_tool=risk_tool)

@app.route('/process_brr', methods=['POST'])
def process_brr():
    risk_tool = RiskMatrix()
    risk_tool.responses = [request.form[f'question_{i}'] for i in range(10)]
    matrix_names = risk_tool.determine_matrices()

    return render_template('brr_results.html', risk_tool=risk_tool, matrix_names=matrix_names)

@app.route('/steps')
def display_steps():
    return render_template('steps.html', steps=steps)

@app.route('/functions')
def display_functions():
    return render_template('functions.html', functions=functions)

@app.route('/roles')
def display_roles():
    return render_template('roles.html', roles=roles)


if __name__ == '__main__':
    app.run(debug=True)
