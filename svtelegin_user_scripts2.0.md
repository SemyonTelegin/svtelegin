# Телегин Семён Васильевич - "Чат-бот во ВКонтакте"
# Пользовательские сценарии
### Группа: 11 - МИ - 2
### Электронная почта: semen-telegin@mail.ru
### VK: https://vk.com/id399074080
### [ Сценарий 1 - Получение доступа к отправке запроса Чат-боту]
1. Пользователь авторизируется в социальной сети ВКонтакте
2. Пользователь находит данный чат-бот среди сообществ
3. Пользователь вступает в данное сообщество для получения доступа к отправке сообщений
4. Далее у пользователя появляется кнопка "Написать сообщение"
5. Пользователь кликает на кнопку "Написать сообщение"
6. Запускается Сценарий 2 - Ознакомление пользователя с правилами работы с данным чат-ботом.
### [ Сценарий 2 - Ознакомление пользователя с правилами работы с данным чат-ботом]
1. Пользователь переходит в диалог с чат-ботом
2. Пользователю автоматически приходит сообщение с правилами пользования продуктом
3. После этого пользователь по умолчанию соглашается с установленными правилами
4. В случае несоглашения или непонимания пользователем правил пользования данным чат-ботом пользователь обращается к администратору сообщества
5. В течении одного-двух дней пользователя проконсультируют по его вопросу
6. Запускается Сценарий 3 - Отправка тематического запроса пользователем.
### [ Сценарий 3 - Отправка тематического запроса пользователем]
1. Для отправки тематического запроса пользователь должен отправить сообщение
2. Тематический запрос - это то, что пользователь желает найти
3. Пользователь вводит запрос в виде сообщения 
4. Тематическая часть запроса представляет собой текст сообщения
5. Тематическая часть запроса не может содержать такие знаки как "[", "]", "(", ")"
6. Запускается Сценарий 4 - Запрос нужного размера искомого изображения пользователем.
### [Сценарий 4 - Запрос нужного размера искомого изображения пользователем]
1. Пользователь может задать размер искомого изображения в виде "[size]"
2. Если пользователю нужна картинка следующих размеров: 1920х1178, 1760х1080, 1280х960, 1245х830, то size=1 
3. Если пользователю нужна картинка следующих размеров: 1280х720, 1024х427, 1023х627, 980х360, 930х570, 800х490, то size=2 
4. Если пользователю нужна картинка следующих размеров: 960х245, 380х233, 230х129, то size=3 
5. Остальные значения size недопустимы
6. Если пользователю неважен размер изображения, то он ничего дополнительного в запрос не вводит
7. Запускается Сценарий 5 - Запрос нужного типа искомого изображения пользователем.
### [Сценарий 5 - Запрос нужного типа искомого изображения пользователем]
1. Пользователь может задать тип искомого изображения в виде "(type)"
2. Если пользователю нужна картинка типа JPEG, то type=1 
3. Если пользователю нужна картинка типа PNG, то type=2 
4. Если пользователю нужна картинка типа GIF, то type=3 
5. Остальные значения type недопустимы
6. Если пользователю неважен тип изображения, то он ничего дополнительного в запрос не вводит
7. Запускается Сценарий 6 - Получение ссылки на изображение по пользовательскому запросу.
### [ Сценарий 6 - Получение ссылки на изображение по пользовательскому запросу ]
1. Пользователь отправляет сообщение с запросом
2. Чат-бот отправляет запрос в Яндекс.Картинки по заданному пользователем теме, типу и размеру изображения
3. Если результатов поиска нет, то пользователь будет об этом уведомлён
4. Чат-бот получает ссылку на нужное изображение
5. Чат-бот отправляет ссылку на данное изображение пользователю
6. Пользователь получает сообщение со ссылкой на нужное изображение
7. Пользователь может просмотреть изображение, кликнув по ссылке в сообщении
8. Запускается Сценарий 7 - Дальнейшее использование чат-бота.
### [ Сценарий 7 - Дальнейшее использование чат-бота ]
1. Пользователь может сохранить где-угодно ссылку на изображение, а так же само изобажение
2. Вся история сохраняется автоматически для просмотра предыдущих запросов
3. Пользователь может отправить тот же запрос повторно согласно Сценарию 3
5. Пользователь может отправлять запрос боту несколько раз
6. Для отправки повторного запроса пользователь должен повторить Сценарии 2-5
7. Если во время пользования возникли проблемы, то пользователь может братиться за помощью к администратору данного сообщества.