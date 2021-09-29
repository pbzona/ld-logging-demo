from dotenv import load_dotenv
load_dotenv()

import ldclient
from ldclient.config import Config

import os
import time

# Setup client
ld_sdk_key = os.environ.get('LD_SDK_KEY')
ldclient.set_config(Config(ld_sdk_key))
ld_client = ldclient.get()

# Encryption details
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# This is the data
data = b'This is some top secret customer data!'

def get_message():
    if ld_client.variation('configure-encrypt-logs', {"key": 123}, True):
        return str(cipher_suite.encrypt(data))
    else:
        return str(data)

# Loop output to illustrate changes in a running process
while True:
    print(get_message() + '\n')
    time.sleep(1)

# Cleanup
ld_client.flush()
time.sleep(5)
ld_client.close()
