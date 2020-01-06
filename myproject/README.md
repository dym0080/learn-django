
本项目是 [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/) 的项目实践。其原项目的中文翻译版本是 [django-beginners-guide](https://github.com/pythonzhichan/django-beginners-guide)

作者在写的时候 

- python：3.6
- Django：1.11

本项目使用的版本如下，所以代码会有所区别(见依赖文件：`requirements.txt`):
- python：3.7.4
- Django：2.2

我所了解的Django 2.x 与 1.x 最大区别

- 路由的变化
- `models.ForeignKey` 的参数 `on_delete` 为**必选参数**

使用Django时在windows环境几个常用的命令：

- `django-admin startproject projectname`: 一般在项目开始时用于创建一个项目。
- `django-admin startapp appname`:在项目中创建应用程序，一个项目可以有一个或多个应用程序。
- `py manage.py runserver`:运行程序。
- `py manage.py test` : 自动化测试项目中的所有测试用例
- `py manage.py test appname`: 自动化测试项目中的appname的所有测试用例
- `py manage.py test appname.tests.classname.functionname`: 自动化测试项目中的appname的类下面的某个具体的测试用例。
- `py manage.py migrate`: 获取迁徙文件，把改动应用到数据库去。
- `py manage.py makemigrations`: 如果models有改动，使用此命令就会生成迁徙文件，但不会更新数据库
- `py manage.py shell`:这与直接输入python指令来调用交互式控制台是非常相似的，除此之外，项目将被添加到sys.path并加载Django。这意味着我们可以在项目中导入我们的模型和其他资源并使用它。
- `manage.py createsuperuser`:创建一个超级管理员用户

