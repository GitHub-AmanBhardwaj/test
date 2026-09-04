from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello from Flask on Vercel!</h1><p>Deployment is working successfully.</p>"

if __name__ == '__main__':
    app.run()
