# <img src="https://flog.pythonanywhere.com/static/favicon/favicon.svg" width="50px"> Flog
[中文版](./README_zh.md)  [![Coverage Status](https://coveralls.io/repos/github/z-t-y/Flog/badge.svg?branch=master)](https://coveralls.io/github/z-t-y/Flog?branch=master)  
Icons made by
[Freepik]("https://www.flaticon.com/authors/freepik") from
[www.flaticon.com](www.flaticon.com)

The blog website created during learning flask.  

## Contributors

[Andy Zhou on Github](https://github.com/z-t-y "ZTY")

## Thanks To

### Projects

- [Flask](https://github.com/pallets/flask)
- [Bootstrap](https://github.com/twbs/bootstrap)
- [Bootstrap-Flask](https://github.com/greyli/bootstrap-flask)
- [Flask-WTF](https://github.com/lepture/flask-wtf)

### Books

- [Python Web Development with Flask by GreyLi](https://helloflask.com)  
- [Flask Web Development by Miguel Grinberg](https://www.oreilly.com/library/view/flask-web-development/9781491991725/)

### People

- [GreyLi](https://greyli.com)

Without these projects, the website cannot be developed.  
At the same time, thanks to [GreyLi](https://greyli.com), it was his _Python Web Development with Flask_
that took me into the wonderful world of Flask.

## Functions

- Login / Register (requires email verification) / Logout / Delete Account
- Collect  
- Follow  
- Write  
- Comment  
- Notifications
- Two languages support (zh_CN and en_US)  

## Prospect

- Chatting Room
- Web API
  - Flog CLI  
  - Linux and Windows application for Flog.  

## Q & A

1. Q: Why 'Flog'?  
A: 'Flog' is a combination of 'Flask' and 'Blog'. The word sounds (and looks) like 'frog'. So I use a frog as its icon.  

2. Q: Why can't the website be updated frequently?  
The website cannot be updated on time because I'm a student in Middle School now. There is much homework.

## Run Flog locally

### Run the website

If you prefer to use pip + requirements.txt, then:

```shell
git clone https://github.com/z-t-y/Flog.git ./flog
cd flog/
python3 -m venv venv # or `python -m venv venv` on windows
source ./venv/bin/activate # or `./venv/Scripts/activate` on windows
pip3 install -r requirements.txt
flask run
```

Or, if you prefer to use pipenv, then:  
(Note that I use [mirrors.aliyun.com](https://mirrors.aliyun.com) in Pipfile to improve the download speed in China, if you don't live in China, use pip+requirements.txt instead)

```shell
# clone the project and change to that directory
pipenv install
pipenv shell
flask run
```

### Run the unittests

pip+requirements.txt

```shell
source ./venv/bin/activate # or `./venv/Scripts/activate` on windows
pip3 install -r requirements-dev.txt
flask test
```

pipenv

```shell
pipenv install --dev
pipenv shell
pytest
```
