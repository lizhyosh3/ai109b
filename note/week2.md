# 爬山演算法結構
* hillClimbing.py
```py
def hillClimbing(s, maxGens, maxFails):   # 爬山演算法的主體函數
    print("start: ", s.str())             # 印出初始解
    fails = 0                             # 失敗次數設為 0
    # 當代數 gen<maxGen，且連續失敗次數 fails < maxFails 時，就持續嘗試尋找更好的解。
    for gens in range(maxGens):
        snew = s.neighbor()               #  取得鄰近的解
        sheight = s.height()              #  sheight=目前解的高度
        nheight = snew.height()           #  nheight=鄰近解的高度
        if (nheight >= sheight):          #  如果鄰近解比目前解更好
            print(gens, ':', snew.str())  #    印出新的解
            s = snew                      #    就移動過去
            fails = 0                     #    移動成功，將連續失敗次數歸零
        else:                             #  否則
            fails = fails + 1             #    將連續失敗次數加一
        if (fails >= maxFails):
            break
    print("solution: ", s.str())          #  印出最後找到的那個解
    return s                              #    然後傳回。
```
## 抽象的解答類別
* solution.py
```py
class Solution: # 解答的物件模版 (類別)
    def __init__(self, v, step = 0.01):
        self.v = v       # 參數 v 為解答的資料結構
        self.step = step # 每一小步預設走的距離

    # 以下兩個函數至少需要覆蓋掉一個，否則會無窮遞迴
    def height(self): # 爬山演算法的高度函數
        return -1*self.energy()               # 高度 = -1 * 能量

    def energy(self): # 尋找最低點的能量函數
        return -1*self.height()               # 能量 = -1 * 高度
```
---
### hillClimbingNumber.py
* 框架
```py
class SolutionNumber(Solution):
    def neighbor(self): # 單變數解答的鄰居函數。
        x = self.v
        dx= self.step               # x:解答 , dx : 移動步伐大小
        xnew = x+dx if random.random() > 0.5 else x-dx # 用亂數決定向左或向右移動
        return SolutionNumber(xnew) # 建立新解答並傳回。

    def energy(self):               # 能量函數
        x = self.v                  # x:解答
        return abs(x*x-4)           # 能量函數為 |x^2-4|

    def str(self): # 將解答轉為字串，以供印出觀察。
        return "energy({:.3f})={:.3f}".format(self.v, self.energy())
```
* 執行結果
```
python -u "c:\Users\User\ai\02-optimize\01-hillclimbing\04-framework\hillClimbingNumber.py"
start:  energy(0.000)=4.000
0 : energy(-0.010)=4.000
4 : energy(-0.020)=4.000
.
.
.
392 : energy(-1.980)=0.080
393 : energy(-1.990)=0.040
394 : energy(-2.000)=0.000
solution:  energy(-2.000)=0.000
```
### 執行hillClimbingArray.py
* 框架
```py
class SolutionArray(Solution):
    def neighbor(self):           #  多變數解答的鄰居函數。
        nv = self.v.copy()        #  nv=v.clone()=目前解答的複製品
        i = randint(0, len(nv)-1) #  隨機選取一個變數
        if (random() > 0.5):      #  擲骰子決定要往左或往右移
            nv[i] += self.step
        else:
            nv[i] -= self.step
        return SolutionArray(nv)  #  傳回新建的鄰居解答。

    def energy(self): #  能量函數
        x, y, z =self.v
        return x*x+3*y*y+z*z-4*x-3*y-5*z+8 #  (x^2+3y^2+z^2-4x-3y-5z+8)

    def str(self):    #  將解答轉為字串的函數，以供列印用。
        return "energy({:s})={:f}".format(str(self.v), self.energy())
```
* 執行結果
```
python -u "c:\Users\User\ai\02-optimize\01-hillclimbing\04-framework\hillClimbingArray.py"
start:  energy([1, 1, 1])=1.000000
0 : energy([1, 1, 1.01])=0.970100
2 : energy([1.01, 1, 1.01])=0.950200
.
.
.
914 : energy([2.000000000000001, 0.49999999999999956, 2.4799999999999907])=-2.999600
919 : energy([2.000000000000001, 0.49999999999999956, 2.4899999999999904])=-2.999900
920 : energy([2.000000000000001, 0.49999999999999956, 2.4999999999999902])=-3.000000
solution:  energy([2.000000000000001, 0.49999999999999956, 2.4999999999999902])=-3.000000
```
### 執行hillClimbingScheduling.py
* 框架
```py
courses = [
{'teacher': '  ', 'name':'　　', 'hours': -1},
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']

rooms = ['A', 'B']

slots = [
'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

cols = 7

def randSlot() :
    return randint(0, len(slots)-1)

def randCourse() :
    return randint(0, len(courses)-1)


class SolutionScheduling(Solution) :
    def neighbor(self):    # 單變數解答的鄰居函數。
        fills = self.v.copy()
        choose = randint(0, 1)
        if choose == 0: # 任選一個改變 
            i = randSlot()
            fills[i] = randCourse()
        elif choose == 1: # 任選兩個交換
            i = randSlot()
            j = randSlot()
            t = fills[i]
            fills[i] = fills[j]
            fills[j] = t
        return SolutionScheduling(fills)                  # 建立新解答並傳回。

    def height(self) :      # 高度函數
        courseCounts = [0] * len(courses)
        fills = self.v
        score = 0
        # courseCounts.fill(0, 0, courses.length)
        for si in range(len(slots)):
            courseCounts[fills[si]] += 1
            #                        連續上課:好                   隔天:不好     跨越中午:不好
            if si < len(slots)-1 and fills[si] == fills[si+1] and si%7 != 6 and si%7 != 3:
                score += 0.1
            if si % 7 == 0 and fills[si] != 0: # 早上 8:00: 不好
                score -= 0.12
        
        for ci in range(len(courses)):
            if (courses[ci]['hours'] >= 0):
                score -= abs(courseCounts[ci] - courses[ci]['hours']) # 課程總時數不對: 不好
        return score

    def str(self) :    # 將解答轉為字串，以供印出觀察。
        outs = []
        fills = self.v
        for i in range(len(slots)):
            c = courses[fills[i]]
            if i%7 == 0:
                outs.append('\n')
            outs.append(slots[i] + ':' + c['name'])
        return 'score={:f} {:s}\n\n'.format(self.energy(), ' '.join(outs))
    
    @classmethod
    def init(cls):
        fills = [0] * len(slots)
        for i in range(len(slots)):
            fills[i] = randCourse()
        return SolutionScheduling(fills)
```
* 執行結果
```
python -u "c:\Users\User\ai\02-optimize\01-hillclimbing\04-framework\hillClimbingScheduling.py"
solution:  score=-3.880000
 A11:電子 A12:電子 A13:電子 A14:電子 A15:離散 A16:離散 A17:離散
 A21:　　 A22:工數 A23:工數 A24:工數 A25:演算 A26:演算 A27:演算
 A31:　　 A32:計概 A33:計概 A34:計概 A35:行動 A36:行動 A37:行動
 A41:　　 A42:網站 A43:網站 A44:網站 A45:視窗 A46:視窗 A47:視窗
 A51:　　 A52:軟工 A53:軟工 A54:軟工 A55:系統 A56:系統 A57:系統
 B11:　　 B12:科學 B13:科學 B14:科學 B15:網頁 B16:網頁 B17:網頁
 B21:　　 B22:網路 B23:網路 B24:網路 B25:智慧 B26:智慧 B27:智慧
 B31:　　 B32:　　 B33:動畫 B34:動畫 B35:結構 B36:結構 B37:結構
 B41:　　 B42:機率 B43:機率 B44:動畫 B45:線代 B46:線代 B47:線代
 B51:　　 B52:媒體 B53:媒體 B54:媒體 B55:嵌入 B56:嵌入 B57:嵌入
```
### 執行hillClimbingEquation.py
* 框架
```py
class SolutionEquation(Solution):
    def neighbor(self):    #  多變數解答的鄰居函數。
        nx = self.v.copy()              #  複製目前解的矩陣
        rows = nx.shape[0]
        #  修改了這裡：最多改變 n 個維度(只是某些 n 維的例子可以，無法確定一定可以，除非能證明能量函數只有一個低點)
        for _ in range(rows):         #  原本只改一維，會找不到！
            i = randint(0, rows-1) #  隨機選取一個變數
            if (random() > 0.5):                    #  擲骰子決定要往左或往右移
                nx[i][0] += self.step * random()  #  原本是 nx.m[i][0] += self.step 
            else:
                nx[i][0] -= self.step * random()  #  原本是 nx.m[i][0] -= self.step 

        return SolutionEquation(nx)                    #  傳回新建的鄰居解答。

    def energy(self):      #  能量函數:計算 ||AX-B||，也就是 ||Y-B||
        X = self.v
        Y = A.dot(X)
        return LA.norm(Y-B, 2)

    def str(self):    #  將解答轉為字串的函數，以供列印用。
        return "energy({:s})={:f}".format(str(self.v.transpose()), self.energy())

    @classmethod
    def zero(cls):
        return SolutionEquation(np.zeros((3,1)))
```
* 執行結果
```
python -u "c:\Users\User\ai\02-optimize\01-hillclimbing\04-framework\hillClimbingEquation.py"
start:  energy([[0. 0. 0.]])=2.449490
1 : energy([[-0.00609901  0.00928858  0.        ]])=2.444282
2 : energy([[-0.00599859  0.01631615  0.        ]])=2.432737
3 : energy([[-0.01386364  0.02253069  0.00673913]])=2.416567
.
.
.
5584 : energy([[-5.00051891  3.00704409  1.9969727 ]])=0.003237
5599 : energy([[-4.99964782  3.00560519  1.9969727 ]])=0.002775
5718 : energy([[-4.99964782  3.00093459  1.99935104]])=0.000443
solution:  energy([[-4.99964782  3.00093459  1.99935104]])=0.000443
```
---
# 模擬退火法
## 演算法
```
Algorithm SimulatedAnnealing(s)
  while (溫度還不夠低，或還可以找到比 s 更好的解 s' 的時候)
    根據能量差與溫度，用機率的方式決定是否要移動到新解 s'。
    # (機率：溫度高時可以往上走，溫度低的時候差不多只能往下走)
    將溫度降低一些
  end
end
```
## 演算步驟
### 初始化
由一個產生函數從當前解產生一個位於解空間的新解，並定義一個足夠大的數值作為初始溫度。
### 疊代過程
疊代過程是模擬退火算法的核心步驟，分為新解的產生和接受新解兩部分：
>1. 由一個產生函數從當前解產生一個位於解空間的新解；為便於後續的計算和接受，減少算法耗時，通常選擇由當前新解經過簡單地變換即可產生新解的方法，如對構成新解的全部或部分元素進行置換、互換等，注意到產生新解的變換方法決定了當前新解的鄰域結構，因而對冷卻進度表的選取有一定的影響。
>2. 計算與新解所對應的目標函數差。因為目標函數差僅由變換部分產生，所以目標函數差的計算最好按增量計算。事實表明，對大多數應用而言，這是計算目標函數差的最快方法。
>3. 判斷新解是否被接受，判斷的依據是一個接受準則，最常用的接受準則是Metropolis準則：若Δt′<0則接受S′作為新的當前解S，否則以概率exp（-Δt′/T）接受S′作為新的當前解S。
>4. 當新解被確定接受時，用新解代替當前解，這只需將當前解中對應於產生新解時的變換部分予以實現，同時修正目標函數值即可。此時，當前解實現了一次疊代。可在此基礎上開始下一輪試驗。而當新解被判定為捨棄時，則在原當前解的基礎上繼續下一輪試驗。
模擬退火算法與初始值無關，算法求得的解與初始解狀態S（是算法疊代的起點）無關；模擬退火算法具有漸近收斂性，已在理論上被證明是一種以概率1收斂於全局最優解的全局優化算法；模擬退火算法具有並行性。
### 停止準則
疊代過程的停止準則：溫度T降至某最低值時，完成給定數量疊代中無法接受新解，停止疊代，接受當前尋找的最優解為最終解。
### 退火方案
在某個溫度狀態T下，當一定數量的疊代操作完成後，降低溫度T，在新的溫度狀態下執行下一個批次的疊代操作。
---
### 參考文獻
https://zh.wikipedia.org/wiki/模拟退火