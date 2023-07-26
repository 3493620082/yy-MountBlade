# --coding=utf-8
import requests  # 爬虫所需库
import os  # 创建目录所需库

save_path = ".\\result_img\\"  # 目录文件夹
if not os.path.exists(save_path):  # 如果该目录不存在则创建一个
    os.mkdir(save_path)  # 创建目录
url = "https://www.thispersondoesnotexist.com/image"  # url
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}  # 头部信息
img_num = 9  # 想要爬取的数量
# ----------------------------------可自定义文件名--------------------------------- #
name_head = '0'  # w文件头
name_content = 11  # 文件名
name_end = '.jpg'  # 文件尾
# ----------------------------------可自定义文件名--------------------------------- #
for i in range(1, img_num + 1):  # 循环爬取想要的图片张数，修改range函数的值即可
    response = requests.get(url=url, headers=headers)  # 使用get请求获取网页信息
    if response.status_code == 200:  # 判断状态码是否正常
        img_name = save_path + name_head + str(name_content + i) + ".jpg"  # 拼接文件名用于保存图片
        with open(img_name, 'wb') as f:  # 打开一个文件，模式是wb，二进制写入
            f.write(response.content)  # 写入图片的二进制数据
            print("图片%s已保存" % img_name)  # 输出保存成功提示