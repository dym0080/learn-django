
本项目是 [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/) 的项目实践。其原项目的中文翻译版本是 [django-beginners-guide](https://github.com/pythonzhichan/django-beginners-guide)

作者在写的时候 

- python：3.6
- Django：1.11

本项目使用的版本如下，所以代码会有所区别
- python：3.7.4
- Django：2.2

我所了解的Django 2.x 与 1.x 最大区别

- 路由的变化
- `models.ForeignKey` 的参数 `on_delete` 为**必选参数**
- ModelForm 

windows环境几个常用的命令：

- `django-admin startproject projectname`: 一般在项目开始时用于创建一个项目。
- `django-admin startapp appname`:在项目中创建应用程序，一个项目可以有一个或多个应用程序。
- `py manage.py runserver`:运行程序。
- `py manage.py test` : 自动化测试项目中的所有测试用例
- `py manage.py test appname`: 自动化测试项目中的appname的测试用例

