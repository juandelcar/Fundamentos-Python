# function imput -> retorna string 

num_a = int(input ("Ingresa un Numero: ")) 
num_b = int(input ("Ingresa un Numero: ")) 

print (num_a + num_b)

name = input ("ingresa tu nombre: ")
age = int(input("ingresa tu edad: "))
city = input ("ingresa tu ciudad/pueblo: ")

# string format
"""
 Holaa, soy name, tengo age años y vivo en city
"""
greeting = "Holaa, soy {},tengo {} años y vivo en {}"


print (greeting.format(name, age, city))

greeting_2 = f"Holaa, soy {name},tengo {age} años y vivo en {city}"

print(greeting_2)