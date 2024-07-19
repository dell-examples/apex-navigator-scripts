# Register trust

This script registers trust between a Powerflex system and the APEX Navigator. This is a pre-requisite to use APEX Navigator to run data mobility operations on the system.
To register the trust, one must -
1) Get the Dell Identity access token
2) Get the Powerflex access token
3) Trigger the register-trust API with the required parameters

This script automates the step #2 and step #3.

Detailed documentation -

https://www.dell.com/support/manuals/en-us/apex-navigator-multi-cloud-storage/apex_nav_multicloud_serviceguide_pub/establishing-a-trust-relationship?guid=guid-2d9c2956-1737-4156-80d3-e81424ecbc06&lang=en-us


## How to run this script?

### Prerequisites

Ensure you have python 3.10 installed on the system.

Open the directory of the script in the terminal and run the following command to install necessary dependencies to run the script. This is a one time activity.

    pip install -r requirements.txt

### Please set the following variables in .env file before executing this script. 

1) DELL_AUTH_TOKEN: Dell Identity access token retrieved after following the steps mentioned in the [Authentication](https://developer.dell.com/apis/83acf3bf-becf-41d2-aa1c-b3deffc5e549/versions/1.0.0/docs/Auth.md) topic in APEX Navigator for Multicloud Storage API Guide.
2) SYSTEM_TYPE is defaulted to "POWERFLEX".
3) SYSTEM_ID: The swid/identifier of the system
4) BASE_URL: The base URL of the APIs as defined in [Dell API documentation](https://developer.dell.com/apis/83acf3bf-becf-41d2-aa1c-b3deffc5e549/versions/1.0.0/docs/Introduction.md)
4) POWERFLEX_USER_NAME: Username to authenticate with the Powerflex system
5) POWERFLEX_PASSWORD: Password to authenticate with the Powerflex system
6) POWERFLEX_ELEMENT_MANAGER_IP: Element manager IP or the hostname

### In the terminal window, execute below command to register the trust
    python .\register-trust.py
