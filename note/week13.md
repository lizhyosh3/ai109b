# 反傳遞演算法
反傳遞演算法是「誤差反向傳播」的簡稱，是一種與最優化方法（如梯度下降法）結合使用的，用來訓練人工神經網絡的常見方法。該方法對網絡中所有權重計算損失函數的梯度。這個梯度會反饋給最優化方法，用來更新權值以最小化損失函數。

反傳遞演算法要求有對每個輸入值想得到的已知輸出，來計算損失函數梯度。因此，它通常被認為是一種監督式學習方法，雖然它也用在一些無監督網絡（如自動編碼器）中。它是多層前饋網絡的Delta規則的推廣，可以用鏈式法則對每層疊代計算梯度。反向傳播要求人工神經元（或「節點」）的激勵函數可微。
## 概括
反傳遞演算法主要由兩個階段組成：激勵傳播與權重更新。
### 第1階段：激勵傳播
每次疊代中的傳播環節包含兩步：
>1. （前向傳播階段）將訓練輸入送入網絡以獲得激勵響應。
>2. （反向傳播階段）將激勵響應同訓練輸入對應的目標輸出求差，從而獲得輸出層和隱藏層的響應誤差。
### 第2階段：權重更新
對於每個突觸上的權重，按照以下步驟進行更新：
>1. 將輸入激勵和響應誤差相乘，從而獲得權重的梯度。
>2. 將這個梯度乘上一個比例並取反後加到權重上。
這個比例（百分比）將會影響到訓練過程的速度和效果，因此成為「訓練因子」。梯度的方向指明了誤差擴大的方向，因此在更新權重的時候需要對其取反，從而減小權重引起的誤差。
第1和第2階段可以反覆循環疊代，直到網絡對輸入的響應達到滿意的預定的目標範圍為止。
---
### net1.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\03-net\net1.py"
net.forward()= 10
net.backwward()
x= v:1 g:2 y= v:3 g:6 o= v:10 g:1
gfx = x.g/o.g =  2.0 gfy = y.g/o.g= 6.0
```
### net2.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\03-net\net2.py"
0  =>  10
1  =>  9.216
2  =>  8.4934656
3  =>  7.827577896960003
.
.
.
97  =>  0.003635960944957329
98  =>  0.003350901606872675
99  =>  0.003088190920893857
x= 0.01687031935884968 y= 0.050610958076549
```
---
# Pytorch
PyTorch是一個開源的Python機器學習庫，基於Torch，底層由C++實現，應用於人工智慧領域，如自然語言處理。它最初由Facebook的人工智慧研究團隊開發，並且被用於Uber的概率編程軟體Pyro。
PyTorch主要有兩大特徵：
* 類似於NumPy的張量計算，可使用GPU加速。
* 基於帶自動微分系統的深度神經網路。
PyTorch包括torch.nn、torch.optim等子模組。
---
### autograd0.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\04-torch\autograd0.py"
tensor(2.)
tensor(6.)
10.0   
```
### autograd1.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\04-torch\autograd1.py"
tensor(2.)
tensor(6.)
10.0
```
### autograd2.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\04-torch\autograd2.py"
f= 10.0
x.grad= tensor([2., 6.])
```
### torchGd1.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\05-torchGd\torchGd1.py"
99 x= 0.05263785645365715 loss= 3.792219400405884
199 x= 0.4059540331363678 loss= 2.540982484817505
299 x= 0.6951667666435242 loss= 1.702589750289917
.
.
.
4899 x= 1.999867558479309 loss= 0.0       
4999 x= 1.9998914003372192 loss= 0.0      
Result: x = 1.9998916387557983 loss=0.0 
```
### torchGd2.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\05-torchGd\torchGd2.py"
99 parameters= [tensor(0.3926, requires_grad=True)] loss= 2.583590269088745
199 parameters= [tensor(0.6843, requires_grad=True)] loss= 1.7311391830444336       
299 parameters= [tensor(0.9230, requires_grad=True)] loss= 1.1599531173706055  
.
.
.
4899 parameters= [tensor(1.9999, requires_grad=True)] loss= 0.0
4999 parameters= [tensor(1.9999, requires_grad=True)] loss= 0.0
Result: parameters = [tensor(1.9999, requires_grad=True)] loss=0.0
```
### torchGd3.py
* 執行結果
```
python -u "c:\Users\User\ai\07-neural\05-torchGd\torchGd3.py"
x= tensor([-0.0018, -0.0035], requires_grad=True)
```
---
### 參考資料
https://zh.wikipedia.org/wiki/反向传播算法
https://zh.wikipedia.org/wiki/PyTorch