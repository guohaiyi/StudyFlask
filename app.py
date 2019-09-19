from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name = '张三'
        xue = '宇宙大学'
        di = '宇宙'

    p = Person()
    context = {
        'username': '张三',
        'sex': '男',
        'age': 18,
        'person': p,
        'web': {
            '百度': 'www.baidu.com',
            '小米': 'www.xiaomi.com'
        }
    }
    return render_template('index.html', **context)  # 渲染模版


@app.route('/book')
def book():
    """for循环"""
    for_data = [
        {'name': '西游记',
         'u_name': '吴承恩',
         'pers': 108},
        {'name': '三国志',
         'u_name': '吴贯中',
         'pers': 189},
        {'name': '红楼梦',
         'u_name': '曹雪芹',
         'pers': 118},
        {'name': '水浒传',
         'u_name': '施耐庵',
         'pers': 169}
    ]
    return render_template('book.html', for_data=for_data)


@app.route('/img')
def img():
    """过滤器"""
    img_url = 'http://e.hiphotos.baidu.com/image/pic/item/359b033b5bb5c9eac1754f45df39b6003bf3b396.jpg'
    comments = [{'name': '张三', 'comment': '这个呀！很不错的喔！'}, {'name': '李四', 'comment': '哎哟！不错哦'}]
    return render_template('img.html', avatar=img_url, comments=comments)


@app.route('/comment')
def comment():
    """过滤器"""
    img_url = 'http://e.hiphotos.baidu.com/image/pic/item/359b033b5bb5c9eac1754f45df39b6003bf3b396.jpg'
    return render_template('comment.html', avatar=img_url)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
