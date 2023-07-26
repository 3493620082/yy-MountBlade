# --coding=utf-8
import csv
import pygame

class level_01:
    def level01Element(self):
        # 背景板
        self.level01_bg = pygame.image.load(".\\module\\image\\box_2.jpg").convert()
        self.level01_bg = pygame.transform.scale(self.level01_bg, self.SIZE)
        # npc背景板
        self.level01_npc_box = pygame.image.load(".\\module\\image\\box_1.png").convert_alpha()
        self.level01_npc_box = pygame.transform.scale(self.level01_npc_box, self.npc_box_size)
        # npc头像
        self.level01_npc_img = pygame.image.load(".\\media\\npc_image\\MartinVinnie.jpg").convert()
        self.level01_npc_img = pygame.transform.scale(self.level01_npc_img, self.npc_img_size)
        # 对话框背景板
        self.level01_talk_box = pygame.image.load(".\\module\\image\\box_2.jpg").convert()
        self.level01_talk_box = pygame.transform.scale(self.level01_talk_box, self.talk_box_size)
        self.level01_talk_box_rect = self.level01_talk_box.get_rect()
        # 读取npc信息
        self.level01_npcInfo_file = csv.reader(open(".\\media\\npc_info\\MartinVinnie.csv", 'r', encoding="UTF-8"))
        self.level01_npcInfo_list = []
        for l in self.level01_npcInfo_file:
            self.level01_npcInfo_list.append(l)
        # 创建姓名对象
        self.level01_npc_name = self.level_font_01.render(self.level01_npcInfo_list[0][1] + " :", True, (0, 0, 0), None)
        self.level01_talk_box.blit(self.level01_npc_name, self.npc_name_pos)  # 同时将姓名也渲染到背景板上去
        # 对话信息
        self.level01_npc_word_01 = self.level_font_01.render("认识你很高兴，这位先生", True, (0, 0, 0), None)
        self.level01_npc_word_01_rect = self.level01_npc_word_01.get_rect()
        self.level01_npc_word_01_rect.center = (self.level01_talk_box_rect[2] / 2, self.level01_talk_box_rect[3] / 2)
        self.level01_talk_box.blit(self.level01_npc_word_01, self.level01_npc_word_01_rect)
        # 选项框背景板
        self.level01_options_box = pygame.image.load(".\\module\\image\\box_4.jpg").convert()
        self.level01_options_box = pygame.transform.scale(self.level01_options_box, self.options_box_size)
        # 选项背景板
        self.level01_options_img = pygame.image.load(".\\module\\image\\box_6.png").convert_alpha()
        self.level01_options_img = pygame.transform.scale(self.level01_options_img, self.options_btn_size)

    def level01Render(self):
        # 将npc背景板和头像渲染
        self.level01_npc_box.blit(self.level01_npc_img, self.npc_img_pos)
        self.level01_bg.blit(self.level01_npc_box, (0, 0))
        # 将对话框渲染
        self.level01_bg.blit(self.level01_talk_box, (self.npc_box_size[0], 0))
        # 将选项框渲染
        # for i in range(3):
        #     self.level01_options_box.blit(self.level01_options_img, (0, 50 * i))
        self.level01_bg.blit(self.level01_options_box, (0, self.npc_box_size[1]))
        # 将这一层的背景渲染到self.screen上
        self.screen.blit(self.level01_bg, (0, 0))

    def level01Event(self):
        pass