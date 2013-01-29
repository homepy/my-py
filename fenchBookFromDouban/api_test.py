import httplib2
httplib2.debuglevel = 1
h = httplib2.Http('.cache')
resp, content = h.request('https://api.douban.com/v2/book/1220562')
print(resp.status)
print(content)
# print(len(content))
# print(resp.fromcache)
# print(dict(resp.items()))
