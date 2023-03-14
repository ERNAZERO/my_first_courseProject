from os import write
import add_product
import sell_product
from openpyxl import load_workbook
import pandas as pd
import info_about_material
import postavshik
import add_material
from colorama import Fore, Back, Style









book = load_workbook('./База данных пользователей.xlsx')
def add_user(url, user_data):
    with pd.ExcelWriter(url, engine = 'openpyxl') as writer:
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        user_data.to_excel(writer, 'Users', index=False)
        writer.save()



def read_Users(url, sheet):
    read = pd.read_excel(url, sheet_name=sheet, index_col=False)
    return read

def vhod():
    wrong_login = 'Wrong password or Login. Please try again.'
    database_of_admins = {'admin': [{'naz@gmail.com': '12345678', 'Asylbek':'12345678'}]}          
    
    while True:
        
        print (Fore.GREEN +  '\nWelcome to Stroi Bishkek Shop!\n')
        login_as_admin = "1. Login as admin"
        login_as_user =  "2. Login as user"
        registration_as_user = "3. Registration as user"
        
        print (Fore.WHITE + login_as_admin) 
        print (Fore.WHITE + login_as_user)
        print (Fore.WHITE + registration_as_user)
        
        choice_of_login = int(input(Fore.CYAN + '\nIf you already have account, please choice the option 1 or 2.\nIf you are not in system, register in the system by clicking the button 3.\n:'))
       



        if choice_of_login == 1:
            print (Fore.GREEN + '\nYou are in the administration authorization option\nPlease enter your login and password\n')
            while True:
                admins_login = input(Fore.WHITE+'Your admin login: ')
                import stdiomask
                admins_password = stdiomask.getpass(prompt = 'Password: ')
                if admins_login in database_of_admins['admin'][0].keys() and admins_password in database_of_admins['admin'][0].values():  
                    print(Fore.BLACK + Back.GREEN +'\n\n  Welcome to admin menu!  \n')
                    
                    def admin():
                            
                            choice_in_menu = int(input(Fore.WHITE + Back.BLACK +'\nChoice your option please:\n\n1. Add capacity\n\n2. Show info about product\n\n3. Show time of deals\n\n4. Delete data from time deals\n\n5. Add supplier\n\n6. Delete supplier\n\n7. Show users feedback\n\n8. Add new product\n\n9. Delete product\n\n10. Exit\n\n: '))
                            if choice_in_menu == 1:                         #пополнение запасов                         
                                add_product.show_tabl()
                                rep_brand = int(input('\nChoice brand for adding capacity:\n  1.Glatt\n  2.Milyi Dom\n:'))                        
                                add_product.add_products(rep_brand)
                                add_product.show_tabl()
                                return admin()
                                    
                                
                            elif choice_in_menu == 2:
                                info_about_material.info() 
                                return admin()

                            elif choice_in_menu == 3:
                                dealsTime = open ('deals_time.txt', 'r', encoding = 'UTF-8')
                                show_time = dealsTime.read()
                                print (Fore.GREEN + '\n----------------------------------------------------------------------------------------------------------------------\n')
                                print (Fore.WHITE + show_time)
                                print (Fore.GREEN + '----------------------------------------------------------------------------------------------------------------------')
                                return admin()

                            elif choice_in_menu == 4:
                                sure = int(input (Fore.YELLOW + 'Are you sure?\n1. Yes\n2. No\n:'))
                                if sure == 1:
                                    print (Fore.YELLOW + 'Данные о времени покупок успешно удалены!')
                                    dealsTime = open ('deals_time.txt', 'w', encoding = 'UTF-8')
                                    dealsTime.close()
                                    return admin()
                                elif sure == 2:
                                    return admin()
                                    # break
                                else:
                                    print (Fore.RED + 'You enter unknown value.')

                            elif choice_in_menu == 5:                                
                                postavshik.add_postavshik(choice_in_menu)
                                return admin()

                            elif choice_in_menu == 6:
                                postavshik.delete_sup()
                                return admin()

                            elif choice_in_menu == 7:
                                read_comments = open ('Comments.txt', 'r', encoding='UTF-8')
                                show_com = read_comments.read()
                                print ('\n', show_com)                                                
                                return admin()
                            
                            elif choice_in_menu == 8:
                                add_material.dobav_material()
                                return admin()

                            elif choice_in_menu == 9:
                                add_material.Udal()
                                return admin()

                            elif choice_in_menu == 10:
                                return vhod()
                    admin()    




                


                else:
                        print(Fore.RED + wrong_login)
                    
                break

                     
        elif choice_of_login == 2:
            print (Fore.GREEN +'\n\nВы перешли в пункт авторизации пользователя. Пожалуйста введите логин и пароль.')
            
            import stdiomask
            users_login = input(Fore.WHITE + 'Логин: ')
            users_password = stdiomask.getpass(prompt='Пароль: ')        
            usery = read_Users('./База данных пользователей.xlsx', 'Users')
            
            for i in range(len(usery['Login'])):
                if (users_login == usery['Login'][i]) and (users_password == usery['Password'][i]):
                            print (Fore.BLACK + Fore.GREEN + '\n\nWelcome to the user menu!\n')                        
                            def users():
                                choice_in_menu_user = int(input(Fore.WHITE + '\nSelect the option you need:\n\n1. Buying building material\n\n2. Show product information\n\n3. Write a feedback\n\n4. Show users feedback\n\n5. Exit\n\n: '))  #надо дополнить меню!!!!!!!!!!!!!!!
                                if choice_in_menu_user == 1:
                                    sell_product.sale_product(choice_in_menu_user, users_login)
                                    return users()
                                elif choice_in_menu_user == 2:
                                    info_about_material.info()
                                    return users()
                                elif choice_in_menu_user == 3:
                                    comment = input (Fore.YELLOW + 'Напишите отзыв: ')
                                    write_comment =  open ('Comments.txt', 'a', encoding = 'UTF-8')
                                    razd = Fore.GREEN + '---------------------------------------------------------------------------------------------------------------'
                                    write_comment.write('{}{}{}{}{}{}{}'.format('Пользователь ', users_login, ' оставил комментарий: \n', comment, '\n', razd, '\n'))  
                                    print (Fore.GREEN + 'Feedback has been added!')                            
                                    write_comment.close()
                                    return users()
                                elif choice_in_menu_user == 4:
                                    read_comments = open ('Comments.txt', 'r', encoding='UTF-8')
                                    show_com = read_comments.read()
                                    print ('\n', show_com)
                                    return users()

                                # elif choice_in_menu_user == 5:
                                    # abt_prgrm = 


                                elif choice_in_menu_user == 6:
                                    return vhod()
                            users()
                

                
                    
                            



                                    

                
            # print ('Неправильный логин или пароль. Попробуйте ещё раз.')
            
            







        elif choice_of_login == 3:
                print(Fore.YELLOW + '\nYou are in the user registration option.\nCreate Login and Password.\n')
                while True:
                    create_name = input(Fore.WHITE + 'Name: ')
                    create_surname = input('Surname: ')
                    create_user=input('Your login: ')
                    create_password=input('Your password: ') 
                    if create_surname != '' and create_name != '' and len(create_password) >= 8 and ('@gmail.com' in create_user) and create_user not in create_password:               
                        saved_user = read_Users('./База данных пользователей.xlsx', 'Users')
                        local_user = pd.DataFrame(saved_user)
                        new_value = local_user.append({'Name':create_name, 'Surname':create_surname, 'Login':create_user, 'Password':create_password}, ignore_index=True)
                        add_user('./База данных пользователей.xlsx', new_value)
                        print(Fore.GREEN +'You are in system,', create_name,'!')                    
                        break
                    elif create_surname == '' or create_name == '':
                        print (Fore.RED +"\nYou didn't enter your first or last name.")
                    elif len(create_password) < 8:
                        print (Fore.RED +'\nYour password must be more than 8 characters long')
                    elif '@gmail.com' not in create_user:
                        print (Fore.RED +"\nLogin must contain the value '@gmail.com'")
                    elif create_user in create_password:
                        print (Fore.RED +'\nThe password must not contain the login.')
vhod()

        # break


          