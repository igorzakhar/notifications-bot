# Notifications bot
Telegram-бот для оповещения студентов курса ["Девман"](https://dvmn.org/modules/) о результатах проверенных заданий. Ранее, чтобы узнать статус своей работы, приходилось заходить на сайт, это неудобно и неэффективно. Данный бот запрашивает результаты проверок работ и оповещает пользователя в Telegram. Так же бот сообщает пользователю о проблемах и ошибках возникших в работе самого бота.

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/devman-bot.gif)

## Запуск бота на сервере

Для размещения бота можно использовать платформу [Heroku](https://www.heroku.com/). Бесплатный вариант включает 550 бесплатных часов в месяц.

#### Регистрируем учетную запись и создаем приложение(app) на платформе [Heroku](https://www.heroku.com/):

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/heroku_create.png)

Получится страница, как на скриншоте ниже:

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/heroku_app.png)

#### Привязываем репозиторий с кодом на Github к приложению на платформе Heroku

Далее нужно разместить репозиторий с кодом бота на своём аккаунте GitHub. Репозиторий должен содержать файл ```requirements.txt``` в котором прописаны зависимости. **Файл ```.env``` публиковать нельзя.**

Затем нужно привязать свой аккаунт GitHub к аккаунту Heroku. Это можно сделать на вкладке **Deploy** в разделе панели инструментов платформы Heroku. В разделе **Deployment method**  выберите **GitHub**, потом найдите свой репозиторий с помощью поиска и подключите его к Heroku.

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/heroku_deploy_github.png)

#### Добавляем переменные окружения 

В панели инструментов платформы Heroku переходим на вкладку **Settings** и в разделе **Config Vars** добавляем переменные окружения которые использует бот:

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/heroku_env_vars.png)



#### Развёртывание бота на сервере Heroku

Репозиторий с кодом должен содержать файл ```Procfile``` со следующим содержимым:  
```
bot: python3 <имя_файла_с_кодом_бота>.py
```

На вкладке **Resources** панели инструментов платформы Heroku переключаем "тумблер" в положение "ON" как показано на скриншоте:  

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/heroku_app_on.png)

Далее переходим на вкладку **Deploy** и в разделе **Manual deploy** нажимаем кнопку **Deploy Branch**, если всё прошло нормально то загорятся зелёные галочки справа, как на скриншоте.:

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/heroku_deploy.png)

#### Логи Heroku

Обычно, если код не работает, ошибка выводится в консоль. Но код запускал Heroku, и он просто так её не покажет. Вывод программы можно посмотреть через специальное приложение [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), которое придётся поставить на свой компьютер. Посмотреть логи можно командой: 

```bash
$ heroku logs --tail --app your_app_name
```

![Screenshot](https://github.com/igorzakhar/notifications-bot/blob/master/media/heroku_logs.png)

Если вы не можете сразу увидеть источник ошибки, попробуйте перезапустить приложение из другого окна терминала.

```bash
$ heroku restart
```

# Цели проекта

Код написан в образовательных целях.