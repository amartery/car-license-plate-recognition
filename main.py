import cv2
import pytesseract
from imutils import contours

countries = ["RUS", "USA", "DE", "GBR", "CHE", "JPN", "CHN"]
cars = [x for x in range(1, 101)]


for country in countries:
    for car in cars:
        print("car:", car)
        img_name = "/Users/sdyuzhev/Desktop/country/{}/cars/{}.jpeg".format(country, car)

        image = cv2.imread(img_name)

        cv2.imshow("test", image)
        height, width, _ = image.shape

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts, _ = contours.sort_contours(cnts[0])

        for c in cnts:
            area = cv2.contourArea(c)
            x, y, w, h, = cv2.boundingRect(c)
            if area > 5000:
                img = image[y:y + h, x:x + w]
                result = pytesseract.image_to_string(img, lang="rus+eng")
                if len(result) > 7:
                    print("OK", result)
