from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
 
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
 
    return response
    

# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#     if response is not None:
#         data = response.data
#         response.data = {}

#         #response.data['status_code'] = response.status_code
#         #response.data['message'] = str(exc)
# #        response.data['status_code'] = '{} - {}'.format(response.status_code, response.status_text)
#         response.data['status_code'] = response.status_code
#         response.data['message'] = response.status_text
#        # response.data['code'] = exc.get_codes()

#     return response
