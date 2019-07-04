from AutoPoem.Model import *
from config import Config

if __name__ == '__main__':
    model = PoetryModel(Config)
    for i in range(3):
        # 给出第一句话进行预测
        sen = model.predict_sen('山为斜好几，')
        print(sen)
