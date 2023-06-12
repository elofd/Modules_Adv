import itertools
import json
import subprocess
from typing import Dict


def trans_logs() -> list[dict]:
    with open('json_messages.log', 'r') as logs:
        json_logs = []
        for i_line in logs:
            i_line_json: dict = json.loads(i_line)
            json_logs.append(i_line_json)
    return json_logs


def types_of_messages() -> Dict[str, int]:
    result = dict()
    data: list[dict] = sorted(trans_logs(), key=lambda i_key: i_key['level'])
    for k, g in itertools.groupby(data, key=lambda i_key: i_key['level']):
        result[k] = len([i for i in g])

    return result


def max_logs_per_hour() -> int:
    grouped_data = dict()
    data: list[dict] = sorted(trans_logs(), key=lambda i_key: i_key['time'][0:2])
    for k, g in itertools.groupby(data, key=lambda i_key: i_key['time'][0:2]):
        grouped_data[k] = len([i for i in g])
    sorted_group_data = sorted(grouped_data, key=lambda i: grouped_data[i], reverse=True)
    return sorted_group_data[0]


def critical_sum(hour_min: str):
    data = subprocess.Popen(['grep', f'"time": {hour_min}', 'json_messages.log'], stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    decode_data = data.stdout.read().decode().split('\n')
    count_logs = 0
    for i_log in decode_data:
        if 'CRITICAL' in i_log:
            count_logs += 1
    return count_logs


def critical_logs_from_5_00_to_5_20() -> int:
    result = (critical_sum(hour_min='"05:0') +
              critical_sum(hour_min='"05:1') +
              critical_sum(hour_min='"05:2'))
    return result


def messages_with_dog() -> int:
    data = subprocess.Popen(['grep', '-c', 'dog', 'json_messages.log'], stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    decode_data = data.stdout.read().decode()
    return int(decode_data) if decode_data else 0


def max_word_in_warning() -> str:
    messages_from_warning_logs = ()
    data: list[dict] = sorted(trans_logs(), key=lambda i_key: i_key['level'])
    for k, g in itertools.groupby(data, key=lambda i_key: i_key['level'] == 'WARNING'):
        if k:
            messages_from_warning_logs = ([i['message'].split() for i in g])

    words = list()
    if messages_from_warning_logs:
        for mess in messages_from_warning_logs:
            words.extend(mess)

        counter = dict()
        for word in words:
            counter[word] = counter.get(word, 0) + 1

        max_count = max(counter.values())
        most_frequent = [k for k, v in counter.items() if v == max_count]

        return min(most_frequent)
    return 'В логах нет WARNING'


if __name__ == '__main__':
    tasks = (
        types_of_messages,
        max_logs_per_hour,
        critical_logs_from_5_00_to_5_20,
        messages_with_dog,
        max_word_in_warning,
    )
    for task in tasks:
        task_answer = task()
        print(f'{task.__name__}: {task_answer}')
