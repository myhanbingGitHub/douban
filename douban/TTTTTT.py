import requests

# 自己IP
html=requests.get('http://httpbin.org/get')
print(html.text)

# 测试IP
# proxy='113.121.39.93:9999'
# print("http://{}".format(proxy))
# html=requests.get('http://httpbin.org/get', proxies={"http": "http://{}".format(proxy)})
# print(html.text)


