# Real example the usage of multiprocessing in python
# processing each image simultaneously


#import library
import time
import concurrent.futures
from PIL import Image, ImageFilter

# list of name of the image files
img_names = [
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg',
    'photo-1603608788391-14b8d9c2ec54.jpg',
    'photo-1592308172888-b7ddcd76fa22.jpg',
    'photo-1603536022807-ef8f002d1b2f.jpg',
    'photo-1603657524073-29d513dce10d.jpg',
    'photo-1603632076161-5836b146638c.jpg'
]

processed_path = './[3] Intermediate Python/multiprocessing/processed'
file_path = './[3] Intermediate Python/multiprocessing'
# size for resizing image
size = (1200, 1200)

# function for processing image and resizing smaller


def resizing_image(img_name):
    img = Image.open(f'{file_path}/{img_name}')
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'{processed_path}/{img_name}')
    print(f'{img_name} processed.... \n')


# ======================================================
# MULTIPROCESSING FOR MULTIPLE IMAGE FILE PROCESSING
# ======================================================
if __name__ == '__main__':
    start = time.perf_counter()  # start performance counter

    # # without mp
    # for img_name in img_names:
    #     resizing_image(img_name)

    # using mp
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(resizing_image, img_names)

    finish = time.perf_counter()  # finish performance counter

    # counting duration with round from start to finish
    duration = round(finish - start, 2)

    # printing the duration
    print(f'Code finished in {duration} second(s)\n\n')
