# 使用代理ip.py
import random
import requests
ip_list = open('quality_ip.txt', encoding='utf-8').read().split('，')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# 这里的url为要爬取的相应网址
url = 'https://www.csdn.net/'
r = requests.get(url, proxies={'http': 'http://' + random.choice(ip_list)}, headers=headers)
r.encoding = 'utf-8'
print(r.text)
