# 爬取代理ip.py
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
ip_list = []
url_list = []
for i in range(1, 35):
    url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(i)
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'
    # print(response.text)
    if response.status_code == 200:
        html = etree.HTML(response.text)
        # //*[@id="footer"]/div/table/tbody/tr
        # ips = html.xpath('//*[@id="footer"]/div/table/tbody/tr')[1:]
        ips = html.xpath('//*[@id="footer"]/div/table/tr')[1:]
        # print(ips)
        for ip in ips:
            IP1 = ip.xpath('./td[1]/text()')[0]
            IP2 = ip.xpath('./td[2]/text()')[0]
            IP = IP1 + ':' + IP2
            ip_list.append(IP)
            print(IP)
with open('ip.txt', 'wb') as f:
    f.write('，'.join(ip_list).encode('utf-8'))






