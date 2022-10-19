###################################################
#相当于同学人脸信息采集
###################################################
from get_data import CatchPICFromVideo

while True:
    print("是否录入同学信息(yes or no)?")
    if input() == 'yes':
        #同学姓名(要输入英文，汉字容易报错)
        new_user_name = input("请输入您的姓名：")

        print("请看摄像头！")

        #采集员工图像的数量自己设定，越多识别准确度越高，但训练速度贼慢
        window_name = '信息采集'                                                                                  #图像窗口
        camera_id = 0                                                                                            #相机的ID号
        images_num = 100                                                                                        #采集图片数量
        path = 'D:\Face_recognition\data\\' + new_user_name   #图像保存位置

        CatchPICFromVideo(window_name,camera_id,images_num,path)
    else:
        break