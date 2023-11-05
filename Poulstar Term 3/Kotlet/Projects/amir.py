from tkinter import Tk,Entry,Label,Button,Toplevel
from tkinter.ttk import Combobox,Spinbox
from os import system
from time import strftime
import pyttsx3
from win10toast import ToastNotifier
from PIL import ImageTk,Image

system("cls")



def page_sabt():
            global lshahr,lshahr0,llocation,elocation,lproblem,eproblem,lnumber_phone,enumber_phone,bnext2
            lshahr = Label(window, text=f"Select Your {ostan} State City:", bg="darkred", fg="black", font=("aria", 10 ,"bold"))
            lshahr0 = Combobox(window, values=shahrha[0], font=("arial", 10 ,"bold"))
            llocation = Label(window, text="Write The Address Of The Accident Area Or Your Area:", bg="darkred", fg="black", font=("aria", 10 ,"bold"))
            elocation = Entry(window, bg="#969492")
            lproblem = Label(window, text="Write a Description Of The Incident:", bg="darkred", fg="black", font=("arial", 10 ,"bold"))
            eproblem = Entry(window, bg="#969492")
            lnumber_phone = Label(window, text="Write Your Contact Number", bg="darkred", fg="black", font=("aria", 10 ,"bold"))
            enumber_phone = Entry(window, bg="#969492")
            bnext2 = Button(window, text="Submit:", bg="darkgreen", fg="black", font=("arial", 10 ,"bold"), command=Sabt)

            bnext.grid_remove()
            lshahr.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
            lshahr0.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
            llocation.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
            elocation.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
            lproblem.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
            eproblem.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
            lnumber_phone.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
            enumber_phone.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
            bnext2.grid(row=5, column=0,columnspan=2 ,sticky="nsew", padx=5, pady=5)
def save_sabt():
        global page_sabt,lshahr,lshahr0,llocation,elocation,lproblem,eproblem,lnumber_phone,enumber_phone,bnext2
        bnext2["state"] = "disabled"
        elocation["state"] = "readonly"
        eproblem["state"] = "readonly"
        enumber_phone["state"] = "readonly"
        text = "Your request has been sent to 9 1 1 Dispatch"
        sound = pyttsx3.init()
        sound.setProperty('rate', 160)
        sound.say(text)
        sound.runAndWait()
        toast = ToastNotifier()
        toast.show_toast(
            "911 Dispatch",
            "Your Request Has Been Sent To 911 Dispatch",
            threaded = True,
            icon_path = None,
            duration = 5)
        reciptime = strftime("%H:%M:%S")
        reciptFile = open("Recipt4.txt","a")
        reciptFile.write("\n")
        reciptFile.write(30*"--")
        reciptFile.write(f"\nTime Ersal Darkhast:{reciptime}")
        reciptFile.write("\nForm Darkhast Amdad!!!")
        reciptFile.write(f"\nName Fard: {ename.get()}")
        reciptFile.write(f"\nJensiat Fard: {combo_gender.get()}")
        reciptFile.write(f"\nSen Fard: {eege.get()}")
        reciptFile.write(f"\nKomak Mord Niaz Frad: {lcombo_opt.get()}")
        reciptFile.write(f"\nOstan Frad: {combo_ostan.get()}")
        reciptFile.write(f"\nShahrestan Frad: {lshahr0.get()}")
        reciptFile.write(f"\nAdres Daghigh Fard Ya Mahal Hadese: {elocation.get()}")
        reciptFile.write(f"\nSharhe Hadese: {eproblem.get()}")
        reciptFile.write(f"\nShomareh Telephone Hamrah Frad: {enumber_phone.get()}")
        reciptFile.close()


ostanha = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware"
        , "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", " Kansas", "Kentucky[B]"
        , "Louisiana", "Maine", "Maryland", "Massachusetts[B]", "Michigan", " Minnesota", "Mississippi"
        , "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York"
        , "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania[B]", "Rhode Island"
        , "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia[B]"
        , "Washington", "West Virginia", " Wisconsin", "Wyoming"]
genders = ["Male","Female"]
ages = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"
        ,"20" ,"21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37"
        ,"38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55"
        ,"56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73"
        ,"75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91"
        ,"92", "93", "94", "95", "96", "97", "98", "99", "100"]
opts = ["FBI", "Police", "Medic", "Fire Fighters", "Mechanic"]
shahrha = {
    0: ("Huntsville", "Birmingham", "Montgomery", "Mobile", "Tuscal", "Other"), # Alabama
    1: ("Anchorage", "Fairbanks", "Juneau", "Wasilla", "Sitka", "Other"), # Alaska
    2: ("Yuma", "Phoenix", "Tucson", "Kingman", "Prescott", "Other"), # Arizona
    3: ("Little Rock", "Fort Smith", "Fayetteville", "Springdale", "Jonesboro", "Other"), # Arkansas
    4: ("Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno", "Other"), # California
    5: ("Denver", "Colorado Springs", "Aurora", "Fort Collins", "Lakewood", "Other"), # Colorado
    6: ("Bridgeport", "Stamford", "New Haven", "Hartford", "Waterbury", "Other"), # Connecticut
    7: ("Wilmington", "Dover", "Newark", "Middletown", "Bear", "Other"), # Delaware
    8: ("Jacksonville", "Miami", "Tampa", "Orlando", "St. Petersburg", "Other"), # Florida
    9: ("Atlanta", "Columbus", "Augusta", "Macon", "Savannah", "Other"), # Georgia
    10: ("Honolulu", "East Honolulu", "Pearl City", "Hilo", "Waipahu", "Other"), # Hawaii
    11: ("", "", "", "", "", "", "Other"),
    12: ("", "", "", "", "", "", "Other"),
    13: ("", "", "", "", "", "", "Other"),
    14: ("", "", "", "", "", "", "Other"),
    15: ("", "", "", "", "", "", "Other"),
    16: ("", "", "", "", "", "", "Other"),
    17: ("", "", "", "", "", "", "Other"),
    18: ("", "", "", "", "", "", "Other"),
    19: ("", "", "", "", "", "", "Other"),
    20: ("", "", "", "", "", "", "Other"),
    21: ("", "", "", "", "", "", "Other"),
    22: ("", "", "", "", "", "", "Other"),
    23: ("", "", "", "", "", "", "Other"),
    24: ("", "", "", "", "", "", "Other"),
    25: ("", "", "", "", "", "", "Other"),
    26: ("", "", "", "", "", "", "Other"),
    27: ("", "", "", "", "", "", "Other"),
    28: ("", "", "", "", "", "", "Other"),
    29: ("", "", "", "", "", "", "Other"),
    30: ("", "", "", "", "", "", "Other"),
    31: ("", "", "", "", "", "", "Other"),
    32: ("", "", "", "", "", "", "Other"),
    33: ("", "", "", "", "", "", "Other"),
    34: ("", "", "", "", "", "", "Other"),
    35: ("", "", "", "", "", "", "Other"),
    36: ("", "", "", "", "", "", "Other"),
    37: ("", "", "", "", "", "", "Other"),
    38: ("", "", "", "", "", "", "Other"),
    39: ("", "", "", "", "", "", "Other"),
    40: ("", "", "", "", "", "", "Other"),
    41: ("", "", "", "", "", "", "Other"),
    42: ("", "", "", "", "", "", "Other"),
    43: ("", "", "", "", "", "", "Other"),
    44: ("", "", "", "", "", "", "Other"),
    45: ("", "", "", "", "", "", "Other"),
    46: ("", "", "", "", "", "", "Other"),
    47: ("", "", "", "", "", "", "Other"),
    48: ("", "", "", "", "", "", "Other"),
    49: ("", "", "", "", "", "", "Other"),
    50: ("", "", "", "", "", "", "Other")
}

# fbi_photo = ImageTk.PhotoImage(Image.open(rf"C:\Users\Zahra Alizadeh\Desktop\اموزش برنامه نویسی\istockphoto-1184836915-612x612.jpg"))
# police_photo = ImageTk.PhotoImage(Image.open(rf"C:\Users\Zahra Alizadeh\Desktop\اموزش برنامه نویسی\1691503985302.JPEG"))
# medic_photo = ImageTk.PhotoImage(Image.open(rf"C:\Users\Zahra Alizadeh\Desktop\اموزش برنامه نویسی\Doctors_For_Men-732x549-thumbnail.jpg"))
# firefighter_photo = ImageTk.PhotoImage(Image.open(rf"C:\Users\Zahra Alizadeh\Desktop\اموزش برنامه نویسی\1691503986623.JPEG"))
# mechanic_photo = ImageTk.PhotoImage(Image.open(rf"C:\Users\Zahra Alizadeh\Desktop\اموزش برنامه نویسی\depositphotos_84859334-stock-photo-hands-of-car-mechanic.jpg"))
x = 0
y = len(ostanha) - 1

def dnext():
    global shahrha,eege,bnext2,ege,name,ostan,lshahr,lshahr0,lshahr1,lshahr2,lshahr3,elocation,enumber_phone,eproblem,page_sabt,x,y,z
    name = ename.get()
    name = name.lower().strip()
    ostan = combo_ostan.get()
    ege = eege.get()
    ege = int(ege)
    if lcombo_opt.get() in opts and combo_gender.get() in genders and (len(name)) > 2 and ege > 0 and ege < 101 and ostan in ostanha:
        while x <= y:
            if ostan == ostanha[x]:
                page_sabt()
                lshahr0.config(values=shahrha[x])
                break
            elif ostan != ostanha[x]:
                x += 1   

def Sabt():
    global page_sabt,lshahr,lshahr0,llocation,elocation,lproblem,eproblem,lnumber_phone,enumber_phone,bnext2,save_sabt
    if ostan == ostanha[x]:
        if lshahr0.get() in shahrha[x] and (len(eproblem.get())) > 2 and (len(elocation.get())) > 2 and (len(enumber_phone.get())) == 11:
            save_sabt()
            
#             End()
# def End():
#     window.deiconify()
#     window_top = Toplevel()
#     end_label = Label(window_top,image=fbi_photo)
#     end_label.pack()
#     window_top.mainloop()

window = Tk()
window.resizable(False, False)
window.title("911 Dispatch")
window["bg"] = "#02e4f0"


l911 = Label(window, text="911 Emergency Responder Dispatch", bg="blue", fg="black", font=("aria", 10 ,"bold"))
lopt = Label(window, text="Select The Type Of Help You Need:", bg="darkred", fg="black", font=("arial", 10 ,"bold"))
lcombo_opt = Combobox(window, values=opts, font=("arial", 10 ,"bold"))
lgender = Label(window, text="Choose Your Gender:", bg="darkred", fg="black", font=("aria", 10 ,"bold"))
combo_gender = Combobox(window, values=genders, font=("aria", 10 ,"bold"))
lname = Label(window, text="Enter Your First And Last Name:", bg="darkred", fg="black", font=("aria", 10 ,"bold"))
ename = Entry(window, bg="white")
lege = Label(window, text="Enter Your Age:", bg="darkred", fg="black", font=("arial", 10 ,"bold"))
eege = Spinbox(window,values=ages)
lostan = Label(window, text="Select Your State:", bg="darkred", fg="black", font=("aria", 10 ,"bold"))
combo_ostan = Combobox(window, values=ostanha, font=("aria", 10 ,"bold"))
bnext = Button(window, text="Next", bg="darkgreen", fg="black", font=("arial", 10 ,"bold"), command=dnext)


l911.grid(row=0, column=0,columnspan=2 , sticky="nsew", padx=5, pady=5)
lopt.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
lcombo_opt.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
lgender.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
combo_gender.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
lname.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
ename.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
lege.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)
eege.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)
lostan.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
combo_ostan.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
bnext.grid(row=6, column=0,columnspan=2 ,sticky="nsew", padx=5, pady=5)

text = "9 1 1 Whats Your Location Emergency"
sound = pyttsx3.init()
sound.setProperty('rate', 160)
sound.say(text)
sound.runAndWait()


window.mainloop()




