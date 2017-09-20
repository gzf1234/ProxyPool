mport requests
from requests.exceptions import ProxyError,Timeout,ConnectionError,ChunkedEncodingError
import time
from proxypool.utils import UserAgents
import random

# user_agent = random.choice(UserAgents)

def get_proxy():
    r = requests.get('http://127.0.0.1:5000/get')
    proxy = r.text
    return proxy


def get_count_proxies():
    r = requests.get('http://127.0.0.1:5000/count')
    proxies = r.text
    return proxies

def crawl(url, proxy, headers):
    proxies = {'http': proxy}
    r = requests.get(url, proxies=proxies, headers=headers, timeout=6)
    return r

def main(url):
    count = 0
    while True:
        print('第',count,'次测试')
        user_agent = random.choice(UserAgents)
        count += 1
        try:
            #请求不同的代理和headers
            global count_proxies
            headers = {'User-Agent':user_agent}
            count_proxies = get_count_proxies()
            print('代理总数:',count_proxies,' 当前所使用的代理:',proxy,'\n',headers)
            start_time = time.clock()
            html = crawl(url, proxy, headers)
            end_time = time.clock()
            print('代理连接时间:',(str(end_time-start_time))[:4], '秒')
            if html.status_code == 200:
                print(html)
                return count
                break
            elif count >= 10:
                print('抓取网页失败')
                break
        except (ChunkedEncodingError,ConnectionError,Timeout,UnboundLocalError,UnicodeError,ProxyError):

            proxy = get_proxy()
            print('代理失败，更换代理','\n')





if __name__ == '__main__':
    url = 'http://www.google.com'
    main(url)

