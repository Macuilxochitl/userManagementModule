User management module
---

简介
---
这是为Django打造的一个非常轻量化的用户管理模块。目前我的两个网站就在使用这个模块进行用户管理。

这个模块只提供了最基础的功能，如创建用户，认证用户，设置管理员，管理员认证等。由于功能非常基础，所以也非常容易上手以及更改。

本模块为一个独立的Django app，多个项目如果要使用同样的用户数据可以直接将本app复制到不同的项目使用即可。（Django项目要连接到同一个数据库。）

因为本模块采用了Apache2协议，所以你可以对本模块进行改进以达到你需要的功能，比如让管理员可以在其用户名前显示一个很cooooool的前缀：）

安装方法
---
1.将authority复制入你Django项目的目录（与其他的app同样的位置）

2.在你的Django项目中添加这个app: "authority"（如果你不知道怎么添加，请看本文档尾部。）

3.同步数据库，调用Django的方法

python manage.py makemigrations

python manage.py migrate

4.在你自己的views中import并调用module.py内的方法即可.

比如你需要新增一个用户，只需要调用umm.py里的addUser方法即可，比如:
>addUser(test,123456)

就新增了一个名为test，密码为123456的用户到数据库里了.(这里建议新建用户的时候的密码加密一下，我自己使用的时候把密码经过了sha512加密,如果需要加密可以直接使用模块里的sha512()方法对密码进行加密)

注意事项
---
本模块中对于用户的认证是基于cookie的，所以判断用户以及判断是否管理员的方法需要的参数为request. 

在用户认证成功后(验证账号密码正确)后，要使用setCookie方法来设置cookie，否则无法识别用户.



如何添加Django App
---

将app复制到Django项目的目录下以后，在你的项目的settings.py内找到

> INSTALLED_APPS = [
>
> …,
>
> ]

后，把app的名字添加到最后就好了，像这样

> INSTALLED_APPS = [
>
> …,
>
> 'authority',
>
> ]

就可以了。