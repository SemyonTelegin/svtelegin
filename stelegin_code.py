import vk_api
import time
import random
import re
import requests
import urllib.request

class Parser:
    def __init__(self, source=""):
        self.source = str(source)

    def exists(self, from_, to_):                  #Проверяет наличие обьекта между двух последовательностей символов
        id1 = self.source.find(from_)
        if id1 == -1:
            return None
        id2 = self.source.find(to_, id1 + len(from_))
        if id2 == -1:
            return None
        return id1, id2

    def unjail(self, from_, to_):           #Возвращает первое вхождение (при наличии)
        if self.exists(from_, to_):
            id1, id2 = self.exists(from_, to_)
        else:
            return None
        res = self.source[id1 + len(from_):id2]
        self.source = self.source[:id1] + self.source[id2 + len(to_):]
        return res

    def unjail_all(self, from_, to_):      #Возвращает все вхождения
        res = []
        while self.exists(from_, to_):
            res.append(self.unjail(from_, to_))
        return res

class Bot:
    def __init__(self, token=""):
        self.token = str(token)

    def massage(self, resp, id):                #Загружает изображение в альбом и отправляет сообщение
        upload = vk_api.VkUpload(vk)
        photo = upload.photo(r"C:\Users\iMac\PycharmProjects\Екг3\imgp.png", album_id=267125590, group_id=186913181)
        try:
            vk.method("messages.send",
                      {"peer_id": id, "message": resp, "random_id": random.randint(1, 2147483647), "attachmenta":'photo' + str(photo[0]['owner_id']) + '_' + str(photo[0]['id']) + ','})
        except:
            vk.method("messages.send",
                      {"peer_id": id, "message": "Не удалось распознать запрос",
                       "random_id": random.randint(1, 2147483647)})
class Saver:
    def __init__(self, res):
        self.res = str(res)

    def save(self):               #Сохраняет изображение по ссылке 
        url = self.res
        img = urllib.request.urlopen(url).read()
        out = open("img.png", "wb")
        out.write(img)
        out.close


token = "e02ab112e4762f188d0bc714ec61edc32d36fdb3ea2144ecdd2bc0ef2bcc25e1db691089011ee46012710"
base_url = 'https://yandex.ru/images/search?text='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
B=Bot(token)
vk = vk_api.VkApi(token=token)
vk._auth_token()
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
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
            ran = random.randint(13, 25)
            S=Saver(response[ran])
            S.save()
            B.massage(response[ran], id)
            print(response[ran])
    except Exception as E:
        time.sleep(1)
