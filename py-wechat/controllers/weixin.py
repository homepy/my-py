#!/usr/bin/env python2
# -- coding: utf-8 --
import hashlib
import web


class WeixinDev:
    def __init__(self):
        # self.app_rootos.path.dirname(__file__)
        # self.templates_rootos.path.join(self.app_root, '/templates')
        # self.renderweb.template.render(self.templates_root)
        pass

    def GET(self):
        params = web.input(signature=None, timestamp=None, nonce=None, echostr=None)
        signature = params.signature  # 微信加密签名
        timestamp = params.timestamp
        nonce = params.nonce  # 随机数
        echostr = params.echostr  # 随机字符串

        token = "hongpai`1234567890"
        if signature and timestamp and nonce and echostr:
            args = [token, timestamp, nonce]
            args.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, args)
            hash_code = sha1.hexdigest()
            if hash_code == signature:
                return echostr
        return 'haha'


    def POST(self):
        pass
