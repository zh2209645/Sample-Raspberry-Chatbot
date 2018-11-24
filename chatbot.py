import yuyinhecheng, turling, yuyinshibie, os, time

def main_loop():
    token = yuyinshibie.get_access_token()

    while True:
        recording_file = recording()
        recording_word = yuyinshibie.asr_main(recording_file, token)
        if "关闭".encode("utf-8") in recording_word:
            while True:
                recording_file = recording()
                
                recording_word = yuyinshibie.asr_main(recording_file, token)
                if "开启".encode("utf-8") in recording_word:
                    break
                else:
                    time.sleep(2)
            voice_file = yuyinhecheng.yuyinhecheng_api("开启成功", token)
            os.system('mpg123 {}'.format(voice_file))

        elif '暂停'.encode("utf-8") in recording_word:
            voice_file = yuyinhecheng.yuyinhecheng_api("开始暂停", token)
            os.system('mpg123 {}'.format(voice_file))

            time.sleep(10)
            voice_file = yuyinhecheng.yuyinhecheng_api("暂停结束", token)
            os.system("mpg123 {}".format(voice_file))

        else:
            turling_resp = turling.tuling(recording_word)
            voice_file = yuyinhecheng.yuyinhecheng_api(turling_resp, token)
            os.system('mpg123 {}'.format(voice_file))
            time.sleep(0.5)


def recording():
    filename = "./voice.wav"
    cmd = 'sudo arecord -D "plughw:1" -f S16-LE -r 16000 -d 3 {}'.format(filename)
    os.system(cmd)
    time.sleep(0.5)
    return filename
