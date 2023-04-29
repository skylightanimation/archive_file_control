# import os, sys
# import __init__ as configuration

import sys
sys.path.append('../')
import config as configuration


class BlackJack():
    __access = configuration.Security
    _salt = __access._data['salt']
    _secret = __access._data['secret_key']
    
class Archive():
    __access = configuration.Security
    _code = __access._data['archive_password']
