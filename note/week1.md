# 爬山演算法
爬山演算法是一種局部擇優的方法，採用啟發式方法，是對深度優先搜尋的一種改進，它利用回饋資訊幫助生成解的決策。
爬山演算法一般存在以下問題：
* 局部最大。
* 高地：也稱為平頂，搜尋一旦到達高地，就無法確定搜尋最佳方向，會產生隨機走動，使得搜尋效率降低。
* 山脊：搜尋可能會在山脊的兩面來回震盪，前進步伐很小。
解決方法：隨機重新啟動爬山演算法。
---
# 一維爬山演算法
## 簡易爬山演算法—針對單變數函數
* hillClimbing1.py
```py
def hillClimbing(f, x, dx=0.01):
    while (True):
        print('x={0:.5f} f(x)={1:.5f}'.format(x, f(x)))
        if f(x+dx)>f(x): # 如果右邊的高度 f(x+dx) > 目前高度 f(x) ，那麼就往右走
            x = x + dx
        elif f(x-dx)>f(x): # 如果左邊的高度 f(x-dx) > 目前高度 f(x) ，那麼就往左走
            x = x - dx
        else: # 如果兩邊都沒有比現在的 f(x) 高，那麼這裡就是區域最高點，直接中斷傳回
            break
    return x

# 高度函數
def f(x):
    return -1*(x*x-2*x+1)
    # return -1*(x*x+3*x+5)
    # return -1*abs(x*x-4)

hillClimbing(f, 0) # 以 x=0 為起點，開始呼叫爬山演算法
```
### 執行結果
```
python -u "c:\Users\User\ai\02-optimize\01-hillclimbing\02-var1\hillClimbing1.py"
x=0.00000 f(x)=-1.00000
x=0.01000 f(x)=-0.98010
x=0.02000 f(x)=-0.96040
x=0.03000 f(x)=-0.94090
x=0.04000 f(x)=-0.92160
.
.
.
x=0.98000 f(x)=-0.00040
x=0.99000 f(x)=-0.00010
x=1.00000 f(x)=-0.00000
```
# 二維爬山演算法
## 固定調整法
* hillClimbing2.py
```py
import random

def hillClimbing(f, x, y, h=0.01):
    while (True):
        fxy = f(x, y)
        print('x={0:.3f} y={1:.3f} f(x,y)={2:.3f}'.format(x, y, fxy))
        if f(x+h, y) >= fxy:
            x = x + h
        elif f(x-h, y) >= fxy:
            x = x - h
        elif f(x, y+h) >= fxy:
            y = y + h
        elif f(x, y-h) >= fxy:
            y = y - h
        else:
            break
    return (x,y,fxy)

def f(x, y):
    return -1 * ( x*x - 2*x + y*y + 2*y - 8 )

hillClimbing(f, 0, 0)
```
### 執行結果
```
python -u "c:\Users\User\ai\02-optimize\01-hillclimbing\03-var2\hillClimbing2.py"
x=0.000 y=0.000 f(x,y)=8.000
x=0.010 y=0.000 f(x,y)=8.020
x=0.020 y=0.000 f(x,y)=8.040
x=0.030 y=0.000 f(x,y)=8.059
x=0.040 y=0.000 f(x,y)=8.078
x=0.050 y=0.000 f(x,y)=8.098
.
.
.
x=1.000 y=-0.980 f(x,y)=10.000
x=1.000 y=-0.990 f(x,y)=10.000
x=1.000 y=-1.000 f(x,y)=10.000
```
## 隨機調整法
* hillClimbing2r.py
```py
import random

def hillClimbing(f, x, y, h=0.01):
    failCount = 0
    while (failCount < 10000):
        fxy = f(x, y)
        dx = random.uniform(-h, h)
        dy = random.uniform(-h, h)
        if f(x+dx, y+dy) >= fxy:
            x = x + dx
            y = y + dy
            print('x={0:.3f} y={1:.3f} f(x,y)={2:.3f}'.format(x, y, fxy))
        else:
            failCount = failCount + 1
    return (x,y,fxy)

def f(x, y):
    return -1 * ( x*x -2*x + y*y +2*y - 8 )

hillClimbing(f, 0, 0)
```
### 執行結果
```
python -u "c:\Users\User\ai\02-optimize\01-hillclimbing\03-var2\hillClimbing2r.py"
x=0.007 y=-0.010 f(x,y)=8.000
x=0.013 y=-0.012 f(x,y)=8.033
x=0.020 y=-0.022 f(x,y)=8.049
x=0.025 y=-0.030 f(x,y)=8.082
x=0.031 y=-0.036 f(x,y)=8.107
.
.
.
x=1.000 y=-1.000 f(x,y)=10.000
x=1.000 y=-1.000 f(x,y)=10.000
x=1.000 y=-1.000 f(x,y)=10.000
x=1.000 y=-1.000 f(x,y)=10.000
```
---
### 參考文獻
https://zh.wikipedia.org/wiki/%E7%88%AC%E5%B1%B1%E7%AE%97%E6%B3%95