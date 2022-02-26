"""Constants used by the Nest component."""

DOMAIN = "nest"
DATA_SDM = "sdm"
DATA_SUBSCRIBER = "subscriber"
DATA_NEST_CONFIG = "nest_config"

WEB_AUTH_DOMAIN = DOMAIN
INSTALLED_AUTH_DOMAIN = f"{DOMAIN}.installed"

DEFAULT_API_HOSTNAME = "smartdevicemanagement.googleapis.com"
DEFAULT_OAUTH_HOSTNAME = "nestservices.google.com"

CONF_PROJECT_ID = "project_id"
CONF_SUBSCRIBER_ID = "subscriber_id"
CONF_CLOUD_PROJECT_ID = "cloud_project_id"
CONF_API_HOSTNAME = "api_hostname"
CONF_OAUTH_HOSTNAME = "oauth_hostname"

SIGNAL_NEST_UPDATE = "nest_update"

# For the Google Nest Device Access API
OAUTH2_AUTHORIZE = "https://{oauth_hostname}/partnerconnections/{project_id}/auth"
OAUTH2_TOKEN = "https://www.googleapis.com/oauth2/v4/token"
SDM_SCOPES = [
    "https://www.googleapis.com/auth/sdm.service",
    "https://www.googleapis.com/auth/pubsub",
]
API_URL = "https://{api_hostname}/v1"
OOB_REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
