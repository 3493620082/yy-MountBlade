# --coding=utf-8
import csv
import os
import datetime
import random
import pygame
# 游戏文件
from setting import config
import module.button_position as btn_pos

class level_player:
    def levelPlayerElement(self):
        # 一些所需变量
        self.levelPlayerVariable()
        # 主要元素
        self.levelPlayer_bg = pygame.image.load(".\\media\\image\\box_background_1.jpg").convert()  # 背景图片
        self.levelPlayer_bg = pygame.transform.scale(self.levelPlayer_bg, self.SIZE)  # 设置大小
        # 返回和开始游戏按钮元素
        self.levelPlayerBackBoxAndStartBoxElement()
        # 姓名框所需元素
        self.levelPlayerNameBoxElement()
        # 临时元素(用完删!!!)
        # self.test = pygame.Surface((self.SIZE[0], self.SIZE[1] - self.levelPlayer_name_box_rect[3])).convert_alpha()
        # self.test.fill((255, 255, 255))
        # self.test.set_alpha(125)
        # self.test_rect = self.test.get_rect()
        # self.test_rect[1] = self.levelPlayer_name_box_rect[3]
        # self.test_font_1 = pygame.font.SysFont("microsoftyahei", 50, bold=True)
        # self.test_font = self.test_font_1.render("TestFrame", True, (0, 0, 0), None)
        # self.test_font_rect = self.test_font.get_rect()
        # self.test_font_rect.center = (self.test_rect[2] / 2, self.test_rect[3] / 2)
        # self.test.blit(self.test_font, self.test_font_rect)  # 将文本渲染在self.test上面
        # 边框线元素
        self.levelPlayerBorderElement()
        # 头像元素
        self.levelPlayerImageElement()
        # 人物属性面板元素
        self.levelPlayerAttributeElement()

    def levelPlayerRender(self):
        # 实时创建字体
        self.levelPlayer_name_font = self.levelPlayer_font_1.render(self.levelPlayer_name_str, True, (255, 255, 255), None)  # 创建字体对象
        self.levelPlayer_name_font_rect = self.levelPlayer_name_font.get_rect()  # 获取rect对象
        # 实时创建背景
        self.levelPlayer_bg = pygame.image.load(".\\media\\image\\box_background_1.jpg").convert()  # 背景图片
        self.levelPlayer_bg = pygame.transform.scale(self.levelPlayer_bg, self.SIZE)  # 设置大小
        # test遮罩
        # self.levelPlayer_bg.blit(self.test, self.test_rect)  # 将test渲染在levelPlayer_bg的最底层
        # 返回界面和开始游戏
        self.levelPlayerBackBoxAndStartBoxRender()
        # 姓名框判断+渲染
        self.levelPlayerNameBoxRender()
        # 边框线渲染
        self.levelPlayerBorderRender()
        # 头像渲染
        self.levelPlayerImageRender()
        # 人物属性面板渲染
        self.levelPlayerAttributeRender()
        # 渲染背景
        self.screen.blit(self.levelPlayer_bg, (0, 0))

    def levelPlayerEvent(self):
        # 姓名框的事件
        self.levelPlayerNameBoxEvent()
        # 返回和开始按钮的事件
        self.levelPlayerBackBoxAndStartBoxEvent()
        # 头像的事件(因为没有事件所以注释掉)
        # self.levelPlayerImageEvent()
        # 人物属性面板的事件
        self.levelPlayerAttributeEvent()

    def levelPlayerVariable(self):
        """
        此函数加载此level所用到的一些变量
        :return:
        """
        self.levelPlayer_cushion_active = True  # 鼠标缓冲
        self.levelPlayer_name_active = False  # 姓名对话框选中状态
        self.levelPlayer_name_edit_active = False  # 姓名编辑状态
        self.levelPlayer_name_tips_active = False  # 姓名编辑提示框状态
        self.levelPlayer_name_str = ""  # 定义变量用于存放键盘打出来的姓名
        self.levelPlayer_cushion_time = 0  # 鼠标缓冲时间
        self.levelPlayer_font_1 = pygame.font.Font(config["BASE_FONT_PATH"], 20)
        # self.levelPlayer_font_1 = pygame.font.SysFont("华文楷体", 20)  # 私有字体_1
        self.PlayerAttributeBaseFont_pos = btn_pos.PlayerAttributeBaseFont_position  # 读出文本坐标
        self.PlayerAttributePassiveFont_pos = btn_pos.PlayerAttributePassiveFont_position  # 读出文本坐标
        self.PlayerAttributeAttackFont_pos = btn_pos.PlayerAttributeAttackFont_position  # 读出文本坐标
        self.PlayerAttributeBaseBtn_pos = btn_pos.PlayerAttributeBaseBtn_position  # 读出按钮坐标
        self.PlayerAttributePassiveBtn_pos = btn_pos.PlayerAttributePassiveBtn_position  # 读出按钮坐标
        self.PlayerAttributeAttackBtn_pos = btn_pos.PlayerAttributeAttackBtn_position  # 读出按钮坐标
        self.PlayerAttributePoints_pos = btn_pos.PlayerAttributePoints_position  # 读出点数坐标

    def levelPlayerNameBoxElement(self):
        """
        姓名框所需的元素
        姓名框、姓名文本(因为是实时创建，所以写在了渲染方法里面)、提示框、提示文本
        :return: 无
        """
        self.levelPlayer_name_box = pygame.image.load(".\\module\\image\\box_8.png").convert_alpha()  # 姓名框背景图片
        self.levelPlayer_name_box = pygame.transform.scale(self.levelPlayer_name_box, (300, 30))  # 设置大小
        self.levelPlayer_name_box_rect = self.levelPlayer_name_box.get_rect()  # 获取姓名框的rect对象
        self.levelPlayer_name_box_rect.centerx = self.SIZE[0] / 2  # 设置坐标居中置顶
        self.levelPlayer_name_tips_box = pygame.image.load(".\\module\\image\\box_2.jpg").convert_alpha()  # 提示框
        self.levelPlayer_name_tips_box.set_alpha(200)  # 设置为200的透明度
        self.levelPlayer_name_tips_box = pygame.transform.scale(self.levelPlayer_name_tips_box, (50, 300))  # 缩放大小
        self.levelPlayer_name_tips_box = pygame.transform.rotate(self.levelPlayer_name_tips_box, 90)  # 旋转角度
        self.levelPlayer_name_tips_box_rect = self.levelPlayer_name_tips_box.get_rect()  # 获取提示框的rect对象
        self.levelPlayer_name_tips_box_rect[0] = self.levelPlayer_name_box_rect[0]  # 以姓名框为基准，渲染在姓名框下面
        self.levelPlayer_name_tips_box_rect[1] = self.levelPlayer_name_box_rect[3]  # 以姓名框为基准，渲染在姓名框下面
        self.levelPlayer_name_tips_font = self.levelPlayer_font_1.render("再次点击姓名框结束输入状态哦", True, (0, 0, 0), None)  # 提示文本
        self.levelPlayer_name_tips_font_rect = self.levelPlayer_name_tips_font.get_rect()  # 提示文本的rect对象
        self.levelPlayer_name_tips_font_rect.center = (
        (self.levelPlayer_name_tips_box_rect[0] + self.levelPlayer_name_tips_box_rect[2] / 2),
        (self.levelPlayer_name_tips_box_rect[1] + self.levelPlayer_name_tips_box_rect[3] / 2))  # 设置提示文本的渲染坐标

    def levelPlayerNameBoxRender(self):
        """
        姓名框的渲染
        :return:无
        """
        if self.levelPlayer_name_active:  # 如果选中姓名框
            self.levelPlayer_name_box.set_alpha(200)  # 设置透明一点表示可编辑
            if self.levelPlayer_name_tips_active:  # 如果提示框为True
                self.levelPlayer_bg.blit(self.levelPlayer_name_tips_box, self.levelPlayer_name_tips_box_rect)  # 渲染提示框
                self.levelPlayer_bg.blit(self.levelPlayer_name_tips_font, self.levelPlayer_name_tips_font_rect)  # 渲染提示框的文字
        else:  #如果没有选中姓名框
            self.levelPlayer_name_box.set_alpha(255)  # 设置不透明表示不可编辑
        self.levelPlayer_bg.blit(self.levelPlayer_name_box, self.levelPlayer_name_box_rect)  # 渲染背景
        self.levelPlayer_bg.blit(self.levelPlayer_name_font, ((self.SIZE[0] / 2 - self.levelPlayer_name_font_rect[2] / 2), 0))  # 渲染文本

    def levelPlayerNameBoxEvent(self):
        """
        姓名框的相关事件
        :return:无
        """
        if self.levelPlayer_name_box_rect[0] < self.mouse_position[0] < (  # 判断是否点击了姓名框
                self.levelPlayer_name_box_rect[0] + self.levelPlayer_name_box_rect[2]) \
                and \
                self.levelPlayer_name_box_rect[1] < self.mouse_position[1] < (
                self.levelPlayer_name_box_rect[1] + self.levelPlayer_name_box_rect[3]):  # 鼠标位于按钮上
            self.levelPlayer_name_tips_active = True
            if self.mouse_pressed[0] and self.cushion_active:  # 如果点击按钮
                self.cushion_active = False  # 将按钮缓冲改为False
                self.btnClick()  # 播放点击音效
                self.levelPlayer_name_active = not self.levelPlayer_name_active  # 将姓名框选中状态取反
                self.levelPlayer_name_edit_active = not self.levelPlayer_name_edit_active  # 将姓名框编辑状态取反
        else:  # 如果鼠标不在姓名框上则将提示框显示状态改为False
            self.levelPlayer_name_tips_active = False
        if self.levelPlayer_name_edit_active:  # 如果当前是编辑状态
            self.levelPlayer_name_str = self.getKeyboardInput(self.levelPlayer_name_str)  # 拼接字符串

    def levelPlayerBackBoxAndStartBoxElement(self):
        """
        返回主界面和开始游戏按钮的元素
        :return:无
        """
        self.levelPlayer_backBox_StartBox_list = []  # 存放两个按钮的列表
        self.levelPlayer_backBox_StartBox_rect_list = []  # 存放两个按钮的rect的列表
        self.levelPlayer_backBox_StartBox_font_list = []  # 存放两个按钮的文本的列表
        self.levelPlayer_backBox_StartBox_str_list = ["返回主界面", "开始游戏"]  # 文本列表
        self.levelPlayer_backBox_StartBox_font_active_list = []  # 存放两个按钮选中状态的列表
        self.levelPlayer_backBox_StartBox_font_rect_list = []  # 存放两个按钮的文本的rect的列表
        self.levelPlayer_backBox_StartBox_active_list = [False, False]  # 存放按钮选中状态(渲染文本用)
        self.levelPlayer_backBox_StartBox_num = 2  # 数量
        for i in range(self.levelPlayer_backBox_StartBox_num):  # 循环创建按钮
            self.levelPlayer_backBox_StartBox_list.append(pygame.image.load(".\\module\\image\\box_8.png").convert_alpha())  # 创建返回框
            self.levelPlayer_backBox_StartBox_list[i].set_alpha(255)  # 设置透明度
            self.levelPlayer_backBox_StartBox_list[i] = pygame.transform.scale(self.levelPlayer_backBox_StartBox_list[i], (200, 30))  # 设置大小
            self.levelPlayer_backBox_StartBox_rect_list.append(self.levelPlayer_backBox_StartBox_list[i].get_rect())  # 创建rect对象
            self.levelPlayer_backBox_StartBox_font_list.append(self.levelPlayer_font_1.render(self.levelPlayer_backBox_StartBox_str_list[i], True, self.FONT_DEFAULT_COLOR, None))  # 创建文本对象
            self.levelPlayer_backBox_StartBox_font_rect_list.append(self.levelPlayer_backBox_StartBox_font_list[i].get_rect())  # 创建字体的rect对象
            self.levelPlayer_backBox_StartBox_font_active_list.append(self.levelPlayer_font_1.render(self.levelPlayer_backBox_StartBox_str_list[i], True, self.FONT_ACTIVE_COLOR, None))  # 创建活动文本对象
        # 单独设置文本和按钮的坐标
        self.levelPlayer_backBox_StartBox_rect_list[1].left = self.SIZE[0] - self.levelPlayer_backBox_StartBox_rect_list[1][2]  # 开始游戏按钮坐标为右上角
        self.levelPlayer_backBox_StartBox_font_rect_list[0].center = (self.levelPlayer_backBox_StartBox_rect_list[0][2] / 2,  # 返回主界面字体的坐标
                                                                      self.levelPlayer_backBox_StartBox_rect_list[0][3] / 2)
        self.levelPlayer_backBox_StartBox_font_rect_list[1].center = (self.levelPlayer_backBox_StartBox_rect_list[0][2] / 2,  # 开始游戏字体的坐标
                                                                      self.levelPlayer_backBox_StartBox_rect_list[1][3] / 2)
        self.levelPlayer_backBox_StartBox_font_rect_list[1][0] += self.SIZE[0] - self.levelPlayer_backBox_StartBox_rect_list[1][2]  # 开始游戏字体坐标的调整

    def levelPlayerBackBoxAndStartBoxRender(self):
        """
        返回主界面和开始游戏按钮元素的渲染
        :return:无
        """
        for i in range(self.levelPlayer_backBox_StartBox_num):  # 循环渲染
            self.levelPlayer_bg.blit(self.levelPlayer_backBox_StartBox_list[i], self.levelPlayer_backBox_StartBox_rect_list[i])
            self.levelPlayer_bg.blit(self.levelPlayer_backBox_StartBox_font_list[i], self.levelPlayer_backBox_StartBox_font_rect_list[i])
        if self.levelPlayer_backBox_StartBox_active_list[0]:  # 如果返回按钮为选中状态
            self.levelPlayer_bg.blit(self.levelPlayer_backBox_StartBox_font_active_list[0], self.levelPlayer_backBox_StartBox_font_rect_list[0])
        elif self.levelPlayer_backBox_StartBox_active_list[1]:  # 如果开始按钮为选中状态
            self.levelPlayer_bg.blit(self.levelPlayer_backBox_StartBox_font_active_list[1], self.levelPlayer_backBox_StartBox_font_rect_list[1])

    def levelPlayerBackBoxAndStartBoxEvent(self):
        """
        返回和开始按钮的事件
        :return:无
        """
        if self.levelPlayer_backBox_StartBox_rect_list[0][0] < self.mouse_position[0] < (  # 判断是否点击了返回框
                self.levelPlayer_backBox_StartBox_rect_list[0][0] + self.levelPlayer_backBox_StartBox_rect_list[0][2]) \
                and \
                self.levelPlayer_backBox_StartBox_rect_list[0][1] < self.mouse_position[1] < (
                self.levelPlayer_backBox_StartBox_rect_list[0][1] + self.levelPlayer_backBox_StartBox_rect_list[0][3]):  # 鼠标位于按钮上
            self.levelPlayer_backBox_StartBox_active_list[0] = True  # 改为True
            if self.mouse_pressed[0] and self.cushion_active:  # 如果点击按钮
                self.cushion_active = False  # 将按钮缓冲改为False
                self.btnClick()  # 播放点击音效
                self.gamePageBackMainPage()  # 触发返回主界面事件
        elif self.levelPlayer_backBox_StartBox_rect_list[1][0] < self.mouse_position[0] < (  # 判断是否点击了开始框
                self.levelPlayer_backBox_StartBox_rect_list[1][0] + self.levelPlayer_backBox_StartBox_rect_list[1][2]) \
                and \
                self.levelPlayer_backBox_StartBox_rect_list[1][1] < self.mouse_position[1] < (
                self.levelPlayer_backBox_StartBox_rect_list[1][1] + self.levelPlayer_backBox_StartBox_rect_list[1][3]):  # 鼠标位于按钮上
            self.levelPlayer_backBox_StartBox_active_list[1] = True  # 改为True
            if self.mouse_pressed[0] and self.cushion_active:  # 如果点击按钮
                self.cushion_active = False  # 将按钮缓冲改为False
                self.btnClick()  # 播放点击音效
                self.levelPlayerSaveGame()  # 保存游戏文件
                self.gamePageGoEndPage()  # 触发开始游戏事件
        else:
            self.levelPlayer_backBox_StartBox_active_list = [False, False]  # 改为False

    def levelPlayerBorderElement(self):
        """
        边框元素
        :return:无
        """
        self.levelPlayer_border_list = []  # 存放边框线的surface对象
        self.levelPlayer_border_rect_list = []  # 存放边框线rect对象
        self.levelPlayer_border_num = 2  # 边框线数量
        self.levelPlayer_border_color = (0, 0, 0)  # 颜色元组
        self.levelPlayer_average_x = int(self.SIZE[0] / (self.levelPlayer_border_num + 1))  # 算法:背景的宽度除以数量加1然后取整
        for i in range(self.levelPlayer_border_num):  # 创建两条边框线
            self.levelPlayer_border_list.append(pygame.Surface((1, self.SIZE[1] - self.levelPlayer_name_box_rect[3])).convert())  # 边框
        for i in range(self.levelPlayer_border_num):  # 创建rect对象
            self.levelPlayer_border_rect_list.append(self.levelPlayer_border_list[i].get_rect())  # 将创建的rect对象存放进列表
        for i in range(self.levelPlayer_border_num):  # 给每个边框填充颜色
            self.levelPlayer_border_list[i].fill(self.levelPlayer_border_color)  # 填充白色
        for i in range(self.levelPlayer_border_num):  # 设置rect
            self.levelPlayer_border_rect_list[i].left = self.levelPlayer_average_x * (i + 1)  # 设置左坐标
            self.levelPlayer_border_rect_list[i].top = self.levelPlayer_name_box_rect[3]

    def levelPlayerBorderRender(self):
        """
        边框元素的渲染
        :return:无
        """
        for i in range(self.levelPlayer_border_num):  # 循环
            self.levelPlayer_bg.blit(self.levelPlayer_border_list[i], self.levelPlayer_border_rect_list[i])  # 渲染

    def levelPlayerImageElement(self):
        """
        头像元素
        :return:无
        """
        # 选择图片文件
        self.levelPlayer_image_list = os.listdir(".\\media\\npc_image\\no_name")  # 获取到所有文件名
        self.random_img = "./media/npc_image/no_name/" + str(random.choice(self.levelPlayer_image_list))  # 随机选择一个文件
        self.levelPlayer_imageRight_list = os.listdir(".\\media\\image\\")
        self.random_imgRight = ".\\media\\image\\" + str(random.choice(self.levelPlayer_imageRight_list))
        # 创建图片盒子
        self.levelPlayer_image_box = pygame.image.load(".\\module\\image\\box_4.jpg").convert_alpha()  # 载入图片
        self.levelPlayer_image_box = pygame.transform.scale(self.levelPlayer_image_box, (self.levelPlayer_average_x, 400))  # 设置大小
        self.levelPlayer_image_box_rect = self.levelPlayer_image_box.get_rect()  # 获取rect
        self.levelPlayer_image_box_rect.top = self.levelPlayer_name_box_rect[3]  # 设置top
        self.levelPlayer_imageRight_box = pygame.image.load(".\\module\\image\\box_3.png").convert_alpha()  # 载入图片
        self.levelPlayer_imageRight_box = pygame.transform.scale(self.levelPlayer_imageRight_box, (self.levelPlayer_average_x, 400))  #设置大小
        self.levelPlayer_imageRight_box_rect = self.levelPlayer_imageRight_box.get_rect()
        self.levelPlayer_imageRight_box_rect.top = self.levelPlayer_image_box_rect.top
        self.levelPlayer_imageRight_box_rect.left = self.levelPlayer_average_x * 2
        # 创建图片对象
        self.levelPlayer_image = pygame.image.load(self.random_img).convert_alpha()  # 创建图片对象
        self.levelPlayer_image = pygame.transform.scale(self.levelPlayer_image, (self.levelPlayer_average_x - 30, 400 - 30))  # 设置比盒子小一圈(小20px)
        self.levelPlayer_image.set_alpha(175)  # 设置透明度
        self.levelPlayer_image_rect = self.levelPlayer_image.get_rect()  # 获取rect对象
        self.levelPlayer_image_rect.top = self.levelPlayer_name_box_rect[3] + 15  # 设置top
        self.levelPlayer_image_rect.left = self.levelPlayer_image_box_rect[0] + 15  # 设置left
        self.levelPlayer_imageRight = pygame.image.load(self.random_imgRight).convert_alpha()
        self.levelPlayer_imageRight = pygame.transform.scale(self.levelPlayer_imageRight, (self.levelPlayer_average_x - 40, 400 - 100))
        self.levelPlayer_imageRight.set_alpha(200)
        self.levelPlayer_imageRight_rect = self.levelPlayer_imageRight.get_rect()
        self.levelPlayer_imageRight_rect.top = self.levelPlayer_name_box_rect[3] + 40
        self.levelPlayer_imageRight_rect.left = self.levelPlayer_imageRight_box_rect[0] + 20

    def levelPlayerImageRender(self):
        """
        头像元素的渲染
        :return:无
        """
        # 渲染图片盒子
        self.levelPlayer_bg.blit(self.levelPlayer_image_box, self.levelPlayer_image_box_rect)
        self.levelPlayer_bg.blit(self.levelPlayer_imageRight_box, self.levelPlayer_imageRight_box_rect)
        # 渲染图片
        self.levelPlayer_bg.blit(self.levelPlayer_image, self.levelPlayer_image_rect)
        self.levelPlayer_bg.blit(self.levelPlayer_imageRight, self.levelPlayer_imageRight_rect)

    def levelPlayerImageEvent(self):
        """
        头像元素的事件
        :return:无
        """
        pass

    def levelPlayerAttributeElement(self):
        """
        人物属性设置面板
        :return:无
        """
        # 从文件中读取并加载人物基础属性表
        self.levelPlayer_playerAttribute_base = []  # 定义字典用于存放角色的属性(Attribute)
        self.levelPlayer_playerAttribute_passive = []  # 定义字典用于存放角色的属性(Attribute)
        self.levelPlayer_playerAttribute_attack = []  # 定义字典用于存放角色的属性(Attribute)
        self.levelPlayer_playerAttributePoints = {}  # 定义字典存放属性点数
        self.levelPlayer_attribute_base_font_pos = []  # 人物属性文本坐标的列表
        self.levelPlayer_attribute_passive_font_pos = []  # 人物属性文本坐标的列表
        self.levelPlayer_attribute_attack_font_pos = []  # 人物属性文本坐标的列表
        self.levelPlayer_attribute_base_btn_pos = []  # 人物属性按钮坐标的列表
        self.levelPlayer_attribute_passive_btn_pos = []  # 人物属性按钮坐标的列表
        self.levelPlayer_attribute_attack_btn_pos = []  # 人物属性按钮坐标的列表
        self.levelPlayer_attributePoints_font_pos = []  # 人物点数文本坐标的列表
        # 四种属性文件读取
        base_attribute = csv.reader(open(".\\media\\playerAttribute\\playerAttribute_Base_CN.csv", 'r', encoding="UTF-8"))
        passive_attribute = csv.reader(open(".\\media\\playerAttribute\\playerAttribute_Passive_CN.csv", 'r', encoding="UTF-8"))
        attack_attribute = csv.reader(open(".\\media\\playerAttribute\\playerAttribute_Attack_CN.csv", 'r', encoding="UTF-8"))
        points_attribute = csv.reader(open(".\\media\\playerAttribute\\playerAttributePoints_CN.csv", 'r', encoding="UTF-8"))
        # 四种属性写入列表
        for line in base_attribute:
            self.levelPlayer_playerAttribute_base.append([line[0], int(line[1])])
        for line in passive_attribute:
            self.levelPlayer_playerAttribute_passive.append([line[0], int(line[1])])
        for line in attack_attribute:
            self.levelPlayer_playerAttribute_attack.append([line[0], int(line[1])])
        for line in points_attribute:  # 取出数据
            self.levelPlayer_playerAttributePoints[line[0]] = int(line[1])  # 添加元素
        # 按钮
        self.levelPlayer_playerAttribute_btnUp = pygame.image.load(".\\module\\image\\btn_2_up.png").convert_alpha()  # 普通状态按钮
        self.levelPlayer_playerAttribute_btnDown = pygame.image.load(".\\module\\image\\btn_2_down.png").convert_alpha()  # 按下状态按钮
        self.levelPlayer_playerAttribute_btnUp = pygame.transform.scale(self.levelPlayer_playerAttribute_btnUp, (20, 20))  # 设置大小
        self.levelPlayer_playerAttribute_btnDown = pygame.transform.scale(self.levelPlayer_playerAttribute_btnDown, (20, 20))  # 设置大小
        self.levelPlayer_playerAttribute_btnUp_rect = self.levelPlayer_playerAttribute_btnUp.get_rect()  # 获取rect
        self.levelPlayer_playerAttribute_btnDown_rect = self.levelPlayer_playerAttribute_btnDown.get_rect()  # 获取rect
        # 按钮状态和选中id和选中类型
        self.levelPlayer_playerAttribute_base_btn_active = False
        self.levelPlayer_playerAttribute_passive_btn_active = False
        self.levelPlayer_playerAttribute_attack_btn_active = False
        self.levelPlayer_playerAttribute_base_btn_choose = -1
        self.levelPlayer_playerAttribute_passive_btn_choose = -1
        self.levelPlayer_playerAttribute_attack_btn_choose = -1
        # 字体
        self.levelPlayer_playerAttribute_font_1 = pygame.font.Font(config["BASE_FONT_PATH"], 30)  # 私有字体
        self.levelPlayer_playerAttribute_font_2 = pygame.font.Font(config["BASE_FONT_PATH"], 25)  # 私有字体
        # self.levelPlayer_playerAttribute_font_1 = pygame.font.SysFont("华文楷体", 30)  # 私有字体
        # self.levelPlayer_playerAttribute_font_2 = pygame.font.SysFont("华文楷体", 25)  # 私有字体
        # 为坐标列表添加元素
        for k, v in self.PlayerAttributeBaseFont_pos.items():  # 循环取出配置文件中文本的坐标数据
            self.levelPlayer_attribute_base_font_pos.append(v)  # 添加到这个列表中
        for k, v in self.PlayerAttributePassiveFont_pos.items():  # 循环取出配置文件中文本的坐标数据
            self.levelPlayer_attribute_passive_font_pos.append(v)  # 添加到这个列表中
        for k, v in self.PlayerAttributeAttackFont_pos.items():  # 循环取出配置文件中文本的坐标数据
            self.levelPlayer_attribute_attack_font_pos.append(v)  # 添加到这个列表中
        for k, v in self.PlayerAttributeBaseBtn_pos.items():  # 循环取出配置文件中按钮的坐标数据
            self.levelPlayer_attribute_base_btn_pos.append(v)  # 添加到这个列表中
        for k, v in self.PlayerAttributePassiveBtn_pos.items():  # 循环取出配置文件中按钮的坐标数据
            self.levelPlayer_attribute_passive_btn_pos.append(v)  # 添加到这个列表中
        for k, v in self.PlayerAttributeAttackBtn_pos.items():  # 循环取出配置文件中按钮的坐标数据
            self.levelPlayer_attribute_attack_btn_pos.append(v)  # 添加到这个列表中
        for k, v in self.PlayerAttributePoints_pos.items():  # 循环取出配置文件中点数的坐标数据
            self.levelPlayer_attributePoints_font_pos.append(v)  # 将坐标添加到列表中

    def levelPlayerAttributeRender(self):
        """
        人物属性设置面板渲染
        :return:无
        """
        j = 0
        # 循环渲染基础属性文本
        for i in self.levelPlayer_playerAttribute_base:
            # 渲染文本
            attribute_str = i[0] + ": " + str(i[1])  # 拼接字符串
            attribute_font = self.levelPlayer_playerAttribute_font_1.render(attribute_str, True, (0, 0, 0), None)  # 创建黑色字体文本对象
            attribute_font_rect = attribute_font.get_rect()  # 获取文本rect
            attribute_font_rect[0], attribute_font_rect[1] = self.levelPlayer_attribute_base_font_pos[j]  # 设置文本坐标
            self.levelPlayer_bg.blit(attribute_font, attribute_font_rect)  # 渲染文本
            # 渲染属性按钮
            self.levelPlayer_bg.blit(self.levelPlayer_playerAttribute_btnUp, self.levelPlayer_attribute_base_btn_pos[j])  # 渲染普通按钮
            if self.levelPlayer_playerAttribute_base_btn_active and \
                self.levelPlayer_playerAttribute_base_btn_choose == j:  # 如果当前编号按钮处于选中状态则改变按钮样式
                self.levelPlayer_bg.blit(self.levelPlayer_playerAttribute_btnDown, self.levelPlayer_attribute_base_btn_pos[j])  # 渲染按下的按钮样式
            # 索引递增
            j += 1
        # 渲染被动属性文本
        j = 0
        for i in self.levelPlayer_playerAttribute_passive:
            # 渲染文本
            attribute_str = i[0] + ": " + str(i[1])  # 拼接字符串
            attribute_font = self.levelPlayer_playerAttribute_font_1.render(attribute_str, True, (0, 0, 0), None)  # 创建黑色字体文本对象
            attribute_font_rect = attribute_font.get_rect()  # 获取文本rect
            attribute_font_rect[0], attribute_font_rect[1] = self.levelPlayer_attribute_passive_font_pos[j]  # 设置文本坐标
            self.levelPlayer_bg.blit(attribute_font, attribute_font_rect)  # 渲染文本
            # 渲染属性按钮
            self.levelPlayer_bg.blit(self.levelPlayer_playerAttribute_btnUp, self.levelPlayer_attribute_passive_btn_pos[j])  # 渲染普通按钮
            if self.levelPlayer_playerAttribute_passive_btn_active and \
                self.levelPlayer_playerAttribute_passive_btn_choose == j:  # 如果当前编号按钮处于选中状态则改变按钮样式
                self.levelPlayer_bg.blit(self.levelPlayer_playerAttribute_btnDown, self.levelPlayer_attribute_passive_btn_pos[j])  # 渲染按下的按钮样式
            # 索引递增
            j += 1
        # 渲染攻击属性文本
        j = 0
        for i in self.levelPlayer_playerAttribute_attack:
            # 渲染文本
            attribute_str = i[0] + ": " + str(i[1])  # 拼接字符串
            attribute_font = self.levelPlayer_playerAttribute_font_1.render(attribute_str, True, (0, 0, 0), None)  # 创建黑色字体文本对象
            attribute_font_rect = attribute_font.get_rect()  # 获取文本rect
            attribute_font_rect[0], attribute_font_rect[1] = self.levelPlayer_attribute_attack_font_pos[j]  # 设置文本坐标
            self.levelPlayer_bg.blit(attribute_font, attribute_font_rect)  # 渲染文本
            # 渲染属性按钮
            self.levelPlayer_bg.blit(self.levelPlayer_playerAttribute_btnUp, self.levelPlayer_attribute_attack_btn_pos[j])  # 渲染普通按钮
            if self.levelPlayer_playerAttribute_attack_btn_active and self.levelPlayer_playerAttribute_attack_btn_choose == j:  # 如果当前编号按钮处于选中状态则改变按钮样式
                self.levelPlayer_bg.blit(self.levelPlayer_playerAttribute_btnDown, self.levelPlayer_attribute_attack_btn_pos[j])  # 渲染按下的按钮样式
            # 索引递增
            j += 1
        # 渲染点数文本
        j = 0
        for k, v in self.levelPlayer_playerAttributePoints.items():
            points_str = k + ": " + str(v)  # 拼接字符串
            points_font = self.levelPlayer_playerAttribute_font_1.render(points_str, True, (0, 0, 0), None)  # 创建文本对象
            self.levelPlayer_bg.blit(points_font, self.levelPlayer_attributePoints_font_pos[j])  # 渲染文本
            j += 1

    def levelPlayerAttributeEvent(self):
        """
        人物属性设置面板事件
        :return:无
        """
        # 基础按钮选中判断
        for i in range(len(self.levelPlayer_playerAttribute_base)):
            if self.levelPlayer_attribute_base_btn_pos[i][0] < self.mouse_position[0] < (
                self.levelPlayer_attribute_base_btn_pos[i][0] + self.levelPlayer_playerAttribute_btnUp_rect[2]) \
                and \
                self.levelPlayer_attribute_base_btn_pos[i][1] < self.mouse_position[1] < (
                self.levelPlayer_attribute_base_btn_pos[i][1] + self.levelPlayer_playerAttribute_btnUp_rect[3]):  # 选中
                self.levelPlayer_playerAttribute_base_btn_active = True  # 改为选中状态
                self.levelPlayer_playerAttribute_base_btn_choose = i  # 选中编号
                if self.mouse_pressed[0] and self.levelPlayer_cushion_active:  # 如果点击左键同时缓冲好
                    self.levelPlayer_cushion_active = False
                    self.btnClick()  # 播放点击音效
                    self.levelPlayerAddAttributeValue(self.levelPlayer_playerAttribute_base_btn_choose)  # 升级属性操作
                break  # 退出循环
            else:
                self.levelPlayer_playerAttribute_base_btn_active = False  # 改为未选中状态
                self.levelPlayer_playerAttribute_base_btn_choose = -1
        # 被动按钮选中判断
        for i in range(len(self.levelPlayer_playerAttribute_passive)):
            if self.levelPlayer_attribute_passive_btn_pos[i][0] < self.mouse_position[0] < (
                self.levelPlayer_attribute_passive_btn_pos[i][0] + self.levelPlayer_playerAttribute_btnUp_rect[2]) \
                and \
                self.levelPlayer_attribute_passive_btn_pos[i][1] < self.mouse_position[1] < (
                self.levelPlayer_attribute_passive_btn_pos[i][1] + self.levelPlayer_playerAttribute_btnUp_rect[3]):  # 选中
                self.levelPlayer_playerAttribute_passive_btn_active = True  # 改为选中状态
                self.levelPlayer_playerAttribute_passive_btn_choose = i  # 选中编号
                if self.mouse_pressed[0] and self.levelPlayer_cushion_active:  # 如果点击左键同时缓冲好
                    self.levelPlayer_cushion_active = False
                    self.btnClick()  # 播放点击音效
                    self.levelPlayerAddAttributeValue(self.levelPlayer_playerAttribute_passive_btn_choose)  # 升级属性操作
                break  # 退出循环
            else:
                self.levelPlayer_playerAttribute_passive_btn_active = False  # 改为未选中状态
                self.levelPlayer_playerAttribute_passive_btn_choose = -1
        # 攻击按钮选中判断
        for i in range(len(self.levelPlayer_playerAttribute_attack)):
            if self.levelPlayer_attribute_attack_btn_pos[i][0] < self.mouse_position[0] < (
                self.levelPlayer_attribute_attack_btn_pos[i][0] + self.levelPlayer_playerAttribute_btnUp_rect[2]) \
                and \
                self.levelPlayer_attribute_attack_btn_pos[i][1] < self.mouse_position[1] < (
                self.levelPlayer_attribute_attack_btn_pos[i][1] + self.levelPlayer_playerAttribute_btnUp_rect[3]):  # 选中
                self.levelPlayer_playerAttribute_attack_btn_active = True  # 改为选中状态
                self.levelPlayer_playerAttribute_attack_btn_choose = i  # 选中编号
                if self.mouse_pressed[0] and self.levelPlayer_cushion_active:  # 如果点击左键同时缓冲好
                    self.levelPlayer_cushion_active = False
                    self.btnClick()  # 播放点击音效
                    self.levelPlayerAddAttributeValue(self.levelPlayer_playerAttribute_attack_btn_choose)  # 升级属性操作
                break  # 退出循环
            else:
                self.levelPlayer_playerAttribute_attack_btn_active = False  # 改为未选中状态
                self.levelPlayer_playerAttribute_attack_btn_choose = -1

    def levelPlayerResetNameStr(self):
        """
        重置姓名字符串，从主界面进入该界面时调用
        :return: 无
        """
        self.levelPlayer_name_str = "输入你的名字"

    def levelPlayerAddAttributeValue(self, attributeID):
        """
        给属性增加值，升级属性的绑定事件
        :param attributeID:传入选中按钮的id，根据id做出判断
        :return:无
        """
        if self.levelPlayer_playerAttribute_base_btn_active:  # 如果基础属性按钮状态为True
            if self.levelPlayer_playerAttributePoints["基础点数"] > 0:
                self.levelPlayer_playerAttribute_base[attributeID][1] += 1  # 该属性加1
                self.levelPlayer_playerAttributePoints["基础点数"] -= 1  # 点数池减1
        elif self.levelPlayer_playerAttribute_passive_btn_active:
            if self.levelPlayer_playerAttributePoints["被动点数"] > 0:
                self.levelPlayer_playerAttribute_passive[attributeID][1] += 1  # 该属性加1
                self.levelPlayer_playerAttributePoints["被动点数"] -= 1  # 点数池减1
        elif self.levelPlayer_playerAttribute_attack_btn_active:
            if self.levelPlayer_playerAttributePoints["武器点数"] > 0:
                self.levelPlayer_playerAttribute_attack[attributeID][1] += 1  # 该属性加1
                self.levelPlayer_playerAttributePoints["武器点数"] -= 1  # 点数池减1

    def levelPlayerCushion(self):
        """
        独属于levelPlayer层的鼠标缓冲
        :return:无
        """
        if not self.levelPlayer_cushion_active:  # 如果鼠标缓冲为False
            self.levelPlayer_cushion_time += 1  # 时间增量
            if self.levelPlayer_cushion_time == 15:  # 如果增到10则缓冲好
                self.levelPlayer_cushion_time = 0  # 归0
                self.levelPlayer_cushion_active = True  # 鼠标缓冲改为True

    def levelPlayerSaveGame(self):
        """
        保存游戏
        :return:无
        """
        saveTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # 格式化时间日期作为文件名使用
        with open(".\\saveFiles\\" + saveTime + ".csv", 'w+', encoding="UTF-8") as f:
            f.write("名字," + self.levelPlayer_name_str + '\n')  # 写入名字
            f.write("头像," + self.random_img + '\n')  # 写入头像图片
            for k, v in self.levelPlayer_playerAttributePoints.items():  # 取出所有的剩余点数写入
                f.write(k + ',' + str(v) + '\n')
            for i in self.levelPlayer_playerAttribute_base:  # 循环字典里面的所有项目取出保存
                f.write(i[0] + ', ' + str(i[1]) + '\n')  # 写入数据
            for i in self.levelPlayer_playerAttribute_passive:
                f.write(i[0] + ', ' + str(i[1]) + '\n')
            for i in self.levelPlayer_playerAttribute_attack:
                f.write(i[0] + ', ' + str(i[1]) + '\n')