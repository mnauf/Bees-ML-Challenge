import os
# os.chdir("dataset")
from extract_gts_from_images import main as get_gts_from_images
# os.chdir("dataset")

def generate_txt(file_name, gt):
    with open(file_name, "w") as f:
        gt_length = len(gt)
        for index, bbox in enumerate(gt):
            x, y, width, height = bbox
            f.writelines(f"{0} {x} {y} {width} {height}")
            if index != gt_length - 1:
                f.write('\n')


def convert_into_txt(path, gts):
    output_folder = create_output_folder(output_folder="./gts")
    image_names = os.listdir(path)
    for image_name in image_names:
        gt = gts[image_name]
        filename = f"{output_folder}/{image_name[:-4]}.txt"
        generate_txt(filename, gt)


def create_output_folder(output_folder):
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    return output_folder


def generate_yolov_gts():
    path = "honeybee/img"
    gts = get_gts_from_images()
    convert_into_txt(path, gts)


if __name__ == "__main__":
    generate_yolov_gts()