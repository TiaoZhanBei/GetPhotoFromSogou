import requests
import os
import re
import requests.utils
import json

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept':'text/plain, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'Host':'pic.sogou.com'
}

url = 'http://pic.sogou.com/pics'



def decode_json(content, text):
    encoding = requests.utils.guess_json_utf(content)
    if encoding is not None:
        try:
            respCmtJson = re.sub(r"(,?)(\w+?)\s+?:", r"\1'\2' :", content.decode(encoding))
            respCmtJson = respCmtJson.replace("'", "\"")
            respCmtJson = respCmtJson.replace("\\", r"\\")
            return json.loads(respCmtJson)
        except UnicodeDecodeError:
            pass
   # respCmtJson = re.sub(r"(,?)(\w+?)\s+?:", r"\1'\2' :", text)
    respCmtJson = text.replace(r'\"',"")
    respCmtJson = re.sub("\"markedTitle\":\".*?\",", "\"markedTitle\":\"\",", respCmtJson)
    respCmtJson = re.sub("\"title\":\".*?\",", "\"title\":\"\",", respCmtJson)
    respCmtJson = re.sub("\"oriTitle\":\".*?\",", "\"oriTitle\":\"\",", respCmtJson)
    respCmtJson = re.sub("\"surr1\":\".*?\",", "\"surr1\":\"\",", respCmtJson)
    respCmtJson = re.sub("\"surr2\":\".*?\",", "\"surr2\":\"\",", respCmtJson)
    print(respCmtJson)
    return json.loads(respCmtJson)


def get_photo(word, num):
    try:
        os.mkdir("pictures")
    except FileExistsError:
        pass
    for i in range(int(num/47)):
        params = {
        'query':word.encode('gbk'),
        'mode':'1',
        'start':str(i*47),
        'reqType':'ajax',
        'reqFrom':'result',
        'tn':0
    }
        z1 = requests.get(url=url, params=params, headers=header)
        print(z1.status_code)
        print(z1.content)
        js = decode_json(z1.content,z1.text)
        #print(js)
        j = 0
        for urls in js['items']:
            each = urls['pic_url']
            get_photo_from_url(each,i*47+j , word)
            j += 1


def get_photo_from_url(Url, id, word):
    print('正在下载第'+str(id)+'张图片')
    print(Url)
    try:
        pic = requests.get(Url, timeout=15)
    except Exception as e:
        print('【错误】当前图片无法下载')
        return
    string = 'pictures/' + word + '_' + str(id) + '.jpg'
    fp = open(string.encode('cp936'), 'wb')
    fp.write(pic.content)
    fp.close()