# Copyright © 2024 Dell Inc. or its subsidiaries.

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

import os
from dotenv import load_dotenv
import util

load_dotenv()  # take environment variables from .env.

DELL_AUTH_TOKEN = os.getenv('DELL_AUTH_TOKEN')
SYSTEM_TYPE = os.getenv('SYSTEM_TYPE')
SYSTEM_ID = os.getenv('SYSTEM_ID')
BASE_URL = os.getenv('BASE_URL')
SYSTEM_USER_NAME = os.getenv('POWERFLEX_USER_NAME')
SYSTEM_PASSWORD = os.getenv('POWERFLEX_PASSWORD')
SYSTEM_ELEMENT_MANAGER_IP = os.getenv('POWERFLEX_ELEMENT_MANAGER_IP')

def checkEnvironmentVariables():
    if DELL_AUTH_TOKEN is None:
        print(util.getEnvNotSetErrorMsg('DELL_AUTH_TOKEN'))
        exit(1) # Exit with error

    if SYSTEM_TYPE is None:
        print(util.getEnvNotSetErrorMsg('SYSTEM_TYPE'))
        exit(1) # Exit with error

    if SYSTEM_ID is None:
        print(util.getEnvNotSetErrorMsg('SYSTEM_ID'))
        exit(1) # Exit with error

    if BASE_URL is None:
        print(util.getEnvNotSetErrorMsg('BASE_URL'))
        exit(1) # Exit with error

    if SYSTEM_USER_NAME is None:
        print(util.getEnvNotSetErrorMsg('POWERFLEX_USER_NAME'))
        exit(1) # Exit with error

    if SYSTEM_PASSWORD is None:
        print(util.getEnvNotSetErrorMsg('POWERFLEX_PASSWORD'))
        exit(1) # Exit with error

    if SYSTEM_ELEMENT_MANAGER_IP is None:
        print(util.getEnvNotSetErrorMsg('POWERFLEX_ELEMENT_MANAGER_IP'))
        exit(1) # Exit with error

checkEnvironmentVariables()
SYSTEM_AUTH_TOKEN = util.getSystemAccessToken(SYSTEM_TYPE, SYSTEM_ELEMENT_MANAGER_IP, SYSTEM_USER_NAME, SYSTEM_PASSWORD)
util.registerTrust(DELL_AUTH_TOKEN, SYSTEM_TYPE, SYSTEM_ID, BASE_URL, SYSTEM_AUTH_TOKEN)