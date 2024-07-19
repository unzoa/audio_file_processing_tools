# 使用cut-pices.py，其中函数包含了平均时间裁剪mp3文件
from cut import split_mp3_loop

if __name__ == '__main__':
    split_mp3_loop('input.mp3', 40 * 60 * 1000)


