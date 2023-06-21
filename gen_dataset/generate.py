from config import Config as c
from PIL import Image, ImageDraw
from tqdm import tqdm
import shutil
import random
import os

'''
ЗАДАЧИ
1. Генерация папки для одного элемента
2. Cимуляция движения
3. Симуляция размера
4. Симуляция шума объекта
'''
TRAIN = "train"
TEST = "test"
LENGTH_INDEX = 6 # For, 000001 


def prepare_dataset_folder_structure():
    if os.path.exists(c.OUTPUT_DIR):
        input_ans = True#input(f"Folder: {c.OUTPUT_DIR} will be deleted. Are you sure? [y/n]\n").lower() == "y"
        if not input_ans:
            exit(0)
        shutil.rmtree(c.OUTPUT_DIR)
    os.mkdir(c.OUTPUT_DIR)
    train_dir = os.path.join(c.OUTPUT_DIR, TRAIN)
    test_dir = os.path.join(c.OUTPUT_DIR, TEST)
    os.mkdir(train_dir)
    os.mkdir(test_dir) 
    amp_file_train = os.path.join(train_dir, "result.txt")
    amp_file_test = os.path.join(test_dir, "result.txt")
    os.mknod(amp_file_train)
    os.mknod(amp_file_test)


def create_element_structure(index, mode=TRAIN):
    path = os.path.join(c.OUTPUT_DIR, TRAIN)
    if mode == TEST:
        path = os.path.join(c.OUTPUT_DIR, TEST)
    element_name = f"img{'0' * (LENGTH_INDEX - len(str(index)))}{index}"
    path = os.path.join(path, element_name)
    os.mkdir(path)
    return path


def empty_noise_img(width, height):
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return img



def gen_simple_objects(img):
    draw = ImageDraw.Draw(img)
    for _ in range(3):
    # Случайно выбираем тип объекта (круг или прямоугольник)
        shape = random.choice(['circle', 'rectangle'])
        
        # Случайно выбираем цвет объекта
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Случайно выбираем координаты и размеры объекта
        x1 = random.randint(0, 400)
        y1 = random.randint(0, 400)
        x2 = random.randint(x1, 500)
        y2 = random.randint(y1, 500)
        print(x1, y1, x2, y2)
        # Рисуем объект на изображении
        if shape == 'circle':
            draw.ellipse((x1, y1, x2, y2), fill=color)
        else:
            draw.rectangle((x1, y1, x2, y2), fill=color)


def get_random_amp_factor():
    return random.random() * 10

def save_img(img, path):
    try:
        img.save(path)
    except:
        print(f"Not saved image - {path}")


def generate():
    #img = empty_noise_img(width=500, height=500)
    #gen_simple_objects(img=img)
    #create_element_structure(1)
# Сохраняем изображение
    #img.save('random_image.png')
    print("GEN train dataset")
    for train_index in tqdm(range(c.TRAIN_DATASET_SIZE)):
        path_el = create_element_structure(train_index, TRAIN)
        amp_factor = get_random_amp_factor()
        for frame in c.FRAME_POSTFIXES:
            img = empty_noise_img(width=c.WIDTH, height=c.HEIGHT)
            gen_simple_objects(img=img)
            #print(frame)
            filename = os.path.join(path_el, f"frame{frame}.png")
            save_img(img=img, path=filename)
            #print(filename)
            #print(amp_factor)


    print("GEN test dataset")
    for test_index in tqdm(range(c.TRAIN_DATASET_SIZE)):
        create_element_structure(test_index, TEST)

if __name__ == "__main__":
    prepare_dataset_folder_structure()
    generate()
    print("Done!")