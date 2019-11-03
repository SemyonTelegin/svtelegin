import vk_api
from vk_api.longpoll import VkLongPoll
import time
import random
import re
import requests
import urllib.request

class Parser:                           
    def __init__(self, source=""):
        self.source = str(source)

    def exists(self, from_, to_):                 #Проверяет наличие чего-либо между двух последовательностей символов
        id1 = self.source.find(from_)
        if id1 == -1:
            return None
        id2 = self.source.find(to_, id1 + len(from_))
        if id2 == -1:
            return None
        return id1, id2

    def unjail(self, from_, to_):                       #Находит первое вхождение (если оно есть)
        if self.exists(from_, to_):
            id1, id2 = self.exists(from_, to_)
        else:
            return None
        res = self.source[id1 + len(from_):id2]
        self.source = self.source[:id1] + self.source[id2 + len(to_):]
        return res

    def unjail_all(self, from_, to_):              #Находит все вхождения
        res = []
        while self.exists(from_, to_):
            res.append(self.unjail(from_, to_))
        return res

class Bot:
    def __init__(self, token=""):
        self.token = str(token)

    def massage(self, resp, id, att):             #Отправляет сообщение
        upload = vk_api.VkUpload(vk)
        photo = upload.photo(r"C:\Users\iMac\PycharmProjects\Екг3\imgp.png", album_id=267125590, group_id=186913181)
        try:
            vk.method('messages.send', {'user_id': id, 'message': response[ran], 'random_id': random.randint(1, 2147483647),"attachment":att})
        except:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Не удалось распознать запрос",
                       "random_id": random.randint(1, 2147483647)})

class Saver:
    def __init__(self, res):
        self.res = str(res)

    def save(self):                    #Сохраняет изображение по ссылке
        url = self.res
        img = urllib.request.urlopen(url).read()
        out = open("img.png", "wb")
        out.write(img)



token = "##############################"          #Уникальный токен. Я не могу его показать
base_url = 'https://yandex.ru/images/search?text='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
B=Bot(token)
session = requests.Session()
vk = vk_api.VkApi(token=token)
vk._auth_token()
longpoll = VkLongPoll(vk)
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            attachments = []
            t = 0
            s = 0
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            q = Parser(body.lower())
            if q.exists("[", "]"):
                s=1
                size = q.unjail("[", "]")
            if s == 1:
                r = requests.get(base_url + body.lower()+"&isize="+size.lower, headers=headers)
            if q.exists("(", ")"):
                t=1
                type = q.unjail("(", ")")
            if t == 1:
                r = requests.get(base_url + body.lower()+"&itype="+type.lower, headers=headers)
            if s+t == 2:
                r = requests.get(base_url + body.lower() + "&isize=" + size.lower + "&itype=" + type.lower, headers=headers)
            if s+t==0:
                r = requests.get(base_url + body.lower(), headers=headers)
            base_parse = r'<img.*"origin":{.*"url":".*"'
            text = re.findall(base_parse, r.text)
            p = Parser(text)
            response = ['https://' + x for x in p.unjail_all('"https://', '"')]
            ran = random.randint(20, 25)
            S=Saver(response[ran])
            S.save()
            image_url = response[ran]
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
            B.massage(response[ran], id, attachments)
            print(response[ran])
    except Exception as E:
        time.sleep(1)
