from yolov5.sample_solution import main, parse_opt


def test_prediction():
    opt = parse_opt()
    opt.source = "yolov5/beeType1_115.jpg"
    opt.weights = "yolov5/custom_model.pt"
    total_bees = main(opt)
    assert total_bees == 27

