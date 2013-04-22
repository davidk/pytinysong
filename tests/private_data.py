import os
# Replace API_KEY with your personal API key from Tinysong if you want 
# to run tests.
if 'TRAVIS_SECURE_ENV_VARS' in os.environ and os.environ['TRAVIS_SECURE_ENV_VARS'] == 'true':
    KEY = os.environ['KEY']
else:
    KEY=''
