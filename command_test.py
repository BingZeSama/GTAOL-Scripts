import tools
from colorama import Fore, Style

menu = tools.Hu4_dong4_cai4_dan1(True)

print('欢迎使用GTAOL_scripts程序，作者：bilibili@一只冰泽。程序目前为半成品，仅供调试。\n')
print(f'{Fore.BLUE}输入序号以选择功能。{Style.RESET_ALL}')
while True:
    print(f'{Fore.RED}请注意，目前的所有功能必须注册保镖事务所或摩托帮才能使用。{Style.RESET_ALL}')
    print(f'''1. 呼叫虎鲸
2. 呼叫麻雀
3. 将个人载具送回库房
4. 切换地图上差事显示
5. 送回虎鲸
{Fore.RED}提交后，程序会执行Alt + Tab快捷键，即切换上次使用的窗口，请确保上一次使用的窗口为游戏窗口。{Style.RESET_ALL}''')
    user_selection = input()
    try:
        user_selection = int(user_selection)
        menu.toggle_window()
        if user_selection == 1:
            menu.hu1_jiao4_hu3_jing1()
        elif user_selection == 2:
            menu.hu1_jiao4_ma2_que4()
        elif user_selection == 3:
            menu.jiang1_ge4_ren2_zai4_ju4_song4_hui3_ku4_fang2()
        elif user_selection == 4:
            menu.toggle_chai1_shi4_xian3_shi4()
        elif user_selection == 5:
            menu.song4Hui2Hu3Jing1()
    except ValueError:
        print('值错误。\n')

