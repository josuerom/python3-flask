# INSTALACIÓN DE XAMPP Y CONFIGURACIÓN EN LINUX

1. git clone https://github.com/josuerom/python3-flask.git /opt/lampp/htdocs/python_flask && cd /opt/lampp/htdocs/python_flask/
2. https://www.apachefriends.org/es/download.html
3. sudo chmod 755 xampp-linux-x64-8.2.4-0-installer.run && sudo ./xampp-linux-x64-8.2.4-0-installer.run
4. sudo chmod -R 777 /opt
6. sudo apt install python3 python3-venv python3-pip -y && python3 -m venv venv && source venv/bin/activate
7. pip install flask flask_mysqldb
8. flask run
