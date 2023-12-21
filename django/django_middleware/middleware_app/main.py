



from typing import Any


class ExampleMiddleWare:
    
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request,  *args, **kwds ):
        print('MiddleWare Called')
        response = self.get_response(request)
        print('response : ', response)
        user_agent =  request.META.get('HTTP_USER_AGENT')
        print('user_agent : ', user_agent)
        return response