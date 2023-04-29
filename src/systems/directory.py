import sys
sys.path.append('../')
import config as configuration


class Path():
    __access = configuration.Path
    master = __access._master
    master_component = __access._master_component
    process  = __access._process
    result = __access._result
    archive = __access._archive
