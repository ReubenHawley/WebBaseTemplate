import os
from django.core.management.utils import get_random_secret_key

if __name__ == '__main__':
    os.environ.setdefault(key="ENV_NAME", value="Development")
    os.environ.setdefault(key="SECRET_KEY", value=get_random_secret_key())
