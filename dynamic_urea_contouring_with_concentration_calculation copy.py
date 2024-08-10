import numpy as np
import cv2

vid = cv2.VideoCapture(r'/Users/advaybajaj/Desktop/milk tests/milk_plus_2_percent_urea_31072022/trimmed_1.mov')

total_area = 0
cnt = 0

while 1:
    
    cnt+=1
    print("images scanned: ", cnt)
    ret,image = vid.read()
    
    if ret:
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        l = np.array([110,49,219])
        u = np.array([179,255,255])

        mask = cv2.inRange(hsv,l,u)
        gus = cv2.GaussianBlur(mask,(11,11),0)

        #plt.imshow(mask)
        #plt.show()
        i=True
        sum_area = 0

        cont,har = cv2.findContours(gus,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for i in cont:
            area = cv2.contourArea(i)
            if area>750:
                #x,y,w,h = cv2.boundingRect(i)
                cv2.drawContours(image,[i],-1,(0,0,255),2)
                #cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)
                sum_area+=area
                
        length = 640
        breadth = 364
        image_area = length * breadth

        urea_percentage = (sum_area*100) / image_area

        # print("\n\n\n\n\n")
        # print("urea composition: ", urea_percentage, "%" )
        total_area+= urea_percentage       
        
    else:
        break
    
avg_area = total_area/cnt
print(cnt)
print(avg_area)