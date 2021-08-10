import time
import urllib
import requests
from splinter import Browser
import os
import sys

class Codebase:

    def __init__(self):
        self.client_code = os.getenv("API_KEY")
        self.username = os.getenv("USERNAME")
        self.pwd = os.getenv("PWD")
        self.sec1 = os.getenv("SEC1")
        self.sec2 = os.getenv("SEC2")
        self.sec3 = os.getenv("SEC3")
        self.sec4 = os.getenv("SEC4")
        self.redirect_uri = 'https://localhost:8000'
        self.base_url = "https://api.tdameritrade.com/v1"



    def open_connection(self):
        executable_path =  r'D:\PY Files\My Projects\stockanalysis\dependencies\chromedriver'
        browser = Browser('chrome', executable_path=executable_path, headless = False)

        method = 'GET'
        url = 'https://auth.tdameritrade.com/auth?'
        payload = {'response_type': 'code', 'redirect_uri': self.redirect_uri, 'client_id': self.client_code}

        built_url = requests.Request(method, url, params= payload).prepare()
        # built_url = requests.get(url, params= payload)
        # print(built_url)
        # response = requests.post(method, url, params= payload)

        built_url = built_url.url
        browser.visit(built_url)

        browser.find_by_id("username0").first.fill(self.username)
        browser.find_by_id("password1").first.fill(self.pwd)
        browser.find_by_id("accept").first.click()


        browser.find_by_xpath('//*[@id="authform"]/main/details/summary').click()
        browser.find_by_name('init_secretquestion').click()


        if browser.is_text_present("In what city was your high school? (Enter full name of city only.)"):
            browser.find_by_name("su_secretquestion").first.fill(self.sec1)
        elif browser.is_text_present("In what city were you born?"):
            browser.find_by_name("su_secretquestion").first.fill(self.sec2)
        elif browser.is_text_present("What was your high school mascot?"):
            browser.find_by_name("su_secretquestion").first.fill(self.sec3)
        else:
            browser.find_by_name("su_secretquestion").first.fill(self.sec4)

        browser.find_by_xpath('//*[@id="authform"]/main/div[5]/span/label').first.click()

        browser.find_by_id("accept").first.click()
        browser.find_by_id("accept").first.click()
        time.sleep(1)
        new_url = browser.url
        parse_url = urllib.parse.unquote(new_url.split('code=')[1])
        browser.quit()


        return parse_url


    def get_access_token(self, grant_type, code, access_type="offline"):
        
        ''' refer to the post access token call on the ameritrade api documentation to get param 
        to get code variable, pass in open_connection method (return value is code)'''
        url = self.base_url + "/oauth2/token"
        payload = {"grant_type": grant_type, "access_type": access_type, "code": code, "client_id": self.client_code, "redirect_uri": self.redirect_uri}

        r = requests.post(url, data= payload)

        return r.json()


    def get_stock_quote(self, access_token, symbol):

        url = self.base_url + f"/marketdata/{symbol}/quotes"
        params = {"apikey": self.client_code}
        headers = {"Authorization": f"Bearer {access_token}"}

        r = requests.get(url, params = params, headers = headers)
        return r.json()

    def get_price_history(self, access_token, symbol, period_type="day", period="10"):
        url = self.base_url + f"/marketdata/{symbol}/pricehistory"
        params = {"apikey": self.client_code, "periodType": period_type, "period": period}
        headers = {"Authorization": f"Bearer {access_token}"}

        r = requests.get(url, params = params, headers = headers)
        return r.json()


# cb = Codebase()
# cb.open_connection()
# x = cb.get_access_token("authorization_code", cb.open_connection())
# # print(x)
# print(cb.get_price_history(x["access_token"], "KO"))
# # # print(cb.get_stock_quote(x["access_token"], "KO"))





