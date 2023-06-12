import heapq
import json
import logging
from typing import List
import time

from flask import Flask, request


app = Flask(__name__)

logger = logging.getLogger("sort")


def bubble_sort(array: List[int]) -> List[int]:
    start = time.time()
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    logger.debug(f'Функция buble_sort выполнялась {time.time() - start:.2f} секунд(ы)')
    return array


def tim_sort(array: List[int]) -> List[int]:
    start = time.time()
    array.sort()
    logger.debug(f'Функция tim_sort выполнялась {time.time() - start:.2f} секунд(ы)')
    return array


def heap_sort(array: List[int]) -> List[int]:
    start = time.time()
    data = []
    for val in array:
        heapq.heappush(data, val)
    logger.debug(f'Функция heap_sort выполнялась {time.time() - start} секунд(ы)')
    return [heapq.heappop(data) for _ in range(len(data))]


algorithms = {
    "bubble": bubble_sort,
    "tim": tim_sort,
    "heap": heap_sort,
}


@app.route("/<algorithm_name>/", methods=["POST"])
def sort_endpoint(algorithm_name: str):
    if algorithm_name not in algorithms:
        return f"Bad algorithm name, acceptable values are {algorithms.keys()}", 400

    form_data = request.get_data(as_text=True)
    array = json.loads(form_data)['array']
    result = algorithms[algorithm_name](array)
    return json.dumps(result)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename='stderr.txt',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S',
    )
    logger.info("Started sort server")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
