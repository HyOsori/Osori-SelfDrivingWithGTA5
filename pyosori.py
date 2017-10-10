import numpy as np
from PIL import ImageGrab
import cv2
import time

DEBUG = True


def process_img(original_image):

        # BGR2GRAY: [R, G, B] => [Black/White]
        processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)

        return processed_image


def get_frame_from_primary_display(x=0, y=25, width=800, height=615):

        if DEBUG:
                last_time = time.time()

        while(True):
                # bbox=(x, y, width, height), 40은 TitleBar의 높이를 의미
                screen = np.array(ImageGrab.grab(bbox=(x, y, width, height)))
                new_screen = process_img(screen)

                if DEBUG:
                        print('Loop took {} secdons', format(time.time() - last_time))
                        last_time = time.time()

                cv2.imshow('OSORI-GTA5', np.array(new_screen))

                # 문자를 "아스키 코드 번호"로 변환하려면 ord() 함수를 사용
                if cv2.waitKey(25) & 0xFF == ord('q'): # waitKey(25) will display a frame for 25 ms
                        cv2.destroyAllWindow()
                        break

if __name__ == "__main__":
        get_frame_from_primary_display()

## Lecture 1
## Sentdex가 진단한 문제점
## 현재 GTA5는 GPU 위주로 실행되지만
## Frame을 가져오는 일은 CPU로 이뤄지기 때문에 끊겨보임
## 하지만 큰 문제는 아님

## Lecture 2
## OpenCV를 이용한 Edge 검출은 차후에 있을
## Neural Network  학습에 필요한 데이터 생성을 위해 필요하다고 함
## Canny Edge 검출 방법을 사용