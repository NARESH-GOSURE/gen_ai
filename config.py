import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

def get_gosure_base_url():
    return os.environ.get("GOSURE_BASE_URL")


def get_gosure_tenant():
    return os.environ.get("GOSURE_TENANT")


def get_gosure_tenant_username():
    return os.environ.get("GOSURE_TENANT_USERNAME")


def get_gosure_tenant_password():
    return os.environ.get("GOSURE_TENANT_PASSWORD")
