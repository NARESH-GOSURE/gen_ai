import requests

class TenantLogin:
    def __init__(self, url, tenant_name, username, password):
        self.api_url = f"{url}/api/v1/users/login"
        self.headers = {"X-Tenant": tenant_name}
        self.json_data = {"username": username, "password": password}
        self.access_token = None

    def tenant_login(self):
        try:
            response = requests.post(self.api_url, headers=self.headers, json=self.json_data)
            if response.status_code == 200:
                api_response = response.json()
                self.access_token = api_response.get("accessToken")
                return self.access_token
            else:
                print(f"Response Failed : {response.status_code}")
                return response.text
        except Exception as error:
            print(f"Error Occurred : {error}")
            return None

if __name__ == "__main__":
    url = "http://localhost:8080"  #config.get_gosure_base_url()
    tenant = "nia"                 #config.get_gosure_tenant()
    username = "admin@gosure.ai"    #config.get_gosure_tenant_username()
    password = "123456"             #config.get_gosure_tenant_password()

    login = TenantLogin(url, tenant, username, password)
    access_token = login.tenant_login()
    if access_token:
        print("AccessToken:", access_token)
    else:
        print("Error in getting access token.")

