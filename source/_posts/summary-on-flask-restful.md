title: flask-restful
date: 2015-06-04 19:47:12
categories: flask
tags: flask,restful
comments: true
description: 
keywords: restful,flask,python

---
6个原则
- Uniform Interface
- Stateless
- Cacheable	
- Client-Server
- Layered System 	#分层系统 多层server
- Code on Demand 	#最小化


> 默认下，RequestParser 试着从 flask.Request.values，以及 flask.Request.json 解析值。


查看了一下json在flask\wrappers.py#Request类中
values在werkzeug\wrappers.py#BaseRequest类中
python,flask及其相关插件，sphinx中文文档
[http://www.pythondoc.com/](http://www.pythondoc.com/)