import re
import string

file_path = '/Users/yueli/Desktop/health_check_case4_cpp_single_live_h265.txt'

# s = 'abc123xyz'
# x = str.maketrans('abcxyz', 'xyzabc')
# # print(x)
# print(s.translate(x))

a = "memory: [{'available': 61264564224, 11.1}]"
b = re.sub("[^a-zA-Z0-9\s.]", '', a)
# print(b)
# b = str.maketrans('[,]', ' ')
# print(a.translate(b))


def calculat(check_op='bps_rx'):
    with open(file_path, 'r') as f:
        data_list = []
        for line in f.readlines():
            a = str(line)
            b = re.sub("[^a-zA-Z0-9\s.\w$]", '', a)
            list_b = b.strip().split(" ") 
            print(list_b)
            if check_op in list_b:
                data = list_b.index(check_op) + 1
                print(data)
                data_list.append(list_b[data])
        # return data_list
print(calculat())

with open(file_path, 'r') as f:
    date_list = []
    # reg = "[^a-zA-Z0-9\s$]"
    for line in f.readlines():
        # date_list.append(line)
        a = str(line)
        b = re.sub("[^a-zA-Z0-9\s$]", '', a)
        date_list = b.strip().split(" ") 
        # print(date_list)

    #     date_list =  re.sub("[^a-zA-Z0-9\s$]", '', str(line))
    # print(date_list)
        # date_list.translate(str.maketrans('', '', string.punctuation))
        # print(date_list)

import re

# # 只保留中文、大小写字母和阿拉伯数字
# reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
# text = "<>\(*芸%芸^)，,\\（-我@）&love=+《你》！【~我//""[们]】2{0}1.6~————、结/婚'吧:：！这.!！_#？?（）个‘’“”￥$主|意()不。错……！"
# print(re.sub(reg, '', text))


punctuation = '!,;:?"\''
def removePunctuation(file_path):
    with open(file_path, 'r') as f:
        date_list = ''
        for line in f.readlines():
            # print(line)
            # date_list = re.sub(r'[{}]+'.format(punctuation),'',line)
            date_list.translate(str.maketrans('', '', string.punctuation))
    # return date_list.strip().lower()
    # print(date_list)
 
# print(removePunctuation(file_path))

