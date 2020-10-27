# Real example the usage of threading in python
# requesting and downloading each image simultaneously

# import library
import requests
import time
import concurrent.futures
# import os.path

# list of image url from unsplash website
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c',
    'https://images.unsplash.com/photo-1603608788391-14b8d9c2ec54',
    'https://images.unsplash.com/photo-1592308172888-b7ddcd76fa22',
    'https://images.unsplash.com/photo-1603536022807-ef8f002d1b2f',
    'https://images.unsplash.com/photo-1603657524073-29d513dce10d',
    'https://images.unsplash.com/photo-1603632076161-5836b146638c'

]

file_path = './[3] Intermediate Python/threading/'

# download_imamge function
# to request and downloading image into a .jpg file


def download_image(img_url):
    img_bytes = requests.get(img_url).content  # get content bytes
    img_name = img_url.split('/')[3]  # get image name from url
    img_name = f'{img_name}.jpg'  # change into .jpg file
    # write binary into img_name to make a valid file
    with open(f'{file_path}{img_name}', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} downloaded.... \n')


# ======================================================
# THREADING TO REQUEST AND DOWNLOAD IMAGE SIMULTANEOUSLY
# ======================================================

if __name__ == '__main__':
    start = time.perf_counter()  # start performance counter

    # without threading
    # for img_url in img_urls:
    #     download_image(img_url)

    # with threading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    finish = time.perf_counter()  # finish performance counter

    # counting duration with round from start to finish
    duration = round(finish - start, 2)
    # printing the duration
    print(f'Code finished in {duration} second(s)\n\n')
