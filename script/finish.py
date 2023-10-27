import HyEmail as Email
import time
import re

t = 0
try:
    t = time.time()
except Exception as e:
    print('except:', e)

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

try:
    sub = "<1><>"
    content = content.replace(sub, "")
except Exception as e:
    print('except:', e)

try:
    sub = r'\[.+\].+Failed to send[\s\S]+?(?=\[)'
    content = re.sub(sub, "", content)
except Exception as e:
    print('except:', e)

try:
    if "任务已全部完成" in content:
        pass
    else:
        title = "[ERROR]MAA 任务出错"
except Exception as e:
    print('except:', e)

try:
    current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(t))
    print(current_time)
    current_time2 = time.strftime('%Y-%m-%d %H:%M', time.localtime(t-60))
    print(current_time2)

    if current_time in content or current_time2 in content:
        pass
    else:
        title = "[ERROR]MAA 记录出错"
except Exception as e:
    print('except:', e)

print(title)
print(content)

try:
    print("sendemail:", Email.send_mail(title, content))
    pass
except Exception as e:
    print('except:', e)


# input("按下任意按键")
