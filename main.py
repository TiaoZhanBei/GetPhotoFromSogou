from getPhoto import get_photo

batch = 10

words = ['梅 雪', '梅 庭院', '菊 霜', '菊 雪', '黄菊', '竹林', '竹篱', '月圆', '月缺', '雪 山', '雪 林',
    '草 河', '草 湖','草丛','落花 飘','落叶 飘','落花','落叶','柳 岸','风吹柳','夕阳 江',
    '夕阳 楼','夕阳 山','流水','兰花']

for word in words:
    get_photo(word, batch * 47)