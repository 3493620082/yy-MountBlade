# --coding=utf-8
import pygame
import sys

from module.getKeyboardInput import getKeyboardInput

class GameEventList(getKeyboardInput):
    """
    次类记录了游戏中的事件，游戏启动时会将该类作为主类的父类继承进去，游戏事件也就加载到主类中了
    """
    def btnClick(self):
        """
        此函数在按钮被点击的时候输出一个点击音效
        :return: 无
        """
        sound_path = ".\\media\\sound\\btn_click.mp3"
        self.btn_click_sound = pygame.mixer.Sound(sound_path)
        self.btn_click_sound.set_volume(0.1)
        self.btn_click_sound.play()

    def startNewGame(self):
        """
        此函数是主界面开始新历程的绑定事件
        :return: 无
        """
        self.IS_GAME_PAGE = True
        self.IS_MAIN_PAGE = False
        self.IS_AUTHORSLIST_PAGE = False
        self.IS_LOAD_PAGE = False
        self.IS_SETTING_PAGE = False
        self.levelPlayerResetNameStr()  # 执行重置玩家姓名的操作
        self.levelPlayerImageElement()  # 执行重新加载头像框的操作
        self.levelPlayerAttributeElement()  # 重新加载人物属性

    def goGameSettingPage(self):
        """
        去往游戏设置界面的事件
        :return:无
        """
        self.IS_SETTING_PAGE     = True
        self.IS_GAME_PAGE        = False
        self.IS_AUTHORSLIST_PAGE = False
        self.IS_MAIN_PAGE        = False
        self.IS_LOAD_PAGE        = False
        self.levelSettingDisplayPageElement()
        self.levelSettingAudioPageElement()
        self.levelSettingOtherPageElement()

    def gameSettingPageBackMainPage(self):
        """
        设置界面返回游戏界面事件
        :return:无
        """
        self.IS_MAIN_PAGE        = True
        self.IS_SETTING_PAGE     = False
        self.IS_GAME_PAGE        = False
        self.IS_AUTHORSLIST_PAGE = False
        self.IS_LOAD_PAGE        = False

    def goGameLoadPage(self):
        """
        去往读取存档界面的事件
        :return:无
        """
        self.IS_SETTING_PAGE     = False
        self.IS_GAME_PAGE        = False
        self.IS_AUTHORSLIST_PAGE = False
        self.IS_MAIN_PAGE        = False
        self.IS_LOAD_PAGE        = True
        # self.levelLoadSaveBoxElement()

    def gameLoadPageBackMainPage(self):
        """
        存档界面返回游戏界面事件
        :return:无
        """
        self.IS_MAIN_PAGE        = True
        self.IS_SETTING_PAGE     = False
        self.IS_GAME_PAGE        = False
        self.IS_AUTHORSLIST_PAGE = False
        self.IS_LOAD_PAGE        = False

    def quitGame(self):
        """
        此函数是主界面退出游戏按钮的绑定事件
        :return: 无
        """
        self.CONSOLE_LOG.close()  # 关闭日志文件
        pygame.quit()
        sys.exit()

    def musicStop(self):
        """
        此函数是主界面右下角停止音乐按钮的绑定事件
        :return: 无
        """
        if pygame.mixer.music.get_busy():  # 如果当前是播放状态才能停止
            pygame.mixer.music.pause()  # 暂停播放

    def musicKeep(self):
        """
        此函数是主界面右下角继续播放按钮的绑定事件
        :return: 无
        """
        if not pygame.mixer.music.get_busy():  # 如果当前为停止状态才能继续播放
            pygame.mixer.music.unpause()  # 播放音乐

    def musicNext(self):
        """
        此函数是主界面右下角下曲按钮的绑定事件
        :return: 无
        """
        self.main_page_music_now_id += 1
        if self.main_page_music_now_id <= self.main_page_music_file_num:
            self.main_page_music_file = ".\\media\\music\\" + self.main_page_music_file_list[self.main_page_music_now_id]
            # print("当前音乐: " + self.main_page_music_file_list[self.main_page_music_now_id])
            self.CONSOLE_LOG.write("当前音乐: " + self.main_page_music_file_list[self.main_page_music_now_id] + "\n")
            pygame.mixer.music.load(self.main_page_music_file)
            pygame.mixer.music.play(-1)
        else:
            self.main_page_music_now_id = -1
            self.musicNext()

    def musicLast(self):
        """
        此函数是主界面右下角下曲按钮的绑定事件
        :return: 无
        """
        self.main_page_music_now_id -= 1
        if self.main_page_music_now_id <= self.main_page_music_file_num:
            self.main_page_music_file = ".\\media\\music\\" + self.main_page_music_file_list[self.main_page_music_now_id]
            # print("当前音乐: " + self.main_page_music_file_list[self.main_page_music_now_id])
            self.CONSOLE_LOG.write("当前音乐: " + self.main_page_music_file_list[self.main_page_music_now_id] + "\n")
            pygame.mixer.music.load(self.main_page_music_file)
            pygame.mixer.music.play(-1)
        else:
            self.main_page_music_now_id = -1
            self.musicNext()

    def gamePageBackMainPage(self):
        """
        此函数的功能是从游戏界面返回主界面
        :return: 无
        """
        self.IS_MAIN_PAGE = True
        self.IS_GAME_PAGE = False
        self.IS_AUTHORSLIST_PAGE = False

    def authorsList(self):
        """
        此函数是主界面贡献者名单的绑定事件
        :return: 无
        """
        self.IS_AUTHORSLIST_PAGE = True
        self.IS_MAIN_PAGE = False
        self.IS_GAME_PAGE = False

    def authorsPageBackMainPage(self):
        """
        此函数用于贡献者页返回主页
        :return: 无
        """
        self.IS_MAIN_PAGE = True
        self.IS_GAME_PAGE = False
        self.IS_AUTHORSLIST_PAGE = False

    def gamePageGoEndPage(self):
        """
        此函数的功能是从游戏界面去到结束界面
        """
        self.IS_END_PAGE = True
        self.IS_GAME_PAGE = True
        self.IS_AUTHORSLIST_PAGE = False

    def loadPageGoEndPage(self):
        """
        此函数的功能是从游戏界面去到结束界面
        """
        self.IS_END_PAGE = True
        self.IS_LOAD_PAGE = True
        self.IS_AUTHORSLIST_PAGE = False