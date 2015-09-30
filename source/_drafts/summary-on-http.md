title: "summary-on-http"
date: 2015-09-20 21:33:07
categories: 
tags: 
comments: true
description: 《图解HTTP》笔记，顺带复习http相关知识点
keywords: 图解HTTP,IP协议,ARP,TCP
---

TCP在网络OSI的七层模型中的第四层——Transport层
IP在第三层——Network层，
ARP在第二层——Data Link层，
在第二层上的数据，我们叫Frame，
在第三层上的数据叫Packet，
第四层的数据叫Segment。

##IP(Internet Protocol)
传送packet
IP地址
MAC地址`（Media Access Control Address）`	
ARP协议 根据IP地址反查对应的MAC地址，在网络设备间中转时使用




##TCP
- 为了更容易传送大数据而分割数据
- 确认数据是否准确送达
	- 三次握手

### 三次握手（three-way handshaking）
SYN
ACK


##DNS
通过domain查找ip地址，或从ip反查domain
![123](http://i.imgur.com/6AuX0a5.jpg)



#URI,URL
URI 统一资源表示符`(Identifier)` 标识资源
URL 统一资源定位符`(Locator)` 标识地点
URL是URI的子集

#HTTP协议
##stateless（无状态）
为了快速处理大量事务，协议的可伸缩性，而做的选择（在目前的大多数场景过时了？即使restful服务也需要维持状态）
Cookie假装是有状态的
HTTP 1.1支持的方法：

| Tables        | 目的           
| - |
| GET	| 获取资源		|
| POST	| 传输实体主体
| PUT	| 传输文件
| HEAD	| 获得报文首部	|和GET一样，但只返回响应头，用于确认URI的有效性及资源更新日期
| DELETE | 删除文件
| OPTIONS| 查询支持的方法
| TRACE	 | 用于追踪路径
| CONNECT|用隧道协议连接

##keep-alive
请求头中：`Connection:keep-alive`
建立一次TCP连接后，可以进行多次（请求-响应）
##pipeling（管线化）
并行发送多个请求，而不用等前一个收到响应，才发送下一请求
##Cookie
1. 响应头中`set-cookie`，
2. 客户端保存cookie，在之后的请求中加入cookie，
3. 服务端检查cookie，获取状态信息

##refer：
[TCP的那些事儿-coolshell](http://coolshell.cn/articles/11564.html)