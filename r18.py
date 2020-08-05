import m3u8
import requests
from Crypto.Cipher import AES

# r18 m3u8 url
m3u8_url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Origin': 'http://www.r18.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*'
}


def decrypt(data, key):
    decryptor = AES.new(key, AES.MODE_CBC, IV=None)
    return decryptor.decrypt(data)


playlist = requests.get(m3u8_url, headers=headers).text
m3u8_obj = m3u8.loads(playlist)
# m3u8_obj = m3u8.load(m3u8_url)

# set ur cookie here
headers['Cookie'] = ''

key = requests.get(m3u8_obj.keys[-1].uri, headers=headers).text

# set the m3u8 base url
base_url = ''

urls = []
for iframe in m3u8_obj.segments:
    if ".ts" in iframe.uri:
        urls.append(base_url + iframe.uri)

for url in urls:
    bin = requests.get(url, headers=headers).content
    print(bin)
    break
