from tkinter import *
from tkinter import ttk

# Pillow import

from PIL import ImageTk, Image

# colour

col1 = '#3b3b3b' # black
col2 = '#ffffff' # white
col3 = '#48b3e0' # blue
col4 = '#000000' # black noir
col5 = '#cdf505' # Yellow

window = Tk()
window.title('')
window.geometry("650x260")
window.configure(bg=col1)


# --------------- Window frames -----------

top_frame = Frame(window, width=450, height=50, bg=col2, pady=0, padx=3, relief='flat')
top_frame.place(x=2, y=2)

left_frame = Frame(window, width=450, height=220, bg=col2, pady=0, padx=3, relief='flat')
left_frame.place(x=2, y=54)

right_frame = Frame(window, width=198, height=260, bg=col2, pady=0, padx=3, relief='flat')
right_frame.place(x=454, y=2)

# --------------- Window style -----------
style = ttk.Style(window)
style.theme_use("clam")

# --------------- Top Frame Config -----------
l_app_name = Label(top_frame, text="Conversion Calculator", height=1, padx=0, relief='flat', anchor='center', font=("Ivy 15 bold"), bg=col2, fg=col3)
l_app_name.place(x=50, y=10)



# --------------- Units -----------

units = {"Weight":[{'kg':1}, {'g':1000}, {'mlg':1000000}, {'p(lb)':2.2046226218488}, {'ton':0.001}, {'grain':15432.358352941}] ,
         "Time":[{'day': 1}, {'sec': 86400}, {'min': 1440}, {'hour': 24}, {'week': 0.142857}, {'month': 0.032854}, {'year': 0.002738}] ,
         "Length":[{'m':1}, {'mlm':1000}, {'cen':100}, {'dec':10}, {'Km':0.001}, {'ft':3.280839895013123}, {'inch':39.370078740157474}, {'mile':0.0006213711922373338}, {'yard':1.0936132983377076}] ,
         "Speed":[{'m/s':1}, {'km/h':3.6}, {'ml/h':2.2369279522789}, {'kn':1.9438444924406}, {'ft/s':3.2808398950131}] ,
         "Area":[{'km2':1}, {'m2':1000000}, {'hec':100}, {'ac':247.1046}, {'mile2':0.3861}, {'inch2':1550003100.0062}] ,
         "Volume":[{'l':1}, {'m3':0.001}, {'ml3':1000000}, {'gal':0.2270208}, {'bu':0.02837759}, {'qt':0.9080832}] ,
         "Temperature":[{'C':1}, {'F':33.8}, {'N':0.33}, {'K':274.15}, {'R':0.8}, {'Ra':493.47}, {'Rø':8.025}] ,
         "Energy":[{'kJ':1}, {'kcal':0.23884589662749592}, {'J':1000}, {'kWh':0.0002777777777777778}, {'cal':238.84589662749596}, {'Wh':0.2777777777777778}, {'Ws':1000}] ,
         "Pressure":[{'atm':1}, {'Pa N/m2':101325}, {'kPa':101.325}, {'mb':1013.25}, {'bar':1.013}, {'kbar':0.00101}, {'kg/cm2':1.033}, {'psi':14.696}, {'psf':2116.217}]}



def show_menu(i):

    unit_from = []
    unit_to = []
    unit_value = []

    for j in units[i]:
        for k, v in j.items():
            unit_from.append(k)
            unit_to.append(k)
            unit_value.append(v)
    

    c_from['values'] = unit_from
    c_to['values'] = unit_to

    l_unit_name['text'] = i



    def calculate():

        # Units Calculation
        a = c_from.get()
        b = c_to.get()

        # Units result
        unit_to_convert = float(e_number.get())

        dist = unit_to.index(b) - unit_from.index(a)
        
        # Mult
        if unit_to.index(a) <= unit_from.index(b):
            
            #Checking Units
            distance = unit_to.index(b) - unit_from.index(a)
            result = unit_to_convert *(10**distance)

            l_result['text'] = result

        else:
            
            #Checking Units
            distance = unit_from.index(a) - unit_to.index(b)
            result = unit_to_convert *(10**distance)

            # Division
        if unit_to.index(a) > unit_from.index(b):
            
            #Checking Units
            distance = unit_to.index(b) - unit_from.index(a)
            result = unit_to_convert /(10**distance)

            l_result['text'] = result

        else:
            
            #Checking Units
            distance = unit_from.index(a) - unit_to.index(b)
            result = unit_to_convert /(10**distance)
            l_result['tex'] = result

    # Label Creation

    l_info = Label(right_frame, text="Enter Unit", width=16, height=2, padx=5, pady=3, relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col2, fg=col4)
    l_info.place(x=0, y=120)

    e_number = Entry(right_frame, width=9, font=("Ivy 15 bold"), justify='center', relief=SOLID)
    e_number.place(x=0, y=150)

    b_calculate = Button(right_frame, command=calculate, text="Calculate", width=8, height=1, overrelief="ridge", relief='raised', anchor='nw', font=("Ivy 10 bold"), bg=col5, fg=col4)
    b_calculate.place(x=115, y=150)
    

    l_result = Label(right_frame, text="", width=11, height=1, padx=5, pady=3, relief='groove', anchor='center', font=("Ivy 18 bold"), bg=col2, fg=col4)
    l_result.place(x=0, y=200)





# --------------- Left Frame Config -----------

# Weight
img_0 = Image.open("images/Weight.png")
img_0 = img_0.resize((50,50))
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(left_frame, command=lambda:show_menu('Weight'), text="Weight", image=img_0, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

# Time
img_1 = Image.open("images/Time.png")
img_1 = img_1.resize((50,50))
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(left_frame, command=lambda:show_menu('Time'), text="Time", image=img_1, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

# Length
img_2 = Image.open("images/Length.png")
img_2 = img_2.resize((50,50))
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(left_frame, command=lambda:show_menu('Length'), text="Length", image=img_2, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_2.grid(row=0, column=2, sticky=NSEW, pady=5, padx=5)

# Area
img_3 = Image.open("images/Area.png")
img_3 = img_3.resize((50,50))
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(left_frame, command=lambda:show_menu('Area'), text="Area", image=img_3, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_3.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

# Volume
img_4 = Image.open("images/Volume.png")
img_4 = img_4.resize((50,50))
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(left_frame, command=lambda:show_menu('Volume'), text="Volume", image=img_4, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_4.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

# Speed
img_5 = Image.open("images/Speed.png")
img_5 = img_5.resize((50,50))
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(left_frame, command=lambda:show_menu('Speed'), text="Speed", image=img_5, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_5.grid(row=1, column=2, sticky=NSEW, pady=5, padx=5)

# Temperature
img_6 = Image.open("images/Temperature.png")
img_6 = img_6.resize((50,50))
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(left_frame, command=lambda:show_menu('Temperature'), text="Temperature", image=img_6, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_6.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

# Energy
img_7 = Image.open("images/Energy.png")
img_7 = img_7.resize((50,50))
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(left_frame, command=lambda:show_menu('Energy'), text="Energy", image=img_7, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_7.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

#Pressure
img_8 = Image.open("images/Pressure.png")
img_8 = img_8.resize((50,50))
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(left_frame, command=lambda:show_menu('Pressure'), text="Pressure", image=img_8, compound=LEFT, width=130, height=50, overrelief="solid", relief='flat', anchor='nw', font=("Ivy 10 bold"), bg=col3, fg=col4)
b_8.grid(row=2, column=2, sticky=NSEW, pady=5, padx=5)


# --------------- Top Right Frame Config -----------

l_unit_name = Label(right_frame, text="Unit", width=15, height=2, padx=0, relief='groove', anchor='center', font=("Ivy 15 bold"), bg=col2, fg=col1)
l_unit_name.place(x=0, y=0)

# --------------- Bottom Right Frame Config -----------

l_from = Label(right_frame, text="From", height=1, padx=3, relief='groove', anchor='center', font=("Ivy 10 bold"), bg=col2, fg=col1)
l_from.place(x=0, y=70)
c_from = ttk.Combobox(right_frame, width=5, justify=("center"),font=("Ivy 10 bold"))
c_from.place(x=45, y=70)


l_to = Label(right_frame, text="To", height=1, padx=3, relief='groove', anchor='center', font=("Ivy 10 bold"), bg=col2, fg=col1)
l_to.place(x=105, y=70)
c_to = ttk.Combobox(right_frame, width=5, justify=("center"),font=("Ivy 10 bold"))
c_to.place(x=135, y=70)






window.mainloop()
