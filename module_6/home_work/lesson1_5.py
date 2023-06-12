import logging
import random
import statistics
from datetime import datetime
from typing import List


logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


def calculating_time(logs: str):
    with open(logs, 'r') as log_file:
        start_flag = False
        total_result = []
        for i_line in log_file:
            if 'Enter measure_me' in i_line:
                start_time = i_line[0:8]
                start_flag = True
            elif ('Leave measure_me' in i_line) and start_flag:
                stop_time = i_line[0:8]
                value = datetime.strptime(stop_time, '%H:%M:%S') - datetime.strptime(start_time, '%H:%M:%S')
                total_result.append(value.total_seconds())
                start_flag = False

        result = statistics.mean(total_result)
        return result


if __name__ == "__main__":
    logging.basicConfig(
        level="DEBUG",
        filename='logs.log',
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%I:%M:%S',
    )
    for it in range(5):
        data_line = get_data_line(5 ** 3)
        measure_me(data_line)

    time = calculating_time(logs='logs.log')
    print(f'Среднее время выполнения функции равно {time}')
