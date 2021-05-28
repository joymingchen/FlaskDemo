f = open('data.txt', "r")  # 打开文件，n的值保存在里面

a = ['one', 'two', 'three']
content = f.read(10)  # 从文件中取出n的值

n = 0
if content != "":  # 第一次打开非空判断
    n = int(content)  # 类型转换

for index in range(len(a)):
    if index == n:
        print('执行: ', a[index])
        n = n + 1
        break

f = open('data.txt', "w")  # 允许写入
if n >= 3:  # 超出范围重新赋值
    n = 0
f.write(str(n))  # write 写入
# writelines()函数 会将列表中的字符串写入文件中，但不会自动换行，如果需要换行，手动添加换行符
# 参数 必须是一个只存放字符串的列表
f.close()  # 关闭文件
