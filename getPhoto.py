import requests
import os

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept':'text/plain, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'Host':'pic.sogou.com'
}

url = 'http://pic.sogou.com/pics'


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
        js = z1.json()
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