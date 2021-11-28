# 验证代理ip.py
import requests
ip_list = open('ip.txt', encoding='utf-8').read().split('，')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

quality_ip = []
# 用百度测试IP是否能正常连网
url = 'https://www.baidu.com'
for ip in ip_list:
    response = requests.get(url, proxies={'http': 'http://' + ip}, headers=headers, timeout=2)
    if response.text:
        quality_ip.append(ip)
        print(ip)
    else:
        continue
with open('quality_ip.txt', 'wb') as f:
    f.write('，'.join(quality_ip).encode('utf-8'))