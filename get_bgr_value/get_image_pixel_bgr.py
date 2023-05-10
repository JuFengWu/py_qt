import cv2

def print_rgb(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        value = img[x][y]
        print("BGR is " + str(value))

img = cv2.imread("Lenna.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',print_rgb)

while True: #27 is esc ascii code
    cv2.imshow("image", img)
    if  cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
