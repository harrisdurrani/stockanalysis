import time
import urllib
import requests
from splinter import Browser
from dotenv import load_dotenv
import os


# load_dotenv()
# client = os.getenv("API_KEY")
# username = os.getenv("USERNAME")

# print(client)
# print(username)
class Codebase:

	def __init__(self):
		self.client_code = os.getenv("API_KEY")
		self.username = os.getenv("USERNAME")
		self.pwd = os.getenv("PWD")
		self.sec1 = os.getenv("SEC1")
		self.sec2 = os.getenv("SEC2")
		self.sec3 = os.getenv("SEC3")
		self.sec4 = os.getenv("SEC4")
		self.auth_code = os.getenv("AUTH_CODE")
		self.redirect_uri = 'https://localhost:8000'




	def open_connection(self):
		executable_path = {'executable_path': r'D:\PY Files\My Projects\stockanalysis\dependencies\chromedriver'}
		browser = Browser('chrome', **executable_path, headless = False)

		method = 'GET'
		url = 'https://auth.tdameritrade.com/auth?'
		payload = {'response_type': 'code', 'redirect_uri': self.redirect_uri, 'client_id': self.client_code}

		built_url = requests.Request(method, url, params= payload).prepare()
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

