import os
import inspect

PROGRAM_NAME 	  	 		= "Tool buat kerja"

BASE_PATH 		     		= os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
OUTPUT_FILES_FOLDER  		= BASE_PATH + "\\files"
AUTH_FOLDER          		= OUTPUT_FILES_FOLDER + "\\auth"
MISC_FOLDER          		= OUTPUT_FILES_FOLDER + "\\auth"
RANKINGKANWIL_FOLDER 		= OUTPUT_FILES_FOLDER + "\\appportal\\rankingkanwil"
RANKINGKANWIL_HTML_FOLDER 	= RANKINGKANWIL_FOLDER + "\html"
HOME_FILE            		= AUTH_FOLDER + "\\appportal-home.html"
CURL_FILE			 		= BASE_PATH + "\curl\curl.exe"

COOKIE_NAME	      	 		= "Appportal_cookie.txt"
COOKIE_FILE       	 		= MISC_FOLDER + "\\" + COOKIE_NAME

HOST        	  	 		= "http://appportal4.intranet.pajak.go.id/"
URL_HOME  		  	 		= HOST + "/portal/index.php"
URL_LOGIN		  	 		= HOST + "/login/login/loging_simpel"
URL_RANKINGKANWIL 	 		= HOST + "/portal/kinerja/hasil.php?"