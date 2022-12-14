# LeetCodePractice

O(1)：陣列讀取
時間複雜度為 O(1) 的演算法，代表著不管你輸入多少個東西，程式都會在同一個時間跑完。在程式設計中，最簡單的例子就是讀取一個陣列中特定索引值的元素

範例
```commandline
Pokemons = ["卡丘","胖丁","尼龜","比獸","呆獸","種子","小剛"]
n = 0
print(Pokemons[n])
>> "卡丘"
```
---

O(n)：簡易搜尋
時間複雜度為 O(n) 的演算法，代表著執行步驟會跟著輸入 n 等比例的增加。

範例
```commandline
Pokemons = ["卡丘","胖丁","尼龜","比獸","呆獸","種子","小剛"]
for Pokemon in Pokemons:
  if Pokemon == "呆獸":
    print("找到呆獸！")
    break
  else:
    print("這個櫃子裡不是呆獸")
```

---

O(log n)：二分搜尋
時間複雜度為 O(log n) 的演算法（這邊的 log 都是以二為底），代表當輸入的數量是 n 時，執行的步驟數會是 log n。（讓忘記 log 是什麼的同學們複習一下，當 log n = x 的意思是 n = 2^x

範例
```commandline
Numbers = [5,17,33,41,55,61,80]
Find = 55
​
low = 0
high = len(Numbers) - 1
​
while low <= high:
    mid = (low + high) / 2
    if Numbers[mid] > Find:
        high = mid - 1
    elif Numbers[mid] < Find:
        low = mid + 1
    else:
        break
​
print(mid)
```

---

O(nlogn)：合併排序 (Merge Sort)
時間複雜度為 O(n log n) 的演算法，代表著執行時間會隨著以二為底的 log n 再乘上 n 成長。最常見的例子是合併排序法 (Merge Sort) 與快速排序法 (Quick Sort)

範例
```commandline
def Merge_Sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
​
        Merge_Sort(left_array)
        Merge_Sort(right_array)
​
        right_index = 0;
        left_index = 0;
        merged_index = 0;
        while right_index < len(right_array) and left_index < len(left_array):
            if(right_array[right_index] < left_array[left_index]):
                array[merged_index] = right_array[right_index]
                right_index = right_index + 1
            else:
                array[merged_index] = left_array[left_index]
                left_index = left_index + 1
​
            merged_index = merged_index + 1
​
        while right_index < len(right_array):
            array[merged_index] = right_array[right_index]
            right_index = right_index + 1
            merged_index = merged_index + 1
​
        while left_index < len(left_array):
            array[merged_index] = left_array[left_index]
            left_index = left_index + 1
            merged_index = merged_index + 1
​
Numbers = [41, 33, 17, 80, 61, 5, 55]
Merge_Sort(Numbers)
print(Numbers)
```

---

O(n²)：

(1)選擇排序 (Selection Sort)
時間複雜度為 O(n²) 的演算法，代表著執行步驟會跟著輸入 n 成次方比例的增加。最基礎的排序法之一：選擇排序法(Selection Sort) 是 O(n²) 複雜度的代表。

(2)插入排序法 (Insertion Sort)
同樣擁有 O(n²) 時間複雜度，插入排序法 Insertion Sort 則是另外一個非常常見的排序法。簡單來說，插入排序法就是你玩撲克牌時用到的排序法。

範例
```commandline
Numbers = [41,33,17,80,61,5,55]
​
length = len(Numbers)
for i in range(length-1):
    min_index = i
    for j in range(i+1, length):
        if Numbers[min_index] > Numbers[j]:
            min_index = j
    Numbers[min_index], Numbers[i] = Numbers[i], Numbers[min_index]
​
print(Numbers)
```

```commandline
Numbers = [41,33,17,80,61,5,55]
​
length = len(Numbers)
for i in range(1, length):
    position = i
    value = Numbers[i]
    while position > 0 and Numbers[position-1] > Numbers[position]:
        Numbers[position], Numbers[position-1] = Numbers[position-1], Numbers[position]
        position -= 1
​
print(Numbers)
```

---

O(2^n)：費波那契數列
時間複雜度為 O(2^n) 的演算法，代表著執行步驟會是 2 的 n 次方。實務上來說，這樣的執行效率非常的慢，例如當輸入為 100 時，執行步驟就會暴增到 30 位數，等於即使每秒都能執行 1 百億個步驟，也需要個天荒地老 1 千億年才能完成。

範例
```commandline
def fibo(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    return fibo(n-1) + fibo(n-2)
​
print(fibo(10))
```

---

**Ref.**

(1)初學者學演算法｜談什麼是演算法和時間複雜度
程式麻瓜的程式知識課（三）

https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E8%AB%87%E4%BB%80%E9%BA%BC%E6%98%AF%E6%BC%94%E7%AE%97%E6%B3%95%E5%92%8C%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6-b1f6908e4b80

---

(2)初學者學演算法｜從時間複雜度認識常見演算法
程式麻瓜的程式知識課（四）

https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E8%AA%8D%E8%AD%98%E5%B8%B8%E8%A6%8B%E6%BC%94%E7%AE%97%E6%B3%95-%E4%B8%80-b46fece65ba5

---

(3)初學者學演算法｜排序法入門：選擇排序與插入排序法
程式麻瓜的程式知識課（五）

https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E5%85%A5%E9%96%80-%E9%81%B8%E6%93%87%E6%8E%92%E5%BA%8F%E8%88%87%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%E6%B3%95-23d4bc7085ff


---

(4)初學者學演算法｜排序法進階：合併排序法
程式麻瓜的程式知識課（六）

https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e

---

(5)初學者學演算法｜從費氏數列認識何謂遞迴
程式麻瓜的程式知識課（七）

https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E8%B2%BB%E6%B0%8F%E6%95%B8%E5%88%97%E8%AA%8D%E8%AD%98%E4%BD%95%E8%AC%82%E9%81%9E%E8%BF%B4-dea15d2808a3