import os
import datetime
import threading
from crawler import Crawler
import constant_vars

status_auth = 0

class Auth :

	def __init__(self) :
		self.crawler     = Crawler()
		self.status_auth = status_auth

	def CheckAuth(self) :
		# crawl home
		result = self.crawler.Grab("must200", [constant_vars.URL_HOME, 
			"-b", constant_vars.COOKIE_FILE, 
			"-o", constant_vars.HOME_FILE], 
			"Curling home")

		if result['file_size_byte'] < 1000 :
			result['status_auth'] = 0
		else :
			result['status_auth'] = 1

		self.status_auth = result['status_auth']
		return result

	def Login(self, username, password) :

		result = self.crawler.Grab("must200", [constant_vars.URL_LOGIN,	
			"-d","username=" + username + "&password=" + password + "&sublogin=Login", 
			"-c", constant_vars.COOKIE_FILE,
		], "Proses Login \t\t\t\t")

		return result

	def modification_date(self, filename) :
		t = os.path.getmtime(filename)
		return datetime.datetime.fromtimestamp(t)
		
	def sizeof_fmt(self, num):
		for x in ['bytes','KB','MB','GB','TB']:
			if num < 1024.0:
				return "%3.1f %s" % (num, x)
			num /= 1024.0
