from bs4 import BeautifulSoup as bs

import pyttsx3 as pt

import speech_recognition as sr

import requests

engine = pt.init()

def get_phone():

    myurl = "https://gadgets.ndtv.com/mobiles/samsung-price-list"

    response = requests.get(myurl)

    soup = bs(response.content,"html.parser")

    name = soup.find_all("a",{"class":"rvw-title"})

    price_list = []

    name_list = []

    for i in name:

        name_list.append(i.text.lower())

    price = soup.find_all("div",{"class":"_flx _bwrp"})

    for x in price:

        price_list.append(x.text)

    myurl2 = "https://gadgets.ndtv.com/mobiles/apple-price-list"

    response2 = requests.get(myurl2)

    soup2 = bs(response2.content,"html.parser")

    name2 = soup2.find_all("a",{"class":"rvw-title"})

    for i in name2:

        name_list.append(i.text.lower())

    price2 = soup2.find_all("div",{"class":"_flx _bwrp"})

    for x in price2:

        price_list.append(x.text)

    print("Welcome to our Website ! How may I help you ? Which phone do you want ? Please enter the phone you want.")

    engine.say("Welcome to our Website ! How may I help you ? Which phone do you want ? Please enter the phone you want.")

    engine.runAndWait()

    while True:

        user_input = int(input("Enter 0 for typing or 1 for speaking: "))

        if user_input == 0:

            user_said = input("Enter the phone name : ")

            break

        elif user_input == 1:

            while True:

                r = sr.Recognizer()

                with sr.Microphone() as source:

                    audio = r.listen(source)

                    said = ""

                    try:

                        said = r.recognize_google(audio)

                        user_said = said.lower()

                        print(user_said)

                        break 

                    except:

                        print("I did not understand.")

            break

        else:

            print("I did not understand.")

    
    a = 0

    for index,value in enumerate(name_list):

        if user_said in value:

            print(value,price_list[index])

            engine.say(value)

            engine.say(price_list[index])

            engine.runAndWait()

            a = 1

    if a == 0:

        print("Sorry this model is not available !")

        engine.say("Sorry this model is not available !")

        engine.runAndWait()


def get_tv():

    myurl3 = "https://gadgets.ndtv.com/tv/samsung-tv"

    response3 = requests.get(myurl3)

    soup3 = bs(response3.content,"html.parser")

    tv_name = soup3.find_all("h3",{"class":"_hd"})

    tvnames = []

    for item in tv_name:

        tvnames.append(item.text.lower())

    tvprices = []

    tv_price = soup3.find_all("a",{"class":"_lprc"})

    for item2 in tv_price:

        tvprices.append(item2.text)

    myurl4 = "https://gadgets.ndtv.com/tv/samsung-tv?facet[brand]=LG&sort=release_priority,product_id&order=desc"

    response4 = requests.get(myurl4)

    soup4 = bs(response4.content,"html.parser")

    lg_name = soup4.find_all("h3",{"class":"_hd"})

    for tv in lg_name:

        tvnames.append(tv.text.lower())

    lg_price = soup4.find_all("div",{"class":"_lprc"})

    for price in lg_price:

        tvprices.append(price.text.lower())

    print("Welcome to our Website ! How may I help you ? Which tv do you want ? Please enter the tv you want.")

    engine.say("Welcome to our Website ! How may I help you ? Which tv do you want ? Please enter the tv you want.")

    engine.runAndWait()

    while True:

        user_input = int(input("Enter 0 for typing or 1 for speaking: "))

        if user_input == 0:

            user_said = input("Enter the tv name : ")

            break

        elif user_input == 1:

            while True:

                r = sr.Recognizer()

                with sr.Microphone() as source:

                    audio = r.listen(source)

                    said = ""

                    try:

                        said = r.recognize_google(audio)

                        user_said = said.lower()

                        print(user_said)

                        break 

                    except:

                        print("I did not understand.")

            break

        else:

            print("I did not understand.")

    b = 0

    for index,value in enumerate(tvnames):

        if user_said in value:

            z = tvprices[index].split()

            if len(z) == 4:

                print(value,"Discounted Price: ",z[0],z[1],"Original Price: ",z[2],z[3])

                engine.say("{} Discounted Price: {} {} Original Price: {} {}".format(value,z[0],z[1],z[2],z[3]))

                engine.runAndWait()

                b = 1

            else:

                print(value,tvprices[index])

                engine.say(value,tvprices[index])

                engine.runAndWait()

                b = 1

    if b == 0:

        print("Sorry this model is not available !")

        engine.say("Sorry this model is not available !")

        engine.runAndWait()

def get_smart_watch():

    myurl5 = "https://gadgets.ndtv.com/wearables/smart-watches-price-list"

    response5 = requests.get(myurl5)

    soup5 = bs(response5.content,"html.parser")

    watch_name = soup5.find_all("h3",{"class":"_hd"})

    watch_names = []

    for watch in watch_name:

        watch_names.append(watch.text.lower())

    watch_price = soup5.find_all("a",{"class":"_lprc"})

    watch_prices = []

    for l in watch_price:

        watch_prices.append(l.text.lower())

    print("Welcome to our Website ! How may I help you ? Which smart watch do you want ? Please enter the smart watch you want.")

    engine.say("Welcome to our Website ! How may I help you ? Which smart watch do you want ? Please enter the smart watch you want.")

    engine.runAndWait()

    while True:

        user_input = int(input("Enter 0 for typing or 1 for speaking: "))

        if user_input == 0:

            user_said = input("Enter the watch name : ")

            break

        elif user_input == 1:

            while True:

                r = sr.Recognizer()

                with sr.Microphone() as source:

                    audio = r.listen(source)

                    said = ""

                    try:

                        said = r.recognize_google(audio)

                        user_said = said.lower()

                        print(user_said)

                        break 

                    except:

                        print("I did not understand.")

            break

        else:

            print("I did not understand.")

    f = 0

    for index,value in enumerate(watch_names):

        if user_said in value:

            y = watch_prices[index].split()

            if len(y) == 4:

                print(value,"Discounted Price: ",y[0],y[1],"Original Price: ",y[2],y[3])

                engine.say("{} Discounted Price: {} {} Original Price: {} {}".format(value,y[0],y[1],y[2],y[3]))

                engine.runAndWait()

                f = 1 

            else:

                print(value,watch_prices[index])

                engine.say(value,watch_prices[index])

                engine.runAndWait()

                f = 1

    if f == 0:

        print("Sorry this model is not available !")

        engine.say("Sorry this model is not available !")

        engine.runAndWait()

def get_camera():

    myurl6 = "https://gadgets.ndtv.com/cameras/price-list-india?sort=release_priority,product_id&order=desc"

    response6 = requests.get(myurl6)

    soup6 = bs(response6.content,"html.parser")

    cam_name = soup6.find_all("h3",{"class":"_hd"})

    camera_names = []

    for u in cam_name:

        camera_names.append(u.text.lower())

    cam_price = soup6.find_all("a",{"class":"_lprc"})

    camera_prices = []

    for x in cam_price:

        camera_prices.append(x.text.lower())

    print("Welcome to our Website ! How may I help you ? Which camera do you want ? Please enter the camera you want.")

    engine.say("Welcome to our Website ! How may I help you ? Which camera do you want ? Please enter the camera you want.")

    engine.runAndWait()

    while True:

        user_input = int(input("Enter 0 for typing or 1 for speaking: "))

        if user_input == 0:

            user_said = input("Enter the watch name : ")

            break

        elif user_input == 1:

            while True:

                r = sr.Recognizer()

                with sr.Microphone() as source:

                    audio = r.listen(source)

                    said = ""

                    try:

                        said = r.recognize_google(audio)

                        user_said = said.lower()

                        print(user_said)

                        break 

                    except:

                        print("I did not understand.")

            break

        else:

            print("I did not understand.")

    f = 0

    for index,value in enumerate(camera_names):

        if user_said in value:

            y = camera_prices[index].split()

            if len(y) == 4:

                print(value,"Discounted Price: ",y[0],y[1],"Original Price: ",y[2],y[3])

                engine.say("{} Discounted Price: {} {} Original Price: {} {}".format(value,y[0],y[1],y[2],y[3]))

                engine.runAndWait()

                f = 1 

            else:

                print(value,camera_prices[index])

                engine.say(value,camera_prices[index])

                engine.runAndWait()

                f = 1

    if f == 0:

        print("Sorry this model is not available !")

        engine.say("Sorry this model is not available !")

        engine.runAndWait()

def get_tablet():

    myurl7 = "https://gadgets.ndtv.com/tablets/price-list-india"

    response7 = requests.get(myurl7)

    soup7 = bs(response7.content,"html.parser")

    tab_name = soup7.find_all("h3",{"class":"_hd"})

    tablet_names = []

    for o in tab_name:

        tablet_names.append(o.text.lower())

    tab_price = soup7.find_all("a",{"class":"_lprc"})

    tablet_prices = []

    for q in tab_price:

        tablet_prices.append(q.text.lower())

    while True:

        user_input = int(input("Enter 0 for typing or 1 for speaking: "))

        if user_input == 0:

            user_said = input("Enter the watch name : ")

            break

        elif user_input == 1:

            while True:

                r = sr.Recognizer()

                with sr.Microphone() as source:

                    audio = r.listen(source)

                    said = ""

                    try:

                        said = r.recognize_google(audio)

                        user_said = said.lower()

                        print(user_said)

                        break 

                    except:

                        print("I did not understand.")

            break

        else:

            print("I did not understand.")

    f = 0

    for index,value in enumerate(tablet_names):

        if user_said in value:

            y = tablet_prices[index].split()

            if len(y) == 4:

                print(value,"Discounted Price: ",y[0],y[1],"Original Price: ",y[2],y[3])

                engine.say("{} Discounted Price: {} {} Original Price: {} {}".format(value,y[0],y[1],y[2],y[3]))

                engine.runAndWait()

                f = 1 

            else:

                print(value,tablet_prices[index])

                engine.say(value,tablet_prices[index])

                engine.runAndWait()

                f = 1

    if f == 0:

        print("Sorry this model is not available !")

        engine.say("Sorry this model is not available !")

        engine.runAndWait()

def get_gameconsole():

    myurl8 = "https://gadgets.ndtv.com/games/gaming-consoles-price-list-india"

    response8 = requests.get(myurl8)

    soup8 = bs(response8.content,"html.parser")

    c_name = soup8.find_all('h3',{"class":"_hd"})

    console_names = []

    for x in c_name:

        console_names.append(x.text.lower())

    c_price = soup8.find_all('a',{"class":"_lprc"})

    console_prices = []

    for y in c_price:

        console_prices.append(y.text.lower())

    while True:

        user_input = int(input("Enter 0 for typing or 1 for speaking: "))

        if user_input == 0:

            user_said = input("Enter the gaming console name : ")

            break

        elif user_input == 1:

            while True:

                r = sr.Recognizer()

                with sr.Microphone() as source:

                    audio = r.listen(source)

                    said = ""

                    try:

                        said = r.recognize_google(audio)

                        user_said = said.lower()

                        print(user_said)

                        break 

                    except:

                        print("I did not understand.")

            break

        else:

            print("I did not understand.")

    f = 0

    for index,value in enumerate(console_names):

        if user_said in value:

            y = console_prices[index].split()

            if len(y) == 4:

                print(value,"Discounted Price: ",y[0],y[1],"Original Price: ",y[2],y[3])

                engine.say("{} Discounted Price: {} {} Original Price: {} {}".format(value,y[0],y[1],y[2],y[3]))

                engine.runAndWait()

                f = 1 

            else:

                print(value,console_prices[index])

                engine.say(value,console_prices[index])

                engine.runAndWait()

                f = 1

    if f == 0:

        print("Sorry this model is not available !")

        engine.say("Sorry this model is not available !")

        engine.runAndWait()     

print('''
Enter: 
1 for phones
2 for tvs
3 for smart watches
4 for cameras
5 for tablets
6 for gaming consoles
0 to exit''')

engine.say("Enter: 1 for phones or 2 for tvs or 3 for smart watches or 4 for cameras or 5 for tablets or 6 for gaming consoles or 0 to exit")

engine.runAndWait()
    
while True:

    user_choice = int(input("Enter your choice (Enter 0 to exit): "))

    if user_choice == 1:

        get_phone()

    elif user_choice == 2:

        get_tv()

    elif user_choice == 0:

        print("Thank you for visiting our website. Good Bye !")

        engine.say("Thank you for visiting our website. Good Bye !")

        engine.runAndWait()

        break

    elif user_choice == 3:

        get_smart_watch()

    elif user_choice == 4:

        get_camera()

    elif user_choice == 5:

        get_tablet()

    elif user_choice == 6:

        get_gameconsole()

    else:

        print("Please enter the correct value !")

        engine.say("Please enter the correct value !")

        engine.runAndWait()