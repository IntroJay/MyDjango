import random

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print('Hello')
        # print(request.path)
        # print(request.META.get("REMOTE_ADDR"))

        # 抢购手机 增加中奖的权重
        if request.path == "/app/getphone/":
            if request.META.get('REMOTE_ADDR') == "127.0.0.1":
                if random.randrange(10) > 5:
                    return HttpResponse('成功抢到')
                elif random.randrange(10) > 2:
                    return HttpResponse('恭喜您抢到')
                else:
                    return HttpResponse('正在排队')
        # 抢购优惠券
        elif request.path == "/app/get_ticket/":
            if request.META.get('REMOTE_ADDR') == "10.0.119.211":
                return HttpResponse('下手慢了没有了')
        # 搜索
        elif request.path == "/app/search/":
            if request.method == "POST":

                result = cache.get(request.META.get("REMOTE_ADDR"))
                if result:
                    return HttpResponse('不要爬啦  没有啥好东西')
                else:
                    cache.set(request.META.get("REMOTE_ADDR"), '这又好玩的东西', timeout=15)

    # 打印出错误类型提示 并重定向到index
    def process_exception(self, request, exception):
        print(str(exception))
        return redirect(reverse("app:index"))
