# 請寫程式列出 n 變數的所有真值表可能狀況
### 程式碼
```py
def truthTable(n): # 主函數
	p = [] # p 代表已經排下去的，一開始還沒排，所以是空的
	return tableNext(n, p) # 呼叫 tableNext 遞迴下去排出所有可能

def tableNext(n, p):# n : n個變數的真值表, p :代表已經排下去的
	i = len(p)
	if i == n:  # 全部排好了
		print(p)  # 印出排列
		return
	binary=[0,1]
	for x in binary:
		p.append(x)     # 把 x 放進表
		#print("append:",p)
		tableNext(n, p) # 繼續遞迴尋找下一個排列
		p.pop()         # 把 x 移出表
		#print("pop:",p)
	
a = input("請輸入想要幾個變數:")
truthTable(int(a))
```
### 執行結果
```
python -u "c:\Users\User\桌面\truthtable.py"
請輸入想要幾個變數:3
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
```
### 參考資料
https://gitlab.com/ccc109/ai/-/blob/master/03-search/Q3-queen/truthtable.py