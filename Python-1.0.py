ReceiptOptions = True

import os
os.system('color a')

Burger_Hardcore_Price = 2.45
Fries_Hardcore_Price = 2.245
Pepsi_Hardcore_Price = 3.50
McFlury_Hardcore_Price = 4.65

print("What's Your Selected Order.\n")
print(f'1.🍔 ${Burger_Hardcore_Price}')
print(f'2.🍟 ${Fries_Hardcore_Price}')
print(f'3.🥤 ${Pepsi_Hardcore_Price}')
print(f'4.🍦 ${McFlury_Hardcore_Price}\n')

UserChoice = input('Select Order (1-4): ')

if ReceiptOptions == True and UserChoice == '1':
    with open('Recent-Orders-MCD.dat', 'a') as f:
        f.write(f'McDonalds Burger - ${Burger_Hardcore_Price}\n')

if ReceiptOptions == True and UserChoice == '2':
    with open('Recent-Orders-MCD.dat', 'a') as f:
        f.write(f'McDonalds Fries - ${Fries_Hardcore_Price}\n')

if ReceiptOptions == True and UserChoice == '3':
    with open('Recent-Orders-MCD.dat', 'a') as f:
        f.write(f'McDonalds Pepsi - ${Pepsi_Hardcore_Price}\n')
        
if ReceiptOptions == True and UserChoice == '4':
    with open('Recent-Orders-MCD.dat', 'a') as f:
        f.write(f'McDonalds McFlury - ${McFlury_Hardcore_Price}\n')

if ReceiptOptions == True:
    input('Thank You For Ordering With Us - Has Been Saved Locally.')
else:
    input("Thank You For Ordering With Us - Hasn't Been Saved Locally.")