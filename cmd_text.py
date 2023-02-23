script_name = ['卡差传']
script_details = {
    '卡差传': '在任务中也能使用差传。'
}


class Cmd():
    def __init__(self):
        print('输入数字执行脚本，输入“h”加“数字”显示脚本描述。')

    def list_script_name(self, script_name):
        for i in range(len(script_name)):
            print(f'{i}. {script_name[i]}')

    def search_script_information(self, script_index):
        print(f'{script_name[script_index]}: {script_details[script_name[script_index]]}')

    def assigning_task(self, input):
        if 'h' in input:
            self.search_script_information()
