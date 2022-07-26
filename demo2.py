import random
import sys
import time
import uuid
from time import sleep

import requests
from fake_useragent import UserAgent

proxy = '20.81.62.32:3128'

proxies = [
    {'http': 'http://{}'.format(proxy), 'https': 'http://{}'.format(proxy)},
]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'Keep-Alive',
    'User-Agent': str(UserAgent().random),
}


def spider(uri):
    r = requests.session().get(uri, headers=headers, timeout=10)
    r.raise_for_status()
    print('status_code: {}'.format(r.status_code))
    r.encoding = r.apparent_encoding
    return r.text


if __name__ == '__main__':
    start_time = time.localtime()
    urls = [
        'https://www.walmart.com/ip/Athletic-Works-Women-s-Core-Active-Racerback-Tank-2-Pack/951258535',
        'https://www.walmart.com/ip/Ugly-Stik-6-6-Elite-Baitcast-Rod-and-Reel-Casting-Combo/49112520',
        'https://www.walmart.com/ip/IRON-Clothing-Men-s-Yukon-Stretch-Twill-Flat-Front-Short/630409295',
        'https://www.walmart.com/ip/Fruit-of-the-Loom-Men-s-Everlight-Short-Sleeve-Raglan-T-Shirt-2-Pack-Sizes-S-2XL/276155124',
        'https://www.walmart.com/ip/Vercelli-Strada-All-Season-235-45R17-97W-Tire/110720598',
        'https://www.walmart.com/ip/Cuisinart-Black-12-Cups-Single-Serve-Brewer/869574526',
        'https://www.walmart.com/ip/Son-of-the-Gods-DVD/15049485',
        'https://www.walmart.com/ip/My-Three-Sons-The-Second-Season-Volume-One-DVD/13269585'
    ]
    for i in range(200):
        headers['referer'] = 'https://www.walmart.com/'
        headers['cookie'] = 'AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1658310398193; ACID={}; hasACID=true; assortmentStoreId=3180; hasLocData=1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; vtc=T9qM4nG79nycr9zsvW7faM; bstc=T9qM4nG79nycr9zsvW7faM; mobileweb=0; xpa=282I9|3JfYH|77hfu|78jM7|Ao5F6|IOIpg|Iui6D|L-48F|LTD5Y|O1c3v|PiOGS|PzQ_l|RAxqf|SmVSa|T-onc|TOmPu|Umo04|ZKQTc|_KTWc|aPJIO|avWsU|cfVAR|duBe9|eEurn|elin2|gXIJ5|kFqfr|lqVt_|pAMXF|qyn67|r8csb|rbr_5|uru_L|xpp-8|yQ2ZK|ymjfc|zCylr; exp-ck=282I913JfYH177hfu178jM71Iui6D1L-48F1O1c3v2PzQ_l1SmVSa1_KTWc4avWsU1eEurn1gXIJ51kFqfr1pAMXF2qyn672r8csb1rbr_53; _pxhd=9a7ab261b180166c742954f3fcb55eab52d3c9a1777a0eef0b7fc4fd74ed702a:d998a108-0810-11ed-a986-556b56716672; TS013ed49a=01538efd7cba7db79d4a6342a79db18c65a7cba8dd449ec0a1788758a992e5ef3606ce484bf7e0c0b64c26e4c128fb07170f798b10; adblocked=false; TBV=7; _pxvid=d998a108-0810-11ed-a986-556b56716672; pxcts=da693a7d-0810-11ed-a712-56464a4c5461; xpm=1+1658310398+T9qM4nG79nycr9zsvW7faM~+0; ak_bmsc=5DEB58E62ED1B6178EB115774FDF1CED~000000000000000000000000000000~YAAQB+pCF9V0+8WBAQAAuZgAGxAItrCtmuup+zbYqK72dvC00jP0MkzSeRVKicKveegxfzUmtCgAC6slK0ksT6+ovXoFIyJyBVr8Rd/dg1qGwMzUpRPhdFjCu5l/X+axgmuDFJRqEaRFdCV4dEBdR4LuwkysusQXLx0krDxGUCXowC6hy3KfQ16EUcVwzlWYDvfQdQ3Zu6i8ugHI+aYDdmwuEbv+famvClweiBtu3bdtPYQiYRCCIXNMS7a9gohKAW5w8fxc2ZG1Cwm7wh8RQo2kf/V5fm4O0eYFkJmmINbnKXQrUAPqcUS7fsN3NI1srSU2nyuj2EA0ArKFtpEf147/le0smOg+mNoffo4dfgFLRc6DI0WR+nqVkmiBbKcg+rnJCBkV2yjdeHEq7jpOGu24LvbKEYKNyowwbi7KZ0diSI/qnwXZRSZPx3QI8mn1vlkVr38oI/8KNMttxZwllduzEwLGvWfLACTelGqix+k4TVyxwnDW9OOmJDdP; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjMxODAiLCJ0aW1lc3RhbXAiOjE2NTgzMTA0MDAwMDN9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY1ODMxMDQwMDAwMywiYmFzZSI6IjkwMDE3In0sInZhbGlkYXRlS2V5IjoicHJvZDp2MjozMWNmM2M5Ni1lYmE4LTRiYjctOGY3Yi1iMDIwYzVkYTUzMzcifQ==; _astc=07800327e2c0b47cc00dce57906084a3; tb_sw_supported=true; auth=MTAyOTYyMDE4T9dofInNd59npz6JphkM6WnqP+GWir9VAXjJBm9KzeDRI36rH9L6RlmmisiSebg41vo01wgjwLS9H4j5bNb0tSHDPbCdhofy1pD4rkmTKRwuXJjZ8T5S978cVTFriLcO767wuZloTfhm7Wk2Kcjygi5k0VvBM/JjwcKWWhCnBS8pcAI6Cj817C1lnnXpqzs6YnWfJnJYq1U6UyrT7WM2iK62R4I83zDF8cM4PhieW4EUMk70P8glgOEpLOprhDfMM/FHGZ2dCNmxWrdkwqEKrt3W38jtNbgpCPCBiQT8ydECVzprPm7p/ca/3Ar/I0CM+wXtRegmKXOtizRagZIHUvB6RgM0mia6ji83mhs4ohsky4IRJU+bLI28rEDaO9njJkc4SiuHvR7beJLz2pe7I0jyrOXbKKhH072NS/W0j/U=; TS01b0be75=01538efd7c602b71db8ed975873e0244d86bc0e96f78de27fdb041d776afe300d617ff300ed32342b5cc5c2c2e4783e10e47404f51; akavpau_p2=1658313353~id=8f026d9cdc2e22383c0fec45ecd42290; TS012768cf=01d05332bdcd20747b5938f29f1e984816f8bc509745f610b1f03c2e2b974a6865dede4570356bf1e9de45d40375eb0fb313f2f4e2; TS2a5e0c5c027=0870aea760ab20001f16a26240a6e1353cec12c539365141666fa088b0c5f3ae4c94a0eb7ebacd3208eae6f0eb113000ae7aae78f0084824da9d5a355296629a5253252954c1ee5761903fe06d105242d093b649cba5f416e9fe24624d114413; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIzMTgwIiwiZGlzcGxheU5hbWUiOiJTb3V0aCBHYXRlIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6IjkwMjgwIiwiYWRkcmVzc0xpbmUxIjoiNDY1MSBGaXJlc3RvbmUgQmx2ZCIsImNpdHkiOiJTb3V0aCBHYXRlIiwic3RhdGUiOiJDQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTAyODAtMDAwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MzMuOTU0ODM4LCJsb25naXR1ZGUiOi0xMTguMTg3NTUzfSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInN0b3JlRmVlVGllciI6IkIiLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImh1Yk5vZGVJZCI6IjMxODAiLCJzdG9yZUhycyI6IjA2OjAwLTIzOjAwIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX0lOU1RPUkUiLCJQSUNLVVBfQ1VSQlNJREUiXX1dLCJzaGlwcGluZ0FkZHJlc3MiOnsibGF0aXR1ZGUiOjM0LjA1MjgsImxvbmdpdHVkZSI6LTExOC4yNjQyLCJwb3N0YWxDb2RlIjoiOTAwMTciLCJjaXR5IjoiTG9zIEFuZ2VsZXMiLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVU0EiLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMxODAiLCJkaXNwbGF5TmFtZSI6IlNvdXRoIEdhdGUgU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NTgzMzQzNTYxNDcsInZhbGlkYXRlS2V5IjoicHJvZDp2MjozMWNmM2M5Ni1lYmE4LTRiYjctOGY3Yi1iMDIwYzVkYTUzMzcifQ==; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1658312756000@firstcreate:1658310398193"; xptwg=3748594363:240A26B5D0F1DC0:5D5761F:A3374AD:6D31E470:F6D1E57E:; bm_sv=3E7D5301E51E25FBF3176149864543DB~YAAQGupCF+S/rwOCAQAAFowkGxCJSBWl3YN/dPfScZ1RrNPfTQd/yXtXI3W8p8pcTNX10vYtHg67R6VGmYgHyrjHLhaMhkoPPO9Gz4m/K0r6GO1m1ZK2Jo06pp4MiUTEPyWk1J5H+Hzwlz+IZdjVutMcv6S4+K2SmUFdnSdgyaD1RjMgo07vt/hEMQ6xmmNrKSFFGB2zDYEnNVv69qMkeJ/n/+JOJYdj4GUBxjVC+qEykwF5RCvm4/0e6yQ8/JiheQ==~1'.format(
            uuid.uuid1())
        response = spider(random.choice(urls))
        if response.find('Robot or human') > 0:
            print('start: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", start_time)))
            print('end: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            sys.exit()
        else:
            print('{}\r\n==> range: {}'.format(response, i + 1))
        sleep_time = random.randint(5, 15)
        print('==> sleep time: {} s'.format(sleep_time))
        sleep(sleep_time)
