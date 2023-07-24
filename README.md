# FFF Taski
���������� ���������� ��� ������������ ����� �����. ����� �������� ����� �� React � backend �� Django. ��������� �� Yandex Cloud � ������� gunicorn � nginx.
�����: https://bigbobs.bounceme.net/

## �� ��������� � �������� ������� ������ �� https://t.me/lordsanchez
### ��� ���������� ������ � ���� �� �������:
__�������������� �� Linux Ubuntu 22.04.1 LTS__

+ ����������� ����������� �� ������ (������ ����� main):
```
git clone https://github.com/FFFSanchez/taski.git
```
+ C������ � ������������ ����������� ���������, ���������� �����������:
```
python3 -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
+ ��������� �������� � ������� ����������:
```
python manage.py migrate
python manage.py createsuperuser
```
+ ��������������� ALLOWED_HOSTS � settings.py
```
ALLOWED_HOSTS = ['ip ������ �������', '127.0.0.1', 'localhost', '���_�����']
```
+ ��������� Debug � settings.py, ������ ��������� � ������� �������
```
DEBUG = False
STATIC_URL = 'static_backend'
STATIC_ROOT = BASE_DIR / 'static_backend'

python3 manage.py collectstatic
```
+ ����������� ���������� static_backend/ � ���������� /var/www/��������_�������/:
```
sudo cp -r ����_�_����������_�_��������/static_backend /var/www/��������_�������
```
+ ������� ����� � ����������� �������(�� ���������� frontend)
```
npm i
npm run build
sudo cp -r ����_�_����������_�_��������-�����������/build/. /var/www/���_�������/
```
+ ���������� � ��������� gunicorn
```
pip install gunicorn
sudo nano /etc/systemd/system/gunicorn_��������_�������.service
```
#### � ������� gunicorn
```
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=���_������������_�_�������
WorkingDirectory=/home/���_������������/�����_�_��������/�����_�_������_manage.py/
ExecStart=/.../venv/bin/gunicorn --bind 0.0.0.0:8000 kittygram_backend.wsgi:application
[Install]
WantedBy=multi-user.target
```
+ ������������ gunicorn
```
sudo systemctl start gunicorn_��������_�������
sudo systemctl enable gunicorn_��������_�������
```
+ ���������� � ��������� Nginx
```
sudo apt install nginx -y
sudo systemctl start nginx
sudo nano /etc/nginx/sites-enabled/default
```
#### � ������� Nginx
```
server {
	listen 80;
	server_name ���_�����;
	location /api/ {
		proxy_pass http://127.0.0.1:8000;
	}
	location /admin/ {
		proxy_pass http://127.0.0.1:8000;
	}
	location / {
		root /var/www/���_�������;
		index index.html index.htm;
		try_files $uri /index.html;
	}
}
```
```
sudo systemctl reload nginx
```

+ ## ������ ������� � �������� �� ������ dns ��� ip.

#### �����: ������ ��������
