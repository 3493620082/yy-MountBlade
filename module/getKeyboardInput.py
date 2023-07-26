# --coding=utf-8
# import pygame
from pygame.locals import *

class getKeyboardInput:
    def getKeyboardInput(self, input_str):
        """
        此函数用于检测键盘输入的所有字符，并组成字符串，旨在模拟输入框的功能
        :return:当前输入的字符
        """
        if (self.keys_mods & KMOD_LSHIFT) or (self.keys_mods & KMOD_RSHIFT):  # 如果按下了左或右shift键就返回大写字母
            for event in self.keys_list:
                if event.type == KEYDOWN:
                    # 英文字母
                    if event.key == K_q:
                        return input_str + 'Q'
                    elif event.key == K_w:
                        return input_str + 'W'
                    elif event.key == K_e:
                        return input_str + 'E'
                    elif event.key == K_r:
                        return input_str + 'R'
                    elif event.key == K_t:
                        return input_str + 'T'
                    elif event.key == K_y:
                        return input_str + 'Y'
                    elif event.key == K_u:
                        return input_str + 'U'
                    elif event.key == K_i:
                        return input_str + 'I'
                    elif event.key == K_o:
                        return input_str + 'O'
                    elif event.key == K_p:
                        return input_str + 'P'
                    elif event.key == K_a:
                        return input_str + 'A'
                    elif event.key == K_s:
                        return input_str + 'S'
                    elif event.key == K_d:
                        return input_str + 'D'
                    elif event.key == K_f:
                        return input_str + 'F'
                    elif event.key == K_g:
                        return input_str + 'G'
                    elif event.key == K_h:
                        return input_str + 'H'
                    elif event.key == K_j:
                        return input_str + 'J'
                    elif event.key == K_k:
                        return input_str + 'K'
                    elif event.key == K_l:
                        return input_str + 'L'
                    elif event.key == K_z:
                        return input_str + 'Z'
                    elif event.key == K_x:
                        return input_str + 'X'
                    elif event.key == K_c:
                        return input_str + 'C'
                    elif event.key == K_v:
                        return input_str + 'V'
                    elif event.key == K_b:
                        return input_str + 'B'
                    elif event.key == K_n:
                        return input_str + 'N'
                    elif event.key == K_m:
                        return input_str + 'M'
                    # 一些标点符号
                    elif event.key == K_1:
                        return input_str + '！'
                    elif event.key == K_2:
                        return input_str + '@'
                    elif event.key == K_3:
                        return input_str + '#'
                    elif event.key == K_4:
                        return input_str + '$'
                    elif event.key == K_5:
                        return input_str + '%'
                    elif event.key == K_6:
                        return input_str + '^'
                    elif event.key == K_7:
                        return input_str + '&'
                    elif event.key == K_8:
                        return input_str + '*'
                    elif event.key == K_9:
                        return input_str + '('
                    elif event.key == K_0:
                        return input_str + ')'
                    elif event.key == K_MINUS:  # 下划线_
                        return input_str + '_'
                    elif event.key == K_EQUALS:  # 加号+
                        return input_str + '+'
        elif self.keys_mods & KMOD_CAPS:  # 按下大写键
            for event in self.keys_list:
                if event.type == KEYDOWN:
                    # 英文字母
                    if event.key == K_q:
                        return input_str + 'Q'
                    elif event.key == K_w:
                        return input_str + 'W'
                    elif event.key == K_e:
                        return input_str + 'E'
                    elif event.key == K_r:
                        return input_str + 'R'
                    elif event.key == K_t:
                        return input_str + 'T'
                    elif event.key == K_y:
                        return input_str + 'Y'
                    elif event.key == K_u:
                        return input_str + 'U'
                    elif event.key == K_i:
                        return input_str + 'I'
                    elif event.key == K_o:
                        return input_str + 'O'
                    elif event.key == K_p:
                        return input_str + 'P'
                    elif event.key == K_a:
                        return input_str + 'A'
                    elif event.key == K_s:
                        return input_str + 'S'
                    elif event.key == K_d:
                        return input_str + 'D'
                    elif event.key == K_f:
                        return input_str + 'F'
                    elif event.key == K_g:
                        return input_str + 'G'
                    elif event.key == K_h:
                        return input_str + 'H'
                    elif event.key == K_j:
                        return input_str + 'J'
                    elif event.key == K_k:
                        return input_str + 'K'
                    elif event.key == K_l:
                        return input_str + 'L'
                    elif event.key == K_z:
                        return input_str + 'Z'
                    elif event.key == K_x:
                        return input_str + 'X'
                    elif event.key == K_c:
                        return input_str + 'C'
                    elif event.key == K_v:
                        return input_str + 'V'
                    elif event.key == K_b:
                        return input_str + 'B'
                    elif event.key == K_n:
                        return input_str + 'N'
                    elif event.key == K_m:
                        return input_str + 'M'
        else:  # 如果没有按下组合键
            for event in self.keys_list:  # 循环所有的事件
                if event.type == KEYDOWN:  # 如果按下了键盘
                    # 小写字母
                    if event.key == K_q:  # 按下了q键
                        return input_str + 'q'
                    elif event.key == K_w:  # 按下了w键
                        return input_str + 'w'
                    elif event.key == K_e:
                        return input_str + 'e'
                    elif event.key == K_r:
                        return input_str + 'r'
                    elif event.key == K_t:
                        return input_str + 't'
                    elif event.key == K_y:
                        return input_str + 'y'
                    elif event.key == K_u:
                        return input_str + 'u'
                    elif event.key == K_i:
                        return input_str + 'i'
                    elif event.key == K_o:
                        return input_str + 'o'
                    elif event.key == K_p:
                        return input_str + 'p'
                    elif event.key == K_a:
                        return input_str + 'a'
                    elif event.key == K_s:
                        return input_str + 's'
                    elif event.key == K_d:
                        return input_str + 'd'
                    elif event.key == K_f:
                        return input_str + 'f'
                    elif event.key == K_g:
                        return input_str + 'g'
                    elif event.key == K_h:
                        return input_str + 'h'
                    elif event.key == K_j:
                        return input_str + 'j'
                    elif event.key == K_k:
                        return input_str + 'k'
                    elif event.key == K_l:
                        return input_str + 'l'
                    elif event.key == K_z:
                        return input_str + 'z'
                    elif event.key == K_x:
                        return input_str + 'x'
                    elif event.key == K_c:
                        return input_str + 'c'
                    elif event.key == K_v:
                        return input_str + 'v'
                    elif event.key == K_b:
                        return input_str + 'b'
                    elif event.key == K_n:
                        return input_str + 'n'
                    elif event.key == K_m:
                        return input_str + 'm'
                    # 小键盘数字
                    elif event.key == K_KP0:
                        return input_str + '0'
                    elif event.key == K_KP1:
                        return input_str + '1'
                    elif event.key == K_KP2:
                        return input_str + '2'
                    elif event.key == K_KP3:
                        return input_str + '3'
                    elif event.key == K_KP4:
                        return input_str + '4'
                    elif event.key == K_KP5:
                        return input_str + '5'
                    elif event.key == K_KP6:
                        return input_str + '6'
                    elif event.key == K_KP7:
                        return input_str + '7'
                    elif event.key == K_KP8:
                        return input_str + '8'
                    elif event.key == K_KP9:
                        return input_str + '9'
                    # 数字(非小键盘)
                    elif event.key == K_0:
                        return input_str + '0'
                    elif event.key == K_1:
                        return input_str + '1'
                    elif event.key == K_2:
                        return input_str + '2'
                    elif event.key == K_3:
                        return input_str + '3'
                    elif event.key == K_4:
                        return input_str + '4'
                    elif event.key == K_5:
                        return input_str + '5'
                    elif event.key == K_6:
                        return input_str + '6'
                    elif event.key == K_7:
                        return input_str + '7'
                    elif event.key == K_8:
                        return input_str + '8'
                    elif event.key == K_9:
                        return input_str + '9'
                    # 一些标点符号
                    elif event.key == K_MINUS:  # 减号-
                        return input_str + '-'
                    elif event.key == K_EQUALS:  # 等号=
                        return input_str + '='
                    # 其他按键
                    elif event.key == K_SPACE:  # 如果按下空格
                        return input_str + ' '
                    elif event.key == K_BACKSPACE:  # 如果按下回退
                        return input_str[0:-1]
                    elif event.key == K_RETURN:  # 回车键
                        pass
        return input_str  # 如果没有任何事件相应则返回空字符
