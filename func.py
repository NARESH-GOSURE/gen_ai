from config import get_gosure_base_url
from src.login import TenantLogin
import config

if __name__ == "__main__":
    # url = "http://localhost:8080"
    # tenant = "nia"
    # username = "admin@gosure.ai"
    # password = "123456"

    url = config.get_gosure_base_url()
    tenant = config.get_gosure_tenant()
    username = config.get_gosure_tenant_username()
    password = config.get_gosure_tenant_password()

    login = TenantLogin(url, tenant, username, password)
    access_token = login.tenant_login()
    if access_token:
        print("AccessToken:", access_token)
    else:
        print("Error in getting access token.")
