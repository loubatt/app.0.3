import queue
import threading
import os
import datetime
import glob
from auth import Auth
from crawler import Crawler
import constant_vars

# tahunranking = 

class Appportal:

	def __init__(self, gui):
		self.auth    = Auth()
		self.gui     = gui
		self.crawler = Crawler()
		self.tahunranking   = ""
		self.total_job      = 0
		self.thread_counter = 0
		self.success_thread_counter = 0
		self.bad_thread_counter = 0

	def Thread_DownloadRankingKanwil(self, tahun, bulan) :
		t = threading.Thread(target = self.CrawlRankingKanwil, args = (tahun, bulan))
		t.daemon = True
		t.start()

	def Thread_ConvertHTMLtoMARK(self, tahun, bulan) :
		t = threading.Thread(target = self.CrawlRankingKanwil, args = (tahun, bulan))
		t.daemon = True
		t.start()

	def Thread_CekAuth(self) :
		t = threading.Thread(target = self.CheckAuth, args = ())
		t.daemon = True
		t.start()

	def Thread_Login(self) :
		username    = self.gui.form_username.get()
		password    = self.gui.form_password.get()

		t = threading.Thread(target = self.doLogin, args = (username, password))
		t.daemon = True
		t.start()

	def doLogin(self, username, password) :
		q = queue.Queue()
		q.put(self.auth.Login(username, password))
		q.put(self.CheckAuth())

	def CheckAuth(self) :
		result = self.auth.CheckAuth()
		if result['status_auth'] == 1 :
			self.gui.stream_info.insert("end", "Valid user !\n")
			self.gui.status_state.config(text="Done")
			# self.gui.menudownloadranking_btn.config(state="normal")
			self.Prepare_DownloadRanking()
		else :
			self.gui.menudownloadranking_btn.config(text="Download Ranking Kanwil")
			self.gui.menudownloadranking_btn.config(state="normal")
			self.gui.Render_Appportal_LoginForm()

	def CrawlRankingKanwil(self, tahun, bulan) :
		self.tahun = tahun
		self.bulan = bulan
		nama_file_html = tahun + bulan + bulan + ".html"
		params         = "tahun=" + tahun + "&bulan1=" + bulan + "&bulan2=" + bulan + "&kanwil=000&urut=PENCAPAIAN"
		status = self.crawler.Grab("must200",[
					constant_vars.URL_RANKINGKANWIL + params,
					"-b", constant_vars.COOKIE_FILE,
					"-o", constant_vars.RANKINGKANWIL_HTML_FOLDER + "\\" + nama_file_html
					], nama_file_html)
		self.thread_counter += 1
		
		if status['info'] == "OK" :
			self.success_thread_counter += 1
		else :
			self.bad_thread_counter += 1
			self.Thread_DownloadRankingKanwil(tahun, bulan)

		# Streammer
		self.gui.stream_info.insert("end", 
			str(self.thread_counter) + "\t" +
			str(status['label']) + "\t" + 
			str(status['time_modified']) + "\t" + 
			str(status['status_code']) + "\t" + 
			str(status['file_size']) + "\n")

		# Evaluator
		if self.total_job == self.success_thread_counter :
			# Download ranking Done
			self.gui.popupTahunRanking.destroy()
			self.gui.status_state.config(text="Done")
			# Lakukan konversi ke .mark
			self.Thread_ConvertHTMLtoMARK()
		msg = str(self.total_job) + " Job \t" + str(self.success_thread_counter) + " Ok \t" + str(self.bad_thread_counter) + " Bad \t"  + str(self.thread_counter) + " Total"
		self.gui.status_info.config(text=msg)

	def Prepare_DownloadRanking(self) :
		if self.auth.status_auth == 0 :
			self.gui.Render_Appportal_LoginForm()
		else :
			self.gui.Render_Appportal_TahunRankingForm()

	def doDownloadRankingKanwil(self) :
		
		''' method ini dieksekusi setelah pilih tahun ranking'''
		
		# bersihkan stream info
		self.gui.stream_info.delete(1.0, "end")
		
		# 
		self.gui.status_state.config(text="loading...")
		self.gui.downloadranking_btn.config(state="disabled")

		# reset thread counter
		self.thread_counter = 0
		self.success_thread_counter = 0
		self.bad_thread_counter = 0

		self.tahunranking = self.gui.form_tahunranking.get()

		bulan = ['01','02','03','04','05','06','07','08','09','10','11','12']
		for _bulan in bulan :
			self.Thread_DownloadRankingKanwil(tahun, _bulan)

		self.total_job = len(bulan)

	def DownloadRankingKanwil(self) :
		'''Lakukan download hanya jika user telah login (queue)'''
		self.gui.status_state.config(text="loading...")
		# self.gui.status_state.config(state="disabled")

		# self.gui.status_state.config(text="Loading...")
		self.gui.stream_info.delete(1.0, "end")
		# reset thread counter
		self.thread_counter = 0
		self.success_thread_counter = 0
		self.bad_thread_counter = 0		
		self.Thread_CekAuth()

	def CekHasilDownloadRankingKanwil(self, tahun) :

		folder = constant_vars.RANKINGKANWIL_HTML_FOLDER
		os.chdir(folder)
		bundel = glob.glob(tahun + "*")
		count = 1
		for files in  bundel :
			mod = self.modification_date(folder + "\\" + files)
			mod = str(mod).split('.')
			size = os.path.getsize(folder + "\\" + files)
			size = self.sizeof_fmt(size)
			self.gui.stream_info.insert("end", str(count) + " " + files + " " + mod[0] + " " + str(size))
			count += 1

	def Login(self) :
		self.Thread_Login()

	def ConvertHTMLtoMark
		