import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from Two.models import Game


def index(request):
    return HttpResponse('<h1>比尔吉沃特</h1>')

#主页
def home(request):
    # 加载模板
    temp = loader.get_template("Home.html")
    print(temp)
    print(type(temp))

    # 渲染模板
    # result = temp.render(context={"username":'匿名'})
    result = temp.render(context={"username": '匿名'})
    print(result)

    return HttpResponse('LPL赛区' + result)

#批量添加游戏
def add_games(request):
    for i in range(6):
        game = Game()
        game.g_name = '腾讯游戏%d' % random.randrange(200)
        game.g_type = random.randrange(5)
        game.save()
    return HttpResponse('游戏创建成功')

#获取游戏
def get_games(request):
    games = Game.objects.all()

    #把hobby传给data
    hobby = {
        "name": "eat",
        "cost": 80,
    }

    #js注入
    code = """
        <script type="text/javascript">
            var lis = document.getElementsByTagName("li");
            for (var i =0; i < lis.length;i++){
                lis[i].innerHTML = "日本是中国的！"+i;
        }
</script>
    """

    data = {
        "games": games,
        "hobby": hobby,
        #是否登录开关
        "is_login": True,
        "score": 50,
        #分数列表
        "scores": [100, 140, 80, 99, 85],

        "code":code,
    }

    return render(request, 'GameList.html', context=data)


def taocan(request):
    return HttpResponse("恭喜您办理成功")
