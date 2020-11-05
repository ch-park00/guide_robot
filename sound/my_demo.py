# -*- coding: utf-8 -*- 


import snowboydecoder
import sys
import signal
import os
import googlesamples.assistant.grpc.my_assist as g_assist 
import wave
import subprocess
import time
"""
This demo file shows you how to use the new_message_callback to interact with
the recorded audio after a keyword is spoken. It uses the speech recognition
library in order to convert the recorded audio into text.

Information on installing the speech recognition library can be found at:
https://pypi.python.org/pypi/SpeechRecognition/
"""


interrupted = False

def detectedCallback():
  global my
  # 핵심어 검출 종료
  detector.terminate()
  # 소리 출력
  snowboydecoder.play_audio_file()
  # 로봇 정지 플래그 보내기
  start=time.time()
  subprocess.Popen(["rosrun","input_msg", "input_talker", "1"])
  print(time.time()-start)
  # 어시스턴스 실행
  a = g_assist.main()
  flag=0
  print(a)
  # 목적지 검출
  if len(a)>0:
      if "고기" in a[0]:
          flag+=2
      if "야채" in a[0]:
          flag+=4
      if "과일" in a[0]:
          flag+=8
      if "과자" in a[0]:
          flag+=16
      if "음료" in a[0]:
          flag+=32
      if "견과류" in a[0]:
          flag+=64
      if "라면" in a[0]:
          flag+=128
      if "위생" in a[0]:
          flag+=256
  print(a,flag)
#  f=open('test.txt','w+')
#  f.write(str(flag))
#  f.close()
  # 목적지 정보 플래그로 보내기
  subprocess.Popen(["rosrun","input_msg", "input_talker", str(flag)])
  detector.start(detected_callback=detectedCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


model = 'resources/models/snowboy.umdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.7)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detectedCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()




