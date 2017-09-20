# ProxyPool


# 安装
## 安装python

至少Python3.5以上

安装Redis

https://github.com/MSOpenTech/redis/releases

安装好之后将Redis服务开启

配置代理池
```cd proxypool
进入proxypool目录,修改settings.py文件
```
安装依赖

```pip3 install -r requirments.txt```

打开代理池和API

```pyhton3 run.py```

获取代理
利用requests访问接口获取代理
```python
import requests
PROXY_POOL_URL = 'http:localhost:5000/get'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except  ConnectionError:
        return None
```
## 各模块的功能
- getter.py

  爬虫模块

        class proxypool.getter.FreeProxyGetter
        
        |爬虫类，用于抓取各个代理免费代理网站上的代理,可以随意改写抓取规则。
- schedule.py

  调度器模块
```
  class proxypool.schedule.ValidityTester
      异步检测类，可以对给定的代理可用性进行异步检测。
  class proxypool.schedule.Schedule
      代理池启动类，运行RUN函数时，会创建两个进程，分别对代理池进行增加和更新。
  class porxypool.schedule.PoolAdder
      代理添加器，用来触发爬虫模块，对代理池的代理进行添加，当代理数量到达指定阈值时停止工作。
```
- db.py

  Redis数据库连接模块
```
  class proxypool.db.RedisClient
    数据库操作类，维持与数据库的连接和数据库的增删改查。
```
- error.py

  异常模块

        class proxypool.error.ResourceDelpetionError

        资源枯竭异常，如果所有的代理网站都抓取不到可用的代理，则抛出异常。

        class proxypool.error.PoolEmptyError

        如果代理池长时间为空，则抛出异常。

- pi.py

  API模块，启动一个Web服务，使用Flask实现，对外提供代理资源

- utils.py

  工具箱，里面包含网页请求方法

- settings.py

  设置

















