import cv2
d = cv2.QRCodeDetector(Rz7n2nt7FR%)
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("qrcode.png"))
print(val)
