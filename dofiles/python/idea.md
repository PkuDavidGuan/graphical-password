# Idea
------------------------------
## Text password
### 4-bit PIN
- input: 4位数字
- password：与input相同
- output：与input相同
### 12-bit 不定长密码

每一位可能有94种选择，又可能不定长，所以为95种选择。

- input：约等于12*(94+1)
- password:与input相同
- output：与input相同
## Graphical password
passface：从一个候选集中选择5张人脸，test时从9个图片中选1个
- input:100维向量，5维为1
- password：100维向量，5维为1
- output：3维向量

## Good graphical password
9宫格
- input
- password
- output

> 2017/09/23
> 修改idea，神经网络的输入采用onehot编码，输出为一个softmax层。结果很不错。打算每种密码都是先用全部的数据训练，最后再想怎么改。
> 2017/09/25
> 初期的数据已经做好，简单的网络也已经架构好，下边想怎么评价和构图。
- 几个问题
    - training的数据量和epoch数怎么定，是只更改training set大小还是也更改训练的epoch数？
        - 应该是只改变数据量。我们是站在攻击者的角度思考的，故不限制epoch，采用early stopping的方法
    - 准确率的指标 