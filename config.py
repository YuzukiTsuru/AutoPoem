class Config(object):
    poetry_file = 'dataset/poetry.txt'
    weight_file = 'poetry_model.h5'
    # 根据前六个字预测第七个字
    max_len = 6
    batch_size = 128
    learning_rate = 0.0005
