import cv2
import os
import numpy as np


def main():
    image_names = os.listdir("honeybee/gt-dots")
    path = r"D:\hasty_ML_challenge\bees\honeybee\gt-dots"
    bee_path = r"D:\hasty_ML_challenge\bees\honeybee\img"
    white = [255, 255, 255]
    locations = {}

    for image_name in image_names:
        bee_image, bee_image_name, image_rgb = read_images(bee_path, image_name, path)
        location = convert_white_pixels_into_yolo_gts(image_rgb, white)
        locations[bee_image_name] = location

    return locations


def convert_white_pixels_into_yolo_gts(image_rgb, white):
    location = []
    for y in range(480):
        for x in range(640):
            if np.array_equal(image_rgb[y][x], white):
                height, width, x_cordinate, y_cordinate = generate_width_height(x, y)
                height, width, x_cordinate, y_cordinate = normalize_coordinates(x_cordinate, y_cordinate, width, height)
                height, width, x_center, y_center = precise_upto_6_decimal_places(height, width, x_cordinate,
                                                                                  y_cordinate)
                location.append([x_center, y_center, width, height])
    return location

def read_images(bee_path, image_name, path):
    bee_image_name = "beeType1_" + image_name[4:-4] + ".jpg"
    image = cv2.imread(os.path.join(path, image_name))
    bee_image = cv2.imread(os.path.join(bee_path, bee_image_name))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return bee_image, bee_image_name, image_rgb


def normalize_coordinates(x_cordinate, y_cordinate, width, height):
    x_cordinate = x_cordinate / 640
    y_cordinate = y_cordinate / 480

    width = width / 640
    height = height / 480

    return height, width, x_cordinate, y_cordinate

def generate_width_height(x_centroid, y_centroid):
    end_point, start_point, x_centroid, y_centroid = recenter_centroid_coordinates(x_centroid, y_centroid)
    width = (x_centroid - start_point[0]) + (end_point[0] - x_centroid)
    height = (y_centroid - start_point[1]) + (end_point[1] - y_centroid)
    return height, width, x_centroid, y_centroid


def recenter_centroid_coordinates(x, y):
    start_point = (max(x - 17, 0), max(y - 17, 0))
    end_point = (min(x + 17, 640), min(y + 17, 480))
    color = (255, 0, 0)
    thickness = 2
    x_cordinate = (start_point[0] + end_point[0]) / 2
    y_cordinate = (start_point[1] + end_point[1]) / 2
    # image = cv2.rectangle(bee_image, start_point, end_point, color, thickness)
    return end_point, start_point, x_cordinate, y_cordinate


def precise_upto_6_decimal_places(height, width, x_cordinate, y_cordinate):
    x_center = "{:.6f}".format(round(x_cordinate, 6))
    y_center = "{:.6f}".format(round(y_cordinate, 6))
    width = "{:.6f}".format(round(width, 6))
    height = "{:.6f}".format(round(height, 6))
    return height, width, x_center, y_center


if __name__ == '__main__':
    main()