# 函数支持输入时间间隔，然后将音频按这个时间段平均切分成多个片段，并存储到根目录下/parts文件夹下
import os
from pydub import AudioSegment

def split_mp3_loop(input_file: str, split_time_ms: int):
    """
    使用循环而非递归来将一个MP3文件分割成多个文件。

    参数:
    input_file: str - 输入的MP3文件路径。
    split_time_ms: int - 分割音频的时间点，以毫秒为单位。
    """

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_dir = 'parts'
    os.makedirs(output_dir, exist_ok=True)

    part = 1
    current_file = input_file
    while True:
        audio = AudioSegment.from_mp3(current_file)
        if audio.duration_seconds * 1000 < split_time_ms:
            # 如果剩余音频长度小于分割时间，则直接导出整个音频并退出循环
            audio.export(f'{output_dir}/{base_name}_part{part}.mp3', format="mp3")
            print(f"输出了最后一段音频，长度为：{audio.duration_seconds}秒")
            os.remove(current_file)
            break
        else:
            # 否则，分割音频并导出第一部分
            first_half = audio[:split_time_ms]
            first_half.export(f'{output_dir}/{base_name}_part{part}.mp3', format="mp3")
            print(f"输出了第{part}段音频，长度为：{first_half.duration_seconds}秒")

            # 更新当前音频文件为未分割的部分
            second_half = audio[split_time_ms:]
            current_file = f'{output_dir}/{base_name}_temp.mp3'
            second_half.export(current_file, format="mp3")

            # 增加部分编号，准备下一次循环
            part += 1

if __name__ == '__main__':
    # 假设在 30 分钟（30 * 60 * 1000 = 1800000 毫秒）处分割
    split_point_ms = 30 * 60 * 1000
    split_mp3_loop('./input.mp3', split_point_ms)

