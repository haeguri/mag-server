from django.contrib.sessions.middleware import SessionMiddleware
from django.conf import settings

import re

class CustomSessionMiddleware(SessionMiddleware):

    def process_response(self, request, response):
        response = super(CustomSessionMiddleware, self).process_response(request, response)
        #You have access to request.user in this method
        # print("response.cookies[settings.SESSION_COOKIE_NAME]",response.cookies[settings.SESSION_COOKIE_NAME])
        # print("response.cookies[settings.CSRF_COOKIE_NAME]", response.cookies[settings.CSRF_COOKIE_NAME])
        try:
            pass
            # path_info = request.path
            # 모바일 클라이언트의 REST API 통신 URL은 "/api/"가 포함되는 패턴이다.
            # 모바일 클라이언트로 응답을 전송할 때는 "sessionid", "csrftoken" 쿠키를 삭제한다.
            #pattern = re.compile("(\/api\/)", re.IGNORECASE)
            # print("request.path", request.path)
            # pattern = re.compile("\/api\/", re.IGNORECASE)
            # if pattern.search(path_info):
                # print("matched patern & response.cookies", response.cookies)
                # del response.cookies[settings.SESSION_COOKIE_NAME]
                # del response.cookies[settings.CSRF_COOKIE_NAME]
        except:
            pass
        return response