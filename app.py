import functools
import json

from flask import Flask
from flask import jsonify, request
from jsonschema import validate, ValidationError

from logger import get_logger
from settings import schemas, config

import features


app = Flask(__name__)
logger = get_logger(__name__)


def handle_exceptions(func):
    """
        Decorator for handling exceptions of all endpoints
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (json.JSONDecodeError, json.decoder.JSONDecodeError,
                ValidationError) as e:
            logger.exception(f'{func.__name__}() got invalid data: {e}')
            return jsonify({'error': f'Invalid data: {e}'}), 400
        except Exception as e:
            logger.exception(f'{func.__name__}() failed - {e}')
            return jsonify({'error': str(e)}), 500

    return wrapper


@app.route('/deposit_calc', methods=['POST'])
@handle_exceptions
def deposit_calc():
    """This endpoint calculates amount of the deposit.

    Request data: JSON with calculating data: {'date': 'dd.mm.YYY',
    'periods': int (1-60), 'amount': int (10 000 - 3 000 000),
    'rate': float (1-8)}

    Returns:
        _type_: JSON with dates and amounts {'date': amount, ...}
    """
    request_data = request.get_json()
    validate(request_data, schemas.deposit_calc)
    result = features.calc_amount(request_data)
    return jsonify(result)


def execute_flask_config():
    for key, value in config.flask_app_config.items():
        app.config[key] = value


if __name__ == '__main__':
    execute_flask_config()
    app.run('0.0.0.0', port=5000)
