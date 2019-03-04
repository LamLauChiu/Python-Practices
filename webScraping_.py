from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser") 

# grabbing each product
containers = page_soup.findAll("div", { "class":"item-container"})


# check length
# >>> len(containers)
# >>> containers[0]
# <
# div class = "item-container item-container-grid" >
#     <!--image-->
#     <
#     a class = "item-img"
# href = "https://www.newegg.com/Special/ShellShocker.aspx?cm_sp=Homepage_SS-_-P1_20-158-570-_-01212019&amp;Index=1" >
#     <
#     img alt = "GeIL SUPER LUCE RGB SYNC AMD Edition 8GB (2 x 4GB) 288-Pin DDR4 SDRAM DDR4 2400 (PC4 19200) Desktop Memory Model ..."
# src = "//c1.neweggimages.com/NeweggImage/ProductImageCompressAll300/20-158-570-V01.jpg"
# title = "GeIL SUPER LUCE RGB SYNC AMD Edition 8GB (2 x 4GB) 288-Pin DDR4 SDRAM DDR4 2400 (PC4 19200) Desktop Memory Model ..." >
#     <
#     /img></a >
#     <
#     div class = "item-info" >
#     <!--price-->
#     <
#     ul class = "price " >
#     <
#     li class = "price-was" >
#     <
#     /li> <
#     li class = "price-map" >
#     <
#     /li> <
#     li class = "price-current" >
#     <
#     span class = "price-current-label" >
#     <
#     /span>$<strong>54</strong > < sup > .99 < /sup>  <
#     span class = "price-current-range" >
#     <
#     abbr title = "to" > – < /abbr> <
#     /span> <
#     /li> <
#     li class = "price-save " >
#     <
#     span class = "price-save-endtime price-save-endtime-current" > < /span> <
#     span class = "price-save-endtime price-save-endtime-another"
# style = "display:none;" > < /span> <
#     /li> <
#     li class = "price-note" >
#     <
#     /li> <
#     li class = "price-ship" >
#     Free Shipping <
#     /li> <
#     /ul>
#     <!--descripiton-->
#     <
#     a class = "item-title"
# href = "https://www.newegg.com/Special/ShellShocker.aspx?cm_sp=Homepage_SS-_-P1_20-158-570-_-01212019&amp;Index=1" > GeIL SUPER LUCE RGB SYNC AMD Edition 8 GB(2 x 4 GB) 288 - Pin DDR4 SDRAM DDR4 2400(PC4 19200) Desktop Memory Model... < /a>
#     <!--promption info-->
#     <
#     p class = "item-promo" > < /p> <
#     /div> <
#     input id = "CoremetricsData"
# type = "hidden"
# value = '[{"position":"ShellShocker1","dataList":[{"cMData":"Homepage_SS-_-P1_20-158-570-_-01212019","itemNumber":"20-158-570"}]}]' >
#     <
#     /input></div >


# contain = containers[0]
# container = containers[0]
filename = "product.csv"

f = open(filename, "w")

headers = "brand, product_name, shipping\n" 

f.write(headers)

for container in containers:
	
	#brand = containers.div.div.a.img["title"]
	brand = container.a.img["title"]

	title_container = container.findAll("a",{"class":"item-title"} )
	product_name = title_container[0].text

	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)
	f.write(brand +  "," + product_name.replace("," ,"|") + "," + shipping + "\n")
	
f.close()
