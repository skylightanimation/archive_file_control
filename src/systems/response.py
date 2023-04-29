import sys
sys.path.append('../')
import config as configuration


class Responses():
        
    def response(option):
        __access = configuration.Response
        if option == 'success':
            success = __access._successResponse
            success['data'] = []
            return success
            
        elif option == 'failed':
            failed = __access._failedResponse
            return failed
            
        elif option == 'notfound':
            notfound = __access._notfoundResponse
            return notfound
            
        elif option == 'error':
            error['message'] = ''
            error = __access._errorResponse
            return error


# class header:
#     __access = configuration.request_header
#     content_type = __access._content_type
