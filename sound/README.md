핵심어 검출 및 대화 모듈 구현

대화 모듈의 경우, 구글 어시스턴스를 활용

그러나 구글 어시스턴스는 핵심어 검출 기능을 제공하지 않아 별도의 snowboy 핵심어 검출 패키지를 활용

구글 어시스턴스 설정 과정
- https://developers.google.com/assistant/sdk/guides/service/python/embed/setup

snowboy 핵심어 검출 설정 과정
- https://github.com/Kitt-AI/snowboy

설치 완료 후, snowboy/examples/Python3 폴더에서 코드 build후 my_demo.py 코드 추가
~/env/lib/python3.x/site_packages/googlesamples/assistant/grpc 폴더에 pushtotalk_fix.py추가

snowboy/examples/Python3 폴더에 my_demo.py 코드 추가

해당 코드를 통해 robot-user 간 음성인식을 통한 communication 진행





