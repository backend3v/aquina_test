import traceback
from functools import wraps
from .exceptions import ApiError
from mysql.connector.errors import IntegrityError


def middleware(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print(
          f'Name:: {f.__name__}\n|Args {str(*args)} |\n|kwds {str(**kwds)}')
        try:
            result = f(*args, **kwds)
            return result
        except ApiError as e:
            print(f"ERROR :: {traceback.format_exc()}\nINFO : {str(e.message)} : {e.code}")
            return {'message': e.message}, e.code
        except IntegrityError as e:
            return {'error': 'User Exist'}, 202
        except Exception as e:
            print(f"ERROR :: {traceback.format_exc()}\nINFO : {str(e)}")
            return {'error': 'Error Interno'}, 500
    return wrapper