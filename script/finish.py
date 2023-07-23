import HyEmail as Email

print("hell world")

title = "MAA任务已完成"
content = "content"
try:
    f = open('debug\gui.log', 'r', encoding='utf-8')
    content = f.read()
    f.close()
except Exception as e:
    print('except:', e)

try:
    sub = "正在连接模拟器"
    content = content[content.rfind(sub):]
except Exception as e:
    print('except:', e)

print(content)

try:
    rtn = Email.send_mail(title, content)
    print("sendemail:", rtn)
    pass
except Exception as e:
    print('except:', e)


# input("按下任意按键")
