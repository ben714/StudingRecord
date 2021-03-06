# -*- coding: utf-8 -*-
# import 进openCV的库
import cv2
import os
import time
from wxpy import *

"""
树莓派打造智能看门狗
sudo pip3 install opencv-python
sudo pip3 install wechat_sender
"""

bot = Bot()
my_friend = bot.friends().search('监控狗')[0]


# 调用摄像头检测人脸并截图
def camera(window_name, path_name):

    # Linux 不显示图形界面
    # cv2.namedWindow(window_name)

    # 视频来源，来自USB摄像头
    cap = cv2.VideoCapture(0)

    # 告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier(os.getcwd()+"/haarcascade/haarcascade_frontalface_alt.xml")

    # 识别出人脸后要画的边框的颜色，RGB格式, color是一个不可增删的数组
    color = (0, 255, 0)

    num = 0
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break

        # 将当前桢图像转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                num = num+1
                # 将当前帧保存为图片
                img_name = "%s/%d.jpg" % (path_name, num)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                print("有人来了~~~")
                alarm(num)
                # 延迟 60s，不要太频繁的发送，知道来了就可以了
                time.sleep(60)
                # 画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                # 显示当前捕捉到了多少人脸图片了
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, 'num:%d/1000' % (num), (x + 30, y + 30), font, 1, (255, 0, 255), 4)

        # 显示图像 Linux 下注释掉即可
        # cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break
    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


def alarm(num):
    print("发送微信通知")
    # 看门狗
    my_friend.send('有人闯进卧室了!')
    my_friend.send_image(os.getcwd()+"/dog/"+str(num)+".jpg")


if __name__ == '__main__':
    camera("watchdog", os.getcwd()+"/dog")

