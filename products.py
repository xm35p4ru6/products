products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    # 1 p = []
    # 2 p.append(name)
    # 3 p.append(price)
    # 4 p = [name, price] # 1, 2, 3,簡寫
    # 5 products.append(p)
    products.append([name, price]) # 4, 5 簡寫 
print(products)

# products[0][1] # 大清單[0] 裡面的小清單 [1]

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'
# 字串可以做 +, * 不能 -, /

for p in products:
    print(p[0], '的價格是',p[1])


# with open('products.csv', 'w', encoding='utf-8') as f:  #遇到亂碼 encoding='utf-8' 使用'utf-8'編碼 來解決亂碼問題
with open('products.csv', 'w') as f:  # 打開 products.txt, 寫入模式(write) 當作/as f 
    f.write('商品,價格\n')        
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')    # f.write 真正寫入   \n 換行符號