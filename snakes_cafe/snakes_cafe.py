print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")

menu = {
  'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
  'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
  'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
  'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
}

print("""********************************* 
* What would you like to order? * 
 *********************************""")
newOrder=input('> ')

while newOrder != 'quit':

    for key in menu.keys():
        if newOrder in menu[key].keys():
            menu[key][newOrder]+=1
            print('**'+ str(menu[key][newOrder])+' order of ' + newOrder +' have been added to your meal **')
    break

while newOrder != 'quit':
    print("To exit enter quit")
    newOrder=input('> ')
    while newOrder != 'quit':
        for key in menu.keys():
            if newOrder in menu[key].keys():
                menu[key][newOrder]+=1
                print('**'+ str(menu[key][newOrder])+' order of ' + newOrder +' have been added to your meal **')
        break

 





