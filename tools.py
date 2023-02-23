import time
import pyautogui
import pydirectinput
from lib import *

screen_size_x, screen_size_y = pyautogui.size()
pydirectinput.PAUSE = 0.02


class General():
    def toggle_window(self):
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.3)

    def is_img_on_screen(self, img, confident):
        """
        检测图片是否显示在屏幕上。
        :param region:
        :param img: 图片
        :param confident: 识别精确度，范围0~1
        :return: 在屏幕上返回True，否则False
        """
        location = pyautogui.locateOnScreen(img, confident)
        if location is not None:
            return True
        else:
            return False

    def waiting_for_img_on_screen(self, img, confident):
        """
        等待图片显示在屏幕上。
        :param img: 图片
        :param confident: 识别精确度，范围0~1
        :return: 在屏幕上时返回True
        """
        while True:
            location = pyautogui.locateOnScreen(img, confident)
            if location is not None:
                return True

    def press(self, key: str, times: int):
        for i in range(times):
            pydirectinput.press(key)


class Phone(General):
    def open_phone(self):
        pydirectinput.press('up')
        time.sleep(0.4)

    def open_chai1_shi4_qing1_dan1(self):
        self.open_phone()
        pydirectinput.press(['left', 'enter'])

    def quit_phone(self):
        for i in range(5):
            pydirectinput.press('backspace')

    def ka3_chai1_chuan2(self):
        self.open_chai1_shi4_qing1_dan1()
        pydirectinput.press('up')
        for i in range(3):
            pydirectinput.press('enter')
        time.sleep(0.5)
        self.open_chai1_shi4_qing1_dan1()
        pydirectinput.press('up')
        for i in range(2):
            pydirectinput.press('enter')
        self.quit_phone()


class Hu4_dong4_cai4_dan1(General):
    def __init__(self, in_team_):
        # in_team变量为是否在保镖事务所或摩托帮
        global in_team
        in_team = in_team_
        # time.sleep(0.1)

    def open_hu4_dong4_cai4_dan1(self):
        pydirectinput.press('m')  # 打开互动菜单

    def exit_hu4_dong4_cai4_dan1(self):
        for i in range(5):
            pydirectinput.press('backspace')

    def open_option(self, row, rows_num):
        """打开菜单的指定行选项。
        会自动计算哪种移动选项的方式（方向键上或下）最高效。
        :param row: 打开的选项序号
        :param rows_num: 选项总数
        :return: None
        """
        if rows_num - row >= rows_num / 2:  # 如果成立，说明选项在一半以上
            self.press('down', row - 1)
        else:
            self.press('up', rows_num - row + 1)
        pydirectinput.press('enter')

    def screen_shot(self):
        """
        给互动菜单截图。
        :return: None
        """
        pyautogui.screenshot('hu4_dong4_cai4_dan1.png', region=(0, 0, 590, 650))

    def hu1_jiao4_hu3_jing1(self):
        self.open_hu4_dong4_cai4_dan1()
        for i, j in zip(option_index['载具资产in_team']['虎鲸']['呼叫虎鲸'],
                        options_num_index['载具资产in_team']['虎鲸']['呼叫虎鲸']):
            self.open_option(i, j)
        self.exit_hu4_dong4_cai4_dan1()

    def hu1_jiao4_ma2_que4(self):
        self.open_hu4_dong4_cai4_dan1()
        for i, j in zip(option_index['载具资产in_team']['虎鲸']['呼叫载具（麻雀）'],
                        options_num_index['载具资产in_team']['虎鲸']['呼叫载具（麻雀）']):
            self.open_option(i, j)
        self.exit_hu4_dong4_cai4_dan1()

    def jiang1_ge4_ren2_zai4_ju4_song4_hui3_ku4_fang2(self):
        self.open_hu4_dong4_cai4_dan1()
        for i, j in zip(option_index['载具']['将个人载具送回库房'],
                        options_num_index['载具']['将个人载具送回库房']):
            self.open_option(i, j)
        self.exit_hu4_dong4_cai4_dan1()

    def toggle_chai1_shi4_xian3_shi4(self):
        self.open_hu4_dong4_cai4_dan1()
        for i, j in zip(option_index['地图标记点选项']['差事']['所有差事'],
                        options_num_index['地图标记点选项']['差事']['所有差事']):
            self.open_option(i, j)
        self.exit_hu4_dong4_cai4_dan1()

    def song4Hui2Hu3Jing1(self):
        self.open_hu4_dong4_cai4_dan1()
        for i, j in zip(option_index['载具资产in_team']['虎鲸']['送回选项']['将虎鲸送回寄存库'],
                        options_num_index['载具资产in_team']['虎鲸']['送回选项']):
            self.open_option(i, j)
        self.exit_hu4_dong4_cai4_dan1()


class Du3_chang3(General):
    def __init__(self):
        global img_dic
        img_dic = {
            'A': {
                'overview': r'img/du3_chang3_fingerprint_lock/A/overview.png',
                'A': r'img/du3_chang3_fingerprint_lock/A/A.png',
                'B': r'img/du3_chang3_fingerprint_lock/A/B.png',
                'C': r'img/du3_chang3_fingerprint_lock/A/C.png',
                'D': r'img/du3_chang3_fingerprint_lock/A/D.png'
            },
            'B': {
                'overview': r'D:\Users\84006\Desktop\img\B\overview.png',
                'A': r'D:\Users\84006\Desktop\img\B\A.png',
                'B': r'D:\Users\84006\Desktop\img\B\B.png',
                'C': r'D:\Users\84006\Desktop\img\B\C.png',
                'D': r'D:\Users\84006\Desktop\img\B\D.png'
            }
        }
        self.toggle_window()

    def check_course(self):
        """
        检测当前指纹类型（A、B或C）
        :return: 指纹类型（A、B或C）
        """
        global course
        print('正在检测指纹类型')
        A = self.is_img_on_screen(img_dic['A']['overview'], 0.7)
        B = self.is_img_on_screen(img_dic['B']['overview'], 0.7)
        # C = self.is_img_on_screen(img_dic['C']['overview'], 0.7)
        # D = self.is_img_on_screen(img_dic['D']['overview'], 0.7)
        if A:
            course = 'A'
        elif B:
            course = 'B'
        # elif C:
        #     course = 'C'
        # elif D:
        #     course = 'D'
        print(f'当前为指纹{course}')

        return course

    def test(self):
        # print(pyautogui.locateOnScreen(img_dic[course]['A'], 0, grayscale=True))
        print(pyautogui.locateOnScreen('img/du3_chang3_fingerprint_lock/B/A.png', 0.1))
