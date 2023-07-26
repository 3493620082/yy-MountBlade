# --coding=utf-8
import csv
import datetime
import os
import pygame
# 游戏文件
from module.button_position import button_position, LoadBox_position
from setting import config

class level_load:
    def levelLoadElement(self):
        """
        读取界面元素
        :return:无
        """
        # 一些变量
        self.levelLoadSomeVariable()
        # 背景图片
        self.levelLoadBgElement()
        # 背景板
        self.levelLoadBgBoxElement()
        # 返回按钮
        self.levelLoadBackBtnElement()
        # 存档格子
        self.levelLoadSaveBoxElement()

    def levelLoadRender(self):
        """
        读取界面元素
        :return:无
        """
        # 创建背景
        self.levelLoadBgElement()
        # 渲染背景板
        self.levelLoadBgBoxRender()
        # 渲染返回按钮
        self.levelLoadBackBtnRender()
        # 渲染存档格子
        self.levelLoadSaveBoxRender()
        # 渲染背景
        self.levelLoadBgRender()

    def levelLoadEvent(self):
        """
        读取界面元素
        :return:无
        """
        # 是否按下esc键
        self.levelLoadBackMainEvent()
        # 是否点击返回按钮
        self.levelLoadBackBtnEvent()
        # 存档盒子的事件
        self.levelLoadSaveBoxEvent()

    def levelLoadSomeVariable(self):
        """
        一些变量
        :return:无
        """
        self.IS_LOAD_PAGE = False
        self.levelLoad_saveBox_pos = LoadBox_position  # 存档盒子坐标
        self.levelLoad_font_1 = pygame.font.Font(config["BASE_FONT_PATH"], 35)  # 35号大小
        self.levelLoad_font_2 = pygame.font.Font(config["BASE_FONT_PATH"], 20)  # 20号大小

    def levelLoadBgElement(self):
        """
        背景
        :return:无
        """
        self.levelLoad_bg = pygame.image.load(".\\media\\image\\background_6.jpg").convert()
        self.levelLoad_bg = pygame.transform.scale(self.levelLoad_bg, self.SIZE)

    def levelLoadBgRender(self):
        """
        背景
        :return:无
        """
        self.screen.blit(self.levelLoad_bg, (0, 0))

    def levelLoadBgBoxElement(self):
        """
        背景板
        :return:无
        """
        self.levelLoad_bgBox = pygame.image.load(".\\module\\image\\box_14.png").convert_alpha()
        self.levelLoad_bgBox = pygame.transform.scale(self.levelLoad_bgBox, (1100, 600))  # 调整大小
        self.levelLoad_bgBox.set_alpha(200)  # 设置透明度
        self.levelLoad_bgBox_rect = self.levelLoad_bgBox.get_rect()  # 获取rect
        self.levelLoad_bgBox_rect.center = (self.SIZE[0] / 2, self.SIZE[1] / 2)  # 设置居中

    def levelLoadBgBoxRender(self):
        """
        背景板的渲染
        :return:无
        """
        self.levelLoad_bg.blit(self.levelLoad_bgBox, self.levelLoad_bgBox_rect)

    def levelLoadBackBtnElement(self):
        """
        返回主界面按钮
        :return:无
        """
        # 文本对象
        self.levelLoad_backMainPage_font = self.BASE_FONT.render("返回主界面", True, self.FONT_DEFAULT_COLOR, None)
        self.levelLoad_backMainPage_font_rect = self.levelLoad_backMainPage_font.get_rect()
        self.levelLoad_backMainPage_active = self.BASE_FONT.render("返回主界面", True, self.FONT_ACTIVE_COLOR, None)
        # 设置坐标
        self.levelLoad_backMainPage_font_rect.left = self.levelLoad_bgBox_rect[0]
        self.levelLoad_backMainPage_font_rect.top = self.levelLoad_bgBox_rect[1] + self.levelLoad_bgBox_rect[3]
        # 变量
        self.levelLoad_backMainPage_choose = False  # 选中状态

    def levelLoadBackBtnRender(self):
        """
        返回主界面按钮
        :return:无
        """
        # 渲染文本
        self.levelLoad_bg.blit(self.levelLoad_backMainPage_font, self.levelLoad_backMainPage_font_rect)
        if self.levelLoad_backMainPage_choose:  # 如果选中就渲染选中状态
            self.levelLoad_bg.blit(self.levelLoad_backMainPage_active, self.levelLoad_backMainPage_font_rect)

    def levelLoadBackBtnEvent(self):
        """
        返回主界面按钮
        :return:无
        """
        if self.levelLoad_backMainPage_font_rect[0] < self.mouse_position[0] < (
            self.levelLoad_backMainPage_font_rect[0] + self.levelLoad_backMainPage_font_rect[2]) \
            and \
            self.levelLoad_backMainPage_font_rect[1] < self.mouse_position[1] < (
            self.levelLoad_backMainPage_font_rect[1] + self.levelLoad_backMainPage_font_rect[3]):  # 如果位于按钮上
            self.levelLoad_backMainPage_choose = True  # 选中状态改为True
            if self.mouse_pressed[0] and self.cushion_active:  # 点击并缓冲好
                self.cushion_active = False  # 缓冲状态改为False
                self.btnClick()  # 播放点击音效
                self.gameLoadPageBackMainPage()  # 返回主界面事件触发
        else:
            self.levelLoad_backMainPage_choose = False

    def levelLoadBackMainEvent(self):
        """
        按下esc返回主界面事件
        :return:无
        """
        for event in self.keys_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameLoadPageBackMainPage()

    def levelLoadSaveBoxElement(self):
        """
        9个存档格子元素
        :return:无
        """
        # 变量
        self.levelLoad_saveBox_list = []  # 存储盒子surface对象
        self.levelLoad_saveBox_size = (340, 173)  # 盒子大小
        self.levelLoad_saveBoxImg_size = (120, 120)  # 头像大小
        self.levelLoad_saveBox_id = 0  # 代表存档盒子的唯一id
        self.levelLoad_saveBox_pid = 1  # 代表存档盒子的页id，默认第一页
        self.levelLoad_saveBox_nowPage = 1  # 当前存档页，默认1
        self.levelLoad_saveBox_choose = -1  # 选中的存档盒子的id
        file_list = os.listdir(".\\saveFiles\\")  # 读取存档文件夹并获取到所有文件名
        self.levelLoad_saveBox_file_num = len(file_list)  # 获取存档数量
        if self.levelLoad_saveBox_file_num % 9 == 0:  # 如果能整除说明是整数页
            self.levelLoad_saveBox_allPage = int(self.levelLoad_saveBox_file_num / 9)  # 直接取整就行了，例:9 / 9 = 1，就是1页
        else:
            self.levelLoad_saveBox_allPage = int(self.levelLoad_saveBox_file_num / 9) + 1  # 取整然后+1才是真正的页数
        # 循环创建surface对象
        for i in range(self.levelLoad_saveBox_file_num):
            # 临时变量
            name_str = ""
            img_path = ""
            # 获取文件日期和玩家姓名和头像
            file_name = file_list[i]
            file_time = str(datetime.datetime.strptime(file_name[0:-4], '%Y-%m-%d %H-%M-%S'))  # 去除字符串并转换一下格式
            file_csv = csv.reader(open(".\\saveFiles\\" + file_name, 'r', encoding="UTF-8"))  # 打开并读取文件
            for line in file_csv:  # 取出姓名
                if line[0] == "名字":
                    name_str = line[1]  # 姓名
                    break
            for line in file_csv:  # 取出头像
                if line[0] == "头像":
                    img_path = line[1]  # 头像
                    break
            # 创建格子
            self.levelLoad_saveBox_list.append([pygame.image.load(".\\module\\image\\box_4.jpg").convert_alpha(), # 载入图片
                                                self.levelLoad_saveBox_pid, self.levelLoad_saveBox_id, False])  # 设置页id和唯一id和选中状态bool
            self.levelLoad_saveBox_list[i][0] = pygame.transform.scale(self.levelLoad_saveBox_list[i][0], self.levelLoad_saveBox_size)  # 设置大小
            self.levelLoad_saveBox_list[i][0].set_alpha(200)  # 设置透明度
            # 创建文本
            name_font = self.levelLoad_font_1.render(name_str, True, (255, 255, 255), None)  # 名字文本
            time_font = self.levelLoad_font_2.render(file_time, True, (255, 255, 255), None)  # 时间文本
            img = pygame.image.load(img_path).convert()  # 获取图片
            img = pygame.transform.scale(img, self.levelLoad_saveBoxImg_size)  # 设置头像大小
            # 绘制在盒子上
            self.levelLoad_saveBox_list[i][0].blit(name_font, (20, 20))  # 绘制姓名
            self.levelLoad_saveBox_list[i][0].blit(time_font, (20, 135))  # 绘制时间
            self.levelLoad_saveBox_list[i][0].blit(img, (210, 27))  # 绘制微缩头像
            # 设置页id和唯一id
            if self.levelLoad_saveBox_id != 8:  # 如果当前不是第九个盒子则加1
                self.levelLoad_saveBox_id += 1  # 增1
            else:  # 当前是第九个盒子
                self.levelLoad_saveBox_id = 0  # 唯一id归0
                self.levelLoad_saveBox_pid += 1  # 页id+1
        # 上翻页按钮和下翻页按钮
        self.levelLoad_nextPage_choose = False
        self.levelLoad_lastPage_choose = False
        self.levelLoad_nextPage = self.BASE_FONT.render("下一页", True, self.FONT_DEFAULT_COLOR, None)
        self.levelLoad_lastPage = self.BASE_FONT.render("上一页", True, self.FONT_DEFAULT_COLOR, None)
        self.levelLoad_nextPage_active = self.BASE_FONT.render("下一页", True, self.FONT_ACTIVE_COLOR, None)
        self.levelLoad_lastPage_active = self.BASE_FONT.render("上一页", True, self.FONT_ACTIVE_COLOR, None)
        self.levelLoad_nextPage_rect = self.levelLoad_nextPage.get_rect()
        self.levelLoad_lastPage_rect = self.levelLoad_lastPage.get_rect()
        self.levelLoad_nextPage_rect.left, self.levelLoad_nextPage_rect.top = 700, (self.levelLoad_bgBox_rect[1] + self.levelLoad_bgBox_rect[3])
        self.levelLoad_lastPage_rect.left, self.levelLoad_lastPage_rect.top = 500, (self.levelLoad_bgBox_rect[1] + self.levelLoad_bgBox_rect[3])
        # 开始游戏按钮
        self.levelLoad_start_choose = False
        self.levelLoad_start_font = self.BASE_FONT.render("开始游戏", True, self.FONT_DEFAULT_COLOR, None)
        self.levelLoad_start_active = self.BASE_FONT.render("开始游戏", True, self.FONT_ACTIVE_COLOR, None)
        self.levelLoad_start_font_rect = self.levelLoad_start_font.get_rect()
        self.levelLoad_start_font_rect.top = self.levelLoad_bgBox_rect[1] + self.levelLoad_bgBox_rect[3]
        self.levelLoad_start_font_rect.left = self.levelLoad_bgBox_rect[0] + self.levelLoad_bgBox_rect[2] - self.levelLoad_start_font_rect[2]

    def levelLoadSaveBoxRender(self):
        """
        存档格子渲染
        :return:无
        """
        # 盒子渲染
        j = 0  # 坐标索引
        for i in range(self.levelLoad_saveBox_file_num):
            # 索引判断
            if i % 9 == 0:  # 当i%9=0的时候就说明当前是新一页的第一项，所以就将坐标索引归0
                j = 0
            # 渲染盒子
            if self.levelLoad_saveBox_list[i][1] == self.levelLoad_saveBox_nowPage:  # 如果盒子属于当前页则渲染，不是则不渲染
                self.levelLoad_bg.blit(self.levelLoad_saveBox_list[i][0], self.levelLoad_saveBox_pos[j])
            # 索引递增
            j += 1
        # 翻页按钮
        self.levelLoad_bg.blit(self.levelLoad_nextPage, self.levelLoad_nextPage_rect)
        self.levelLoad_bg.blit(self.levelLoad_lastPage, self.levelLoad_lastPage_rect)
        if self.levelLoad_nextPage_choose:
            self.levelLoad_bg.blit(self.levelLoad_nextPage_active, self.levelLoad_nextPage_rect)
        elif self.levelLoad_lastPage_choose:
            self.levelLoad_bg.blit(self.levelLoad_lastPage_active, self.levelLoad_lastPage_rect)
        # 页数创建并渲染
        page = str(self.levelLoad_saveBox_nowPage) + " / " + str(self.levelLoad_saveBox_allPage)  # 拼接字符串
        page_font = self.BASE_FONT.render(page, True, self.FONT_DEFAULT_COLOR, None)
        self.levelLoad_bg.blit(page_font, (620, self.levelLoad_nextPage_rect.top))
        # 开始游戏按钮
        self.levelLoad_bg.blit(self.levelLoad_start_font, self.levelLoad_start_font_rect)
        if self.levelLoad_start_choose:
            self.levelLoad_bg.blit(self.levelLoad_start_active, self.levelLoad_start_font_rect)

    def levelLoadSaveBoxEvent(self):
        """
        存档格子的事件
        :return:无
        """
        # 几个按钮的判断
        # 点击下一页按钮
        if self.levelLoad_nextPage_rect[0] < self.mouse_position[0] < (
            self.levelLoad_nextPage_rect[0] + self.levelLoad_nextPage_rect[2]) \
            and \
            self.levelLoad_nextPage_rect[1] < self.mouse_position[1] < (
            self.levelLoad_nextPage_rect[1] + self.levelLoad_nextPage_rect[3]):  # 如果位于按钮上
            self.levelLoad_nextPage_choose = True  # 选中状态改为True
            if self.mouse_pressed[0] and self.cushion_active:  # 点击并缓冲好
                self.cushion_active = False  # 缓冲状态改为False
                self.btnClick()  # 播放点击音效
                if self.levelLoad_saveBox_nowPage < self.levelLoad_saveBox_allPage:  # 如果当前页面小于总页面才能继续翻页
                    self.levelLoad_saveBox_nowPage += 1
        # 点击上一页按钮
        elif self.levelLoad_lastPage_rect[0] < self.mouse_position[0] < (
            self.levelLoad_lastPage_rect[0] + self.levelLoad_lastPage_rect[2]) \
            and \
            self.levelLoad_lastPage_rect[1] < self.mouse_position[1] < (
            self.levelLoad_lastPage_rect[1] + self.levelLoad_lastPage_rect[3]):  # 如果位于按钮上
            self.levelLoad_lastPage_choose = True  # 选中状态改为True
            if self.mouse_pressed[0] and self.cushion_active:  # 点击并缓冲好
                self.cushion_active = False  # 缓冲状态改为False
                self.btnClick()  # 播放点击音效
                if self.levelLoad_saveBox_nowPage > 1:  # 如果大于1才能减，否则不能减
                    self.levelLoad_saveBox_nowPage -= 1
        # 点击开始游戏按钮
        elif self.levelLoad_start_font_rect[0] < self.mouse_position[0] < (
            self.levelLoad_start_font_rect[0] + self.levelLoad_start_font_rect[2]) \
            and \
            self.levelLoad_start_font_rect[1] < self.mouse_position[1] < (
            self.levelLoad_start_font_rect[1] + self.levelLoad_start_font_rect[3]):  # 如果位于按钮上
            self.levelLoad_start_choose = True  # 选中状态改为True
            if self.mouse_pressed[0] and self.cushion_active:  # 点击并缓冲好
                self.cushion_active = False  # 缓冲状态改为False
                self.btnClick()  # 播放点击音效
                self.loadPageGoEndPage()  # 去往结束界面
        else:
            self.levelLoad_nextPage_choose = False
            self.levelLoad_lastPage_choose = False
            self.levelLoad_start_choose    = False
        # 存档盒子的点击判断
        for i in range(self.levelLoad_saveBox_file_num):
            if self.levelLoad_saveBox_list[i][1] == self.levelLoad_saveBox_nowPage:  # 如果是当前页才进行点击判断
                pos_id = int(i - 9 * (self.levelLoad_saveBox_nowPage - 1))  # pos坐标列表的id，算法:int(i - 9 * (当前页id - 1))
                if self.levelLoad_saveBox_pos[pos_id][0] < self.mouse_position[0] < (
                    self.levelLoad_saveBox_pos[pos_id][0] + self.levelLoad_saveBox_size[0]) \
                    and \
                    self.levelLoad_saveBox_pos[pos_id][1] < self.mouse_position[1] < (
                    self.levelLoad_saveBox_pos[pos_id][1] + self.levelLoad_saveBox_size[1]) \
                    and \
                    self.mouse_pressed[0] and self.cushion_active:  # 当前在该盒子上方并点击盒子
                    self.cushion_active = False  # 鼠标缓冲改为False
                    self.btnClick()  # 播放点击音效
                    self.levelLoad_saveBox_list[i][3] = not self.levelLoad_saveBox_list[i][3]  # 取反，点击选中和取消选中
                    if self.levelLoad_saveBox_list[i][3]:  # 如果是选中状态就将透明度改为不透明，目的:加深显示
                        self.levelLoad_saveBox_list[i][0].set_alpha(255)  # 更改透明度
                        self.levelLoad_saveBox_choose = i  # 选中id设置为当前盒子id
                    else:
                        self.levelLoad_saveBox_list[i][0].set_alpha(200)  # 更改透明度
                    break  # 停止循环判断