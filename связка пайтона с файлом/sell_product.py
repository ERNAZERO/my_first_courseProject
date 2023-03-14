from colorama import Fore, Back


def sale_product(vybor_brenda, users_login):
    import openpyxl
    import datetime
    time = open('deals_time.txt', 'a', encoding = 'UTF-8')
    wb = openpyxl.load_workbook('stroishop.xlsx')
    wb.active = 0
    sheet = wb.active
    time1 = datetime.datetime.now()
    pol = 'User' 
    iden = users_login
    kol = 'The number of purchased items: '
    
    price_stroi_splat = 200
    price_white_dye = 400
    price_shiff = 300
    def check (a, b):
        return a*b


    vybor_brenda = int(input('\nPlease select the name of the brand to buy the building material\n1.Glatt\n2.Milyi Dom\n:'))
    if vybor_brenda == 1:  #Glatt
        users_choice_name = int(input('\nSelect the name of the building material\n1.Building putty\n2.White Dye\n3.Slate\n:'))
        if users_choice_name == 1:                   #пользователь хочет купить строительную шпатлевку GLATT
            
            print ('\nAt the moment the amount of construction putty from the company Glatt is:', sheet['C2'].value, '\n')
            while True:                                
                if sheet['C2'].value == 0:
                    print (Fore.RED + 'At the moment product out of stock.    ¯\_(ツ)_/¯')
                    print (Fore.YELLOW +'\nReplenishment is coming soon!')    
                    break                                
                else:
                    print ('The price of construction putty is:', price_stroi_splat, 'som')
                    kolvo_stroisplat = int(input('\nQuantity: '))  #Количество которое хочет купить пользователь                                                               
                    if kolvo_stroisplat > sheet['C2'].value:
                        print ('\nYour request exceeded the number of items in stock. Try again.')
                    elif kolvo_stroisplat == 0:
                        print ("You didn't buy anything(")
                    else:
                        
                        sheet['C2'].value = sheet['C2'].value - kolvo_stroisplat

                        splat = 'bought a construction putty from Glatt at:'
                        time.write("\n{} {} {} {}\n\t{} {}\n". format(pol, iden, splat, time1, kol, kolvo_stroisplat))                        
                        
                        print (Fore.GREEN + '\nThe transaction was successful!        ᕙ(  • ‿ •  )ᕗ\n'+ Fore.WHITE)
                        check(a=kolvo_stroisplat, b=price_stroi_splat)
                        print ('You bought an item for the amount: ',check(a = kolvo_stroisplat, b = price_stroi_splat), 'som')
                        
                        break
        
        if users_choice_name == 2:                   #пользователь хочет купить белую краску
            
            print ('\nAt the moment the amount of White Paint from the company Glatt is:', sheet['C3'].value, '\n')
            while True:
                if sheet['C3'].value == 0:
                    print (Fore.RED + 'At the moment product out of stock.    ¯\_(ツ)_/¯')
                    print (Fore.YELLOW +'\nReplenishment is coming soon!')
                    break
                else:    
                    print ('The price of White Paint is:', price_white_dye, 'som')
                    kolvo_beloi_kraski_gl = int(input('\nQuantity: '))  #Количество которое хочет купить пользователь
                    if kolvo_beloi_kraski_gl > sheet['C3'].value:
                        print ('\nYour request exceeded the number of items in stock. Try again.')
                    elif kolvo_beloi_kraski_gl == 0:
                        print ("You didn't buy anything(")
                    else:
                        sheet['C3'].value = sheet['C3'].value - kolvo_beloi_kraski_gl
                        kraska = 'bought White Paint from Glatt at:'
                        time.write("\n{} {} {} {}\n\t{} {}\n". format(pol, iden, kraska, time1, kol, kolvo_beloi_kraski_gl))
                        print (Fore.GREEN + '\nThe transaction was successful!      ᕙ(  • ‿ •  )ᕗ\n'+ Fore.WHITE)
                        check(a=kolvo_beloi_kraski_gl, b=price_white_dye)
                        print ('You bought an item for the amount: ',check(a = kolvo_beloi_kraski_gl, b = price_white_dye), 'som')
                        # wb.save('stroishop.xlsx')
                        break
        
        if users_choice_name == 3:                   #пользователь хочет купить шифер
            
            print ('\nAt the moment the amount of slate from the company Glatt is:', sheet['C4'].value, '\n')
            while True:
                if sheet['C4'].value == 0:
                    print (Fore.RED + 'At the moment product out of stock.    ¯\_(ツ)_/¯')
                    print (Fore.YELLOW +'\nReplenishment is coming soon!')
                    break
                else:    
                    print ('The price of slate is:', price_shiff, 'som')
                    kolvo_shif_gl = int(input('\nQuantity:: '))  #Количество которое хочет купить пользователь
                    if kolvo_shif_gl > sheet['C4'].value:
                        print ('\nYour request exceeded the number of items in stock. Try again.')
                    elif kolvo_shif_gl == 0:
                        print ("You didn't buy anything(")
                    else:
                        sheet['C4'].value = sheet['C4'].value - kolvo_shif_gl 
                        shif = 'bought a slate from Glatt at:'
                        time.write("\n{} {} {} {}\n\t{} {}\n". format(pol, iden, shif, time1, kol, kolvo_shif_gl))               
                        print (Fore.GREEN+ '\nThe transaction was successful!      ᕙ(  • ‿ •  )ᕗ\n' + Fore.WHITE)
                        check(a=kolvo_shif_gl, b=price_shiff)
                        print ('You bought an item for the amount: ',check(a = kolvo_shif_gl, b = price_shiff), 'som')
                        # wb.save('stroishop.xlsx')                                        
                        break
        
    elif vybor_brenda == 2:    
        users_choice_name_product_md = int(input('Select the name of the building material\n1.Building putty\n2.White Dye\n3.Slate\n:'))
        if users_choice_name_product_md == 1: #Шпатлевка
        
            print ('\nAt the moment the amount of construction putty from the company Milyi Dom is:', sheet['C5'].value, '\n')
            while True:                                
                if sheet['C5'].value == 0:
                    print (Fore.RED + 'At the moment product out of stock.    ¯\_(ツ)_/¯')
                    print (Fore.YELLOW +'\nReplenishment is coming soon!')
                    break
                else:
                    print ('The price of is construction putty:', price_stroi_splat, 'som')
                    kolvo_stroisplat_md = int(input('\nQuantity: '))  #Количество которое хочет купить пользователь                                                               
                    if kolvo_stroisplat_md > sheet['C5'].value:
                        print ('\nYour request exceeded the number of items in stock. Try again.')
                    elif kolvo_stroisplat_md == 0:
                        print ('You didnt buy anything(')
                    else:
                        sheet['C5'].value = sheet['C5'].value - kolvo_stroisplat_md
                        splat_md = 'bought a construction putty from Milyi Dom at:'
                        time.write("\n{} {} {} {}\n\t{} {}\n". format(pol, iden, splat_md, time1, kol, kolvo_stroisplat_md))
                        print (Fore.GREEN +'\nTransaction was succesful!        ᕙ(  • ‿ •  )ᕗ\n'+ Fore.WHITE)
                        check(a=kolvo_stroisplat_md, b=price_stroi_splat)
                        print ('You bought an item for the amount: ',check(a = kolvo_stroisplat_md, b = price_stroi_splat), 'som')
                        # wb.save('stroishop.xlsx')
                        break
        
        
        elif users_choice_name_product_md == 2:
            
            print ('\nAt the moment the amount of slate from the company Milyi Dom is:', sheet['C6'].value, '\n')
            while True:                                
                if sheet['C6'].value == 0:
                    print (Fore.RED + 'At the moment product out of stock.    ¯\_(ツ)_/¯')
                    print (Fore.YELLOW +'\nReplenishment is coming soon!')                  
                    break                  
                else:
                    print ('The price of White Paint is:', price_white_dye, 'som')
                    kolvo_beloikraski_md = int(input('\nQuantity: '))  #Количество которое хочет купить пользователь                                                               
                    if kolvo_beloikraski_md > sheet['C6'].value:
                        print ('\nYour request exceeded the number of items in stock. Try again.')
                    elif kolvo_beloikraski_md == 0:
                        print ('You didnt buy anything(')
                    else:
                        sheet['C6'].value = sheet['C6'].value - kolvo_beloikraski_md
                        kraska_md = 'bought White Paint from Milyi Dom at:'
                        time.write("\n{} {} {} {}\n\t{} {}\n". format(pol, iden, kraska_md, time1, kol, kolvo_beloikraski_md))
                        print ( Fore.GREEN + '\nThe transaction was successful!        ᕙ(  • ‿ •  )ᕗ\n'+ Fore.WHITE)
                        check(a=kolvo_beloikraski_md, b=price_white_dye)
                        print ('You bought an item for the amount: ',check(a = kolvo_beloikraski_md, b = price_white_dye), 'som')
                        # wb.save('stroishop.xlsx')
                        break
        
        
        
        elif users_choice_name_product_md == 3:
            
            print ('\nAt the moment the amount of slate from the company Milyi is:', sheet['C7'].value, '\n')
            while True:                                
                if sheet['C7'].value == 0:
                    print (Fore.RED + 'At the moment product out of stock.    ¯\_(ツ)_/¯')
                    print (Fore.YELLOW +'\nReplenishment is coming soon!')                
                    break

                else:
                    print ('The price of shiffer is:', price_shiff, 'som')
                    kolvo_shif_md = int(input('\nQuantity: '))  #Количество которое хочет купить пользователь                                                               
                    if kolvo_shif_md > sheet['C7'].value:
                        print ('\nYour request exceeded the number of items in stock. Try again.')
                    elif kolvo_shif_md == 0:
                        print ("You didn't buy anything(")
                    else:
                        sheet['C7'].value = sheet['C7'].value - kolvo_shif_md
                        shif_md = 'bought a slate from Milyi Dom at:'
                        time.write("\n{} {} {} {}\n\t{} {}\n". format(pol, iden, shif_md, time1, kol, kolvo_shif_md))
                        print (Fore.GREEN + '\nThe transaction was successful!      ᕙ(  • ‿ •  )ᕗ\n' + Fore.WHITE)
                        check(a=kolvo_shif_md, b=price_shiff)
                        print ('You bought an item for the amount: ',check(a = kolvo_shif_md, b = price_shiff), 'som')
                        # wb.save('stroishop.xlsx')
                        break
    wb.save('stroishop.xlsx')
    time.close()
        