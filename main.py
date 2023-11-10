import cv2
import numpy as np

file_name = "TEST02.jpg"
img = cv2.imread('./IMAGE/'+file_name)

contrast = 1200
brightness = -700
output = img * (contrast/127 + 1) - contrast + brightness # 轉換公式
# 轉換公式參考 https://stackoverflow.com/questions/50474302/how-do-i-adjust-brightness-contrast-and-vibrance-with-opencv-python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
output = np.clip(output, 0, 255)
output = np.uint8(output)

output1 = cv2.dilate(output, kernel)     # 先侵蝕，將白色小圓點移除

cv2.imshow('BEFORE', img)    # 原始圖片
cv2.imshow('mid', output1)    # 原始圖片ˊ
cv2.imshow('AFTER', output) # 調整亮度對比的圖片
cv2.imwrite('./after_image/'+file_name+'_'+'BEFORE.jpg', img)    # 原始圖片
cv2.imwrite('./after_image/'+file_name+'_'+'mid.jpg', output1)    # 原始圖片
cv2.imwrite('./after_image/'+file_name+'_'+'AFTER.jpg', output) # 調整亮度對比的圖片
cv2.waitKey(0)                    # 按下任意鍵停止
cv2.destroyAllWindows()