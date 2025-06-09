#!/usr/bin/env python3
import os
import datetime
import logging

log_file = '/home/developers/logs/monitoring.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
output_file = '/home/developers/reports/system_usage.txt'

def read_cpu_load():
    try:
        load_avg = os.getloadavg()[0]
        num_cpus = os.cpu_count()
        cpu_percent = (load_avg / num_cpus) * 100
        return round(cpu_percent, 2)
    except Exception as e:
        logging.error(f'Ошибка при чтении нагрузки на CPU: {e}')
        return None

def read_memory_usage():
    try:
        with open('/proc/meminfo', 'r') as meminfo:
            lines = meminfo.readlines()
            total_mem = int(lines[0].split(':')[1].strip().replace('kB', ''))
            free_mem = int(lines[1].split(':')[1].strip().replace('kB', ''))
            used_mem = total_mem - free_mem
            percent_used = (used_mem / total_mem) * 100
            return round(percent_used, 2)
    except Exception as e:
        logging.error(f'Ошибка при чтении состояния памяти: {e}')
        print(f'Ошибка при чтении состояния памяти: {e}')
        return None

def monitor_system():
    try:
        cpu_percent = read_cpu_load()
        memory_used = read_memory_usage()
        timestamp = datetime.datetime.now()
        output = f'''
Timestamp: {timestamp}
CPU Usage (%): {cpu_percent:.2f}%
Memory Used (%): {memory_used:.2f}%
'''
        with open(output_file, 'a') as f:
            f.write(output)
        logging.info('Мониторинг выполнен успешно.')
        print('Данные мониторинга успешно сохранены!')
    except Exception as e:
        logging.error(f'Ошибка при мониторинге системы: {e}')

if __name__ == '__main__':
    monitor_system()