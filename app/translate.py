import json
import requests
import uuid
import urllib.parse
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY'] \
            or 'MS_TRANSLATOR_REGION' not in app.config \
            or not app.config['MS_TRANSLATOR_REGION']:
        return _('Error: the translation service is not configured.')
    endpoint =  'https://api.cognitive.microsofttranslator.com/translate?'
    params = {'api-version': '3.0', 'from': source_language, 'to': dest_language }
    translate_url = endpoint + urllib.parse.urlencode(params)
    payload = [{'text': text}]
    headers = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': app.config['MS_TRANSLATOR_REGION'],
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    r = requests.post(translate_url, headers=headers, json=payload)
    if r.status_code != 200:
        return 'Error: the translation service failed.'
    return json.loads(r.content.decode('utf-8-sig'))[0]['translations'][0]['text']
