# --coding=utf-8
import pygame
# 游戏文件
from module.button_position import button_position
from setting import config

class level_setting:
    def levelSettingElement(self):
        """
        游戏设置界面的元素
        :return:无
        """
        # 当前页面
        self.IS_SETTING_PAGE = False
        # 所需变量
        self.levelSettingSomeVariable()
        # 设置背景板
        self.levelSetting_bgBox = pygame.image.load(".\\module\\image\\box_11.png").convert_alpha()
        self.levelSetting_bgBox.set_alpha(225)
        self.levelSetting_bgBox_rect = self.levelSetting_bgBox.get_rect()
        self.levelSetting_bgBox_rect.center = (self.SIZE[0] / 2, self.SIZE[1] / 2)
        # 测试遮罩(用完删!!!)
        self.levelSetting_test = pygame.Surface((self.levelSetting_bgBox_rect[2], self.levelSetting_bgBox_rect[3])).convert_alpha()
        self.levelSetting_test.fill((255, 0, 0))
        self.levelSetting_test.set_alpha(200)
        # 返回主界面按钮
        self.levelSettingBackBtnElement()
        # 三个选项页元素
        self.levelSettingDisplayPageElement()
        self.levelSettingAudioPageElement()
        self.levelSettingOtherPageElement()

    def levelSettingRender(self):
        """
        游戏设置界面的渲染
        :return:无
        """
        # 实时创建背景
        self.levelSetting_bg = pygame.image.load(".\\media\\image\\background_3.jpg").convert()  # 背景
        self.levelSetting_bg = pygame.transform.scale(self.levelSetting_bg, self.SIZE)  # 设置大小
        # 测试遮罩
        # self.levelSetting_bg.blit(self.levelSetting_test, self.levelSetting_bgBox_rect)
        # 背景板
        self.levelSetting_bg.blit(self.levelSetting_bgBox, self.levelSetting_bgBox_rect)
        # 返回按钮
        self.levelSettingBackBtnRender()
        # 选项页渲染
        self.levelSettingDisplayPageRender()
        self.levelSettingAudioPageRender()
        self.levelSettingOtherPageRender()
        # 渲染背景
        self.screen.blit(self.levelSetting_bg, (0, 0))  # 渲染背景

    def levelSettingEvent(self):
        """
        游戏设置界面的事件
        :return:无
        """
        # 判断esc退出界面事件
        for event in self.keys_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameSettingPageBackMainPage()
        # 判断返回按钮事件
        self.levelSettingBackBtnEvent()
        # 选项页事件
        self.levelSettingDisplayPageEvent()
        self.levelSettingAudioPageEvent()
        self.levelSettingOtherPageEvent()

    def levelSettingSomeVariable(self):
        """
        一些变量
        :return:无
        """
        self.levelSetting_averageX = 1200 / 3  # x平均值
        self.levelSetting_font_1 = pygame.font.Font(config["BASE_FONT_PATH"], 100)  # 私有字体1
        self.levelSetting_font_2 = pygame.font.Font(config["BASE_FONT_PATH"], 20)  # 私有字体2
        self.levelSetting_font_3 = pygame.font.Font(config["BASE_FONT_PATH"], 15)  # 私有字体3

    def levelSettingBackBtnElement(self):
        """
        返回主界面按钮
        :return:无
        """
        # 文本对象
        self.levelSetting_backMainPage_font = self.BASE_FONT.render("返回主界面", True, self.FONT_DEFAULT_COLOR, None)
        self.levelSetting_backMainPage_font_rect = self.levelSetting_backMainPage_font.get_rect()
        self.levelSetting_backMainPage_active = self.BASE_FONT.render("返回主界面", True, self.FONT_ACTIVE_COLOR, None)
        # 设置坐标
        self.levelSetting_backMainPage_font_rect[0], self.levelSetting_backMainPage_font_rect[1] = button_position["author_page_back_main_page_btn"]
        # 变量
        self.levelSetting_backMainPage_choose = False  # 选中状态

    def levelSettingBackBtnRender(self):
        """
        返回主界面按钮
        :return:无
        """
        # 渲染文本
        self.levelSetting_bg.blit(self.levelSetting_backMainPage_font, self.levelSetting_backMainPage_font_rect)
        if self.levelSetting_backMainPage_choose:  # 如果选中就渲染选中状态
            self.levelSetting_bg.blit(self.levelSetting_backMainPage_active, self.levelSetting_backMainPage_font_rect)

    def levelSettingBackBtnEvent(self):
        """
        返回主界面按钮
        :return:无
        """
        if self.levelSetting_backMainPage_font_rect[0] < self.mouse_position[0] < (
            self.levelSetting_backMainPage_font_rect[0] + self.levelSetting_backMainPage_font_rect[2]) \
            and \
            self.levelSetting_backMainPage_font_rect[1] < self.mouse_position[1] < (
            self.levelSetting_backMainPage_font_rect[1] + self.levelSetting_backMainPage_font_rect[3]):  # 如果位于按钮上
            self.levelSetting_backMainPage_choose = True  # 选中状态改为True
            if self.mouse_pressed[0] and self.cushion_active:  # 点击并缓冲好
                self.cushion_active = False  # 缓冲状态改为False
                self.btnClick()  # 播放点击音效
                self.gameSettingPageBackMainPage()  # 返回主界面事件触发
        else:
            self.levelSetting_backMainPage_choose = False

    def levelSettingDisplayPageElement(self):
        """
        显示选项页
        :return:无
        """
        # 变量
        self.is_levelSetting_displayPage = True  # 规定当前是否选中此页面
        # 创建显示选项页
        self.levelSetting_displayPage_btn = pygame.image.load(".\\module\\image\\box_12.png").convert_alpha()  # 载入图片
        self.levelSetting_displayPage_btn = pygame.transform.scale(self.levelSetting_displayPage_btn, (self.levelSetting_averageX, 50))  # 设置大小
        self.levelSetting_displayPage_btn.set_alpha(225)  # 设置透明度
        self.levelSetting_displayPage_btn_rect = self.levelSetting_displayPage_btn.get_rect()  # 获取rect
        self.levelSetting_displayPage_btn_rect.left = self.levelSetting_bgBox_rect.left  # 设置left
        self.levelSetting_displayPage_btn_rect.top = self.levelSetting_bgBox_rect.top  # 设置top
        # 创建显示选项页文本
        self.levelSetting_displayPage_font = self.BASE_FONT.render("显示", True, self.FONT_DEFAULT_COLOR, None)  # 创建字体
        self.levelSetting_displayPage_font_rect = self.levelSetting_displayPage_font.get_rect()  # 获取rect
        self.levelSetting_displayPage_font_rect.center = (self.levelSetting_displayPage_btn_rect[2] / 2,
                                                          self.levelSetting_displayPage_btn_rect[3] / 2)  # 设置坐标
        self.levelSetting_displayPage_font_rect[1] -= 3  # 微调
        # 背景板提示文本
        self.levelSetting_displayPage_tips = self.levelSetting_font_1.render("显示选项页(暂无选项)", True, (255, 255, 255), None).convert_alpha()  # 白色字体
        self.levelSetting_displayPage_tips.set_alpha(125)  # 设置透明度
        self.levelSetting_displayPage_tips_rect = self.levelSetting_displayPage_tips.get_rect()  # 获取rect
        self.levelSetting_displayPage_tips_rect.center = (self.SIZE[0] / 2, self.SIZE[1] / 2)  # 设置居中
        # 直接渲染(因为该字体没有其他功能，所以直接绘制，后面不重复渲染)
        self.levelSetting_displayPage_btn.blit(self.levelSetting_displayPage_font, self.levelSetting_displayPage_font_rect)

    def levelSettingDisplayPageRender(self):
        """
        显示选项页渲染
        :return:无
        """
        # 渲染显示选项页
        self.levelSetting_bg.blit(self.levelSetting_displayPage_btn, self.levelSetting_displayPage_btn_rect)
        # 如果当前页为选中状态则渲染提示文本
        if self.is_levelSetting_displayPage:
            self.levelSetting_bg.blit(self.levelSetting_displayPage_tips, self.levelSetting_displayPage_tips_rect)

    def levelSettingDisplayPageEvent(self):
        """
        显示选项页事件
        :return:无
        """
        if self.levelSetting_displayPage_btn_rect[0] < self.mouse_position[0] < (
            self.levelSetting_displayPage_btn_rect[0] + self.levelSetting_displayPage_btn_rect[2]) \
            and \
            self.levelSetting_displayPage_btn_rect[1] < self.mouse_position[1] < (
            self.levelSetting_displayPage_btn_rect[1] + self.levelSetting_displayPage_btn_rect[3]) \
            and \
            self.mouse_pressed[0] and self.cushion_active:  # 如果鼠标点击选项页按钮
            self.cushion_active = False  # 鼠标缓冲改为False
            self.btnClick()  # 播放点击音效
            self.is_levelSetting_displayPage = True  # 显示选项页改为True
            self.is_levelSetting_audioPage = False  # 声音选项页改为False
            self.is_levelSetting_otherPage = False  # 其他选项页改为False
        if self.is_levelSetting_displayPage:
            self.levelSetting_displayPage_btn.set_alpha(225)  # 设置显示选项页透明度为225
            self.levelSetting_audioPage_btn.set_alpha(125)  # 设置声音选项页透明度为125
            self.levelSetting_otherPage_btn.set_alpha(125)  # 设置其他选项页透明度为125

    def levelSettingAudioPageElement(self):
        """
        声音选项页
        :return:无
        """
        # 变量
        self.is_levelSetting_audioPage = False  # 规定当前是否选中此页面
        # 创建显示选项页
        self.levelSetting_audioPage_btn = pygame.image.load(".\\module\\image\\box_12.png").convert_alpha()  #载入图片
        self.levelSetting_audioPage_btn = pygame.transform.scale(self.levelSetting_audioPage_btn, (self.levelSetting_averageX, 50))  # 设置大小
        self.levelSetting_audioPage_btn.set_alpha(225)  #设置透明度
        self.levelSetting_audioPage_btn_rect = self.levelSetting_audioPage_btn.get_rect()  # 获取rect
        self.levelSetting_audioPage_btn_rect.left = self.levelSetting_bgBox_rect.left + self.levelSetting_displayPage_btn_rect[2]  # 设置left
        self.levelSetting_audioPage_btn_rect.top = self.levelSetting_bgBox_rect.top  # 设置top
        # 创建显示选项页文本
        self.levelSetting_audioPage_font = self.BASE_FONT.render("声音", True, self.FONT_DEFAULT_COLOR, None)  # 创建字体
        self.levelSetting_audioPage_font_rect = self.levelSetting_audioPage_font.get_rect()  # 获取rect
        self.levelSetting_audioPage_font_rect.center = (self.levelSetting_audioPage_btn_rect[2] / 2,
                                                        self.levelSetting_audioPage_btn_rect[3] / 2)  # 设置坐标
        self.levelSetting_audioPage_font_rect[1] -= 3  # 微调
        # 背景板提示文本
        self.levelSetting_audioPage_tips = self.levelSetting_font_1.render("声音选项页", True, (255, 255, 255), None).convert_alpha()  # 白色字体
        self.levelSetting_audioPage_tips.set_alpha(125)  # 设置透明度
        self.levelSetting_audioPage_tips_rect = self.levelSetting_audioPage_tips.get_rect()  # 获取rect
        self.levelSetting_audioPage_tips_rect.center = (self.SIZE[0] / 2, self.SIZE[1] / 2)  # 设置居中
        # 导入音量控制选项元素
        self.levelSettingVolumeCtrlElement()
        # 直接渲染(因为该字体没有其他功能，所以直接绘制，后面不重复渲染)
        self.levelSetting_audioPage_btn.blit(self.levelSetting_audioPage_font, self.levelSetting_audioPage_font_rect)

    def levelSettingAudioPageRender(self):
        """
        声音选项页渲染
        :return:无
        """
        # 渲染声音选项页
        self.levelSetting_bg.blit(self.levelSetting_audioPage_btn, self.levelSetting_audioPage_btn_rect)
        # 如果当前是声音选项页
        if self.is_levelSetting_audioPage:
            # 渲染提示文本
            self.levelSetting_bg.blit(self.levelSetting_audioPage_tips, self.levelSetting_audioPage_tips_rect)
            # 渲染音量控制选项
            self.levelSettingVolumeCtrlRender()

    def levelSettingAudioPageEvent(self):
        """
        声音选项页事件
        :return:无
        """
        if self.levelSetting_audioPage_btn_rect[0] < self.mouse_position[0] < (
            self.levelSetting_audioPage_btn_rect[0] + self.levelSetting_audioPage_btn_rect[2]) \
            and \
            self.levelSetting_audioPage_btn_rect[1] < self.mouse_position[1] < (
            self.levelSetting_audioPage_btn_rect[1] + self.levelSetting_audioPage_btn_rect[3]) \
            and \
            self.mouse_pressed[0] and self.cushion_active:  # 如果鼠标点击选项页按钮
            self.cushion_active = False  # 鼠标缓冲改为False
            self.btnClick()  # 播放点击音效
            self.is_levelSetting_displayPage = False  # 显示选项页改为False
            self.is_levelSetting_audioPage = True  # 声音选项页改为True
            self.is_levelSetting_otherPage = False  # 其他选项页改为False
        if self.is_levelSetting_audioPage:
            self.levelSetting_displayPage_btn.set_alpha(125)  # 设置显示选项页透明度为125
            self.levelSetting_audioPage_btn.set_alpha(225)  # 设置声音选项页透明度为225
            self.levelSetting_otherPage_btn.set_alpha(125)  # 设置其他选项页透明度为125
        # 音量控制选项的事件
        self.levelSettingVolumeCtrlEvent()

    def levelSettingOtherPageElement(self):
        """
        其它选项页
        :return:无
        """
        # 变量
        self.is_levelSetting_otherPage = False  # 规定当前是否选中此页面
        # 创建显示选项页
        self.levelSetting_otherPage_btn = pygame.image.load(".\\module\\image\\box_12.png").convert_alpha()  # 载入图片
        self.levelSetting_otherPage_btn = pygame.transform.scale(self.levelSetting_otherPage_btn,(self.levelSetting_averageX, 50))  # 设置大小
        self.levelSetting_otherPage_btn.set_alpha(225)  # 设置透明度
        self.levelSetting_otherPage_btn_rect = self.levelSetting_otherPage_btn.get_rect()  # 获取rect
        self.levelSetting_otherPage_btn_rect.left = self.levelSetting_bgBox_rect.left + \
                                                    self.levelSetting_displayPage_btn_rect[2] + \
                                                    self.levelSetting_audioPage_btn_rect[2]# 设置left
        self.levelSetting_otherPage_btn_rect.top = self.levelSetting_bgBox_rect.top  # 设置top
        # 创建显示选项页文本
        self.levelSetting_otherPage_font = self.BASE_FONT.render("其它", True, self.FONT_DEFAULT_COLOR, None)  # 创建字体
        self.levelSetting_otherPage_font_rect = self.levelSetting_otherPage_font.get_rect()  # 获取rect
        self.levelSetting_otherPage_font_rect.center = (self.levelSetting_otherPage_btn_rect[2] / 2,
                                                        self.levelSetting_otherPage_btn_rect[3] / 2)  # 设置坐标
        self.levelSetting_otherPage_font_rect[1] -= 3  # 微调
        # 背景板提示文本
        self.levelSetting_otherPage_tips = self.levelSetting_font_1.render("其它选项页(暂无选项)", True, (255, 255, 255), None).convert_alpha()  # 白色字体
        self.levelSetting_otherPage_tips.set_alpha(125)  # 设置透明度
        self.levelSetting_otherPage_tips_rect = self.levelSetting_otherPage_tips.get_rect()  # 获取rect
        self.levelSetting_otherPage_tips_rect.center = (self.SIZE[0] / 2, self.SIZE[1] / 2)  # 设置居中
        # 直接渲染(因为该字体没有其他功能，所以直接绘制，后面不重复渲染)
        self.levelSetting_otherPage_btn.blit(self.levelSetting_otherPage_font, self.levelSetting_otherPage_font_rect)

    def levelSettingOtherPageRender(self):
        """
        其它选项页渲染
        :return:无
        """
        # 渲染其他选项页
        self.levelSetting_bg.blit(self.levelSetting_otherPage_btn, self.levelSetting_otherPage_btn_rect)
        # 如果当前是其它选项页则渲染提示文本
        if self.is_levelSetting_otherPage:
            self.levelSetting_bg.blit(self.levelSetting_otherPage_tips, self.levelSetting_otherPage_tips_rect)

    def levelSettingOtherPageEvent(self):
        """
        其它选项页事件
        :return:无
        """
        if self.levelSetting_otherPage_btn_rect[0] < self.mouse_position[0] < (
            self.levelSetting_otherPage_btn_rect[0] + self.levelSetting_otherPage_btn_rect[2]) \
            and \
            self.levelSetting_otherPage_btn_rect[1] < self.mouse_position[1] < (
            self.levelSetting_otherPage_btn_rect[1] + self.levelSetting_otherPage_btn_rect[3]) \
            and \
            self.mouse_pressed[0] and self.cushion_active:  # 如果鼠标点击选项页按钮
            self.cushion_active = False  # 鼠标缓冲改为False
            self.btnClick()  # 播放点击音效
            self.is_levelSetting_displayPage = False  # 显示选项页改为False
            self.is_levelSetting_audioPage = False  # 声音选项页改为False
            self.is_levelSetting_otherPage = True  # 其他选项页改为True
        if self.is_levelSetting_otherPage:
            self.levelSetting_displayPage_btn.set_alpha(125)  # 设置显示选项页透明度为125
            self.levelSetting_audioPage_btn.set_alpha(125)  # 设置声音选项页透明度为125
            self.levelSetting_otherPage_btn.set_alpha(225)  # 设置其他选项页透明度为225

    def levelSettingVolumeCtrlElement(self):
        """
        音量控制选项的元素
        :return:无
        """
        # 变量
        self.levelSetting_volumeNumTips_active = False  # 默认不显示提示文本
        # 文本盒子
        self.levelSetting_volumeCtrl_box = pygame.image.load(".\\module\\image\\box_10.png").convert_alpha()  # 加载图片
        self.levelSetting_volumeCtrl_box = pygame.transform.scale(self.levelSetting_volumeCtrl_box, (200, 30))  # 设置大小
        self.levelSetting_volumeCtrl_box.set_alpha(225)  # 设置透明度
        self.levelSetting_volumeCtrl_box_rect = self.levelSetting_volumeCtrl_box.get_rect()  # 获取rect
        self.levelSetting_volumeCtrl_box_rect.left = self.levelSetting_bgBox_rect.left  # 设置left
        self.levelSetting_volumeCtrl_box_rect.top = self.levelSetting_bgBox_rect.top + self.levelSetting_audioPage_btn_rect[3]  # 设置top
        self.levelSetting_volumeCtrl_box_rect.left += 150  # 坐标微调
        # 文本
        self.levelSetting_volumeCtrl_font = self.levelSetting_font_2.render("音量调节", True, (0, 0, 0), None)  # 文本对象
        self.levelSetting_volumeCtrl_font_rect = self.levelSetting_volumeCtrl_font.get_rect()  # 获取rect
        self.levelSetting_volumeCtrl_font_rect.center = (self.levelSetting_volumeCtrl_box_rect[2] / 2,
                                                         self.levelSetting_volumeCtrl_box_rect[3] / 2)  # 设置居中
        # 进度条
            # 1.进度条长度
        self.levelSetting_volumeCtrl_progressBar_width = 600  # 长度设置为600
            # 2.加载图片
        self.levelSetting_volumeCtrl_progressBarUp = pygame.image.load(".\\module\\image\\progressBar_2.png").convert_alpha()
        self.levelSetting_volumeCtrl_progressBarDown = pygame.image.load(".\\module\\image\\progressBar_2.png").convert_alpha()
            # 3.设置大小
        self.levelSetting_volumeCtrl_progressBarUp = pygame.transform.scale(self.levelSetting_volumeCtrl_progressBarUp, (600, 20))
                # 3.1根据当前音量设置长度
        width = int(self.levelSetting_volumeCtrl_progressBar_width * pygame.mixer.music.get_volume())  # 音量进度条长度
        self.levelSetting_volumeCtrl_progressBarDown = pygame.transform.scale(self.levelSetting_volumeCtrl_progressBarDown, (width, 20))
            # 4.获取rect
        self.levelSetting_volumeCtrl_progressBarDown_rect = self.levelSetting_volumeCtrl_progressBarDown.get_rect()
        self.levelSetting_volumeCtrl_progressBarUp_rect = self.levelSetting_volumeCtrl_progressBarUp.get_rect()
            # 5.设置透明度
        self.levelSetting_volumeCtrl_progressBarUp.set_alpha(125)
        self.levelSetting_volumeCtrl_progressBarDown.set_alpha(200)
            # 6.设置坐标
        self.levelSetting_volumeCtrl_progressBar_pos = (450, 65)
            # 7.进度条小按钮
        self.levelSetting_volumeCtrl_progressBarBtn = pygame.image.load(".\\module\\image\\btn_1_small.png").convert_alpha()
            # 8.设置按钮大小和创建rect
        self.levelSetting_volumeCtrl_progressBarBtn = pygame.transform.scale(self.levelSetting_volumeCtrl_progressBarBtn, (30, 30))
        self.levelSetting_volumeCtrl_progressBarBtn_rect = self.levelSetting_volumeCtrl_progressBarBtn.get_rect()
            # 9.设置按钮坐标
        self.levelSetting_volumeCtrl_progressBarBtn_rect.left = (self.levelSetting_volumeCtrl_progressBar_pos[0] +   # 进度条的起始坐标
                                                                 self.levelSetting_volumeCtrl_progressBarDown_rect[2] -   # 进度条的长度
                                                                 (self.levelSetting_volumeCtrl_progressBarBtn_rect[2] / 2))  # 按钮本身的长度除以2
        self.levelSetting_volumeCtrl_progressBarBtn_rect.top = self.levelSetting_volumeCtrl_box_rect.top  # top设置为和文本盒子一样的top
        # 直接渲染文本
        self.levelSetting_volumeCtrl_box.blit(self.levelSetting_volumeCtrl_font, self.levelSetting_volumeCtrl_font_rect)

    def levelSettingVolumeCtrlRender(self):
        """
        音量控制选项的渲染
        :return:无
        """
        self.levelSetting_bg.blit(self.levelSetting_volumeCtrl_box, self.levelSetting_volumeCtrl_box_rect)  # 渲染文本盒子
        self.levelSetting_bg.blit(self.levelSetting_volumeCtrl_progressBarUp, self.levelSetting_volumeCtrl_progressBar_pos)  # 渲染底层进度条
        self.levelSetting_bg.blit(self.levelSetting_volumeCtrl_progressBarDown, self.levelSetting_volumeCtrl_progressBar_pos)  # 渲染上层进度条
        self.levelSetting_bg.blit(self.levelSetting_volumeCtrl_progressBarBtn, self.levelSetting_volumeCtrl_progressBarBtn_rect)  # 渲染进度条按钮
        if self.levelSetting_volumeNumTips_active:  # 渲染音量数字提示
            self.levelSetting_bg.blit(self.levelSetting_volumeNumTips_box, self.mouse_position)  # 在鼠标位置绘制提示面板

    def levelSettingVolumeCtrlEvent(self):
        """
        音量控制选项的事件
        :return:无
        """
        if self.levelSetting_volumeCtrl_progressBar_pos[0] < self.mouse_position[0] < (
            self.levelSetting_volumeCtrl_progressBar_pos[0] + self.levelSetting_volumeCtrl_progressBarUp_rect[2]) \
            and \
            self.levelSetting_volumeCtrl_progressBar_pos[1] < self.mouse_position[1] < (
            self.levelSetting_volumeCtrl_progressBar_pos[1] + self.levelSetting_volumeCtrl_progressBarUp_rect[3]):  # 如果鼠标位于进度条上方
            self.levelSetting_volumeNumTips_active = True  # 音量提示改为True
            # 提示文本盒子和文本
            self.levelSetting_volumeNumTips_box = pygame.image.load(".\\module\\image\\box_2.jpg").convert()
            self.levelSetting_volumeNumTips_box = pygame.transform.scale(self.levelSetting_volumeNumTips_box, (30, 50))  # 设置大小
            self.levelSetting_volumeNumTips_box = pygame.transform.rotate(self.levelSetting_volumeNumTips_box, 90)  # 旋转90度
            self.levelSetting_volumeNumTips_font = self.levelSetting_font_3.render(str(round(pygame.mixer.music.get_volume(), 2)), True, (0, 0, 0), None)  # 创建音量数字文本
            self.levelSetting_volumeNumTips_font_rect = self.levelSetting_volumeNumTips_font.get_rect()  # 获取rect
            self.levelSetting_volumeNumTips_font_rect.center = (25, 15)
            # 直接渲染
            self.levelSetting_volumeNumTips_box.blit(self.levelSetting_volumeNumTips_font, self.levelSetting_volumeNumTips_font_rect)
            # 点击进度条
            if self.mouse_pressed[0] and self.cushion_active:  # 如果鼠标位于进度条上方并且点击进度条
                self.cushion_active = False  # 重置按钮缓冲
                mouse_x = self.mouse_position[0] - self.levelSetting_volumeCtrl_progressBar_pos[0]  # 获取并计算鼠标在进度条上方的x位置
                if mouse_x >= 300:  # 如果坐标达到了进度条左边
                    volume_set = 1 - round((600 - mouse_x) / 600, 2)  # 此处的数字常量600是进度条的长度，因为如果使用变量名的话代码就太长了，所以这样写，理解一下
                elif mouse_x < 300:  # 如果坐标达到了进度条右边
                    volume_set = 1 - round((600 - mouse_x) / 600, 2)
                # 算法:长度600减去鼠标在进度条上的位置，然后除以总长度600，就得出了应该设置的音量比例，直接通过set_volume()方法设置就行了
                # 播放点击音效并设置音量
                self.btnClick()
                pygame.mixer.music.set_volume(volume_set)
                # 创建一个新的上层进度条长度
                self.levelSetting_volumeCtrl_progressBarDown = pygame.image.load(".\\module\\image\\progressBar_2.png").convert_alpha()
                self.levelSetting_volumeCtrl_progressBarDown.set_alpha(200)
                self.levelSetting_volumeCtrl_progressBarDown = pygame.transform.scale(self.levelSetting_volumeCtrl_progressBarDown, (mouse_x, 20))
                self.levelSetting_volumeCtrl_progressBarDown_rect = self.levelSetting_volumeCtrl_progressBarDown.get_rect()  # 获取rect
                # 设置按钮的坐标
                self.levelSetting_volumeCtrl_progressBarBtn_rect.left = (self.levelSetting_volumeCtrl_progressBar_pos[0] +  # 进度条的起始坐标
                                                                         self.levelSetting_volumeCtrl_progressBarDown_rect[2] -  # 进度条的长度
                                                                         (self.levelSetting_volumeCtrl_progressBarBtn_rect[2] / 2))  # 按钮本身的长度除以2
        else:
            self.levelSetting_volumeNumTips_active = False