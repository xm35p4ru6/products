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

products[0][1] # 大清單[0] 裡面的小清單 [1]