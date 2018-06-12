import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/')
def hello():
    #return redirect("http://www.google.com", code=302)
    return redirect("http://localhost:3000", code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)