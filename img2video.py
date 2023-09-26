import os
import imageio
# from PIL import Image

# set file name and path for the video
filename = 'output.mp4'
filepath = "/home/hefan/puzzles/"

# read all pictures
input_path = "/home/hefan/puzzles/imgs/"
img_paths = os.listdir(input_path)
img_paths.sort(key=lambda x:int(x[:-4].split('_')[0]))
mp4_images = []
for path in img_paths:
    if path[:-4].split('_')[1] == "normal":
        mp4_images.append(imageio.imread(input_path + path))
    elif path[:-4].split('_')[1] == "operate":
        for i in range(10):
            mp4_images.append(imageio.imread(input_path + path))

# turn .jpg to mp4
fps = 10  # 10 frame per second
with imageio.get_writer(filepath + filename, fps=fps) as video:
    for image in mp4_images:
        # frame = image.convert('RGB')
        video.append_data(image)