from AutoPoem.Model import *
from config import Config


if __name__ == '__main__':
    model = PoetryModel(Config)

    for temp in [0.5, 1, 1.5]:
        # 随机抽取第一句话进行预测
        sen = model.predict_random(temperature=temp)
        print(sen)
