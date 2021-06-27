# 遺傳演算法
遺傳演算法是計算數學中用於解決最佳化的搜尋演算法，是進化演算法的一種。進化演算法最初是借鑑了進化生物學中的一些現象而發展起來的，這些現象包括遺傳、突變、自然選擇以及雜交等等。
遺傳演算法通常實現方式為一種電腦模擬。對於一個最佳化問題，一定數量的候選解（稱為個體）可抽象表示為染色體，使種群向更好的解進化。傳統上，解用二進位表示（即0和1的串），但也可以用其他表示方法。進化從完全隨機個體的種群開始，之後一代一代發生。在每一代中評價整個種群的適應度，從當前種群中隨機地選擇多個個體（基於它們的適應度），通過自然選擇和突變產生新的生命種群，該種群在演算法的下一次疊代中成為當前種群。
## ketGa.py
```py
from geneticAlgorithm import GeneticAlgorithm
import random

class KeyGA(GeneticAlgorithm):
    def __init__(self, key):
        super().__init__()
        self.key = key

    def randomChromosome(self): # 隨機產生一個染色體 (一個 16 位元的 01 字串)
        bits=[]
        for _ in range(len(self.key)):
            bit = str(random.randint(0,1))
            bits.append(bit)
        return ''.join(bits)
  
    def calcFitness(self, c): # 分數是和 key 一致的位元個數
        fitness=0
        for i in range(len(self.key)):
            fitness += 1 if c[i]==self.key[i] else 0
        return fitness
  
    def crossover(self, c1, c2):
        cutIdx = random.randint(0, len(c1)-1)
        head   = c1[0:cutIdx]
        tail   = c2[cutIdx:]
        return head + tail
    
    def mutate(self, chromosome): # 突變運算
        i=random.randint(0, len(chromosome)-1) # 選擇突變點
        cMutate = chromosome[0:i]+random.choice(['0','1'])+chromosome[i+1:] # 在突變點上隨機選取 0 或 1
        return cMutate # 傳回突變後的染色體

# 執行遺傳演算法，企圖找到 key，最多執行20代，每代族群都是一百人
kga = KeyGA("1010101010101010")
kga.run(100, 20)
```
* geneticAlgorithm.py
```py
import random
import math

class GeneticAlgorithm:
    def __init__(self): 
        self.population = []    # 族群
        self.mutationRate = 0.1 # 突變率

    def run(self, size, maxGen) :  # 遺傳演算法主程式
        self.population = self.newPopulation(size) # 產生初始族群
        for t in range(maxGen):  # 最多產生 maxGen 代
            print("============ generation", t, "===============")
            self.population = self.reproduction() # 產生下一代
            self.dump() # 印出目前族群
  
    def newPopulation(self, size): 
        newPop=[]
        for _ in range(size): 
            chromosome = self.randomChromosome() # 隨機產生新染色體
            newPop.append({'chromosome':chromosome, 
                           'fitness':self.calcFitness(chromosome)})
        newPop.sort(key = lambda c: c['fitness']) # 對整個族群進行排序
        return newPop
  
    # 輪盤選擇法: 隨機選擇一個個體 -- 落點在 i*i ~ (i+1)*(i+1) 之間都算是 i
    def selection(self): 
        n = len(self.population)
        shoot  = random.randint(0, (n*n/2)-1)
        select = math.floor(math.sqrt(shoot*2))
        return self.population[select]
  
    # 產生下一代
    def reproduction(self):
        newPop = []
        for i in range(len(self.population)): 
            parent1 = self.selection()['chromosome'] # 選取父親
            parent2 = self.selection()['chromosome'] # 選取母親
            chromosome = self.crossover(parent1, parent2) # 父母交配，產生小孩
            prob = random.random()
            if prob < self.mutationRate: # 有很小的機率
                chromosome = self.mutate(chromosome) # 小孩會突變
            newPop.append({ 'chromosome':chromosome, 'fitness':self.calcFitness(chromosome) })  # 將小孩放進下一代族群裡
        newPop.sort(key = lambda c: c['fitness']) # 對新一代根據適應性（分數）進行排序
        return newPop
  
    def dump(self):  # 印出一整代成員
        for i in range(len(self.population)):
            print(i, self.population[i])
```
* 執行結果
```
python -u "c:\Users\User\ai\02-optimize\03-genetic\keyGa.py"
============ generation 0 ===============
0 {'chromosome': '0101000001010110', 'fitness': 4}
1 {'chromosome': '0110100101110101', 'fitness': 5}
2 {'chromosome': '0001000010010101', 'fitness': 5}
3 {'chromosome': '0111110111011001', 'fitness': 5}
.
.
.
97 {'chromosome': '1010101010101010', 'fitness': 16}
98 {'chromosome': '1010101010101010', 'fitness': 16}
99 {'chromosome': '1010101010101010', 'fitness': 16}
```
---
# 凱薩加密
凱撒加密是一種最簡單且最廣為人知的加密技術。凱撒加密是一種替換加密技術，明文中的所有字母都在字母表上向後（或向前）按照一個固定數目進行偏移後被替換成密文。例如，當偏移量是3的時候，所有的字母A將被替換成D，B變成E，以此類推。這個加密方法是以羅馬共和時期凱撒的名字命名的，據稱當年凱撒曾用此方法與其將軍們進行聯繫。

凱撒加密通常被作為其他更複雜的加密方法中的一個步驟，例如維吉尼亞密碼。凱撒加密還在現代的ROT13系統中被應用。但是和所有的利用字母表進行替換的加密技術一樣，凱撒加密非常容易被破解，而且在實際應用中也無法保證通信安全。
---
# 維吉尼亞密碼
維吉尼亞密碼是使用一系列凱撒加密組成密碼字母表的加密算法，屬於多表密碼的一種簡單形式。

維吉尼亞密碼曾多次被發明。該方法最早記錄在吉奧萬·巴蒂斯塔·貝拉索於1553年所著的書《吉奧萬·巴蒂斯塔·貝拉索先生的密碼》中。然而，後來在19世紀時被誤傳為是法國外交官布萊斯·德·維吉尼亞所創造，因此現在被稱為「維吉尼亞密碼」。

維吉尼亞密碼以其簡單易用而著稱，同時初學者通常難以破解，因而又被稱為「不可破譯的密碼」（法語：le chiffre indéchiffrable）。這也讓很多人使用維吉尼亞密碼來加密的目的就是為了將其破解
---
# ROT13
ROT13是一種簡易的替換式密碼。ROT13是一種在英文網路論壇用作隱藏八卦、妙句、謎題解答以及某些髒話的工具，目的是逃過版主或管理員的匆匆一瞥。ROT13被描述成「雜誌字謎上下顛倒解答的Usenet對等體」。ROT13也是過去在古羅馬開發的凱撒加密的一種變體。

ROT13是它自己本身的逆反；也就是說，要還原ROT13，套用加密同樣的演算法即可得，故同樣的操作可用再加密與解密。該演算法並沒有提供真正的密碼學上的保全，故它不應該被套用在需要保全的用途上。它常常被當作弱加密範例的典型。ROT13激勵了廣泛的線上書信撰寫與字母遊戲，且它常於新聞群組對話中被提及。
---
### 參考文獻
https://zh.wikipedia.org/wiki/遗传算法
https://zh.wikipedia.org/wiki/凱撒密碼
https://zh.wikipedia.org/wiki/维吉尼亚密码
https://zh.wikipedia.org/wiki/ROT13