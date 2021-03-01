# Методы сравнения изображения

## Перцептивный хэш - phash

### Реализация в Python

Установка дополнительных библиотек

```sh
pip3 install Pillow
pip3 install ImageHash
```

Как выглядит хэш:
```sh
98ace3532c6d6c39
```

#### Тестирование 

###### Изображение с исправлениями

||Изображение 1|Изображение 2|
|-----|-----|-----|
|Изображение|![Image1](img/kvar_1.jpg)|![Image2](img/kvar_2.jpg)|
|phash|92de50cb1b6b4f81|82df50cb1b6b4f81
Разница хэша: 2

###### Обрезка изображения

||Изображение 3|Изображение 4|
|-----|-----|-----|
|Изображение|![Image3](img/kvar_3.jpg)|![Image4](img/kvar_4.jpg)|
|phash|d1927eed8361234e|d49b4f6791f9a003
Разница хэша: 22

###### Отзеркаливание изображения

||Изображение 5|Изображение 6|
|-----|-----|-----|
|Изображение|![Image5](img/kvar_5.jpg)|![Image6](img/kvar_6.jpg)|
|phash|98ace3532c6d6c39|cdf9960679383964
Разница хэша: 34

###### Разные изображения

||Изображение 1|Изображение 3|
|-----|-----|-----|
|Изображение|![Image1](img/kvar_1.jpg)|![Image3](img/kvar_3.jpg)|
|phash|92de50cb1b6b4f81|d1927eed8361234e
Разница хэша: 28

#### Код программы
```sh
import os
import time
import imagehash
from PIL import Image

start_time = time.time()

IMAGE_PATH = "img/"
image_1_name = "kvar_1.jpg"
image_2_name = "kvar_2.jpg"

def get_image(image_name):
    return Image.open(IMAGE_PATH + image_name)

def get_hash(image_name):
    image = get_image(image_name)
    return imagehash.phash(image)

def get_difference(hash_x, hash_y):
    return abs(hash_x - hash_y)

img_1_h = get_hash(image_1_name)
img_2_h = get_hash("image_2_name)

print(img_1_h)
print(img_2_h)
print(get_difference(img_1_h, img_2_h))

program_time = time.time() - start_time
print(program_time)

```

# Ссылки:
* ImageHash - https://pypi.org/project/ImageHash/