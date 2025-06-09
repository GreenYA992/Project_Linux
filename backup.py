#!/usr/bin/env python3
import os
import tarfile
from datetime import datetime
import logging

LOG_FILENAME = '/home/developers/logs/backup.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
backup_dir = '/home/developers/'
direction = '/home/extracted/backups/'
backup_day = datetime.now().strftime("%Y-%m-%d")
backup_arch = f'{direction}backup_{backup_day}.tar.gz'

def create_backup():
    try:
        with tarfile.open(backup_arch, 'w:gz') as tar:
            tar.add(backup_dir)
        logging.info(f'Резервная копия успешно создана: {backup_arch}')
        print(f'Резервная копия успешно создана: {backup_arch}')
    except Exception as e:
        logging.error(f'Ошибка при создании резервной копии: {e}')
        print(f'Ошибка при создании резервной копии: {e}')

def create_copy():
    os.makedirs(direction, exist_ok=True)
    try:
        with tarfile.open(backup_arch) as tar:
            tar.extractall(path=direction)
        logging.info(f'Распаковка архива выполнена успешно: {backup_arch}')
        print(f'Архив {backup_arch} успешно распакован')
    except Exception as e:
        logging.error(f'Ошибка при распаковке архива: {e}')
        print(f'Ошибка при распаковке архива: {e}')

if __name__ == '__main__':
    create_backup()
    create_copy()