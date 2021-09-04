import os
import cv2


def crop_redmask(path):
    ## Read and merge
    imgs_list = os.listdir(path)
    for img_name in imgs_list:
        img_path = os.path.join(path, img_name)
        img = cv2.imread(img_path)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ## Gen lower mask (0-5) and upper mask (175-180) of RED
        # mask1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
        # mask2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))
        mask1 = cv2.inRange(img_hsv, (0,43,46), (25,255,255))
        mask2 = cv2.inRange(img_hsv, (146,43,46), (190,255,255))
        ## Merge the mask and crop the red regions
        mask = cv2.bitwise_or(mask1, mask2 )
        croped = cv2.bitwise_and(img, img, mask=mask)
        ## Display
        mask_name = img_name.split('.')[0]+"_mask"+'.png'
        crop_name = img_name.split('.')[0] + "_crop" + '.png'
        cv2.imwrite(os.path.join(path, mask_name), mask)
        cv2.imwrite(os.path.join(path, crop_name), croped)

path = r'C:\Users\17562\Desktop\img\pre'
crop_redmask(path)
