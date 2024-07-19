# Copyright © 2024 Dell Inc. or its subsidiaries.

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
Returns an error message indicating that the specified environment variable is not set.

Parameters:
    envVarName (str): The name of the environment variable.

Returns:
    str: The error message indicating that the environment variable is not set.
"""
def getEnvNotSetErrorMsg(envVarName):
    return f"Error: {envVarName} is not set in the environment. Please check the .env file"

"""
Fetches the system authentication token.

Args:
    systemType (str): The type of the system.
    systemElementManagerIp (str): The IP address of the system element manager.
    systemUserName (str): The username for the system.
    systemPassword (str): The password for the system.

Returns:
    str: The system authentication token.

Raises:
    Exception: If the system authentication token cannot be fetched.

"""
def getSystemAccessToken(systemType, systemElementManagerIp, systemUserName, systemPassword):
    print("Fetching the system authentication token...")

    try:
        response = requests.post(
            f"https://{systemElementManagerIp}/rest/auth/login",
            headers={"Content-Type": "application/json"},
            json={"username": systemUserName, "password": systemPassword},
            verify=False
        )
    except Exception as e:
        print(f"Error: Failed to fetch the {systemType} authentication token, please validate the system IP {systemElementManagerIp}")
        print(e)
        exit(1) # Exit with error

    if(response.status_code == 401):
        print(f"Error: Failed to fetch the {systemType} authentication token, please validate the system credentials")
        exit(1) # Exit with error

    if(response.status_code < 200 or response.status_code >= 300):    
        print(f"Error: {response.json()}")
        exit(1) # Exit with error
    
    return response.json()["access_token"]

"""
Registers the trust of the APEX Navigator with the specified system.

Args:
    dellAuthToken (str): The Dell authentication token.
    systemType (str): The type of the system.
    systemId (str): The ID of the system.
    baseUrl (str): The fully qualified domain name.
    systemAuthToken (str): The system authentication token.

Returns:
    None

Raises:
    Exception: If there is an error while registering the trust.

"""
def registerTrust(dellAuthToken, systemType, systemId, baseUrl, systemAuthToken):
    print(f"Registering the trust of the APEX Navigator with the system {systemId}...")

    try:
        response = requests.post(
        f"{baseUrl}/rest/services/storage/v1/storage-systems/{systemType}-{systemId}/register-trust",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {dellAuthToken}"
        },
        json={
            "initial_access_token": systemAuthToken,
            "system_type": systemType
        },
        verify=False
    )
    except Exception as e:
        print(f"Error: Failed to register the trust, please validate the baseUrl {baseUrl}")
        print(e)
        exit(1) # Exit with error

    if(response.status_code == 401):
        print("Error: Please provide a valid Dell auth token")
        exit(1) # Exit with error

    if(response.status_code < 200 or response.status_code >= 300):    
        jsonResponse = response.json()
        print(f"Error: {jsonResponse['messages'][0]['message']}")
        print(f"Error code: {jsonResponse['messages'][0]['code']}")
        exit(1) # Exit with error

    if(response.status_code < 200 or response.status_code >= 204):    
        print(f"Trust is successfully registered with the system {systemId}")
        exit()