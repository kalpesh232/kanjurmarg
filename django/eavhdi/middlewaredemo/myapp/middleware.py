from django.http import HttpResponse

class CustomMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(f'Requested Path : {request.path}')

        # user_agent = request.META.get('HTTP_USER_AGENT','')

        # if "BadBot" in user_agent:
        #     from django.http import HttpResponseForbidden
        #     return HttpResponseForbidden("Forbidden: BadBot detected.")
        
        # response = self.get_response(request)
        # return response
        if request.path == '/register/' and request.method == 'POST' :
            name = request.POST.get('name')
            price = request.POST.get('price')

            if not name or not price :
                return HttpResponse("⛔ Name and Price are required.")
            
            try:
                if int(price) < 1000 :
                    return HttpResponse("⚠️ Price must be ₹1000 or more.")
            except ValueError :
                return HttpResponse("❌ Price must be a valid number.")
            
        return self.get_response(request)
