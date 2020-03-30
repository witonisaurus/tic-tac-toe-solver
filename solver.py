import pyscreenshot as ImageGrab
import cv2
import PIL
import numpy as np
import imutils

scale_factor = 0.3

while True:
	screen_img = np.array(ImageGrab.grab())
	screen_img_gray = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)

	template = cv2.imread("sampleBoard.png", 0)
	w, h = template.shape[::-1]

	screen_img_gray = imutils.resize(screen_img_gray, width=int(screen_img_gray.shape[1]*scale_factor))
	template = imutils.resize(template, width=int(template.shape[1]*scale_factor))

	res = cv2.matchTemplate(screen_img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8

	loc = np.where(res >= threshold)

	for pnt in zip(*loc[::-1]):
		cv2.rectangle(screen_img, (int(pnt[0]*(1/scale_factor)),int(pnt[1]*(1/scale_factor))), (int(pnt[0]*(1/scale_factor) + w), int(pnt[1]*(1/scale_factor) + h)), (0,255,255), 2)
		print("det", pnt[0], pnt[1])
		cv2.imwrite("af.png", screen_img)

	cv2.imshow("af", screen_img)


	if cv2.waitKey(1000) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break