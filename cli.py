import uuid

import click
from dotenv import load_dotenv
import requests


# Environment Variables - set these in .env in the root directory
load_dotenv()
APP_ID = os.getenv("APP_ID")
VERSION = os.getenv("APP_VERSION")
CLIENT_ID = os.getenv("APP_CLIENT_ID")
CLIENT_SECRET = os.getenv("APP_CLIENT_SECRET")
AUTHORIZATION_BASE_URL = os.getenv("AMAZON_AUTHORIZATION_BASE_URL")
TOKEN_BASE_URL = os.getenv("AMAZON_TOKEN_BASE_URL")


@click.group()
def cli():
    """
    Generate Amazon Selling Partners API credentials.
    """
    pass


@click.command()
def generate_authorization_url(
    authorization_base_url=AUTHORIZATION_BASE_URL,
    app_id=APP_ID,
    version=VERSION,
    nonce=uuid.uuid4()
):
    """
    Generate an Amazon Selling Partners API authorization URL.
    End user who wants to use Mitto to pull data from Amazon SP APIs,
    logs into Amazon, loads this URL, and authenticates the Mitto app.
    The user is redirected to https://oauthdebugger.com/debug and
    provided data back (e.g. spapi_oauth_code).

    IMPORTANT: This response data is only valid for 5 minutes and must be used
    to generate a refresh token (see: generate_refresh_token command).
    """
    authorization_url = f"{authorization_base_url}?application_id={app_id}" \
                        f"&version={version}&state={nonce}"
    click.echo(authorization_url)


@click.command()
@click.argument("spapi_oauth_code")
def generate_refresh_token(
    spapi_oauth_code,
    token_base_url=TOKEN_BASE_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
):
    """
    Generate an Amazon Selling Partners API refresh token
    using an spapi_oauth_code.

    SPAPI_OAUTH_CODE is generated after the user authenticates the Mitto app
    with the authorization url (see: generate_authorization_url).

    This refresh token is used in Mitto Amazon SP IO jobs.
    """
    params = {
        "grant_type": "authorization_code",
        "code": spapi_oauth_code,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url=token_base_url, json=params)

    token_data = response.json()
    refresh_token = token_data["refresh_token"]

    click.echo(refresh_token)


cli.add_command(generate_authorization_url)
cli.add_command(generate_refresh_token)
