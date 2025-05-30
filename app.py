from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

OFFSET_FILE = 'offsets.json'

@app.route('/api/offsets')
def get_offsets():
    with open(OFFSET_FILE) as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/edit', methods=['GET', 'POST'])
def edit_offsets():
    if request.method == 'POST':
        data = dict(request.form)
        with open(OFFSET_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    with open(OFFSET_FILE) as f:
        offsets = json.load(f)
    return render_template('editor.html', offsets=offsets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
