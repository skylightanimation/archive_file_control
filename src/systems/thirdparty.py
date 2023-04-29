import sys
sys.path.append('../')
import config as configuration


class Thirdparty():
    __access = configuration.Thirdparty
    archive = __access._tool['archive']