import requests

class WebShareIo:
    def __init__(self,key=None):
        if key == None:
            raise ValueError("Key is not provided.")

        self.host = "https://proxy.webshare.io/api/"
        self.headers = {"Authorization":f"Token {key}"}

    def request_handler(self,method=None,path=None,body=None):
        if method.lower() == "get":
            response = requests.get(self.host+path, headers=self.headers).json()
        elif method.lower() == "post" and body == None:
            response = requests.get(self.host+path, headers=self.headers,json=body).json()
        else:
            response = {"error":"Invalid request method."}
            
        return response

    def user_profile(self):
        return self.request_handler("GET","profile")

    def my_subscription(self):
        return self.request_handler("GET","subscription")

    def proxy_config(self):
        return self.request_handler("GET","proxy/config")
    
    def set_authorized_ip(self,ip=None):
        if key == None:
            raise ValueError("authorized ip missing.")
        return self.request_handler("POST","proxy/config",{"authorized_ips":[ip]})

    def reset_proxy_password(self):
        return self.request_handler("POST","proxy/config/reset_password")

    def proxy_list(self,page=None,countries=None):
        if page != None and countries != None:
            return self.request_handler("GET",f"proxy/list/?page={page}&countries={countries}")
        elif page != None and countries == None:
            return self.request_handler("GET",f"proxy/list/?page={page}")
        elif page == None and countries != None:
            return self.request_handler("GET",f"proxy/list/?countries={countries}")
        else:
            return self.request_handler("GET","proxy/list")

    def download_proxies(self,page=None,countries=None):
        response = self.proxy_list(page,countries)
        proxies = [f"{i['username']}:{i['password']}@{i['proxy_address']}:80" for i in response['results']]
        open("proxies.txt","w+").write("\n".join(proxies))
        print("Downloaded!\nFile name: proxies.txt.")
        
    def proxy_stats(self):
        return self.request_handler("GET","proxy/stats")

    def get_location(self,ip):
        return requests.get('http://lumtest.com/myip.json',proxies = {'http': "http://"+ip,'https': "http://"+ip}).json()



