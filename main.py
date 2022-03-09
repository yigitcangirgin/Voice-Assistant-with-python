import playsound
import speech_recognition as sr
from gtts import gTTS
import random
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options




def konuş(yazı):
    tts = gTTS(text=yazı, lang="tr")
    dosya_ismi = "ses"+ str(random.randint(0,1000000000000000000000)) + ".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)

def sesi_kaydet():
    r = sr.Recognizer()

    with sr.Microphone() as kaynak:
        ses = r.listen(kaynak)

        söylenen_cümle = ""

        try:
            söylenen_cümle = r.recognize_google(ses, language="Tr-tr")
            print(söylenen_cümle)

        except Exception:
            konuş("söylediğin cümleyi anlayamadım")

    return söylenen_cümle

while True:
    yazı = sesi_kaydet()
    if "Google'ı açar mısın" in yazı:
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://www.google.com/"
        driver.get(url)
        time.sleep(3)
        driver.close()
    elif "YouTube'u açar mısın" in yazı:
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://www.youtube.com/"
        driver.get(url)
        time.sleep(3)
        driver.close()
    elif "Twitter'ı açar mısın" in yazı:
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://twitter.com/"
        driver.get(url)
        time.sleep(3)
        driver.close()

    elif "Facebook'u açıp giriş yapar mısın" in yazı:
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://www.facebook.com/"
        driver.get(url)

        searchInput = driver.find_element_by_name("email")
        searchInput.send_keys("")
        time.sleep(1)

        searchInput = driver.find_element_by_name("pass")
        searchInput.send_keys("")
        time.sleep(1)

        searchInput.send_keys(Keys.ENTER)
        time.sleep(30)
        driver.close()
    elif "" in yazı:
        continue