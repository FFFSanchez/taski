# FFF Taski
Приложение Приложение для планирования своих задач. Имеет фронтенд часть на React и backend на Django. Развернут на Yandex Cloud с помощью gunicorn и nginx.
Адрес: https://bigbobs.bounceme.net/

## По проблемам и вопросам запуска писать на https://t.me/lordsanchez
### Как развернуть проект у себя на сервере:
__Протестировано на Linux Ubuntu 22.04.1 LTS__

+ Клонировать репозиторий на сервер (дефолт ветка main):
```
git clone https://github.com/FFFSanchez/taski.git
```
+ Cоздать и активировать виртуальное окружение, установить зависимости:
```
python3 -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
+ Выполнить миграции и создать суперюзера:
```
python manage.py migrate
python manage.py createsuperuser
```
+ Отредактировать ALLOWED_HOSTS в settings.py
```
ALLOWED_HOSTS = ['ip вашего сервера', '127.0.0.1', 'localhost', 'ваш_домен']
```
+ Выключить Debug в settings.py, задать константы и собрать статику
```
DEBUG = False
STATIC_URL = 'static_backend'
STATIC_ROOT = BASE_DIR / 'static_backend'

python3 manage.py collectstatic
```
+ Скопировать директорию static_backend/ в директорию /var/www/название_проекта/:
```
sudo cp -r путь_к_директории_с_бэкендом/static_backend /var/www/название_проекта
```
+ Собрать фронт и скопировать статику(из директории frontend)
```
npm i
npm run build
sudo cp -r путь_к_директории_с_фронтенд-приложением/build/. /var/www/имя_проекта/
```
+ Установить и настроить gunicorn
```
pip install gunicorn
sudo nano /etc/systemd/system/gunicorn_название_проекта.service
```
#### в конфиге gunicorn
```
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=имя_пользователя_в_системе
WorkingDirectory=/home/имя_пользователя/папка_с_проектом/папка_с_файлом_manage.py/
ExecStart=/.../venv/bin/gunicorn --bind 0.0.0.0:8000 kittygram_backend.wsgi:application
[Install]
WantedBy=multi-user.target
```
+ Активировать gunicorn
```
sudo systemctl start gunicorn_название_проекта
sudo systemctl enable gunicorn_название_проекта
```
+ Установить и настроить Nginx
```
sudo apt install nginx -y
sudo systemctl start nginx
sudo nano /etc/nginx/sites-enabled/default
```
#### В конфиге Nginx
```
server {
	listen 80;
	server_name ваш_домен;
	location /api/ {
		proxy_pass http://127.0.0.1:8000;
	}
	location /admin/ {
		proxy_pass http://127.0.0.1:8000;
	}
	location / {
		root /var/www/имя_проекта;
		index index.html index.htm;
		try_files $uri /index.html;
	}
}
```
```
sudo systemctl reload nginx
```

+ ## Проект запущен и доступен по вашему dns или ip.

#### Автор: Санчез Трифонов
