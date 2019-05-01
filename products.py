#二維清單  目的:將product_name(char)以及product_price(int)同時顯示出來
#大清單裝著小清單
#大清單->products ; 小清單->p 其中小清單裝著product_name 、product_price

products = [] #大清單
while True:
	product_name = input('請輸入商品名稱 :')
	if product_name == 'q':  #當輸入q時離開
		break
	product_price = input('請輸入商品價格 :') #此時所輸入的資料型態是字串
	product_price  = int(product_price) #資料型態的轉換 :字串-> int

	p = []
	p.append(product_name)
	p.append(product_price) 
	#line 14 & line15 can be combined : p = [product_name, product_price]
	products.append(p) #大清單裝小清單

	#而line12 ~line16 can be combined : 
	#	=> products.append([product_name, product_price])
print(products)

for p in products:
	print(p[0], '的價格', p[1])

#字串可以用+ 做合併 ex : 'abc' + '123' = 'abc123' 
						#(前提是雙方都是字串型態才可以)
#以下程式碼 :寫入檔案
with open('product.csv', 'w') as f: #開檔 'w'->寫入模式 
									#在這模式下若已經存在有檔案 則會覆寫掉
									#若沒有，則自動會建立一個新的檔案"product.txt"
	f.write('商品,價格\n') #寫入欄位名稱 (在csv檔)
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') 	#f.write:寫入
												#csv檔記得用','作區隔
												#str(p[1]) :int -> str