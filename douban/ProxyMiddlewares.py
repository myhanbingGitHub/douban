# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 阿不云解决方案：
# import base64
# proxyServer="http://http-dyn.abuyun.com:9020"
# proxyUser="xxxxxxxx"
# proxyPass="xxxxxxxx"
# proxyAuth='Basic'+base64.b64encode(proxyUser+":"+proxyPass)
#
# class ProxyMiddleware:
#
#     def process_request(self, request, spider):
#         request.meta["proxy"]=proxyServer
#         request.headers["Proxy-Authorization"]=proxyAuth
#         return None


# 其他方案
# import random
# proxyServer = [
#     '39.108.59.34:8118',
#
# ]
# class ProxyMiddleware:
#
#     def process_request(self, request, spider):
#         request.meta["proxy"] = random.choice(proxyServer)
#         print(request.meta["proxy"], "|")
#         return None