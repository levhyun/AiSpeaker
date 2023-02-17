import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

list = [
    ['안녕','주인님, 안녕하세요.'],
    ['슬퍼','주인님, 힘내세요. 제가 있잖아요!'],
    ['행복해','주인님이 행복하니 저도 행복하네요.'],
    ['고마워','별 말씀을요.'],
    ['종료','인공지능 스피커 종료'],
]

def ai(text):
    print("[인공지능] " + text)
    fileName = 'speak.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(fileName)
    playsound(fileName)
    if os.path.exists(fileName):
        os.remove(fileName)

def fintAnswer(text):
    answerText = ''
    for i in range(5):
        if list[i][0] in text:
            answerText = list[i][1]
    if answerText == '':
        answerText = '무슨말인지 모르겠어요..'
    return answerText

def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        return text
    except sr.UnknownValueError:
        print('[오류] 음성 인식을 실패하였습니다.')
    except sr.RequestError as err:
        print('[오류] 서버 요청중 에러가 발생하였습니다.\n[상세] {0}'.format(err))

def process(recognizer, audio):
    text = listen(recognizer, audio)
    if text != '':
        print('[사용자] ' + text)
        answer = fintAnswer(text)
        ai(answer)

def aiRun():
    ai('인공지능 스피커 실행')
    ai('주인님, 무엇을 도와 드릴까요?')

def init():
    r = sr.Recognizer()
    m = sr.Microphone()
    aiRun()
    listenStop = r.listen_in_background(m, process)
    while True:
        pass

init()