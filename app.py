from flask import Flask

import redis
import os

envhost = os.getenv('REDIS_HOST', 'redis')
accesskey = os.getenv('REDIS_KEY', '')

print envhost
print accesskey

app = Flask(__name__)

if envhost == 'redis':
  r = redis.Redis(host=envhost, port=6379)
else:
  r = redis.StrictRedis(host=envhost, port=6380, db=0, password=accesskey, ssl=True)

@app.route('/')
def hello():
    r.incr('hits')
    return 'Hello NDC! I have been seen %(hits)s times, and read from %(host)s' % {"hits": r.get('hits'), "host": envhost}

@app.route('/d')
def debug():
    return 'H: %(host)s, K: %(key)s' % {"host": envhost, "key": accesskey}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
