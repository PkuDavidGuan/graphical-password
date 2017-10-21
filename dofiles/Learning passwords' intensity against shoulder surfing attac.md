# Learning passwords' intensity against shoulder surfing attacks with neural networks

==introduction和related works打算占1.5页,preliminary打算占1/4页，model占3/4页。实验占1页，最后总结。==

## Introduction

For the vast majority of computer systems, password schemes are always been used to authenticate users. In traditional analysis, researchers attempted to improve the theoretical complexity of password schemes. A significant latent hypothesis in traditional analysis is that the identification process was finished in a relative safe environment, like in people's home or ATMs in the bank. Therefore, attackers had no chance to get any information about the password of users, and they could only use Brute-force attacks, so the high theoretical complexity of password schemes improved strength against these guessing attacks. However, with the development of mobile devices in recent years, password schemes are applied in less safe environments and meet with challenges with peeping attacks. And high theoretical complexity means nothing against such attacks.

In \cite{DBLP:journals/iacr/LiS05}, shoulder surfing attacks are defined as attacks during which adversaries can observe all actions of humans on input terminals and interactions between humans (provers) and computers (verifiers). Attackers may utilize direct observation or high-resolution cameras to record passwords. The theoretical complexity of password schemes will decrease quickly after successive shoulder surfing attacks. For example, the remaining theoretical complexity of text password will decrease to $O(1)$ after attackers recorded the whole authentication process.

In this paper, we utilized neural networks to analyze passwords's intensity against shoulder surfing attacks. We first revised the definition of the password architecture and proposed a indictor to measure passwords' intensity against shoulder surfing attacks. We then bulit up a three-layer neural networks to learn the intensity 

## Related works

据我们所知，我们的工作是第一个。传统的关于shoulder-surfing attack的研究着重于发明抗攻击的密码模型，一些文章提出抗攻击的理论方法，比如\cite{DBLP:journals/iacr/LiS05}提出抗攻击的三个原则 Three Basic Principles： Time-variant responses、 Uncertainty、 Balance，并提出Two General Structures of SecHCI Protocols；另外一些文章提出各个领域的一些抗攻击的密码，\cite{DBLP:conf/icc/ZhangZDLHK17}、\cite{DBLP:conf/percom/MaitiJW17}探讨了在AR中抗攻击的模型，\cite{DBLP:journals/mta/LuoY16}、\cite{DBLP:conf/ic-nc/HigashiyamaYOF15}探讨了phone中抗攻击的模型，他们的弱点在于只能通过用户体验来验证，无法从数学的角度特别完美地去验证抗攻击的能力。

## Preliminaries

这里介绍几个概念，分别是Challenge Space C、Password Space F、Answer Space A，尽量加入数学元素。。。$$f(c) = a, f \in F, c \in C, a \in A $$（其实很简单，以文本密码举例，challenge space是不同提问的数量，文本密码只有一个，就是“请输入你的密码”；password space就是密码的最大数量，字母的排列组合；answer space是用户需要输入在电脑上的信息，这里和password space一样。）

## Model（==这个地方也没想好名字==）

### password architecture

这里把密码系统分成server、user、attacker。server是生成不同的challenge，然后对比用户的answer和标准answer；user是知道密码f，在收到challenge c后，算出answer $a = f(c)$；attacker是可以看到c和a，需要猜$f$。attacker越难猜到密码，密码的强度越高。

### attacker model

这里讲神经网络的结构，分成1位输出和多位输出两种，前者是regression，后者是softmax。

## Experiments

### set up(==实验设置，不知道标准的翻译是不是这个==)

1. 4-bits PIN，代表ATM、支付宝等环境的密码
2. 12-bits text password，代表各种门户网站的密码
3. passface（从一个候选集中选择5张人脸，test时从9个图片中选1个）
4. 九宫格， 最后两个是新兴的图形密码

### Analysis（==这个地方挺重要的，还没有想好==）

这里截取曲面的三个截面，进行分析。（现在我的一个思路是从两个方面着手：第一，从我们的模型来看，密码强度是4>3>2>1；第二，从理论分析，4是一个单射，3是一个双射，2和1都是一个常数函数，所以强度是4>3>2>1。两个方面是自洽的，所以我们的模型是合理的）



