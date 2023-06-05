# 把用户输入的换行符\n或者\r\n替换成</br>，把空格转换为&nbsp;
# 去除用户输入的html标签
def ConvertToWebString(val):
    val = val.replace(" ", "&nbsp;")
    val = val.replace("<", "&lt;")
    val = val.replace(">", "&gt;")
    val = val.replace("\n", "</br>")
    val = val.replace("\r\n", "</br>")
    return val
