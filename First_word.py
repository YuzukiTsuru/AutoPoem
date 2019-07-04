from AutoPoem.Model import *
from config import Config


if __name__ == '__main__':

    model = PoetryModel(Config)
    for i in range(100):
        # 给出第一个字进行预测
        sen = model.predict_first('山')
        print(sen)
