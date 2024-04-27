# -*- coding: utf-8 -*-

from PIL import Image

# ��������
image_path = "present.png"
image = Image.open(image_path)

# ��������������ϡ������������
coordinates = [
    (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12),
    (8, 93), (8, 94), (8, 95), (8, 96), (8, 97), (8, 98), (8, 99), (8, 100),
    (8, 157), (8, 158), (8, 159), (8, 160), (8,
                                             161), (8, 162), (8, 163), (8, 164), (8, 165),
    (8, 166), (8, 167), (8, 168), (8, 169), (8, 170), (8, 171)
]

# �������ϡ��������
extracted_pixels = []
for coordinate in coordinates:
    pixel = image.getpixel(coordinate)
    extracted_pixels.append(pixel)

# ������������?�����������?��������
width = len(coordinates)
height = 1
extracted_image = Image.new("RGB", (width, height))
extracted_image.putdata(extracted_pixels)

# ������������
extracted_image_path = "extracted_image.png"
extracted_image.save(extracted_image_path)

print("�������������?:", extracted_image_path)
