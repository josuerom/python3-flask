# INSTALACIÓN DE XAMPP Y CONFIGURACIÓN EN LINUX

## Para ejecutar este proyecto debe realizar las siguientes tareas
1. git clone https://github.com/josuerom/python3-flask.git /opt/lampp/htdocs/python_flask && cd /opt/lampp/htdocs/python_flask/ && ls
2. https://www.apachefriends.org/es/download.html
3. sudo chmod 755 xampp-linux-x64-8.2.4-0-installer.run && sudo ./xampp-linux-x64-8.2.4-0-installer.run
4. sudo chmod -R 777 /opt
6. sudo apt install python3 python3-venv python3-pip libmysqlclient-dev python3-dev python3-flask mysql-server python3-flask-mysqldb -y && python3 -m venv venv && source venv/bin/activate
7. pip install mysqlclient --global-option=build_ext --global-option="-I/usr/include/mysql"
8. python3 -m pip install flask flask_mysqldb
9. python3 src/app.py
