import cv2
import numpy as np

CAMERA_INDEX = 0

cap = cv2.VideoCapture(CAMERA_INDEX) 

if not cap.isOpened():
    print(f"Error: Gagal membuka kamera di index {CAMERA_INDEX}.")
    exit()

print(f"Berhasil terhubung ke kamera index: {CAMERA_INDEX}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Gagal membaca frame. Koneksi kamera terputus?")
        break

    # Konversi BGR ke HSV (Hue, Saturation, Value)
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(hsvImage, lower_red1, upper_red1)
    
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(hsvImage, lower_red2, upper_red2)
    mask_red = mask_red1 + mask_red2

    # Warna Kuning di HSV
    lower_yellow = np.array([15, 70, 70])
    upper_yellow = np.array([35, 255, 255])
    mask_yellow = cv2.inRange(hsvImage, lower_yellow, upper_yellow)

    # Gabungin semua mask
    final_mask = cv2.bitwise_or(mask_red, mask_yellow)
    result = cv2.bitwise_and(frame, frame, mask=final_mask)
    
    cv2.imshow(f'Deteksi Warna (Kamera Index: {CAMERA_INDEX})', result)
    cv2.imshow('Original', frame)

    # Tombol keluar: pencet 'esc'
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()