# --coding=utf-8
# 游戏文件
import pygame.font

from setting import config
from media.level.level_01 import level_01
from media.level.level_02 import level_02
from media.level.level_player import level_player
from media.level.level_end import level_end
from media.level.level_load import level_load
from media.level.level_setting import level_setting

class LoadLevel(level_01, level_02, level_player, level_end, level_load, level_setting):
    def LoadLevelInit(self):
        pygame.font.init()
        # 一些公用的设置
        self.npc_box_size = config["npc_box_size"]
        self.npc_img_size = config["npc_img_size"]
        self.talk_box_size = config["talk_box_size"]
        self.options_box_size = config["options_box_size"]
        self.options_btn_size = config["options_btn_size"]
        self.npc_img_pos = ((self.npc_box_size[0] - self.npc_img_size[0]) / 2, (self.npc_box_size[1] - self.npc_img_size[1]) / 2)
        self.npc_name_pos = (10, 10)
        self.level_font_01 = pygame.font.Font(config["BASE_FONT_PATH"], 25)
        # self.level_font_01 = pygame.font.SysFont("华文楷体", 25)