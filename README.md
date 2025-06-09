# Project_Linux
=====================================================
Настроить и управлять Linux-системой в виртуальной машине (VM),
выполнить задачи, связанные с основами администрирования, написанием
Python-скриптов, работой с Docker и управлением пользователями.
=====================================================

1. Создание и настройка виртуальной машины
-------------------

1.1 Установка виртуальной машины (опционально):
- Установите VirtualBox или VMware
- Создайте новую виртуальную машину с Ubuntu 22.04 LTS
- Рекомендуемые параметры: 2 ядра CPU, 4 ГБ RAM, 25 ГБ HDD

1.2 Настройка окружения:
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install python3 python3-pip python3-venv

1.3 Добавление пользователя:
$ sudo useradd 'имя пользователя'

2. Права доступа и группы
-------------------

2.1 Создайте группу developers:
$ sudo groupadd developers

2.2 Добавьте пользователя с ограниченными правами в эту группу
$ sudo usermod -aG developers 'имя пользователя'

2.3 Настройте директорию /home/developers, чтобы только члены группы
могли вносить изменения.
$ sudo mkdir /home/developers
$ sudo chown root:developers /home/developers
$ sudo chmod 770 /home/developers

3. Работа с файлами и архивами
-------------------

3.1 В директории /home/developers создайте файлы:
$ touch /home/developers/report.txt && touch /home/developers/data.csv && touch /home/developers/script.py

3.2 Python-скрипт file_manager.py:
$ (Приложен к работе), запускается через /home/developers/file_manager.py
  (Создает архив из файлов report.txt, data.csv, script.py, в формате gz, в папке /tmp/ и распаковывает его в /home/extracted/) 

4. Автоматизация резервного копирования
-------------------

4.1 Python-скрипт backup.py:
$ (Приложен к работе), запускается через /home/developers/backup.py, создает копию директории /home/developers/, 
  в формате gz, в папку /home/extracted/backups/ и распаковывает ее туда-же.
$ Для выполнения скрипта ежедневно, в 2:00, заходим в crontab -e и прописываем туда 0 2 * * * /home/developers/backup.py

5. Мониторинг системы
-------------------

5.1 Python-скрипт system_monitor.py:
$ (Приложен к работе), запускается через /home/developers/system_monitor.py, 
  создает отчет system_usage.txt в папке /home/developers/reports

6. Работа с Docker
-------------------

6.1 Установите Docker:
$ sudo apt-get update
$ sudo apt-get install ca-certificates curl
$ sudo install -m 0755 -d /etc/apt/keyrings
$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
$ sudo chmod a+r /etc/apt/keyrings/docker.asc
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

6.2 Python-скрипт docker_manager.py:
$ (Приложен к работе), запускается через sudo /home/developers/docker_manager.py
  !!! Перед запуском нужно авторизироваться в dockerhub, для этого прописать sudo docker login
$ Результат сохраняется в папку /home/developers/reports

7. Логирование работы скриптов 
$ Логи работы скриптов system_monitor.py, docker_manager.py и backup.py, сохраняются в папку /home/developers/logs/
