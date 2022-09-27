import time


print("\n\n\n\n\n\t\t\t\t\t    *|*|*|*|*|*|*|*|*|*|*|*|*|*|*|                                |*|*|*|*|*|*|*|*|*|*|*|*|*|* ")
print("\n\n\t\t\t\t\t    *|*|*|*|*|*|*|*|*|*|*|*|*|*|*|    CHAPPAN BHOG RESTAURANT     |*|*|*|*|*|*|*|*|*|*|*|*|*|* ")
print("\n\n\t\t\t\t\t    *|*|*|*|*|*|*|*|*|*|*|*|*|*|*|                                |*|*|*|*|*|*|*|*|*|*|*|*|*|* \n\n\n ")

time.sleep(1)
name=input("\t Enter your name ::: ")


print("\n\n\n\t\t\t\t\t\t\t\t\t WELCOME, TO OUR RESTAURANT!!! ", name)
time.sleep(1)

print(" \n\n\n\t\t\t\t\t\t\t\t\t     |||||| MENU CARD ||||||   \n")

print(" \n\n\t\t\t\t\t\t\t BREAKFAST \t\t\t\t")
print(" \n\t\t\t\t\t\t\t 1.ALOO KA PARATHAA \t\t\t\t Rs.10 \n\t\t\t\t\t\t\t 2.METHI KE PAKODE \t\t\t\t Rs.20 \n\t\t\t\t\t\t\t 3.PYAAZ KE PAKODE CHAI KE SATH \t\t Rs.25 \n\t\t\t\t\t\t\t 4.POHA WITH CHAI \t\t\t\t Rs.45 \n\t\t\t\t\t\t\t 5.EGG SALAD SANDWICH AND COFFEE \t\t Rs.35 \n\t\t\t\t\t\t\t 6.WHITE BREAD WITH OMLETTE AND COFFEE \t\t Rs.50")

print(" \n\n\t\t\t\t\t\t\t LUNCH ")
print(" \n\t\t\t\t\t\t\t 1.ROASTED CHICKEN  \t\t\t\t Rs.20 \n\t\t\t\t\t\t\t 2.PANEER WITH LACCHA PARATHA \t\t\t Rs.34 \n\t\t\t\t\t\t\t 3.SPICY BEEF BARBEQUE \t\t\t\t Rs.34 \n\t\t\t\t\t\t\t 4.PORK BARBEQUE \t\t\t\t Rs.56 \n\t\t\t\t\t\t\t 5.PULLED BEEF BARBEQUE BURGER \t\t\t Rs.45")


print(" \n\n\t\t\t\t\t\t\t DINNER ")
print(" \n\t\t\t\t\t\t\t 1.MAJBOOS RICE WITH BBQ CHICKEN \t\t Rs.34 \n\t\t\t\t\t\t\t 2.BARKA SPECIAL KABAB  \t\t\t Rs.67 \n\t\t\t\t\t\t\t 3.KAPPA BIRYANI  \t\t\t\t Rs.56 \n\t\t\t\t\t\t\t 4.YAM POTTAGE  \t\t\t\t Rs.78 \n\t\t\t\t\t\t\t ")

time.sleep(1)
choice=input("\n\t SIR WHAT DO YOU LIKE TO TAKE WHETHER 'BREAKFAST' OR 'LUNCH' OR 'DINNER' ::: ")

if choice=="BREAKFAST" or choice=="breakfast":
    meal_no=input("\n\t WRITE MEAL NAME WHICH YOU WANT TO TAKE FROM BREAKFAST SECTION ::: ")
    if meal_no=="aloo ka parathaa" or meal_no=="ALOO KA PARATHAA":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED ALOO KE PARATHAA")
    elif meal_no=="methi ke pakode" or meal_no=="METHI KE PAKODE":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED METHI KE PAKODE")
    elif meal_no=="pyaaz ke pakode chai ke sath" or meal_no=="PYAAZ KE PAKODE CHAI KE SATH":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED PYAAZ KE PAKODE CHAI KE SATH")
    elif meal_no=="poha with chai" or meal_no=="POHA WITH CHAI":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED POHA WITH CHAI")
    elif meal_no=="egg salad sandwich and coffee" or meal_no=="EGG SALAD SANDWICH AND COFFEE":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED EGG SALAD SANDWICH AND COFFEE")
    elif meal_no=="white bread with omlette and coffee" or meal_no=="WHITE BREAD WITH OMLETTE AND COFFEE":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED WHITE BREAD WITH OMLETTE AND COFFEE")
    else:
        print(" \n\t\t\t\t\t\t\t THIS MEAL IS NOT AVAILABLE IN OUR RESTAURANT")
    

elif choice=="LUNCH" or choice=="lunch":
    meal_no=input("\n\t WRITE MEAL NAME WHICH YOU WANT TO TAKE FROM LUNCH SECTION :::")
    if meal_no=="roasted chicken" or meal_no=="ROASTED CHICKEN":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED ROASTED CHICKEN ")
    elif meal_no=="paneer with laccha paratha" or meal_no=="PANEER WITH LACCHA PARATHA":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED PANEER WITH LACCHA PARATHA")
    elif meal_no=="spicy beef barbeque" or meal_no=="SPICY BEEF BARBEQUE":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED SPICY BEEF BARBEQUE")
    elif meal_no=="pork barbeque" or meal_no=="PORK BARBEQUE":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED PORK BARBEQUE")
    elif meal_no=="pulled beef barbeque burger" or meal_no=="PULLED BEEF BARBEQUE BURGER":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED PULLED BEEF BARBEQUE BURGER")
    else:
        print(" \n\t\t\t\t\t\t\t THIS MEAL IS NOT AVAILABLE IN OUR RESTAURANT")

elif choice=="DINNER" or choice=="dinner":
    meal_no=input("\n\t WRITE MEAL NAME WHICH YOU WANT TO TAKE FROM DINNER SECTION :::")
    if meal_no=="majboos rice with bbq chicken" or meal_no=="MAJBOOS RICE WITH BBQ CHICKEN":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED MAJBOOS RICE WITH BBQ CHICKEN")
    elif meal_no=="barka special kabab" or meal_no=="BARKA SPECIAL KABAB":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED BARKA SPECIAL KABAB")
    elif meal_no=="kappa biryani" or meal_no=="KAPPA BIRYANI":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED KAPPA BIRYANI")
    elif meal_no=="yam pottage" or meal_no=="YAM POTTAGE":
        print(" \n\t\t\t\t\t\t\t YOU HAVE ORDERED YAM POTTAGE")
    else:
        print(" \n\t\t\t\t\t\t\t THIS MEAL IS NOT AVAILABLE IN OUR RESTAURANT")

print("\n\n\n\n\t ** WHAT DO YOU WANT TO TAKE FROM OUR DRINKS SECTION,HERE IS THE LIST ** ")
time.sleep(1)

print("\n\n\t\t\t\t\t\t\t SOFT DRINKS ")
print("\n\t\t\t\t\t\t\t 1.COLA BOTTLE \t\t\t\t Rs.45 \n\t\t\t\t\t\t\t 2.SODA WATER \t\t\t\t Rs.50 \n\t\t\t\t\t\t\t 2.TONIC WATER \t\t\t\t Rs.30 \n\t\t\t\t\t\t\t 3.RED BULL \t\t\t\t Rs.95 \n\t\t\t\t\t\t\t 4.GUAVA JUICE \t\t\t\t Rs.67 \n\t\t\t\t\t\t\t 5.APPLE JUICE \t\t\t\t Rs.56 ")

print("\n\n\t\t\t\t\t\t\t BEERS ")
print("\n\t\t\t\t\t\t\t 1.SMB HORSE STALLION \t\t\t Rs.100 \n\t\t\t\t\t\t\t 2.RED HORSE STALLION \t\t\t Rs.150 \n\t\t\t\t\t\t\t 3.PALE PILSEN \t\t\t\t Rs.160 ")

print("\n\n\t\t\t\t\t\t\t COCKTAILS ")
print("\n\t\t\t\t\t\t\t 1.E&S SIGNATURE \t\t\t Rs.210 \n\t\t\t\t\t\t\t 2.MARGARITA CALSSIC \t\t\t Rs.328 \n\t\t\t\t\t\t\t 3.MOJITO ClASSIC \t\t\t Rs.350 \n\t\t\t\t\t\t\t 4.GREEN PARADISE \t\t\t Rs.324")

time.sleep(1)
ch2=input("\n\n\t SIR WHAT DO YOU LIKE TO TAKE WHETHER 'SOFT DRINKS' OR 'BEERS' OR 'COCKTAILS' ::: ")

if ch2=="soft drinks" or ch2=="SOFT DRINKS":
    drinks=input("\n\t WRITE DRINK NAME WHICH YOU WANT TO TAKE FROM SOFT DRINKS SECTION ::: ")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED COLA BOTTLE")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED SODA WATER")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED TONIC WATER ")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED RED BULL")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED GUAVA JUICE")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED APPLE JUICE")
    else:
        print("\n\t\t\t\t\t\t\t THIS DRINK IS NOT AVILABLE IN OUR RESTAURANT")

if ch2=="beers" or ch2=="BEERS":
    drinks=input("\n\t WRITE DRINK NAME WHICH YOU WANT TO TAKE FROM BEERS SECTION :::")
    if drinks=="smb horse stallion" or drinks=="SMB HORSE STALLION":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED SMB HORSE STALLION")
    elif drinks=="red horse stallion" or drinks=="RED HORSE STALLION":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED RED HORSE STALLION ")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED PALE PILSEN")
    else:
        print("\n\t\t\t\t\t\t\t THIS BEER IS NOT AVAILABLE IN OUR RESTAURANT")

    
if ch2=="cocktails" or ch2=="COCKTAILS":
    drinks=input("\n\t WRITE DRINK NAME WHICH YOU WANT TO TAKE FROM COCKTAILS SECTION :::")
    if drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED E&S SIGNATURE")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED MARGARITA CLASSIC")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED MOJITO CLASSIC")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\n\t\t\t\t\t\t\t YOU HAVE ORDERED GREEN PARADISE")
    else:
        print("\n\t\t\t\t\t\t\t THIS COCKTAIL DRINK IS NOT AVILABLE IN OUR RESTAURANT")

print("\n\n\n\n\t PROCESSING......")
time.sleep(4)

print("\n\t YOUR TOTAL ORDER IS :::")
print("\n\n\n\t\t\t\t\t\t\t\t\t    ||||| ORDER ||||| ")

print("\n\t\t\t\t\t\t\t ______________________________________________________")
print("\n\t\t\t\t\t\t\t ITEM \t\t\t\t\t\t Amount")
print("\t\t\t\t\t\t\t ______________________________________________________")
if meal_no=="aloo ka parathaa" or meal_no=="ALOO KA PARATHAA":
    print("\n\t\t\t\t\t\t\t ALOO KA PARATHAA \t\t\t\t Rs.10")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.55")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.60")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.40")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.105")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.77")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.66")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.110")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.160")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.170")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.220")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.338")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.360")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.334")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.10")
        
elif meal_no=="methi ke pakode" or meal_no=="METHI KE PAKODE":
    print("\n\t\t\t\t\t\t\t METHI KE PAKODE \t\t\t\t Rs.20")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.65")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.70")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.50")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.115")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.87")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.76")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.120")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.170")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.180")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.230")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.348")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.370")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.344")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.20")

elif meal_no=="pyaaz ke pakode chai ke sath" or meal_no=="PYAAZ KE PAKODE CHAI KE SATH":
    print("\n\t\t\t\t\t\t\t PYAAZ KE PAKODE CHAI KE SATH \t\t\t Rs.25")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.70")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.75")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.55")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.120")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.92")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.81")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.125")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.175")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.185")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.235")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.353")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.375")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.349")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.25")
        
elif meal_no=="poha with chai" or meal_no=="POHA WITH CHAI":
    print("\n\t\t\t\t\t\t\t POHA WITH CHAI \t\t\t\t Rs.45")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.90")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.95")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.75")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.140")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.112")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.101")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.145")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.195")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.205")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.255")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.373")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.395")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.369")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.45")
    
elif meal_no=="egg salad sandwich and coffee" or meal_no=="EGG SALAD sandwich AND COFFEE":
    print("\n\t\t\t\t\t\t\t EGG SALAD WITH OMLETTE AND COFFEE \t\t Rs.35")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.80")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.85")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.65")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.130")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.102")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.91")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.135")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.185")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.195")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.245")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.363")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.385")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.359")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.35")
    
elif meal_no=="white bread with omlette and coffee" or meal_no=="WHITE BREAD WITH OMLETTE AND COFFEE":
    print("\n\t\t\t\t\t\t\t WHITE BREAD WITH OMLETTE AND COFFEE \t\t Rs.50")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.95")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.100")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.80")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.145")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.117")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.106")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.150")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.200")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.210")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.260")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.378")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.400")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.374")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.50")
    
elif meal_no=="roasted chicken" or meal_no=="ROASTED CHICKEN":
    print("\n\t\t\t\t\t\t\t ROASTED CHICKEN \t\t\t\t Rs.20")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.65")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.70")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.50")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.115")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.87")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.76")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.120")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.170")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.180")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.230")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.348")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.370")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.344")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.20")
    
elif meal_no=="paneer with laccha paratha" or meal_no=="PANEER WITH LACCHA PARATHA":
    print("\n\t\t\t\t\t\t\t PANEER WITH LACCHA PARATHA \t\t\t Rs.34")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.79")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.84")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.64")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.129")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.101")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.90")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.134")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.184")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.194")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.244")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.362")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.384")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.358")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.34")
    
elif meal_no=="spicy beef barbeque" or meal_no=="SPICY BEEF BARBEQUE":
    print("\n\t\t\t\t\t\t\t SPICY BEEF BARBEQUE \t\t\t\t Rs.34")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.79")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.84")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.64")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.129")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.101")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.90")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.134")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.184")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.194")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.244")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.362")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.384")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.358")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.34")
    
    
elif meal_no=="pork barbeque" or meal_no=="PORK BARBEQUE":
    print("\n\t\t\t\t\t\t\t PORK BARBEQUE \t\t\t\t\t Rs.56")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.101")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.106")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.86")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.151")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.123")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.112")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.156")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.206")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.216")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.266")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.384")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.406")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.380")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.56")

    
elif meal_no=="pulled beef barbeque burger" or meal_no=="PULLED BEEF BARBEQUE BURGER":
    print("\n\t\t\t\t\t\t\t PULLED BEEF BARBEQUE BURGER \t\t\t Rs.45")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.90")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.95")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.75")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.140")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.112")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.101")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.145")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.195")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.205")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.255")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.373")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.395")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.369")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.45")
    
elif meal_no=="majboos rice with bbq chicken" or meal_no=="MAJBOOS RICE WITH BBQ CHICKEN":
    print("\n\t\t\t\t\t\t\t MAJBOOS RICE WITH BBQ CHICKEN \t\t\t Rs.34")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.79")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.84")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.64")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.129")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.101")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.90")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.134")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.184")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.194")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.244")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.362")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.384")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.358")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.34")
    
    
elif meal_no=="barka special kabab" or meal_no=="BARKA SPECIAL KABAB":
    print("\n\t\t\t\t\t\t\t BARKA SPECIAL KABAB \t\t\t\t Rs.67")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.112")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.117")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.97")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.162")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.134")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.123")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.167")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.217")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.227")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.277")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.395")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.400")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.391")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.67")
    

    
elif meal_no=="kappa biryani" or meal_no=="KAPPA BIRYANI":
    print("\n\t\t\t\t\t\t\t KAPPA BIRYANI \t\t\t\t\t Rs.56")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.101")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.106")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.86")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.151")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.123")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.112")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.156")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.206")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.216")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.266")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.384")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.406")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.380")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.56")

    
elif meal_no=="yam pottage" or meal_no=="YAM POTTAGE":
    print("\n\t\t\t\t\t\t\t YAM POTTAGE \t\t\t\t\t Rs.78")
    if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.123")
    elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.128")
    elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.108")
    elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.173")
    elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.145")
    elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.134")
    elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.178")
    elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.228")
    elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.238")
    elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.288")
    elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.406")
    elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.428")
    elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.402")
    else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.78")
    

else:
     if drinks=="cola bottle" or drinks=="COLA BOTTLE":
        print("\t\t\t\t\t\t\t COLA BOTTLE \t\t\t\t\t Rs.45")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL  \t\t\t\t\t Rs.45")
     elif drinks=="soda water" or drinks=="SODA WATER":
        print("\t\t\t\t\t\t\t SODA WATER \t\t\t\t\t Rs.50")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.50")
     elif drinks=="tonic water" or drinks=="TONIC WATER":
        print("\t\t\t\t\t\t\t TONIC WATER \t\t\t\t\t Rs.30")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.30")
     elif drinks=="red bull" or drinks=="RED BULL":
        print("\t\t\t\t\t\t\t RED BULL \t\t\t\t\t Rs.95")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.95")
     elif drinks=="guava juice" or drinks=="GUAVA JUICE":
        print("\t\t\t\t\t\t\t GUAVA JUICE \t\t\t\t\t Rs.67")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.67")
     elif drinks=="apple juice" or drinks=="APPLE JUICE":
        print("\t\t\t\t\t\t\t APPLE JUICE \t\t\t\t\t Rs.56")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.56")
     elif drinks=="smb horse stallion" or drinks=="SMB HORSE STALLLION":
        print("\t\t\t\t\t\t\t SMB HORSE STALLION \t\t\t\t Rs.100")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t RS.100")
     elif drinks=="red horse stallion" or drinks=="red horse stallion":
        print("\t\t\t\t\t\t\t RED HORSE STALLION \t\t\t\t Rs.150")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.150")
     elif drinks=="pale pilsen" or drinks=="PALE PILSEN":
        print("\t\t\t\t\t\t\t PALE PILSEN \t\t\t\t\t Rs.160")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.160")
     elif drinks=="e&s signature" or drinks=="E&S SIGNATURE":
        print("\t\t\t\t\t\t\t E&S SIGNATURE \t\t\t\t\t Rs.210")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.210")
     elif drinks=="margarita classic" or drinks=="MARGARITA CLASSIC":
        print("\t\t\t\t\t\t\t MARGARITA CLASSIC \t\t\t\t Rs.328")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.328")
     elif drinks=="mojito classic" or drinks=="MOJITO CLASSIC":
        print("\t\t\t\t\t\t\t MOJITO CLASSIC \t\t\t\t Rs.350")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.350")
     elif drinks=="green paradise" or drinks=="GREEN PARADISE":
        print("\t\t\t\t\t\t\t GREEN PARADISE \t\t\t\t Rs.324")
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t TOTAL BILL \t\t\t\t\t Rs.402")
     else:
        print("\n\t\t\t\t\t\t\t ______________________________________________________\n") 
        print("\t\t\t\t\t\t\t NOTHING ORDERED FROM OUR RESTAURANT ")
    

time.sleep(1)


print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t    THANK YOU FOR VISITING!! ")
print("\n\t\t\t\t\t\t\t\t\t      SEE YOU AGAIN SOON ")


    










          
