#! ./venv/Scripts/python.exe
# --coding=utf-8
# import sys
try:
    import pygame
except Exception as e:
    print("您的python没有pygame库，请双击目录下的|安装pygame库.bat|文件")
    input("请手动关闭窗口")
# 游戏文件
from setting import config  # 基本配置文件
from module.gameElementList import GameElementList  # 游戏中一部分元素
from module.gameEventList import GameEventList  # 游戏中一部分事件
from loadLevel import LoadLevel  # 游戏中的level元素

class Game(GameEventList, GameElementList, LoadLevel):
    def __init__(self):
        # 一些初始化设置
        pygame.init()  # pygame库初始化
        self.CONSOLE_LOG = open(config["CONSOLE_LOG_FILE"], 'w+', encoding="UTF-8")  # 打开日志记录文件
        self.SIZE = config["WINDOW_SIZE"]  # 全局变量尺寸
        self.GAME_ICON = pygame.image.load(config["WINDOW_ICON"])  # 创建图标对象
        self.FPS = config["FPS"]  # 帧率
        self.BASE_FONT = pygame.font.Font(config["BASE_FONT_PATH"], config["BASE_FONT_SIZE"])
        # self.BASE_FONT = pygame.font.SysFont("华文楷体", config["BASE_FONT_SIZE"])  # 从系统字体中引入华文楷体, 大小为20
        self.FONT_DEFAULT_COLOR = config["FONT_DEFAULT_COLOR"]  # 默认字体颜色
        self.FONT_ACTIVE_COLOR = config["FONT_ACTIVE_COLOR"]  # 字体选中颜色
        self.screen = pygame.display.set_mode(self.SIZE)  # 设置窗口大小
        pygame.display.set_caption(config["WINDOW_NAME"])  # 设置窗口名称
        pygame.display.set_icon(self.GAME_ICON)  # 设置窗口图标
        self.LoadLevelInit()  # LoadLevel类的初始化(此处不用super().__init__()是因为编译成exe的程序可能会报一些未知的错误)
        # 加载元素
        self.elementLoad()  # 调用加载函数
        self.run()

    def run(self):
        """
        死循环，也是游戏运行的主要部分
        :return: 无
        """
        while True:
            self.clock.tick(self.FPS)  # 帧率
            self.FPS_TIME += 1  # 帧率变量增值
            if self.FPS_TIME % 10 == 0:
                print("帧率: " + str(int(self.clock.get_fps())))  # 每6/1秒输出一下当前帧率
            # 键盘鼠标事件
            self.mouse_pressed = pygame.mouse.get_pressed()  # 获取鼠标左、中、右键的状态
            self.mouse_position = tuple(pygame.mouse.get_pos())  # 获取鼠标坐标并转换为元组
            self.keys_list = pygame.event.get()  # 获取所有键盘事件(一次性的)
            self.keys_pressed = pygame.key.get_pressed()  # 获取所有键盘事件(连续性的)
            self.keys_mods = pygame.key.get_mods()  # 获取组合键
            self.cushion()  # 更新鼠标缓冲
            self.levelPlayerCushion()  # 更新鼠标缓冲
            # 获取事件，监听事件状态
            for event in self.keys_list:
                if event.type == pygame.QUIT:  # 点击了关闭按钮
                    self.quitGame()
            # 执行判断元素事件的函数
            self.elementEvent()
            # 执行元素的渲染函数
            self.elementRender()
            # 更新
            pygame.display.update()  # 刷新画面

    def elementLoad(self):
        """
        此函数的作用是将游戏内所需的元素加载
        音乐，文字按钮，图片之
        :return: 无
        """
        # 鼠标样式
        self.mouse()
        # 缓冲变量
        self.cushion_time = 0
        self.cushion_active = True
        # 时钟，规定帧率用
        self.clock = pygame.time.Clock()
        # 定义帧率变量用于定时输出帧率
        self.FPS_TIME = 0
        # 主界面背景音乐元素
        self.mainPageMusic()
        # 主界面元素
        self.mainPageMusicCtrlBtn()  # 音乐控件按钮
        self.mainPageTextBtn()  # 文字按钮
        self.mainPageBackground()  # 主界面背景图片
        # 新游戏界面元素
        self.levelPlayerElement()
        self.levelEndElement()
        # 读取存档界面元素
        self.levelLoadElement()
        # 游戏设置界面元素
        self.levelSettingElement()
        # 贡献者名单界面元素
        self.authorsListPageBackground()
        self.authorsListPageText()
        self.authorsListPageAuthorInfo()
        self.authorsListPageBackMainPageBtn()

    def elementRender(self):
        """
        此函数的作用是在游戏过程中渲染刷新后的游戏内容
        :return: 无
        """
        # 渲染(顺序一定不能错，否则可能出现覆盖现象)
        # 主界面
        if self.IS_MAIN_PAGE:
            # 1.背景图片
            self.screen.blit(self.main_page_background, (0, 0))
            # 2.字体按钮
            self.screen.blit(self.start_new_game_font, self.btn_pos["start_new_game_btn"])
            self.screen.blit(self.start_old_game_font, self.btn_pos["start_old_game_btn"])
            self.screen.blit(self.setting_game_font, self.btn_pos["setting_game_btn"])
            self.screen.blit(self.authors_list_font, self.btn_pos["authors_list_btn"])
            self.screen.blit(self.quit_game_font, self.btn_pos["quit_game_btn"])
            # 2.1音乐暂停、播放、上曲和下曲按钮
            self.screen.blit(self.main_music_ctrl_btn_bg, (self.SIZE[0] - self.main_music_ctrl_btn_bg_rect[2], self.SIZE[1] - self.main_music_ctrl_btn_bg_rect[3]))
            self.screen.blit(self.main_music_stop_btn, self.btn_pos["main_music_stop_btn"])
            self.screen.blit(self.main_music_keep_btn, self.btn_pos["main_music_keep_btn"])
            self.screen.blit(self.main_music_next_btn, self.btn_pos["main_music_next_btn"])
            self.screen.blit(self.main_music_last_btn, self.btn_pos["main_music_last_btn"])
            # 选中字体情况判断
            # (此处可以改用另一种写法，将需要更改的按钮将其和其余3个一同显示出来，但是这样要给每个判断都写上这几行，这样一来会增加过多的代码冗余，所以此处不采用)
            if self.active_btn_choose == 1:
                self.screen.blit(self.start_new_game_active, self.btn_pos["start_new_game_btn"])
            elif self.active_btn_choose == 2:
                self.screen.blit(self.start_old_game_active, self.btn_pos["start_old_game_btn"])
            elif self.active_btn_choose == 3:
                self.screen.blit(self.setting_game_active, self.btn_pos["setting_game_btn"])
            elif self.active_btn_choose == 4:
                self.screen.blit(self.authors_list_active, self.btn_pos["authors_list_btn"])
            elif self.active_btn_choose == 5:
                self.screen.blit(self.quit_game_active, self.btn_pos["quit_game_btn"])
            elif self.active_btn_choose == 6:
                self.screen.blit(self.main_music_stop_active, self.btn_pos["main_music_stop_btn"])
            elif self.active_btn_choose == 7:
                self.screen.blit(self.main_music_keep_active, self.btn_pos["main_music_keep_btn"])
            elif self.active_btn_choose == 8:
                self.screen.blit(self.main_music_next_active, self.btn_pos["main_music_next_btn"])
            elif self.active_btn_choose == 9:
                self.screen.blit(self.main_music_last_active, self.btn_pos["main_music_last_btn"])
        # 游戏界面
        elif self.IS_GAME_PAGE:
            if self.IS_END_PAGE:  # 如果是结束界面
                self.levelEndRender()
            else:  #如果不是结束界面
                self.levelPlayerRender()
        # 如果是读取存档界面
        elif self.IS_LOAD_PAGE:
            if self.IS_END_PAGE:  # 如果是结束界面
                self.levelEndRender()
            else:  # 如果不是结束界面
                self.levelLoadRender()
        # 如果是设置界面
        elif self.IS_SETTING_PAGE:
            self.levelSettingRender()
        # 贡献者名单界面
        elif self.IS_AUTHORSLIST_PAGE:
            self.screen.blit(self.authors_page_background, (0, 0))  #背景图片
            for i in range(self.authors_num):  # 循环将所有的作者名绘制到上面
                self.screen.blit(self.authors_text_list[i], (self.average_xy_list[i][0], self.average_xy_list[i][1]))
            if self.is_author_info:  # 如果鼠标在文字按钮上方则显示信息板
                for i in range(self.authors_num):
                    if self.author_info_choose == i:
                        self.screen.blit(self.author_info_background_list[self.author_info_choose], self.mouse_position)
                        break
                self.is_author_info = False  # 将显示重置为False
            self.screen.blit(self.back_main_page_font, self.btn_pos["author_page_back_main_page_btn"])  # 绘制退出按钮
            if self.active_btn_choose == 10:  # 如果选择编号为10说明鼠标在退出按钮上面，然后渲染选中状态的按钮
                self.screen.blit(self.back_main_page_active, self.btn_pos["author_page_back_main_page_btn"])
        # 鼠标外形渲染
        self.screen.blit(self.mouse_img, self.mouse_position)  # 在真正鼠标的坐标绘制小鼠标图片

    def elementEvent(self):
        """
        此函数的作用是判断一些跟键鼠相关的事件, 然后具体发生事件可以链接新的函数
        :return:无
        """
        # 此处判断的是鼠标是否在相应的文字按钮上面
        # 主界面
        if self.IS_MAIN_PAGE:  # 如果当前还是主界面的话就继续执行，如果不是则没必要往下执行了
            if self.btn_pos["start_new_game_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["start_new_game_btn"][0] + self.start_new_game_font_rect[2]) \
                    and \
                    self.btn_pos["start_new_game_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["start_new_game_btn"][1] + self.start_new_game_font_rect[3]):
                self.active_btn_choose = 1
            elif self.btn_pos["start_old_game_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["start_old_game_btn"][0] + self.start_old_game_font_rect[2]) \
                    and \
                    self.btn_pos["start_old_game_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["start_old_game_btn"][1] + self.start_old_game_font_rect[3]):
                self.active_btn_choose = 2
            elif self.btn_pos["setting_game_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["setting_game_btn"][0] + self.setting_game_font_rect[2]) \
                    and \
                    self.btn_pos["setting_game_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["setting_game_btn"][1] + self.setting_game_font_rect[3]):
                self.active_btn_choose = 3
            elif self.btn_pos["authors_list_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["authors_list_btn"][0] + self.authors_list_font_rect[2]) \
                    and \
                    self.btn_pos["authors_list_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["authors_list_btn"][1] + self.authors_list_font_rect[3]):
                self.active_btn_choose = 4
            elif self.btn_pos["quit_game_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["quit_game_btn"][0] + self.quit_game_font_rect[2]) \
                    and \
                    self.btn_pos["quit_game_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["quit_game_btn"][1] + self.quit_game_font_rect[3]):
                self.active_btn_choose = 5
            elif self.btn_pos["main_music_stop_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["main_music_stop_btn"][0] + self.main_music_stop_btn_rect[2]) \
                    and \
                    self.btn_pos["main_music_stop_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["main_music_stop_btn"][1] + self.main_music_stop_btn_rect[3]):
                self.active_btn_choose = 6
            elif self.btn_pos["main_music_keep_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["main_music_keep_btn"][0] + self.main_music_keep_btn_rect[2]) \
                    and \
                    self.btn_pos["main_music_keep_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["main_music_keep_btn"][1] + self.main_music_keep_btn_rect[3]):
                self.active_btn_choose = 7
            elif self.btn_pos["main_music_next_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["main_music_next_btn"][0] + self.main_music_next_btn_rect[2]) \
                    and \
                    self.btn_pos["main_music_next_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["main_music_next_btn"][1] + self.main_music_next_btn_rect[3]):
                self.active_btn_choose = 8
            elif self.btn_pos["main_music_last_btn"][0] < self.mouse_position[0] < (
                    self.btn_pos["main_music_last_btn"][0] + self.main_music_last_btn_rect[2]) \
                    and \
                    self.btn_pos["main_music_last_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["main_music_last_btn"][1] + self.main_music_last_btn_rect[3]):
                self.active_btn_choose = 9
            else:  # 如果什么按钮都没有被选中，则将变量值赋为0
                self.active_btn_choose = 0
            # 对于鼠标点击的判断
            if self.mouse_pressed[0] and self.cushion_active:  # 如果缓冲好了才能点击
                self.cushion_active = False
                if self.active_btn_choose == 1:  # 点击开始新游戏按钮
                    self.btnClick()
                    self.startNewGame()
                elif self.active_btn_choose == 2:  # 点击读取游戏按钮
                    self.btnClick()
                    self.goGameLoadPage()
                elif self.active_btn_choose == 3:  # 点击游戏选项按钮
                    self.btnClick()
                    self.goGameSettingPage()
                elif self.active_btn_choose == 4:  # 点击贡献者名单按钮
                    self.btnClick()
                    self.authorsList()
                elif self.active_btn_choose == 5:  # 点击退出游戏按钮
                    self.btnClick()
                    self.quitGame()
                elif self.active_btn_choose == 6:  # 点击暂停按钮
                    self.btnClick()
                    self.musicStop()
                elif self.active_btn_choose == 7:  # 点击继续按钮
                    self.btnClick()
                    self.musicKeep()
                elif self.active_btn_choose == 8:  # 点击下曲按钮
                    self.btnClick()
                    self.musicNext()
                elif self.active_btn_choose == 9:  # 点击上曲按钮
                    self.btnClick()
                    self.musicLast()
        # 游戏界面
        elif self.IS_GAME_PAGE:
            if self.IS_END_PAGE:
                self.levelEndEvent()  # 结束界面事件
            else:
                self.levelPlayerEvent()  # 游戏界面事件
                if not self.levelPlayer_name_edit_active:  # 如果不是编辑状态才能退出界面
                    for event in self.keys_list:  # 循环监听事件
                        if event.type == pygame.KEYDOWN:  # 判断是否按下了键盘
                            if event.key == pygame.K_ESCAPE:  # 如果键盘按下了Esc键，则返回主界面
                                self.gamePageBackMainPage()
        # 存档界面
        elif self.IS_LOAD_PAGE:
            if self.IS_END_PAGE:  # 结束界面事件
                self.levelEndEvent()
            else:
                self.levelLoadEvent()
        # 设置界面
        elif self.IS_SETTING_PAGE:
            self.levelSettingEvent()  # 设置界面事件
        # 贡献者名单界面
        elif self.IS_AUTHORSLIST_PAGE:
            if self.btn_pos["author_page_back_main_page_btn"][0] < self.mouse_position[0] < (  # 是否在返回按钮上方
                    self.btn_pos["author_page_back_main_page_btn"][0] + self.back_main_page_font_rect[2]) \
                    and \
                    self.btn_pos["author_page_back_main_page_btn"][1] < self.mouse_position[1] < (
                    self.btn_pos["author_page_back_main_page_btn"][1] + self.back_main_page_font_rect[3]):
                self.active_btn_choose = 10
                if self.mouse_pressed[0]:  # 是否点击了返回按钮
                    if self.cushion_active:
                        self.cushion_active = False
                        self.btnClick()
                        self.authorsPageBackMainPage()
            else:
                self.active_btn_choose = 0
            for i in range(self.authors_num):
                # 是否在第1个作者名上方
                if self.average_xy_list[i][0] < self.mouse_position[0] < (self.average_xy_list[i][0] + self.authors_text_rect_list[i][2]) \
                    and self.average_xy_list[i][1] < self.mouse_position[1] < (self.average_xy_list[i][1] + self.authors_text_rect_list[i][3]):
                    self.author_info_choose = i
                    self.is_author_info = True
                    break
                if not self.is_author_info:
                    self.author_info_choose = -1

    def cushion(self):
        """
        缓冲, 因为游戏引擎的缘故，点击按钮容易一次性按很多下，无法有效控制操作，所以弄一个缓冲操作，这样就能点击一次不会出现多次操作
        :return:无
        """
        if not self.cushion_active:
            self.cushion_time += 1
            if self.cushion_time == 20:
                self.cushion_time = 0
                self.cushion_active = True

    def mouse(self):
        """
        更改鼠标样式
        :return: 无
        """
        # self.cursor = pygame.cursors.load_xbm(".\\module\\image\\mouse.xbm", ".\\module\\image\\mouse.xbm")  # 导入xbm文件
        # pygame.mouse.set_cursor(*self.cursor)  # 设置鼠标样式
        pygame.mouse.set_visible(False)  # 设置鼠标隐藏，用一个鼠标图标替代
        self.mouse_img = pygame.image.load(".\\module\\image\\mouse.png").convert_alpha()

if __name__ == "__main__":  # 执行入口
    game = Game()  # 实例化Game类
    # game.run()  # 运行run方法让程序真正跑起来
