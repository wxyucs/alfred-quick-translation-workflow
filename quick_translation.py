import requests
import json
import time


q = '$1'
key = '$key'


def detect(q):
    url = f'https://translation.googleapis.com/language/translate/v2/detect?key={key}'
    data = {'q': q}
    resp_json = requests.post(url, data=data).json()
    if 'error' in resp_json:
        raise Exception(f"Failed to detect language: {resp_json}")
    lang = resp_json['data']['detections'][0][0]['language']
    return lang.lower()


def translate(q, source, target):
    url = f'https://translation.googleapis.com/language/translate/v2?key={key}'
    data = {
        'source': source,
        'target': target,
        'q': q,
        'format': 'text',
    }
    resp_json = requests.post(url, data=data).json()
    if 'error' in resp_json:
        raise Exception(f"Failed to translate: {resp_json}")
    text = resp_json['data']['translations'][0]['translatedText']
    output = {
        'items': [
            {
                'uid': 'text',
                'title': text,
                'arg': text,
                'mods': {
                    'alt': {
                        'valid': True,
                        'arg': q,
                        'subtitle': f'按「Enter键」复制原文到剪贴板',
                    },
                    'cmd': {
                        'valid': True,
                        'arg': text,
                        'subtitle': f'按「Enter键」复制翻译结果到剪贴板',
                    },
                }
            }
        ]
    }
    return output


begin = time.time()
language = detect(q)
if language != 'zh-cn':
    output = translate(q, language, 'zh-cn')
else:
    output = translate(q, language, 'en')
cost = time.time() - begin
output['items'][0]['subtitle'] = 'Cost: %.2f s' % cost
print(json.dumps(output))
