import snowboydecoder
import sys
import signal
import os
import googlesamples.assistant.grpc.pushtotalk_fix as g_assist 
import wave

"""
This demo file shows you how to use the new_message_callback to interact with
the recorded audio after a keyword is spoken. It uses the speech recognition
library in order to convert the recorded audio into text.

Information on installing the speech recognition library can be found at:
https://pypi.python.org/pypi/SpeechRecognition/
"""


interrupted = False


def detectedCallback():
  # 소리 출력
  #play_audio()
  snowboydecoder.play_audio_file()
  # 핵심어 검출 종료
  detector.terminate()
  # 어시스턴스 실행
  a = g_assist.main()
  print(a)
  # 핵심어 검출 재수행
  detector.start(detected_callback=detectedCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

#if len(sys.argv) == 1:
#    print("Error: need to specify model name")
#    print("Usage: python demo.py your.model")
#    sys.exit(-1)

model = 'resources/models/snowboy.umdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.38)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detectedCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()




