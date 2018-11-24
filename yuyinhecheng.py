import sys, requests, json, os, yuyinshibie, base64

temp_file_name = "temp.mp3"

def yuyinhecheng_api(text_content, token):
    cuid = "B8-27-EB-BA-24-14"
    url = "http://tsn.baidu.com/text2audio?tex={}&lan=zh&cuid={}&ctp=1&tok={}&per=3".format(text_content, cuid, token)

    resp = requests.get(url)
    print(resp)
    with open(temp_file_name, "wb") as file_to_write:
        file_to_write.write(resp.content)
    return temp_file_name
    
    
