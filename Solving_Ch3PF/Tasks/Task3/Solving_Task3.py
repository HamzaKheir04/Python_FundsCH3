Price = '123$'
""" 
here as we can see price is String and we need to add 100$ to it 

we can use int(price)+100 but we got a problem which is the ( $ ) symbol 
  
then to solve it i'm gonna use replace() to remove the symbol and convert it to int using int() like this :

"""
New_Price=int(Price.replace('$',''))
print(New_Price)
# now add the 100 
New_Price= New_Price+100
print(New_Price)
# now we added the 100 let's get back the symbol ($) and convert it to String 
Last_Price = str(New_Price)+'$'

print(f"The Price Before Adding the 100$ : {Price}",
     f"The Price After Adding the 100$ : {Last_Price}", sep="\n")
 
