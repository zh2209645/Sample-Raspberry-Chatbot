import sys, json, requests

def tuling(words):
    Tuling_API_KEY = "ad65aaa7e97e4d28bdb3c34fbabf4259"

    body = {
        "key": Tuling_API_KEY,
        "info": words.encode("utf-8")
    }

    url = "http://www.tuling123.com/openapi/api"
    resp = requests.post(url=url, data=body, verify=True)

    if resp:
        data = json.loads(resp.text)
        print(data["text"])
        return data["text"]
    else:
        return None