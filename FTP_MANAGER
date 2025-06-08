import os
from ftplib import FTP
from time_manager import time_manager
class FTP_MANAGER:
	def __init__(self,IP_ADD,USER,PASS,DIR,DIR_DEST,MOD_STR,ID_STR):
		self.IP_ADD = IP_ADD
		self.USER = USER
		self.PASS = PASS
		self.DIR = DIR
		self.DIR_DEST = DIR_DEST
		self.MOD_STR = MOD_STR
		self.ID_STR = ID_STR
		self.FTP = None
		self.FILES_LIST = None
		self.array_list = []
		self.date_string = None
		self.ftp_connect()
		self.set_date_str()
		self.check_directory_save()
		self.get_list_files()
		self.download_list()
		self.remove_local_files()
		self.remove_remote_files()
		self.end_ftp()

	def set_date_str(self):
		obj_time = time_manager()
		self.date_string = obj_time.get_date_str()

	def check_directory_save(self):
		path = self.DIR_DEST+'/'+self.date_string+"/"+self.MOD_STR + "/" + self.ID_STR
		isExist = os.path.exists(path)
		if isExist == False:
			print("create dir")
			os.makedirs(path)
		else:
			print("ok")
		self.DIR_DEST = self.DIR_DEST+'/'+self.date_string+"/"+self.MOD_STR + "/" + self.ID_STR
		print(self.DIR_DEST)
		print(isExist)

	def ftp_connect(self):
		self.FTP = FTP(self.IP_ADD, user=self.USER, passwd=self.PASS)
		self.FTP.cwd(self.DIR)

	def get_list_files(self):
		self.FILES_LIST = self.FTP.nlst()
		for files in self.FILES_LIST:
			self.array_list.append(files)

	def download_list(self):
		print(self.date_string)
		xlen = len(self.array_list)
		for x in range(xlen):
			name_str = self.array_list[x]
			print(name_str)
			with open(name_str, 'wb') as local_file:
				self.FTP.retrbinary("RETR " + name_str, open(self.DIR_DEST+ '\\' + name_str, 'wb').write)


	def remove_local_files(self):
		xlen = len(self.array_list)
		for x in range(xlen):
			os.remove(str(self.array_list[x]))

	def remove_remote_files(self):
		for x in range(len(self.array_list)):
			self.FTP.delete(self.array_list[x])
	
	def end_ftp(self):
		self.FTP.quit()


FTP_OBJECT = FTP_MANAGER('10.52.150.65','trebor','x509w802.11','/home/trebor/Pictures/',"download","MDF","00001")
