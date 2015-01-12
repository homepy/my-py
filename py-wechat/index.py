# -- coding: utf-8 --
import os

import sae
import web

import controllers

class Redirect:
    def GET(self, path):
        web.seeother('/' + path)

        
web.config.debug = True
urls = (
    '/(.*)/', 'Redirect',
    '/weixin-dev', 'controllers.weixin.WeixinDev'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)
