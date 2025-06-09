#!/usr/bin/env python3
import subprocess
import json
import logging

LOG_FILE = '/home/developers/logs/docker_manager.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DOCKER_IMAGE = 'nginx'
PORT_MAP = {'80': '8080'}
STATUS_OUTPUT = '/home/developers/reports/docker_status.txt'

def download_image(image_name):
    result = subprocess.run(['docker', 'pull', image_name], capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f'Ошибка при загрузке образа: {result.stderr.strip()}')
        raise RuntimeError(result.stderr.strip())
    logging.info(f'Образ {image_name} успешно загружен.')
    print(f'Образ {image_name} загружен!')

def run_container(image_name, port_map):
    try:
        cmd = [
            'docker', 'run',
            '-p', f'{list(port_map.values())[0]}:{list(port_map.keys())[0]}',
            '--rm', '--detach', image_name
        ]
        container_id = subprocess.check_output(cmd, text=True).strip()
        logging.info(f'Контейнер запущен, ID: {container_id}')
        print(f'Контейнер запущен, ID: {container_id}')
        return container_id
    except subprocess.CalledProcessError as e:
        logging.error(f'Ошибка при запуске контейнера: {e.stderr.strip()}')
        print(f'Ошибка при запуске контейнера: {e.stderr.strip()}')
        raise RuntimeError(e.stderr.strip())

def check_container_status(container_id):
    try:
        result = subprocess.run(
            ['docker', 'inspect', container_id],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        info = json.loads(result.stdout)[0]
        state = info['State']['Status']
        logging.info(f'Проверка статуса контейнера {container_id}, статус: {state}')
        return state
    except subprocess.CalledProcessError as e:
        logging.error(f'Ошибка при проверке статуса контейнера: {e.stderr.strip()}')
        raise RuntimeError(e.stderr.strip())

def save_status(status):
    try:
        with open(STATUS_OUTPUT, 'w') as f:
            f.write(f'Status of the Docker Container: {status}\n')
        logging.info(f'Статус контейнера сохранён в {STATUS_OUTPUT}')
    except IOError as e:
        logging.error(f'Ошибка при сохранении статуса: {e}')
        raise RuntimeError(str(e))

if __name__ == '__main__':
    try:
        download_image(DOCKER_IMAGE)
        container_id = run_container(DOCKER_IMAGE, PORT_MAP)
        status = check_container_status(container_id)
        save_status(status)
        print(f'Статусы сохранены в {STATUS_OUTPUT}')
    except Exception as e:
        logging.error(f'Критическая ошибка: {e}')
        raise