from flask import Flask
from flask import request
from tinderstats import stats
from flask import json
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print(request.files)
        file = request.files.get('file', None)
        file.seek(0)
        result = stats(json.loads(file.read()))
        return render_template("table.html", data=result)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()