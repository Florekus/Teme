#SHOP Homework

shop = ['shirts', 'scarfs','gloves','hats' ] 
sizes = ['S','M','L', 'XL','XXL']
qty  = '400'
print(f' The shop sells a selection of {qty} different models of {shop} and each item has {sizes} sizes.')

# 400 articles
articles = [x for x in shop if x != 0]*100
print(articles)

#different sizes for each article
print([(x,y) for x in shop for y in sizes])

#remove the last article
print(articles[-1])

#insert a new article in the first position
articles.insert(0, 'RED hat')
print(articles)

import random
#pick any item that is in the shop
print(random.choice(articles))
print(random.sample(articles,3))