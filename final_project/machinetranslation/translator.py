import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)


lang_trlt = LanguageTranslatorV3(version='2022-12-09',authenticator=auth)
lang_trlt.set_service_url(url)


def englishtofrench(englishtext):
    translation = lang_trlt.translate(text=englishtext, source='English', target='French').get_result()
    frenchtext = translation["translations"][0]["translation"]
    return frenchtext

def frenchtoenglish(frenchtext):
    translation = lang_trlt.translate(text=frenchtext, source='French', target='English').get_result()
    englishtext = translation["translations"][0]["translation"]
    return englishtext
