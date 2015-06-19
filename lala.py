import os

envhost = os.getenv('REDIS_HOST', 'redis')

if envhost == 'redis':
  print 'asdf'
  print 'r'
else:
  print 'x'
