# DonationAlerts to Telegram
Telegram бот, пересылающий оповещения о новых донатах в личные сообщения
## Установка
 Python 3.8+
 
 Клонируйте репозиторий и скачайте зависимости из файла `requirements.txt`
 
 После этого, создайте файл `config.yml` на основе файла  `config.template.yml`
 ```yaml
donation_alerts_token: "ваш токен авторизации для донейшен алертса"
bot_token: "токен для телеграм бота"
reciever_chat_id: 12345 #id телеграм чата, в который будут отправляться сообщения
 ```

И запустите бота
```
python3 main.py
```
