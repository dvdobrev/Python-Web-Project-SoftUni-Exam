from poker_app.web.views import raises_exception


# def handle_exceptions(get_response):
#     def middleware(request):
#         response = get_response(request)
#
#         if response.status_code > 400:
#             return raises_exception
#
#         return response
#
#     return middleware
