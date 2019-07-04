### AutoPoem 自动古诗生成器

本项目使用这些技术:

- RNN
- LSTM
- Keras
- Tensorflow

### 输出结果

```reStructuredText
策杖政成时，山无火不白。若生心中心，可为子我间。
侧闻郡守至，入事天新尚。非长吟风病，何过远城不。
候馆扫清昼，静日君心缘。发游心休心，处雪白成间。
晚景微雨歇，归门深长鸟。心间老望回，头柳空月下。
亩浍敷四海，心野无未微。时尚月初行，自不夕闻古。
关河月未晓，雪中人终后。肠异知谁名，堪薄难今生。
```

### 环境配置

模型运行在Python3下,请注意.

```bash
pip install tensorflow Keras h5py numpy

# 如果使用GPU,请使用以下命令
conda install keras-gpu
```

### 调用方法

#### 先进行设置

```python
class Config(object):
    poetry_file = 'dataset/poetry.txt'   # 数据集
    weight_file = 'poetry_model.h5'      # 模型
    max_len = 6                          # 根据前六个字预测第七个字
    batch_size = 128                     # Batch Size
    learning_rate = 0.0005               # Learning Rate
```

#### 写藏头诗

```python
from AutoPoem.Model import *
from config import Config


if __name__ == '__main__':
    model = PoetryModel(Config)
    for i in range(3):
        sen = model.predict_hide('我不要你')
        print(sen)

# 输出:我何人清落，不后百能天。要作欲清自，你知自人九。
```

#### 随机写诗

```python
from AutoPoem.Model import *
from config import Config


if __name__ == '__main__':
    model = PoetryModel(Config)
    for temp in [0.5, 1, 1.5]:
        sen = model.predict_random(temperature=temp)
        print(sen)
        
# 输出:名士竹林隈，人池生行是。事无松有所，有相此门人。
```

### 模型:

![](poetry_model.png)





### 参考了:

- https://github.com/youyuge34/Poems_generator_Keras
- https://github.com/ioiogoo/poetry_generator_Keras

