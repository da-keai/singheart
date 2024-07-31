import os
import shutil
def update_select_music():
    return "网页状态：需选择要转换的音乐"

def update_upload_success():
    return "网页状态：上传成功，请点击start SingHeart之旅"

def update_trans_success():
    print("转换成功")
    return "网页状态：转换成功，请下载聆听成功的音乐"

def update_start(input_audio):
    print(f"点击了start按钮，输入音乐临时地址：{input_audio}")
    if input_audio is None:
        return "网页状态：请上传要转换的音乐再点击Start SingHeart之旅"
    else:
        return "网页状态：已经开启转换，请您静心等待..."

def start_process(person_select, input_audio):
    if input_audio is None:
        return None
    else:
        target_folder = "music/"
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        target_name = os.path.basename(input_audio)
        target_name, ext = os.path.splitext(target_name)
        target_name = target_name + '_' + person_select + ext
        target_location = os.path.join(target_folder, target_name)
        target_location = os.path.normpath(target_location)
        print(f"角色:{person_select}，输入：{input_audio}，输出在云端：{target_location}")

        try:
            with open(target_location, "wb") as f:
                shutil.copy2(src=input_audio, dst=target_location)
                if os.path.exists(target_location):
                    print(f"文件已下载至云端电脑：{target_location}")
                else:
                    print(f"文件传向云端保存失败")
        except Exception as e:
            print(f"保存文件时发生错误：{str(e)}")

    print("正在上传转换好的音乐")
    return target_location