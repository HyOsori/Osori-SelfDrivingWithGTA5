import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, DirectionKey

DEBUG = True


def region_of_interest(img, vertices):
        """Image Processing 된 결과 이미지에서 적용할 부분만을 반환

        (1) 이미지 크기의 영 행렬 Mask 생성
        (2) Mask 에서 관심 영역(vertices)을 값 1로 변경
        (3) Bitwise And 연산을 이용해 Masking

        Args:
            img (np.array): Input Image
            vertices (np.array): Area For Using Next Image Processing

        Returns:
            np.array: Masked Image
        """
        mask = np.zeros_like(img)
        cv2.fillPoly(mask, vertices, 255)

        masked = cv2.bitwise_and(img, mask)
        return masked


def draw_lines(img, lines):
        """Draw Lines On The Image

        (1)

        Args:
            img (np.array): Input Image
            lines (): Input Lines

        Returns:
            np.array: Image With Lines Added
        """
        try:
            for line in lines:
                coords = line[0]
                cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)
        except:
            pass


def process_img(original_image):
        """Apply Several Image Processing Tech

        (1) BGR to RGB
        (2) Canny Edge Detect
        (3) Remove Results Except Region Of Interest

        Args:
            original_image (np.array): Input Image

        Returns:
            np.array: Processed Image
        """

        # BGR2GRAY: [R, G, B] => [Black/White]
        processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
        processed_image = cv2.GaussianBlur(processed_image, (3, 3), 0)
        vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]], np.int32)
        processed_image = region_of_interest(processed_image, [vertices])

        lines = cv2.HoughLinesP(processed_image, 1, np.pi / 180, 180, np.array([]), 100, 5)
        draw_lines(processed_image, lines)

        return processed_image


def get_frame_from_primary_display(x=25, y=25, width=825, height=615):
        """Get Frame From Monitor from (x, y) to (x + width, y + height)

        Use ImageGrab.grab

        Args:
            x (int): Frame x-pos
            y (int): Frame y-pos
            width (int): Frame Width
            height (int): Frame Height

        Returns:
            np.array: Monitor Screen For Input Area
        """

        if DEBUG:
                last_time = time.time()

        while(True):
                # PressKey(DirectionKey.W.value)  # frame
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
                        breakd

if __name__ == "__main__":

        # gives us time to get situated in the game
        for i in list(range(4))[::-1]:
            print(i + 1)
            time.sleep(1)

        get_frame_from_primary_display()