from flask import Flask
from redis import Redis

app = Flask(__name__)
db = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    keys = [key.decode('utf-8') for key in db.keys()]
    if len(keys) > 0:
        message = 'DB size is ' + str(len(keys)) + '<br/><br/>' \
                  'Data Available on the DB: <br/>' \
                  '{}'.format('<br/>'.join([key + ': ' + db.get(key).decode('utf-8') for key in sorted(keys)]))
    else:
        message = 'Hello <br/><br/>' \
                  'DB is empty'
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
    # app.run(host="0.0.0.0", port=8080, debug=True)
