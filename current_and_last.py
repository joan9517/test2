# 创建人  :joan
# 创建日期 :2024/8/2 15:52
# 文件名称 :
# 软件    :PyCharm

#将本期存在相同的趋势写入
import csv
file1=open(r"F:\learn\01.csv",'r+',newline="",encoding="utf-8")
file2=open(r"F:\learn\12.csv",'r+',newline="",encoding="utf-8")
file3=open(r"F:\learn\4.csv",'r+',newline="",encoding="utf-8")
write=csv.writer(file3)
datas1=csv.reader(file1)
datas2=csv.reader(file2)
current_data=[d.copy() for d in datas1]
for data2 in datas2:
    # file1.seek(0)
    # datas1 = csv.reader(file1)
    for data1 in current_data:
        if data2[0]==data1[0]:
            data1.append(data2[0])
            data1.append(data2[1])

write.writerows(current_data)


