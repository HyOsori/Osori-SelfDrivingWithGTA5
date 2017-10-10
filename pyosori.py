import numpy as np
from PIL import ImageGrab
import cv2
import time


def get_frame_from_primary_display(x=0, y=25, width=800, height=615):
        last_time = time.time()

        while(True):
                # bbox=(x, y, width, height), 40은 TitleBar의 높이를 의미
                printscreen_pil = ImageGrab.grab(bbox=(x, y, width, height))

                print('Loop took {} secdons', format(time.time() - last_time))
                last_time = time.time()
                cv2.imshow('OSORI-GTA5', cv2.cvtColor(np.array(printscreen_pil), cv2.COLOR_BGR2RGB)) # BGR to RGB

                # 문자를 "아스키 코드 번호"로 변환하려면 ord() 함수를 사용
                if cv2.waitKey(25) & 0xFF == ord('q'): # waitKey(25) will display a frame for 25 ms
                    cv2.destroyAllWindow()
                    break

if __name__ == "__main__":
        get_frame_from_primary_display()

## Sentdex가 진단한 문제점
## 현재 GTA5는 GPU 위주로 실행되지만
## Frame을 가져오는 일은 CPU로 이뤄지기 때문에 끊겨보임
## 하지만 큰 문제는 아님