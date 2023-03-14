from colorama import Fore, Back
from colorama.ansi import Style
import pandas as pd




def show_tabl():
    show = pd.read_excel('stroishop.xlsx', 'Количество строй материалов')    
    print ('\n\n', show)
# def error(a, b):
#     import openpyxl
#     wb = openpyxl.load_workbook('stroishop.xlsx')
#     wb.active = 0
#     if a <= 0:
#         print (Fore.RED + '\nYou can not add that value\n')
#     else:
#         b = a + b    
# #     else:
# #         b = b + a 
#         print (Fore.GREEN + '\n\nYou have replenished your putty stock! The renewed amount of Glatt putty is:', b,'\n')
#     wb.save('stroishop.xlsx')
#         return add_products



def add_products(brand):
    import openpyxl
    wb = openpyxl.load_workbook('stroishop.xlsx')
    wb.active = 0
    sheet = wb.active
    if brand == 1:                          # пополнение Glatt 
        choice_glat = int(input(Fore.LIGHTWHITE_EX + '\nChoice name of material:\n    1.Putty\n    2.White Paint\n    3.Slate\n:'))
        if choice_glat == 1:        #Администратор решил пополнить запасы шпатлефки GLATT

            print (Fore.LIGHTGREEN_EX + Style.BRIGHT +'\n\nAt the moment Quantity of putty is:',sheet['C2'].value, '\n')
            num_of_splat_glatt = int (input( Fore.LIGHTYELLOW_EX + '\nWrite the amount of putty to restock: '))  
            # error(a = num_of_splat_glatt, b = sheet['C2'].value) 

            sheet['C2'].value = sheet['C2'].value + num_of_splat_glatt
            print (Fore.GREEN + '\n\nYou have replenished your putty stock! The renewed amount of Glatt putty is:' + Fore.WHITE, sheet['C2'].value,'\n')                        
        
            


        elif choice_glat == 2:      #Администратор решил пополнить запасы белой краски
            
            print ('At the moment Quantity of White Paint from the company Glatt is:',sheet['C3'].value, '\n')
            num_of_kraska_glatt = int (input('Write the amount of White Paint to restock:'))
            sheet['C3'].value = sheet['C3'].value + num_of_kraska_glatt
            print ('\nYou have replenished white paint stock! The renewed quantity of white from Glatt is:', sheet['C3'].value)
            


        elif choice_glat == 3: # Администратор решил пополнить запасы шифера
            
            print ('At the moment the amount of slate from the company Glatt is:',sheet['C4'].value)
            num_of_shif_glatt = int (input('Write the quantity: '))
            sheet['C4'].value = sheet['C4'].value + num_of_shif_glatt
            print ('\nYou have restocked the slate! The renewed quantity of slate from Glatt is: ', sheet['C4'].value)
        


    elif brand == 2:                        #пополнение Милый ДОМ    
        choice_name_md = int(input(Fore.LIGHTWHITE_EX + '\nChoice name of material:\n    1.Putty\n    2.White Paint\n    3.Slate\n:'))
        if choice_name_md == 1: #Администратор решил пополнить запасы шпатлефки
            
            print ('At the moment Quantity of putty is:', sheet['C5'].value, '\n')
            num_of_splat_md = int (input('\n Write the amount of putty to restock: '))
            sheet['C5'].value = sheet['C5'].value + num_of_splat_md
            print ('\nYou have restocked the putty! The renewed quantity of putty from Milyi Dom is: ', sheet['C5'].value)
           


        elif choice_name_md == 2:  #Администратор решил пополнить запасы белой краски
    
            print ('At the moment Quantity of White paint is:', sheet['C6'].value, '\n')
            num_of_kraska_md = int (input('Write the amount of White paint to restock:'))
            sheet['C6'].value = sheet['C6'].value + num_of_kraska_md
            print ('\nYou have replenished white paint stock! The renewed quantity of white from MIlyi Dom is:', sheet['C6'].value)
            

        elif choice_name_md == 3: #ШиФер 
            
            print ('At the moment Quantity of slate is:', sheet['c7'].value)
            num_of_shif_md = int (input('Write the amount of slate to restock: '))
            sheet['C7'].value = sheet['C7'].value + num_of_shif_md
            print ('\nYou have restocked the slate! The renewed quantity of slate from Milyi Dom is:', sheet['C7'].value)
    else:
            print ('No optoins!')
            
            
    wb.save('stroishop.xlsx')
            
        # num_of_shif_md = int (input('Напишите количество шифера для пополнения запаса:'))

