#!/usr/bin/env python3
import os
import tarfile

direction = '/home/developers'
arch_name = 'backup.tar.gz'
ext_dir = '/home/extracted'


def create_and_extract_archive():
    # Создаем архив
    with tarfile.open(os.path.join('/tmp/', arch_name), 'w:gz') as tar:
        for filename in os.listdir(direction):
            if filename in ['data.csv', 'report.txt', 'script.py']:
                file_path = os.path.join(direction, filename)
                tar.add(file_path, arcname=filename)
    # Показываем размер архива
    size_bytes = os.path.getsize(f'/tmp/{arch_name}')
    print(f'Размер архива {arch_name}: {size_bytes} байт.')
    # Список файлов в архиве
    with tarfile.open(f'/tmp/{arch_name}', 'r:*') as tar:
        members = tar.getnames()
        print('Файлы в архиве:', ', '.join(members))
    # Распаковываем архив
    os.makedirs(ext_dir, exist_ok=True)
    with tarfile.open(f'/tmp/{arch_name}') as tar:
        tar.extractall(path=ext_dir)

if __name__ == '__main__':
    create_and_extract_archive()
