import sys, json, urllib, base64, requests

def get_access_token():
    url = "https://openapi.baidu.com/oauth/2.0/token"
    body = {
        "grant_type": "client_credentials",
        "client_id": "API Key goes here",
        "client_secret": "Secret Key goes here"
    }
    r = requests.post(url, data=body, verify=True)
    respond = json.loads(r.text)
    print(respond)
    return respond["access_token"]

def yuyinshibie_api(audio_data, token):
    speech_data = base64.b64encode(audio_data).decode("utf-8")
    speech_length = len(audio_data)
    post_data = {
        "format": "wav",
        "rate": 16000,
        "channel": 1,
        "cuid": "B8-27-EB-BA-24-14",
        "token": token,
        "speech": speech_data,
        "len": speech_length
    }
    url = "http://vop.baidu.com/server_api"
    json_data = json.dumps(post_data).encode("utf-8")
    json_length = len(json_data)

    req = urllib.request.Request(url, data=json_data)
    req.add_header("Content-Type", "application/json")
    req.add_header("Content-Length", json_length)

    resp = urllib.request.urlopen(req)
    resp = resp.read()
    resp_data = json.loads(resp.decode("utf-8"))
    if resp_data["err_no"] == 0:
        return resp_data["result"]
    else:
        print(resp_data)
        return None

def asr_main(filename, token):
    try:
        with open(filename, "rb") as file_to_read:
            audio_data = file_to_read.read()
            resp = yuyinshibie_api(audio_data, token)
            return resp[0]
    except Exception:
        # print("e: {}".format(e))
        return "识别失败".encode("utf-8")




