from config import Config as c
from PIL import Image, ImageDraw
import shutil
import random
import os


def prepare_dataset_structure():
    if os.path.exists(c.OUTPUT_DIR):
        input_ans = input(f"Folder: {c.OUTPUT_DIR} will be deleted. Are you sure? [y/n]\n").lower() == "y"
        if not input_ans:
            exit(0)
        shutil.rmtree(c.OUTPUT_DIR)
    os.mkdir(c.OUTPUT_DIR)
    train_dir = os.path.join(c.OUTPUT_DIR, "train")
    test_dir = os.path.join(c.OUTPUT_DIR, "test")
    os.mkdir(train_dir)
    os.mkdir(test_dir) 
    amp_file_train = os.path.join(train_dir, "result.txt")
    amp_file_test = os.path.join(test_dir, "result.txt")
    os.mknod(amp_file_train)
    os.mknod(amp_file_test)


def empty_noise_img(width, height):
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return img


def gen_simple_objects(img):
    draw = ImageDraw.Draw(img)
    for i in range(10):
    # Случайно выбираем тип объекта (круг или прямоугольник)
        shape = random.choice(['circle', 'rectangle'])
        
        # Случайно выбираем цвет объекта
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Случайно выбираем координаты и размеры объекта
        x1 = random.randint(0, 400)
        y1 = random.randint(0, 400)
        x2 = random.randint(x1, 500)
        y2 = random.randint(y1, 500)
        
        # Рисуем объект на изображении
        if shape == 'circle':
            draw.ellipse((x1, y1, x2, y2), fill=color)
        else:
            draw.rectangle((x1, y1, x2, y2), fill=color)


def generate():
    img = empty_noise_img(width=500, height=500)
    gen_simple_objects(img=img)
# Сохраняем изображение
    img.save('random_image.png')

if __name__ == "__main__":
    prepare_dataset_structure()
    generate()