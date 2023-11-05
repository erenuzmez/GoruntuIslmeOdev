import cv2
import matplotlib.pyplot as plt
img = cv2.imread("C:\\Users\ereny\\The_Photographer.jpg")
histogram = [0] * 256#Boş liste oluşturulur.
for i in range(img.shape[0]):#Piksellere ulaşmak için iç içe for döngüsü.
    for v in range(img.shape[1]):
        piksel_degeri = img[i, v, 0]
        histogram[piksel_degeri] += 1
plt.bar(range(256), histogram, )# Histogramı grafiğe aktarılır.
plt.xlim([0, 255])
plt.show()