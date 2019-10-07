import json

from django.core.exceptions import ImproperlyConfigured

from mysite.settings.base import *


with open(BASE_DIR + "/config/secrets.json") as f:
    secrets = json.loads(f.read())


def get_env_variable(variable_name):
    """
    Get a secret value stored inside your environment variable
    :param variable_name: the name of the variable
    :return: the secret string
    """
    try:
        return secrets[variable_name]
    except KeyError:
        error_msg = f'Set the {variable_name} variable.'
        raise ImproperlyConfigured(error_msg)


# Configure default database for dev
# secret keys configured as environment variables

DATABASES['default']['USER'] = get_env_variable('db_user')
DATABASES['default']['PASSWORD'] = get_env_variable('db_password')
DATABASES['default']['ENGINE'] = get_env_variable('db_type')

if '__name__' == '__main__':
    db = DATABASES
