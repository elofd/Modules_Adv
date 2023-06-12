import logging
import json


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        new_message = msg.replace('"', "'")
        return new_message, kwargs


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='json_messages.log',
        format=json.dumps({"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}),
        datefmt='%H:%M:%S',
    )

    logger = JsonAdapter(logging.getLogger(__name__))
    logger.info('Сообщение с "двойными кавычками"')
    logger.info('"')
    logger.info('Сообщение')
    logger.error('Кавычка)"')
    logger.debug("Еще одно сообщение")

