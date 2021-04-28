from app import app


@app.route('/garys-tricks/api/v1.0/gary-can-do/')
def get_tricks():
    return jsonify({'tricks': tricks})
