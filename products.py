#二維清單  目的:將product_name(char)以及product_price(int)同時顯示出來
#大清單裝著小清單
#大清單->products ; 小清單->p 其中小清單裝著product_name 、product_price

products = [] #大清單
while True:
	product_name = input('請輸入商品名稱 :')
	if product_name == 'q':  #當輸入q時離開
		break
	product_price = input('請輸入商品價格 :')

	p = []
	p.append(product_name)
	p.append(product_price) 
	#line 14 & line15 can be combined : p = [product_name, product_price]
	products.append(p) #大清單裝小清單

	#而line12 ~line16 can be combined : 
	#	=> products.append([product_name, product_price])
print(products)

