import os
import cv2
import pandas as pd
# input: txt
# output: csv   >> image_name/category/ltx/lty/w/h

label_path="./wbf/runs/wbf_labels"

label_folder = os.listdir(label_path)
print(len(label_folder))

all_image_name = []
all_c = []
all_ltx = []
all_lty = []
all_w = []
all_h = []


for i in label_folder:
    f = open(label_path+i)
    img = cv2.imread("./datasets/test/images/"+i[:-4]+".png")
    W = img.shape[1]
    H = img.shape[0]

    for line in f.readlines():
        line = line[:-1]
        s = line.split(" ") #class, cx, cy, w, h
        c, cx, cy, w, h =int(s[0]), float(s[1]), float(s[2]), float(s[3]), float(s[4])
        ltx = cx-0.5*w
        lty = cy-0.5*h
        print(i[:-4], c, int(ltx*W), int(lty*H), int(w*W), int(h*H))
        all_image_name.append(i[:-4])
        all_c.append(c)
        all_ltx.append(int(ltx*W))
        all_lty.append(int(lty*H))
        all_w.append(int(w*W))
        all_h.append(int(h*H))


df = pd.DataFrame({'name': all_image_name,
                   'c': all_c,
                   'ltx': all_ltx,
                   'lty': all_lty,
                   'w': all_w,
                   'h': all_h,
                   })
df.to_csv('yolov7andyolor_final.csv',header=None, index=False)




