import os
from dataset.run import create_output_folder, generate_txt
from dataset.extract_gts_from_images import normalize_coordinates
import numpy as np


def test_create_output_folder():
    create_output_folder("testing")
    assert os.path.isdir("testing") == True
    os.removedirs("testing")


def read_txt(filename):
    with open(filename) as f:
        return f.read()


def test_generate_txt():
    class_id = 0
    filename = "testing.txt"
    gt = [[0, 1, 5, 5]]
    generate_txt(filename, gt)
    output = read_txt(filename)
    assert output == f"{class_id} " + " ".join(str(x) for x in gt[0])
    os.remove(filename)


def test_normalize_coordinates():
    x_cordinate = 640
    y_cordinate = 480
    width = 640
    height = 480
    assert np.array_equal([1,1,1,1], normalize_coordinates(x_cordinate, y_cordinate, width, height))