import logging
import logging.config
import random
from flask import Flask, jsonify


app = Flask(__name__)
logger = logging.getLogger(__name__)


logging.config.dictConfig({
    'disable_existing_loggers': False,
    'version': 1,
    'root': {
        'level': logging.INFO,
    }
})


@app.route('/')
def index():
    return 'Hello world!\n'


@app.route('/api/v1/luck')
def luck():
    try:
        1/random.choice([0, 1])
        res = random.randint(1, 9999)
    except Exception as e:
        logger.exception(e)
        return jsonify({'error': {'message': 'How unlucky!', 'code': 400}}), 400

    return jsonify({'lucky_number': res})


if __name__ == '__main__':
    app.run()

