from tkinter import *
import tkinter.scrolledtext as tkst
from appportal import Appportal

class Gui:

	def __init__(self, root):
		self.root      = root
		self.appportal = Appportal(self)

	def Render(self) :

		self.topFrame = Frame(height=20)
		self.topFrame.pack(side="top", fill=X)

		self.middleFrame = Frame()
		self.middleFrame.pack(fill="both")

		self.leftFrame = Frame(self.middleFrame, bg="green")
		self.leftFrame.pack(side="left",fill="x")

		self.rightFrame = Frame(self.middleFrame, bg="red")
		self.rightFrame.pack(side="right",fill="x", expand=1)

		self.bottomFrame = Frame(height=20)
		self.bottomFrame.pack(side="bottom", fill="both")
		
		# self.menudownloadranking_btn = Button(self.topFrame, text="Download Ranking Kanwil", command= self.Event_Appportal_DownloadRankingKanwil)
		# self.menudownloadranking_btn.pack(side="left")

		# self.btn_CekHasilDownloadRankingKanwil = Button(self.topFrame, text="Cek Hasil Download Ranking Kanwil", command= self.Event_Appportal_CekHasilDownloadRankingKanwil)
		# self.btn_CekHasilDownloadRankingKanwil.pack(side="left")

		self.task_info = tkst.ScrolledText( master = self.leftFrame, wrap   = "word", width  = 30, height = 25)
		self.task_info.pack(fill="both", expand=True)

		self.stream_info = tkst.ScrolledText( master = self.rightFrame, wrap   = "word",height = 25)
		self.stream_info.pack(fill="both", expand=True)

		self.status_state = Label(self.bottomFrame, text="Idle")
		self.status_state.pack(side="left")

		self.status_info = Label(self.bottomFrame)
		self.status_info.pack(side="right")

	def Menu(self) :
		# MENU
		self.menu_bar = Menu(self.root)

		self.appportal_menu = Menu(self.menu_bar, tearoff=0)
		self.appportal_menu.add_command(label="Update ranking kanwil", accelerator='', compound='left', underline=0, command=self.Event_Appportal_DownloadRankingKanwil)
		self.appportal_menu.add_command(label="Tarik PKPM", accelerator='', compound='left', underline=0, command=self.Event_Appportal_DownloadRankingKanwil)

		self.file_menu = Menu(self.menu_bar, tearoff=0)
		self.file_menu.add_command(label="Open", accelerator='', compound='left', underline=0, command=self.Event_Appportal_DownloadRankingKanwil)
		self.file_menu.add_command(label="Tambah Text", accelerator='', compound='left', underline=0, command=self.Event_Appportal_DownloadRankingKanwil)

		self.about_menu  	= Menu(self.menu_bar, tearoff=0)
		self.about_menu.add_command(label="Tools 0.1", accelerator='', compound='left', underline=0, command=self.Event_Appportal_DownloadRankingKanwil)

		self.edit_menu   	= Menu(self.menu_bar, tearoff=0)
		self.view_menu   	= Menu(self.menu_bar, tearoff=0)
		self.themes_menu 	= Menu(self.view_menu, tearoff=0)

		self.view_menu.add_checkbutton(label="Show Line Number")
		self.view_menu.add_cascade(label="Themes", menu=self.themes_menu)
		self.themes_menu.add_radiobutton(label="Default")

		self.menu_bar.add_cascade(label='Appportal', menu=self.appportal_menu)
		# menu_bar.add_cascade(label='File', menu=file_menu)
		# menu_bar.add_cascade(label='Edit', menu=edit_menu)
		# menu_bar.add_cascade(label='View', menu=view_menu)
		self.menu_bar.add_cascade(label='About', menu=self.about_menu)

		self.root.config(menu=self.menu_bar)		

	def Render_Appportal_LoginForm(self) :

		self.popup = Toplevel()
		self.popup.title("Login Appportal")
		self.popup.iconbitmap(r'D:\\PROJECTS\\PYTHON\\python-app\\Kantor\\AppDesktop\\app.0.3\\images\\window.ico')

		self.label_1 = Label(self.popup, text="Username")
		self.label_2 = Label(self.popup, text="Password")

		self.form_username = Entry(self.popup)
		self.form_password = Entry(self.popup, show="*")

		self.label_1.pack(side=LEFT,fill=X)
		self.form_username.pack(side=LEFT,fill=X)

		self.label_2.pack(side=LEFT,fill=X)
		self.form_password.pack(side=LEFT,fill=X)

		self.logbtn = Button(self.popup, text="Login", command = self.Event_Appportal_Login)
		self.logbtn.pack(side=LEFT, expand=1, fill=X)

		self.popup.resizable(width=FALSE, height=FALSE)
		self.popup.geometry("400x200")

	def Render_Appportal_TahunRankingForm(self) :

		self.popupTahunRanking = Toplevel()
		self.popupTahunRanking.title("Tahun Ranking")
		self.popupTahunRanking.iconbitmap(r'D:\\PROJECTS\\PYTHON\\python-app\\Kantor\\AppDesktop\\app.0.3\\images\\window.ico')

		self.form_tahunranking  = Entry(self.popupTahunRanking)
		self.form_tahunranking.pack(side="left", fill="x", expand=1)

		self.downloadranking_btn = Button(self.popupTahunRanking, text="Download", command = self.Event_Appportal_do_DownloadRankingKanwil)
		self.downloadranking_btn.pack(side="left")

		self.popupTahunRanking.resizable(width=FALSE, height=FALSE)
		self.popupTahunRanking.geometry("400x200")

	def Event_Appportal_DownloadRankingKanwil(self) :
		self.appportal.DownloadRankingKanwil()

	def Event_Appportal_do_DownloadRankingKanwil(self) :
		self.appportal.doDownloadRankingKanwil()

	def Event_Appportal_CekHasilDownloadRankingKanwil(self) :
		self.appportal.CekHasilDownloadRankingKanwil()

	def Event_Appportal_Login(self) :
		self.appportal.Login()