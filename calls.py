from codebase import code


class Calls:

	def __init__(self):
		self.base_url = "https://api.tdameritrade.com/v1"



	def get_access_token(self):
		pass


cb = code.Codebase()
cb.open_connection()

print(cb.auth_code)
