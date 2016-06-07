import subprocess
import constant_vars
import os
import datetime
import threading

class Crawler:

	def __init__(self) :
		pass

	def Grab(self, mode, list, label) :

		parameter = [constant_vars.CURL_FILE, "-H", "User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 FirePHP/0.7.4","--max-time", "10000", "--write-out", "%{http_code}", "--silent"]
		DETACHED_PROCESS = 0x00000008
		
		for l in list :
			parameter.append(l)

		if mode == "must200" :

			proc = subprocess.Popen(parameter,stdout=subprocess.PIPE, creationflags=DETACHED_PROCESS)
			(out, err) = proc.communicate()
			
			if str(out) == "b'200'" :
				info = "OK"
			else :
				info = "BAD"

			file  = self.outputfile(list)

			if file :
				mod   = self.modification_date(file)
				mod   = str(mod).split('.')
				_size = os.path.getsize(file)
				size  = self.sizeof_fmt(_size)
			else :
				mod   = "-"
				_size = None
				size  = None

			result = {
				"status_code"   : str(out),
				"info"	        : info,
				"label"		    : label,
				"file_size"		: size,
				"file_size_byte": _size,
				"time_modified" : mod[0]
			}

			return result
				
		elif mode == "onceshoot" :

			proc = subprocess.Popen(parameter,stdout=subprocess.PIPE, creationflags=DETACHED_PROCESS)

			for line in iter(proc.stdout.read, b''):
			    return line
			proc.stdout.close()
			proc.wait()

	def outputfile(self, params) :
		index = 0
		for p in params :
			if p == '-o' :
				the_file = params[index + 1]
				# print(the_file)
				return the_file
			# print(str(index) + "=>" + p)
			index += 1

	def modification_date(self, filename) :
		t = os.path.getmtime(filename)
		return datetime.datetime.fromtimestamp(t)
		
	def sizeof_fmt(self, num):
		for x in ['bytes','KB','MB','GB','TB']:
			if num < 1024.0:
				return "%3.1f %s" % (num, x)
			num /= 1024.0			

if __name__ == "__main__" :
	Crawler.Grab('onceshoot', ['http://10.29.254.215'], "")