import sys
sys.path.append('../')
import config as configuration


class Master():
    __access = configuration.Master
    __embeddedFileRedirectPage = __access._embeddedFileRedirectPage
    pack = __embeddedFileRedirectPage['pack']
    single = __embeddedFileRedirectPage['single']
    brand = __access._brand
    typeString = __access._type_string
    # master_component = __access._master_component
    # process  = __access._process
    # result = __access._result
    # archive = __access._archive
