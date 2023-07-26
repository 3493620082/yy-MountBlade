# --coding=utf-8
import os
import pygame
import csv
# 一些游戏文件
from setting import config  # 配置文件
from module.button_position import button_position # 游戏按钮坐标记录文件

class GameElementList:
    """
    一些游戏内容的显示放置在此处用于引用
    """
    def mainPageMusic(self):
        # 主界面的背景音乐
        self.main_page_music_file_list = os.listdir(".\\media\\music\\")  # 获取media/music下的所有音乐文件名
        self.main_page_music_file_num = len(self.main_page_music_file_list) - 1  # 获取到数组的长度
        self.main_page_music_now_id = 4
        self.main_page_music_file = ".\\media\\music\\" + self.main_page_music_file_list[self.main_page_music_now_id]
        pygame.mixer.music.load(self.main_page_music_file)  # 默认播放音乐文件
        pygame.mixer.music.set_volume(0.1)  #设置声音为大小为0.1
        pygame.mixer.music.play(-1)  # 将值赋为-1表示循环播放，这样就不需要手动控制循环了

    def mainPageMusicCtrlBtn(self):
        # 创建一个小透明背景板
        self.is_main_music_ctrl_btn_bg = False
        self.main_music_ctrl_btn_bg = pygame.Surface((56, 95)).convert_alpha()
        self.main_music_ctrl_btn_bg.fill((0, 0, 0))
        self.main_music_ctrl_btn_bg.set_alpha(75)
        self.main_music_ctrl_btn_bg_rect = self.main_music_ctrl_btn_bg.get_rect()
        # 创建暂停、继续、上曲、下曲按钮
        # 1.新建一个小号的字体
        self.MAIN_MUSIC_FONT = pygame.font.Font(config["BASE_FONT_PATH"], 18)
        # self.MAIN_MUSIC_FONT = pygame.font.SysFont("华文楷体", 18)  # 15号大小
        # 2.创建文字按钮
        self.main_music_stop_btn = self.MAIN_MUSIC_FONT.render("停止", True, self.FONT_DEFAULT_COLOR, None)
        self.main_music_stop_btn_rect = self.main_music_stop_btn.get_rect()
        self.main_music_keep_btn = self.MAIN_MUSIC_FONT.render("继续", True, self.FONT_DEFAULT_COLOR, None)
        self.main_music_keep_btn_rect = self.main_music_keep_btn.get_rect()
        self.main_music_next_btn = self.MAIN_MUSIC_FONT.render("下曲", True, self.FONT_DEFAULT_COLOR, None)
        self.main_music_next_btn_rect = self.main_music_next_btn.get_rect()
        self.main_music_last_btn = self.MAIN_MUSIC_FONT.render("上曲", True, self.FONT_DEFAULT_COLOR, None)
        self.main_music_last_btn_rect = self.main_music_last_btn.get_rect()
        # 2.1文字选中按钮
        self.main_music_stop_active = self.MAIN_MUSIC_FONT.render("停止", True, self.FONT_ACTIVE_COLOR, None)
        self.main_music_keep_active = self.MAIN_MUSIC_FONT.render("继续", True, self.FONT_ACTIVE_COLOR, None)
        self.main_music_next_active = self.MAIN_MUSIC_FONT.render("下曲", True, self.FONT_ACTIVE_COLOR, None)
        self.main_music_last_active = self.MAIN_MUSIC_FONT.render("上曲", True, self.FONT_ACTIVE_COLOR, None)

    def mainPageTextBtn(self):
        # 1.文字按钮
        self.btn_pos = button_position  # 将按钮坐标字典赋给btn_pos
        self.start_new_game_font = self.BASE_FONT.render("开始新历程", True, self.FONT_DEFAULT_COLOR, None)  # 开始新游戏按钮
        self.start_new_game_font_rect = self.start_new_game_font.get_rect()  # 获取rect
        self.start_old_game_font = self.BASE_FONT.render("载入历程", True, self.FONT_DEFAULT_COLOR, None)  # 读取存档按钮
        self.start_old_game_font_rect = self.start_old_game_font.get_rect()
        self.setting_game_font = self.BASE_FONT.render("游戏选项", True, self.FONT_DEFAULT_COLOR, None)  # 游戏选项按钮
        self.setting_game_font_rect = self.setting_game_font.get_rect()
        self.authors_list_font = self.BASE_FONT.render("贡献者名单", True, self.FONT_DEFAULT_COLOR, None)  # 贡献者名单按钮
        self.authors_list_font_rect = self.authors_list_font.get_rect()
        self.quit_game_font = self.BASE_FONT.render("退出游戏", True, self.FONT_DEFAULT_COLOR, None)  # 退出游戏按钮
        self.quit_game_font_rect = self.quit_game_font.get_rect()
        # 2.文字活动按钮:也就是被鼠标选中时的按钮
        self.active_btn_choose = 0  # 代表选中的按钮的变量
        self.start_new_game_active = self.BASE_FONT.render("开始新历程", True, self.FONT_ACTIVE_COLOR, None)
        self.start_old_game_active = self.BASE_FONT.render("载入历程", True, self.FONT_ACTIVE_COLOR, None)
        self.setting_game_active = self.BASE_FONT.render("游戏选项", True, self.FONT_ACTIVE_COLOR, None)
        self.authors_list_active = self.BASE_FONT.render("贡献者名单", True, self.FONT_ACTIVE_COLOR, None)
        self.quit_game_active = self.BASE_FONT.render("退出游戏", True, self.FONT_ACTIVE_COLOR, None)
        # 一些变量
        self.IS_MAIN_PAGE = True  # 表示开始界面是否加载
        self.IS_GAME_PAGE = False  # 表示游戏界面是否加载

    def mainPageBackground(self):
        # 1.背景图片
        self.main_page_background_file = ".\\media\\image\\background_4.jpg"  # 背景图片路径
        self.main_page_background = pygame.image.load(self.main_page_background_file).convert()  # 加载背景图片
        self.main_page_background = pygame.transform.scale(self.main_page_background, self.SIZE)  # 将原图片改变大小为窗口大小
        self.main_page_background_rect = self.main_page_background.get_rect()

    def authorsListPageBackground(self):
        # 背景图片
        self.authors_page_background_file = ".\\media\\image\\background_5.jpg"
        self.authors_page_background = pygame.image.load(self.authors_page_background_file).convert()
        self.authors_page_background = pygame.transform.scale(self.authors_page_background, self.SIZE)
        self.authors_page_background_rect = self.authors_page_background.get_rect()

    def authorsListPageText(self):
        # 文字内容(内容读取，对象加载，坐标处理)
        self.authors_file = csv.reader(open(".\\media\\authors.csv", 'r', encoding="UTF-8"))  # 打开并读取CSV文件内容
        self.authors_str_list = []  # 建立空列表存放贡献者名字
        for l in self.authors_file:
            self.authors_str_list.append(l[0])  # 将数据读出并添加到列表中
        self.authors_num = len(self.authors_str_list)  # 获取数量
        self.authors_text_list = []  # 存放文字surface对象
        self.authors_text_rect_list = []  # 存放surface对应的rect
        for name_str in self.authors_str_list:
            self.authors_text_list.append(self.BASE_FONT.render(name_str, True, self.FONT_DEFAULT_COLOR, None))  # 创建每个名字对应的文字绘制对象
        for text in self.authors_text_list:
            self.authors_text_rect_list.append(text.get_rect())  # 获取每个文字绘制对象的rect
        self.average_x = 400  # x轴起始坐标
        self.average_y = int(600 / self.authors_num)  # 求高度平均值，用于表示y轴坐标
        self.average_xy_list = []  # 存放每个文字所在的坐标
        for i in range(self.authors_num):
            # [x=左边界到达x轴的距离360 - 字体长度除以2，这样就得到了能让元素居中的x坐标, y=平均值加40像素，这样显示紧凑美观，不会像之前那样间距太大]
            self.average_xy_list.append([self.average_x - self.authors_text_rect_list[i][2] / 2, self.average_y + 40 * i])

    def authorsListPageAuthorInfo(self):
        # 贡献者详细信息显示板
        self.is_author_info = False  # 显示信息板的布尔型变量
        self.author_info_choose = -1  # 选择显示的信息编号
        self.AUTHOR_INFO_FONT = pygame.font.Font(config["BASE_FONT_PATH"], 15)
        # self.AUTHOR_INFO_FONT = pygame.font.SysFont("华文楷体", 15)  # 使用于信息板的私有字体
        # 从文件中读取信息
        self.authorsInfo_file = csv.reader(open(".\\media\\authorsInfo.csv", 'r', encoding="UTF-8"))  # 打开并读取作者信息文件
        self.authorsInfo_str_list = []  # 存放信息字符串
        for l in self.authorsInfo_file:
            self.authorsInfo_str_list.append(l)  # 将元素添加到列表中
        self.authorsInfo_num = len(self.authorsInfo_str_list)  # 获取数量
        # 创建信息对应的surface对象和rect
        self.authorsInfo_text_list = []  # 存放文字surface对象
        self.authorsInfo_text_rect_list = []  # 存放surface对应的rect
        for i in range(self.authorsInfo_num):  # 外层循环取出二维数组
            self.authorsInfo_text_list.append([])
            for info in self.authorsInfo_str_list[i]:  # 取出二维数组的信息并给另一个二维数组添加创建一个文字对象
                self.authorsInfo_text_list[i].append(self.AUTHOR_INFO_FONT.render(info, True, self.FONT_DEFAULT_COLOR, None))
        for i in range(self.authorsInfo_num):  # 外层循环创建好的文字的二维数组
            self.authorsInfo_text_rect_list.append([])
            for text in self.authorsInfo_text_list[i]:  # 取出二维数组的文字对象并创建获取rect并添加到数组中
                self.authorsInfo_text_rect_list[i].append(text.get_rect())  # 获取每个文字绘制对象的rect
        self.author_info_bg_x = config["author_info_bg_x"]  # 信息板的x轴(宽度)
        self.author_info_bg_y = config["author_info_bg_y"]  # 信息板的y轴(高度)
        self.author_info_xy_list = []  # 存放每个文字的坐标
        for i in range(self.authorsInfo_num):
            self.author_info_xy_list.append([])  # 添加一个空列表
            info_num = len(self.authorsInfo_text_list[i])  # 获取到当前作者信息条目的数量
            average_y = int(self.author_info_bg_y / info_num)  # 求出该平均分配的高度
            for j in range(info_num):
                # [x=x轴的长度/2 - 字体长度/2，这样就得到了能让元素居中的x坐标, y=平均值加20像素，这样显示紧凑美观，不会像之前那样间距太大]
                self.author_info_xy_list[i].append((self.author_info_bg_x / 2 - self.authorsInfo_text_rect_list[i][j][2] / 2, average_y + 20 * j - 20))
        # 渲染
        self.author_info_background_list = []  # 存放每个信息板surface, 一个作者一个信息板
        for i in range(self.authorsInfo_num):  # 循环指定作者数
            self.author_info_background = pygame.image.load(".\\module\\image\\box_2.jpg").convert()
            self.author_info_background = pygame.transform.rotate(self.author_info_background, 90)  # 旋转90度，横过来显示
            self.author_info_background = pygame.transform.scale(self.author_info_background, (self.author_info_bg_x, self.author_info_bg_y))  # 将大小缩小为100x200
            # author_info_background_rect = author_info_background.get_rect()  # 此处不需要rect
            self.author_info_background_list.append(self.author_info_background)  # 往列表中添加这个单独的面板
            for j in range(len(self.authorsInfo_text_list[i])):
                # 循环给当前信息板渲染上所有他的信息
                self.author_info_background_list[i].blit(self.authorsInfo_text_list[i][j], self.author_info_xy_list[i][j])

    def authorsListPageBackMainPageBtn(self):
        # 返回按钮
        self.back_main_page_font = self.BASE_FONT.render("返回主界面", True, self.FONT_DEFAULT_COLOR, None)
        self.back_main_page_font_rect = self.back_main_page_font.get_rect()
        self.back_main_page_active = self.BASE_FONT.render("返回主界面", True, self.FONT_ACTIVE_COLOR, None)
        # 变量
        self.IS_AUTHORSLIST_PAGE = False