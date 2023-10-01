from flask import Flask, render_template, request

from utils.dread import RiskAssessment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    damage = float(request.form['damage'])
    reproducibility = float(request.form['reproducibility'])
    exploitability = float(request.form['exploitability'])
    affected_users = float(request.form['affected_users'])
    discoverability = float(request.form['discoverability'])

    assessment = RiskAssessment(damage, reproducibility, exploitability, affected_users, discoverability)
    result = {
        'damage': damage,
        'reproducibility': reproducibility,
        'exploitability': exploitability,
        'affected_users': affected_users,
        'discoverability': discoverability,
        'risk_value': assessment.calculate_dread_risk(),
        'risk_level': assessment.determine_risk_level(assessment.calculate_dread_risk())
    }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
