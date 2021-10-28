# Python_Spider {ignore}
[toc]

## 爬虫基础



我们可以把互联网比作一张大网，而爬虫（即网络爬虫）便是在网上爬行的蜘蛛。把网的节点比作一个个网页，爬虫爬到这就相当于访问了该页面，获取了其信息。可以把节点的连线比作网页与网页之间的链接关系，这样蜘蛛通过一个节点后，可以顺着节点连线继续爬行到下一个节点，即通过一个网页继续获取后续的网页，这样整个网的节点便可以被蜘蛛全部爬行到，网站的数据就可以被抓取下来了。

### 为什么学习爬虫

为了装x

### 爬虫概述

简单来说，爬虫就是获取网页并提取和保存信息的自动化程序

#### 获取网页

爬虫首先要做的就是爬取网页，这里就是获取网页的源代码，源代码里包含了网页的部分有用信息，所以只要把源代码获取下来，就可以从中提取想要的信息了。

#### 提取信息

获取网页源代码后，接下来就是分析网页源代码，从中提取我们想要的数据。

- 首先，最通用的方法就是采用正则表达式提取，这是一个万能的方法，但是在构造正则表达式时比较复杂且容易出错

- 另外由于网页的结构有一定的规则，所以还有一些根据网页节点属性、CSS选择器或XPath来提取网页信息的库，如 BeautifulSoup，pyquery，lxml 等。使用这些库，我们可以高效快速地从中提取网页信息，如节点的属性、文本值等

提取信息是爬虫非常重要的部分，它可以使复杂的数据变得条理清晰，以便我们后续处理和分析数据。

#### 保存数据

提取信息后，我们一般会将提取到的数据保存到某处以便后续使用。这里保存形式有多种多样，如可以简单保存为txt文本或 json 文本，也可以保存到数据库，如 MySQL 和 MongoDB 等，也可以保存至远程服务器，如借助SFTP进行操作等

#### 自动化程序

说到自动化程序，意思是说爬虫可以代替人来完成这些操作。首先，我们手工当然可以提取到这些信息，但是当量特别大或者想快速获取大量数据的话，肯定还是要借助程序。爬虫就是代替我们来完成这份爬取工作的自动化程序，它可以在抓取过程中进行各种异常处理、错误重试等草垛，确保爬取持续高效的运行。

### 能爬取怎样的数据

在网页中我们能看到各种各样的信息，最常见的便是常规网页，它们对应着HTML代码，而最常抓取的便是HTML源代码

另外，可能有些网页返回的不是HTML代码，而是一个JSON字符串（其中API接口大多采用这样的形式），这种格式的数据方便传输和解析，它们同样可以抓取，而且数据提取更方便

此外，我们还可以看到各种二进制数据，如图片、视频和音频等。利用爬虫，我们可以将这些二进制数据抓取下来，最后保存成对应的文件名。

另外，还可以看到各种扩展名的文件，如CSS、JavaScript和配置文件等，这些其实也是最普通的文件，只要在浏览器里面可以访问到，就可以将其抓取下来

上述内容其实都对应各自的URL，是基于HTTP或HTTPS协议的，只要是这种数据，爬虫都可以抓取



对于爬虫来说，用于爬虫爬取速度过快，在爬取过程中可能遇到同一个IP访问过于频繁的问题，此时网站就会让我们输入验证码登录或者直接封锁IP，这样会给爬取带来机打的不便

使用代理隐藏真实的IP，让服务器误以为是代理服务器在请求自己。这样在爬取过程中通过不断更换代理，就不会被封锁，可以达到很好的爬取效果

### urllib

#### urllib

urllib库，是Python内置的HTTP请求库，不需要额外安装，它包含如下四个模块

- **request** ：它是最基本的HTTP请求模块，可以用来模拟发送请求。就像在浏览器里输入网址一样，只需要给库方法传入URL以及额外的参数，就可以模拟实现这个过程了

- **error** ：异常处理模块，如果出翔请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止

- **parse** ：一个工具模块，提供了许多URL处理方法，比如拆分，解析，合并等

- **rebotparser** ：主要是用来识别网站的robots.txt文件，然后判断哪些网站不可以爬，用得比较少

##### 发送请求

使用urllib的request模块，我们可以方便的实现请求发送并得到响应，

##### urlopen

urllib.request模块提供了最基本的构造HTTP请求的方法，利用它可以模拟浏览器的一个请求发起过程，同时它还带有处理授权验证（authentication）、重定向（redirect）、浏览器Cookies以及其他内容

##### 基本使用

```python
import urllib.request  

response = urllib.request.urlopen('https://www.python.org')
html = response.read().decode('utf-8')
print(type(response))   # <class 'http.client.HTTPResponse'>
```


它是一个HTTPResponse类型的对象，主要包含read、readinto、getheader、getheaders、fileno等方法，以及msg、version、status、reason、debuglevel、closed等属性

调用 read 方法可以得到返回的网页内容，调用 status 属性可以得到返回结果的状态码， 200 代表请求成功，404 代表网页未找到等。

```pyrhon
import urllib.request  

response = urllib.request.urlopen('https://www.python.org')  
print(response.status)  
print(response.getheaders())  
print(response.getheader('Server'))  # 得到以下结果
```


```python
200  
[('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'), ('X-Frame-Options', 'SAMEORIGIN'),   
    ('X-Clacks-Overhead', 'GNU Terry Pratchett'), ('Content-Length', '47397'), ('Accept-Ranges', 'bytes'),   
    ('Date', 'Mon, 01 Aug 2016 09:57:31 GMT'), ('Via', '1.1 varnish'), ('Age', '2473'), ('Connection', 'close'),   
    ('X-Served-By', 'cache-lcy1125-LCY'), ('X-Cache', 'HIT'), ('X-Cache-Hits', '23'), ('Vary', 'Cookie'),   
    ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')]  
nginx
```


前两个分别输出了相应的状态码和头信息，最后一个输出通过调用getheader方法并传递一个参数Server获取了响应头中的Server值，结果是Nginx，意思是服务器是用Nginx搭建的

利用最基本的urlopen方法，可以完成最基本的简单网页的GET请求抓取

##### 参数

```python
urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
```


1. **data参数** 

data参数是可选的。如果要添加改参数，需要使用bytes方法将参数转化为字节流编码格式的内容，即bytes类型。另外，如果传递了这个参数，则它的请求方式就不再是GET请求，而是POST请求

```python
import urllib.parse  
import urllib.request  

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')  
response = urllib.request.urlopen('http://httpbin.org/post', data=data)  
print(response.read()) 
```


```python
{"args": {},  
     "data": "","files": {},"form": {"word":"hello"},"headers": {"Accept-Encoding":"identity","Content-Length":"10","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"Python-urllib/3.5"},"json": null,"origin":"123.124.23.253","url":"http://httpbin.org/post"}
```


这里我们传递了一个参数 word，值是 hello。它需要被转码成 bytes（字节流）类型。其中转字节流采用了 bytes 方法，该方法的第一个参数需要是 str（字符串）类型，需要用 urllib.parse 模块里的 urlencode 方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为 utf8。

在这里请求的站点是 [httpbin.org](http://httpbin.org)，它可以提供 HTTP 请求测试，本次我们请求的 URL 为：[http://httpbin.org/post](http://httpbin.org/post)，这个链接可以用来测试 POST 请求，它可以输出 Request 的一些信息，其中就包含我们传递的 data 参数

2. **timeout参数** 

timeout参数用于设置超时时间，单位为秒，意思就是如果请求超出了设置的这个时间，还没有得到响应，就会抛出异常。如果不指定该参数，就会使用全局默认时间。它支持HTTP、HTTPS、FTP请求

```python
import urllib.request  

response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)  
print(response.read())

```


```python
During handling of the above exception, another exception occurred:
Traceback (most recent call last): File "/var/py/python/urllibtest.py", line 4, in <module> response =
urllib.request.urlopen('http://httpbin.org/get', timeout=1)
...
urllib.error.URLError: <urlopen error timed out>
```


这里我们设置超时时间是1秒，程度一秒过后，服务器依然没有响应，于是抛出了URLError异常。该异常属于urllib.error模块，错误原因是超时。因此我们可以使用异常处理

3. **其他参数** 

	- 除了data参数和timeout参数外，还有context参数，它必须是ssl.SSLContext类型，用来指定SSL设置

	- 此外，cafile和capath这两个参数分别制定CA证书和它的路劲，这个在请求HTTPS链接时会有用

4. **官方文档** ：[https://docs.python.org/3/library/urllib.request.html](https://docs.python.org/3/library/urllib.request.html)

#### request

urlopen方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建一个完整的请求，如果请求中需要加入Headers等信息，就可以利用更强大的Request类来构建

```python
import urllib.request  
  
request = urllib.request.Request('https://python.org')  
response = urllib.request.urlopen(request)  
print(response.read().decode('utf-8'))
```


我们依然是用urlopen方法来发送这个请求，只不过这次该方法的参数不再是URL，而是一个Request类型的对象。通过构造这个数据结构，一方面我们可以将请求独立成一个对象，另一方面可更加丰富灵活地配置参数

```python
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```


- 第一个参数url用于请求URL，这是必传参数，其他都是可选参数

- 第二个参数data如果要传，必须传bytes（字节流）类型的。如果它是字典，可以先用urllib.parse模块里的urlencode() 编码

- 第三个参数headers是一个字典，它就是请求头，我们可以在构造请求时通过headers参数直接构造，也可以通过调用请求实例的add_headers() 方法添加

- 添加请求头最常用的用法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是Python-urllib，我们可以通过修改它来伪装浏览器。

- 第四个参数 origin_req_host 指的是请求方的 host 名称或者 IP 地址。

- 第五个参数unverifiable表示这个请求是否是无法验证的，默认为False，意思就是说用户没有足够的权限来选择接受这个请求的结果。例如，我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，这时unverifiable 的值就是 True。

- 第六个参数method是一个字符串，用来指定请求使用的方法，比如GET、POST、PUT等

```python
from urllib import request, parse  

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'  
}
dict = {'name': 'Germey'}
data = bytes(parse.urlencode(dict), encoding='utf8')

req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
```


#### 高级用法

Handler。简而言之，我们可以把它理解为各种处理器，有专门处理登录验证的，有处理Cookies的，有处理代理设置的。利用他们，我们几乎可以做到HTTP请求中所有的事情

urllib.request模块里的BaseHandler类，它是所有其他Handler的父类，它提供了最基本的方法，例如default_open、protocol_request等

- HTTPDefaultErrorHandler 用于处理 HTTP 响应错误，错误都会抛出 HTTPError 类型的异常。

- HTTPRedirectHandler 用于处理重定向。

- HTTPCookieProcessor 用于处理 Cookies。

- ProxyHandler 用于设置代理，默认代理为空。

- HTTPPasswordMgr 用于管理密码，它维护了用户名密码的表。

- HTTPBasicAuthHandler 用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题。

- 官方文档： [https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler)

1. **验证** 

有些网站在打开时就会弹出提示框，直接提示输入用户名和密码，验证成功才能查看页面，如果要请求这样的页面，需要借助HTTPBasicAuthHandler就可以完成

```python
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener  
from urllib.error import URLError  

username = 'username'  
password = 'password'  
url = 'http://localhost:5000/'  

p = HTTPPasswordMgrWithDefaultRealm()  
p.add_password(None, url, username, password)  
auth_handler = HTTPBasicAuthHandler(p)  
opener = build_opener(auth_handler)  

try:  
    result = opener.open(url)  
    html = result.read().decode('utf-8')  
    print(html)  
except URLError as e:  
    print(e.reason)
```


这里首先实例化HTTPBasicAuthHandler对象，其参数是HTTPPasswordMgrWithDefaultRealm对象，它利用add_password方法添加进去用户名和密码，这样就建立了一个处理验证的Handler

接下来利用Opener的open方法打开链接，就可以完成验证了。这里获取到的结果就是验证后的页面源码内容

2. **代理** 

在做爬虫的时候，免不了要使用代理，如果要添加代理，可以

```python
from urllib.error import URLError  
from urllib.request import ProxyHandler, build_opener  

proxy_handler = ProxyHandler({  
    'http': 'http://127.0.0.1:9743',  
    'https': 'https://127.0.0.1:9743'  
})  
opener = build_opener(proxy_handler)  
try:  
    response = opener.open('https://www.baidu.com')  
    print(response.read().decode('utf-8'))  
except URLError as e:  
    print(e.reason)
```


这里我们在本地搭建了一个代理，它运行在9743端口上

这里使用了ProxyHandler，其参数是一个字典，键名是协议类型（比如HTTP或者HTTPS等），键值是代理链接，可以添加多个代理

然后，利用这个Handler及build_opener方法构造一个Opener，之后发送请求即可

3. **Cookies** 

Cookies的处理就需要相关的Handler，将网站的Cookies获取下来的代码如下

```python
import http.cookiejar, urllib.request  

cookie = http.cookiejar.CookieJar()  
handler = urllib.request.HTTPCookieProcessor(cookie)  
opener = urllib.request.build_opener(handler)  
response = opener.open('http://www.baidu.com')  
for item in cookie:  
    print(item.name+"="+item.value) 
```


```python
BAIDUID=2E65A683F8A8BA3DF521469DF8EFF1E1:FG=1  
BIDUPSID=2E65A683F8A8BA3DF521469DF8EFF1E1  
H_PS_PSSID=20987_1421_18282_17949_21122_17001_21227_21189_21161_20927  
PSTM=1474900615  
BDSVRTM=0  
BD_HOME=0
```


首先，我们必须声明一个CookieJar对象。接下来，就需要利用HTTPCookisProcessor来构建一个Handler，最后利用build_opener方法构建出Opener，执行open函数即可

```python
filename = 'cookies.txt'  
cookie = http.cookiejar.MozillaCookieJar(filename)  
handler = urllib.request.HTTPCookieProcessor(cookie)  
opener = urllib.request.build_opener(handler)  
response = opener.open('http://www.baidu.com')  
cookie.save(ignore_discard=True, ignore_expires=True)
```


这时CookieJar就需要换成MozillaCookieJar，它在生成文件时会用到，是CookieJar的子类，可以用来处理Cookies和文件相关的事件，比如读取和保存Cookies，可以将Cookies保存成Mozilla型浏览器的Cookies格式

运行之后，可以生成一个cookies.txt文件

另外，LWPCookieJar同样可以读取和保存Cookies，但是保存的格式和MozillaCookieJar不一样，它会保存成libwww-perl（LWP）格式的Cookies文件

要保存成LWP格式的Cookies文件，可以在声明时改为

```python
cookie = http.cookiejar.LWPCookieJar(filename)
```


生成Cookies文件后，我们可以通过以下方法读取并利用

```python
cookie = http.cookiejar.LWPCookieJar()  
cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)  
handler = urllib.request.HTTPCookieProcessor(cookie)  
opener = urllib.request.build_opener(handler)  
response = opener.open('http://www.baidu.com')  
print(response.read().decode('utf-8'))
```


这里调用load方法来读取本地的Cookies 文件，获取到了Cookies的内容。不过前提是我们首先生成了LWPCookieJar格式的Cookies，并保存成文件，然后读取Cookies之后使用相同的方法构建Handler和Opener即可完成操作

运行结果正常的话，会输出网页的源代码

通过上面的方法，我们就可以实现大多数请求功能的设置了

官方文档：[https://docs.python.org/zh-cn/3/library/urllib.html](https://docs.python.org/zh-cn/3/library/urllib.html)

## requests

## 页面解析

### Python正则表达式

---

### BeautifulSoup

#### 简介和安装

- Beautiful Soup是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.

- 环境安装

- pip install bs4

- pip install lxml

#### 使用

1. 将一段文档传入BeautifulSoup的构造方法，就能得到一个文档的对象，可以传入一段字符换或一个文件句柄

```python
from bs4 import BeautifulSoup
# 本地文件
soup = BeautifulSoup(open("index.html"))
# 直接解析
soup = BeautifulSoup("<html>data</html>") 
```


然后BeautifulSoup会选择最合适的解析器来解析这段文档，如果手动指定解析器那么BeautifulSoup会选择指定的解析器来解析文档

2. 获取元素

```Python
from bs4 import BeautifulSoup
html = 'xxx'
# 解析数据，以lxml的形式解析
soup = BeautifulSoup(html, 'lxml') 

print(soup.prettify())  # 格式化输出文档
print(soup.title.string)  # 输出文档title节点文本内容

# 提取标签
print(soup.title)  # <title> title </title>
print(type(soup.title))  # <class 'bs4.element.Tag'>
print(soup.title.string) # title
print(soup.head)  # <head><title>title</title></head>
print(soup.p)  # <p> 这是p标签 </p>

# 获取信息
print(soup.title.name)  # 获取节点名称， title

# 获取属性
print(soup.p.attrs) # 返回标签属性(字典形式)
print(soup.p.attrs['class'])  # 返回类名
# 也可以
print(soup.p['class'])  # 返回类名
# 有些属性的值是唯一的，返回字符串，有解属性可能有多个值（如class），返回列表


# 获取文本
print(soup.p.string)  # 获取节点之间的文本（只能获取直系内容）
print(soup.p.get_text())  # 获取标签下所有文本内容
 
#子节点
print(soup.p.contents)  # 获取节点内的所有内容（包括缩进，标签）
print(soup.p.children)  # 和上述一样
 
 
print(soup.a.parent)  # 返回父节点（即a元素所在标签）
 
print(soup.c.parents)  # 返回所有的祖先节点

# 兄弟节点
print( soup.a.next_sibling)
print(soup.a.previous_sibling)
print(soup.a.next_siblings)
print(soup.a.previous_siblings)
 
```


3. **方法选择器** 

- find，返回第一个符合要求的元素

- find_all，返回所有符合标签的元素

```python
soup.find_all(name='ul')  # 返回所有的ul标签
soup.find_all(name='ul', class_/id/attr='value')  # 返回所有符合标签的元素，name表示标签名，后面的表示筛选条件（因为class在Python中是一个关键字，所以使用class_

soup.find_all(attrs={'name': 'username'}
soup.find_all(class_='header')

# text参数可以用来匹配节点的文本，传入的形式可以是字符串，也可是正则表达式对象
soup.find_all(text=re.compile('this')) 
```


- select，select可以使用css选择器来选择元素

```python
soup.select('.header .ul>li a')
```


- 其他

- find_parents 和 find_parent

- find_next_siblings 和 find_next_sibling

- find_previous_siblings 和 find_previous_sibling

- find_all_next 和 find_next

- find_all_previous 和 find_previous

---

### Xpath

Xpath的选择功能十分强大，它提供了非常简洁明了的路径选择表达式。另外，它还提供了超过100个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理等。

- 官方文档：[https://www.w3.org/TR/xpath/](https://www.w3.org/TR/xpath/)

#### Xpath 使用

```Python
from lxml import etree  # 导入相关库

# 将本地的html文档中的源码数据加载到etree对象中
etree.pase(filePath)

# 从互联网上获取的源码数据加载到该对象中
etree.HTML('page_text') 
```


#### Xpath 语法

##### 选取节点

|**表达式** |**描述** |
|---|---|
|nodename|选取此节点的所有子节点|
|/|从根节点选取|
|//|从匹配选择当前节点选择文档中的节点，不考虑他们的位置|
|.|选取当前节点|
|..|选取当前节点的父节点|
|@|选取属性|



例：

|**路径表达式** |**结果** |
|---|---|
|bookstore|选取 bookstore 元素的所有子节点。|
|/bookstore|选取根元素 bookstore。<br /><br />注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！|
|bookstore/book|选取属于 bookstore 的子元素的所有 book 元素。|
|//book|选取所有 book 子元素，而不管它们在文档中的位置。|
|bookstore//book|选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。|
|//@lang|选取名为 lang 的所有属性。|



##### 指定特定节点

|路径表达式|结果|
|---|---|
|路径表达式|结果|
|/bookstore/book[1]|选取属于 bookstore 子元素的第一个 book 元素。|
|/bookstore/book[last()]|选取属于 bookstore 子元素的最后一个 book 元素。|
|/bookstore/book[last()-1]|选取属于 bookstore 子元素的倒数第二个 book 元素。|
|/bookstore/book[position()<3]|选取最前面的两个属于 bookstore 元素的子元素的 book 元素。|
|//title[@lang]|选取所有拥有名为 lang 的属性的 title 元素。|
|//title[@lang='eng']|选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。|
|/bookstore/book[price>35.00]|选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。|
|/bookstore/book[price>35.00]/title|选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。|



##### 选取未知节点

|**路径表达式** |**结果** |
|---|---|
|*|匹配任何元素节点。|
|@*|匹配任何属性节点。|
|node()|匹配任何类型的节点。|
|/bookstore/*|选取 bookstore 元素的所有子元素。|



##### 选取若干路径

|**路径表达式** |**结果** |
|---|---|
|//book/title | //book/price|选取 book 元素的所有 title 和 price 元素。|
|//title | //price|选取文档中的所有 title 和 price 元素。|
|/bookstore/book/title | //price|选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。|



#####  Xpath轴

|**轴名称** |**结果** |
|---|---|
|ancestor|选取当前节点的所有先辈（父、祖父等）。|
|ancestor-or-self|选取当前节点的所有先辈（父、祖父等）以及当前节点本身。|
|attribute|选取当前节点的所有属性。|
|child|选取当前节点的所有子元素。|
|descendant|选取当前节点的所有后代元素（子、孙等）。|
|descendant-or-self|选取当前节点的所有后代元素（子、孙等）以及当前节点本身。|
|following|选取文档中当前节点的结束标签之后的所有节点。|
|namespace|选取当前节点的所有命名空间节点。|
|parent|选取当前节点的父节点。|
|preceding|选取文档中当前节点的开始标签之前的所有节点。|
|preceding-sibling|选取当前节点之前的所有同级节点。|
|self|选取当前节点。|



##### 获取内容

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())

# 获取文本内容（直系文本内容） /text()
print(html.xpath('//li[@class="item"]/text()'))

# 获取文本内容（所有文本内容）  //text()
print(html.xpath('//li[@class="item"]//text()'))

#  获取属性
print(html.xpath('//li/a/@href')) # 获取a标签的href 属性
```


##### 多条件匹配

1. 属性多值匹配

```python
from lxml import etree  
text = '''  
<li class="li li-first">122</li> 
'''  
html = etree.HTML(text)

# 如果li标签的class属性有多个值，以下方法将不能获取到正确的元素
result = html.xpath('//li[@class="li"]/text()')  
print(result)  # 输出 []

# 想要通过一个属性获取到正确的元素，可以使用contains方法
result = html.xpath('//li[contains(@class, "li")]/text()')  
print(result)  # 输出['122']
```


2. 多属性匹配

```python
from lxml import etree  
text = '''  
<li class="li li-first" name="item">123</li>
'''  
html = etree.HTML(text) 

# 同时满足所有条件才能匹配到
result = html.xpath('//li[contains(@class, "li") and @name="item"]/text()')  
print(result)  # 输出 ['123'] 
```


##### Xpath运算符

|运算符|描述|实例|返回值|
|---|---|---|---|
|||计算两个节点集|//book | //cd|返回所有拥有 book 和 cd 元素的节点集|
|+|加法|6 + 4|10|
|-|减法|6 - 4|2|
|*|乘法|6 * 4|24|
|div|除法|8 div 4|2|
|=|等于|price=9.80|如果 price 是 9.80，则返回 true。<br /><br />如果 price 是 9.90，则返回 false。|
|!=|不等于|price!=9.80|如果 price 是 9.90，则返回 true。<br /><br />如果 price 是 9.80，则返回 false。|
|<|小于|price<9.80|如果 price 是 9.00，则返回 true。<br /><br />如果 price 是 9.90，则返回 false。|
|<=|小于或等于|price<=9.80|如果 price 是 9.00，则返回 true。<br /><br />如果 price 是 9.90，则返回 false。|
|>|大于|price>9.80|如果 price 是 9.90，则返回 true。<br /><br />如果 price 是 9.80，则返回 false。|
|>=|大于或等于|price>=9.80|如果 price 是 9.90，则返回 true。<br /><br />如果 price 是 9.70，则返回 false。|
|or|或|price=9.80 or price=9.70|如果 price 是 9.80，则返回 true。<br /><br />如果 price 是 9.50，则返回 false。|
|and|与|price>9.00 and price<9.90|如果 price 是 9.80，则返回 true。<br /><br />如果 price 是 8.50，则返回 false。|
|mod|计算除法的余数|5 mod 2|1|

## 数据存储

### 文件存储

#### txt文本存储

直接通过文件写入的方式存取数据文件操作（见Python笔记）

---

#### JSON文件存储

JSON，全称为 JavaScript Object Notation，也就是JavaScript对象标记，它通过对象和数组的组合来表示数据，构造简洁但是结构化程度非常高，是一种轻量级的数据交换格式。

1. Python3中可以使用JSON模块来对JSON数据进行编解码，它包含了两个函数：

- json.dumps()：对数据进行编码

- json.loads()：对数据进行解码

![](https://www.runoob.com/wp-content/uploads/2016/04/json-dumps-loads.png)

2. Python编码为JSON类型转换对应表

|Python|JSON|
|---|---|
|dict|object|
|list、tuple|array|
|str|string|
|int、float、int & float-derived Enums|number|
|True|true|
|False|false|
|None|null|



```python
import json
 
# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


# 中文写入文件
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(data, indent=2, ensure_ascii=False)
# 如果没有ensure_ascii 参数，会默认将中文转换为Unicode字符
```

---

#### CSV文件存储

CSV，全称为Comma-Separated Values，中文可以叫做都好分隔值或字符分隔值，其文件以纯文本形式存储表格数据。该文件是一个字符序列，可以由任意数目的记录组成，记录间以某种换行符分割。每条记录由字符组成，字段间的分隔符是其他字符或字符串，最常见的是逗号或制表符。不过所有记录都有完全相同的字符序列，相当于一个结构化表的纯文本形式。它比Excel文件更加简洁，XLS文本时电子表格，它包含了文本、数值、公式、和格式等内容，而CSV中不包含这些内容，就是特定字符分隔的纯文本，结构简单清晰。所以，有时候用CSV来保存数据是比较方便的。

**也可以通过pandas库来进行存储和读取数据** 

##### 文件写入

```python
import csv

# 打开文件，如果有中文需要指定字符编码
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')  # 获得文件句柄, delimiter参数表示列与列之间的分隔符，没有次参数时分隔符为逗号
    writer.writerow(['id', 'name', 'age'])  # 写入数据
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    
    # 可以使用writerows同时写入多行，此时的参数为二维列表
     writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22]])

```


**通过字典方式写入** 

```python
import csv

with open('data.csv', 'w') as csvfile:
'''先定义三个字段，用filednames表示，然后将其传给DictWriter来初始化一个字典写入对象，接着可以调用writerheader方法写入头信息，然后调用writerow方法传入相应字典即可'''
    filednames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, filednames=filednames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
```


##### 文件读取

```python
import csv  

with open('data.csv', 'r', encoding='utf-8') as csvfile:  
    reader = csv.reader(csvfile)  
    for row in reader:  
        print(row)
```

---

### 数据库存储

##### 	1. MySQL

##### 	2. MongoDB

##### 	3. Redis


## Ajax数据和动态渲染

### Ajax

有时候我们在用requests抓取网页的时候，得到的结果可能和在浏览器中看到的不一样，在浏览器中可以看到正常显示的页面数据，但是使用requests得到的结果并没有。这是因为requests获取的都是原始的HTML文档，而浏览器中的页面则是通过JavaScript处理数据后生成的结果，这些数据的来源有多重，可能是通过Ajax加载的，可能是包含在HTML文档中的，也可能是通过JavaScript和特定算法计算后生成的

对于第一种情况，数据加载是一种异步加载方式，原始的网页最初不会包含某些数据，原始页面加载后，会再向服务器请求某个接口获取数据，然后数据才被处理从而呈现到网页上，这其实就是发送了一个Ajax请求

#### Ajax

Ajax，全称Asynchronous JavaScript and XML，即异步的JavaScript和XML。

#### Ajax分析方法

打开浏览器开发者工具，网络下面的XHR筛选

---

### 动态渲染页面

JavaScript动态渲染的页面不止Ajax这一种，有些网页是由JavaScript生成的，并非原始HTML代码，这其中并不包含Ajax请求，例如淘宝这样的页面，即使是Ajax获取的数据，但是其Ajax接口含有很多加密参数，我们难以直接找出其规律，也很难直接找出去去规律，也很难分析Ajax来抓取

为了解决这些问题，我们可以直接使用模拟浏览器运行的方式来实现，这样就可以做到在浏览器中看到什么样，抓取的源码就是什么样，可见即可爬。

Python提供了很多模拟浏览器运行的库，如Selenium，Splash，PyV8，Ghost等。

---

#### Selenium的使用

Selenium是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击、下拉等操作，同时还可以获取浏览器当前呈现的页面的源代码。对于一些JavaScript动态渲染的页面来说，这种抓取方式非常有效。

##### 准备工作

在开始之前，需要安装好Chrome浏览器并配置好ChromeDriver（两者版本需要一致，将ChromeDriver放到Python的Scripts目录下，其他操作系统需要配置环境变量），还需要安装好Python的Selenium库。

##### 开始使用

```python
from selenium import webdriver

# 打开浏览器, 传入的参数是驱动的路径
wd = webdriver.Chrome(r'D:\Installation package\Chrome\chromedriver.exe')

# 浏览器打开某个网址
wd.get('https://www.baidu.com')

# 关闭浏览器
wd.quit()
```


##### 选择元素

- 使用 `find_elements` 选择的是符合条件的 `所有` 元素， 如果没有符合条件的元素， `返回空列表`

- 使用 `find_element` 选择的是符合条件的 `第一个` 元素， 如果没有符合条件的元素， `抛出 NoSuchElementException 异常`

    ```python
    username = wd.find_element_by_id('username')  # 通过 id
    header= element.find_element_by_class_name('header')  # 通过 类名
    div = wd.find_element_by_tag_name('div')  # 通过标签名
    container = wd.find_element_by_css_selector('.container')  # 通过css选择器
    footer = wd.find_elements_by_css_selector('.footer, #footer')
    
    # 通过xpath选择
    div = wd.find_elements_by_xpath('//div')
    ```


- 在我们进行网页操作的时候，有的元素不是可以立即出现的，可能需要加载一段时间，Selenium提供了一个周期性（每隔半秒钟）重新查找该元素的方案`implicitly_wait`，直到该元素找到。

    ```python
    wd.implicitly_wait(10)  # 参数用来指定最大等待时长
    ```


##### 操作元素

1. 点击元素

	- `element.click()`方法，点击元素的时候，浏览器点击的是该元素的`中心点`位置

2. 输入框

	- `element.send_key(需要输入的字符)`在元素内输入文字

	- `element.clear()`清空文字

3. 获取元素信息

	- `element.text`获取元素`展示在页面上`的文本内容

	- 有时候元素的文本内容没有展示在页面上，或者没有完全展示在页面上。这时可以尝试使用	`element.get_attribute('innerText')` ，或者 		`element.get_attribute('textContent')`

	- `element.get_attribute('class')`获取元素属性class（可以更换为其他）的值

4. 获取元素对应的HTML

	- `element.get_attribute('outerHTML')`获取整个元素对应的HTML文本内容

	- `element.get_attribute('innerHTML')`获取某个元素`内部`的HTML内容

5. 获取输入框文字

	- `element.get_attribute('value')`获取输入框中的内容

6. 动作链（鼠标拖拽、键盘按键）

	- 文档：[https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains)

        ```python
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        
        browser = webdriver.Chrome()
        url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
        browser.get(url)
        browser.switch_to.frame('iframeResult')
        source = browser.find_element_by_css_selector('#draggable')
        target = browser.find_element_by_css_selector('#droppable')
        actions = ActionChains(browser)
        actions.drag_and_drop(source, target)  # 将source拖拽到target
        actions.perform()  # 执行操作
        ```


7. 执行JavaScript代码

	- `wd.execute_script('js代码')`

8. Cookies操作

	- `wd.get_cookies()`获取Cookies

	- `wd.add_cookie()`设置Cookies

	- `wd.delete_all_cookies()`删除Cookies

##### 窗口操作

有时候，网页中会嵌入另一个网页（iframe元素），这时候按照之前的方法将不能选取到想要的元素，或者有时候点击一个链接浏览器会打开一个新的窗口

1. `wd.switch_to.frame(frame_reference)`参数可以是iframe元素的id或者name属性值，或者通过上述方法选取到的iframe对象

2. 切换到原来的主HTML，`wd.switch_to.default_content()`，有时候我们切换到iframe界面操作完之后，还需要返回到原来的主界面进行操作

3. 切换窗口，`wd.switch_to.window(handle)`

	- 打开多个窗口，需要定位到最新打开的窗口

        ```python
        # 获取打开的多个窗口句柄
        windows = wd.window_handles 
        # 切换到当前最新打开的窗口
        wd.switch_to.window(windows[-1])
       ```
   
   - 打开两个窗口，需要新打开的窗口

        ```python
        # 获得打开的第一个窗口句柄
        window_1 = wd.current_window_handle
        # 获得打开的所有的窗口句柄
        windows = wd.window_handles
        # 切换到最新的窗口
        for current_window in windows:
        if current_window != window_1:
        wd.switch_to.window(current_window) 
        ```

    - 返回之前的窗口
   
        ``` python
        # 保存当前窗口的句柄
        mainWindow = wd.current_window_handle
        # 切换到之前的窗口
        wd.switch_to.window(mainWindow) 
        ```


4. 前进后退

    ```python
    # 返回
    wd.back()
    # 前进
    wd.forward()
    
    ```


##### 选择框（单选框，多选框，select）

1. 单选框radio和多选框checkbox使用选取元素之后点击的形式即可选取

2. select

	- `select_by_value()`通过value选择

	- `select_by_index()`取消选择

	- `select_by_index()`通过索引选择（索引从0开始）

	- `deselect_by_index()`取消选择

	- `select_by_visible_text()`通过可见文本选择

	- `deselect_by_visible_text()`取消选择

	- `deselect_all()`取消所有选择

## Splash

## 验证码识别
