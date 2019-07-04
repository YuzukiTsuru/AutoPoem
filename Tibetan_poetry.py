from AutoPoem.Model import *
from config import Config


if __name__ == '__main__':
    model = PoetryModel(Config)
    for i in range(3):
        # 藏头诗
        sen = model.predict_hide('我不要你')
        print(sen)

