#!/usr/bin/env python
import httplib2
httplib2.debuglevel = 1
h = httplib2.Http('.cache')
resp, content = h.request('http://api.douban.com/v2/movie/subject/24753811')
