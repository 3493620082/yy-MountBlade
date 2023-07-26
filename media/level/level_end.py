# --coding=utf-8
import pygame
from setting import config

class level_end:
    def levelEndElement(self):
        """
        界面元素
        """
        self.IS_END_PAGE = False  # 是否在结束界面
        self.levelEnd_font_1 = pygame.font.Font(config["BASE_FONT_PATH"], 50)
        # self.levelEnd_font_1 = pygame.font.SysFont("华文楷体", 50)  # 创建字体
        self.levelEnd_font_2 = pygame.font.SysFont("microsoftyahei", 20)  # 创建字体
        self.levelEnd_bgMask = pygame.Surface(self.SIZE).convert_alpha()  # 创建遮罩
        self.levelEnd_bgMask.fill((0, 0, 0))
        self.levelEnd_bgMask.set_alpha(100)
        self.levelEnd_bgMask_rect = self.levelEnd_bgMask.get_rect()  # 获取rect
        self.levelEnd_bgMask_font_line_01 = self.levelEnd_font_1.render("非常感谢您的使用", True, (255, 255, 255), None)  # 行01
        self.levelEnd_bgMask_font_line_02 = self.levelEnd_font_1.render("因为游戏支持库的原因", True, (255, 255, 255), None)  # 行02
        self.levelEnd_bgMask_font_line_03 = self.levelEnd_font_1.render("本游戏已经不再适合制作后续流程", True, (255, 255, 255), None)  # 行03
        self.levelEnd_bgMask_font_line_04 = self.levelEnd_font_1.render("非常抱歉", True, (255, 255, 255), None)  # 行04
        self.levelEnd_bgMask_font_line_05 = self.levelEnd_font_2.render("点击任意处退出", True, (0, 255, 0), None)  # 行05
        self.levelEnd_bgMask_font_line_06 = self.levelEnd_font_1.render("本游戏代码是免费且带注释的", True, (255, 255, 255), None)  # 行06
        self.levelEnd_bgMask_font_line_07 = self.levelEnd_font_1.render("本人技术有限，制作不易，谢谢您的游玩", True, (255, 255, 255), None)  # 行07
        self.levelEnd_bgMask_font_line_rect_01 = self.levelEnd_bgMask_font_line_01.get_rect()
        self.levelEnd_bgMask_font_line_rect_02 = self.levelEnd_bgMask_font_line_02.get_rect()
        self.levelEnd_bgMask_font_line_rect_03 = self.levelEnd_bgMask_font_line_03.get_rect()
        self.levelEnd_bgMask_font_line_rect_04 = self.levelEnd_bgMask_font_line_04.get_rect()
        self.levelEnd_bgMask_font_line_rect_05 = self.levelEnd_bgMask_font_line_05.get_rect()
        self.levelEnd_bgMask_font_line_rect_06 = self.levelEnd_bgMask_font_line_06.get_rect()
        self.levelEnd_bgMask_font_line_rect_07 = self.levelEnd_bgMask_font_line_07.get_rect()
        self.levelEnd_bgMask_font_line_rect_01.centerx = self.SIZE[0] / 2
        self.levelEnd_bgMask_font_line_rect_02.centerx = self.SIZE[0] / 2
        self.levelEnd_bgMask_font_line_rect_03.centerx = self.SIZE[0] / 2
        self.levelEnd_bgMask_font_line_rect_04.centerx = self.SIZE[0] / 2
        self.levelEnd_bgMask_font_line_rect_05.centerx = self.SIZE[0] / 2
        self.levelEnd_bgMask_font_line_rect_06.centerx = self.SIZE[0] / 2
        self.levelEnd_bgMask_font_line_rect_07.centerx = self.SIZE[0] / 2
        # 高度66px，开始与228px
        self.levelEnd_bgMask_font_line_rect_01.top = 150
        self.levelEnd_bgMask_font_line_rect_02.top = 150 + self.levelEnd_bgMask_font_line_rect_02[3] * 1
        self.levelEnd_bgMask_font_line_rect_03.top = 150 + self.levelEnd_bgMask_font_line_rect_03[3] * 2
        self.levelEnd_bgMask_font_line_rect_04.top = 150 + self.levelEnd_bgMask_font_line_rect_04[3] * 3
        self.levelEnd_bgMask_font_line_rect_06.top = 150 + self.levelEnd_bgMask_font_line_rect_06[3] * 4
        self.levelEnd_bgMask_font_line_rect_07.top = 150 + self.levelEnd_bgMask_font_line_rect_07[3] * 5
        # 提前渲染文本
        self.levelEnd_bgMask.blit(self.levelEnd_bgMask_font_line_01, self.levelEnd_bgMask_font_line_rect_01)
        self.levelEnd_bgMask.blit(self.levelEnd_bgMask_font_line_02, self.levelEnd_bgMask_font_line_rect_02)
        self.levelEnd_bgMask.blit(self.levelEnd_bgMask_font_line_03, self.levelEnd_bgMask_font_line_rect_03)
        self.levelEnd_bgMask.blit(self.levelEnd_bgMask_font_line_04, self.levelEnd_bgMask_font_line_rect_04)
        self.levelEnd_bgMask.blit(self.levelEnd_bgMask_font_line_05, self.levelEnd_bgMask_font_line_rect_05)
        self.levelEnd_bgMask.blit(self.levelEnd_bgMask_font_line_06, self.levelEnd_bgMask_font_line_rect_06)
        self.levelEnd_bgMask.blit(self.levelEnd_bgMask_font_line_07, self.levelEnd_bgMask_font_line_rect_07)

    def levelEndRender(self):
        """
        元素渲染
        """
        # 实时创建背景板
        self.levelEnd_bg = pygame.image.load(".\\media\\image\\box_background_1.jpg").convert()  # 载入图片
        self.levelEnd_bg = pygame.transform.scale(self.levelEnd_bg, self.SIZE)  # 设置大小
        # 遮罩渲染
        self.levelEnd_bg.blit(self.levelEnd_bgMask, self.levelEnd_bgMask_rect)
        # 提示文本渲染
        self.levelEnd_bg.blit(self.levelEnd_bgMask_font_line_05, self.levelEnd_bgMask_font_line_rect_05)
        # 背景板
        self.screen.blit(self.levelEnd_bg, (0, 0))

    def levelEndEvent(self):
        """
        元素事件
        """
        if self.mouse_pressed[0] and self.cushion_active:  # 如果点击了任意处
            self.cushion_active = False
            self.quitGame()  # 退出游戏