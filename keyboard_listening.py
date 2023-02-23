from pynput import keyboard


# 定义按下按键时调用的函数
def on_press(key):
    try:
        print(f'按下按键 {key}.')
    except AttributeError:
        print(f'特殊按键 {key} 被按下。')


# 定义释放按键时调用的函数
def on_release(key):
    print(f'按键 {key} 被释放。')
    if key == keyboard.Key.esc:  # 如果按下的是 ESC 键，就停止监听
        return False


# 创建键盘监听器
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # 开始监听按键
