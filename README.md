
Python CLI for generating credentials allowing [Mitto](https://www.zuar.com/help/mitto/) to pull data from [Amazon Selling Partners API](https://github.com/amzn/selling-partner-api-docs).

## Installing

### Create a virtual environment and install the package with pip
```bash
cd /path/to/project
virtualenv venv
. venv/bin/activate
pip install --editable .
```

### Create an .env file
APP_ID=  
APP_VERSION=beta
APP_CLIENT_ID=  
APP_CLIENT_SECRET=   
AMAZON_AUTHORIZATION_BASE_URL=https://sellercentral.amazon.com/apps/authorize/consent
AMAZON_TOKEN_BASE_URL=https://api.amazon.com/auth/o2/token

### Run the CLI
```bash
cli --help
```
