import tkinter.messagebox
from tkinter import *
from funcs import get_miles_from_zips, get_coordinates_from_zip


def get_trip_info():
    origin = origin_field.get()
    dest = dest_field.get()
    origin_payload = get_coordinates_from_zip(origin)
    destination_payload = get_coordinates_from_zip(dest)
    the_results = get_miles_from_zips(origin_payload['coordinates'], destination_payload['coordinates'])
    if origin_payload['msg'] != 'success' or destination_payload['msg'] != 'success':
        tkinter.messagebox.showerror("Mileage Error", "Invalid Request")
        return None
    if len(origin) != 5 or len(dest) != 5:
        tkinter.messagebox.showerror("Zip Code Error", "Zip Codes will need to be 5 digits")
        return None
    if not origin.isdigit():
        tkinter.messagebox.showerror("Zip Code Error", "Origin Zip will need to be a numerical value")
        return None
    if not dest.isdigit():
        tkinter.messagebox.showerror("Zip Code Error", "Destination Zip will need to be a numerical value")
        return None
    try:
        mystr.set(origin_payload['zip info']['locality'])
    except:
        mystr.set("None")
    try:
        origin_state.set(origin_payload['zip info']['adminDistrict'])
    except:
        origin_state.set("XX")
    try:
        destination_city.set(destination_payload['zip info']['locality'])
    except:
        destination_city.set("None")
    try:
        destination_state.set(destination_payload['zip info']['adminDistrict'])
    except:
        destination_state.set("XX")
    try:
        mileage.set(the_results['resourceSets'][0]['resources'][0]['travelDistance'])
    except:
        mileage.set("-1")
    return None


def clear_data():
    origin_field.delete(0, END)
    dest_field.delete(0, END)
    mystr.set("")
    origin_state.set("")
    destination_city.set("")
    destination_state.set("")
    mileage.set("")


if __name__ == "__main__":
    root = Tk()

    mystr = StringVar()
    origin_state = StringVar()
    destination_city = StringVar()
    destination_state = StringVar()
    mileage = StringVar()

    root.configure(background='light green')
    root.geometry('500x300')
    root.title("Sean Smith Trucking API GUI")

    head_label = Label(root, text="GUI For Trucking API", fg='black', bg='white')
    head_label.grid(row=0, column=0)

    origin_label = Label(root, text="Origin ZIP", fg='black', bg='white')
    origin_label.grid(row=1, column=0, sticky='W')

    dest_label = Label(root, text="Destination ZIP", fg='black', bg='white')
    dest_label.grid(row=2, column=0, sticky='W')

    origin_field = Entry(root)
    origin_field.grid(row=1, column=1, ipadx="100")

    dest_field = Entry(root)
    dest_field.grid(row=2, column=1, ipadx="100")

    dest_label = Label(root, text="Destination Zip", fg='black', bg='white')
    dest_label.grid(row=2, column=0, sticky='W')

    results_label = Label(root, text="Distance Results", fg='black', bg='white')
    results_label.grid(row=7, column=0, sticky='W')

    origin_city_label = Label(root, text="Origin City", fg='black', bg='white')
    origin_city_label.grid(row=8, column=0, sticky='W')

    origin_state_label = Label(root, text="Origin State", fg='black', bg='white')
    origin_state_label.grid(row=9, column=0, sticky='W')

    dest_city_label = Label(root, text="dest City", fg='black', bg='white')
    dest_city_label.grid(row=10, column=0, sticky='W')

    origin_state_label = Label(root, text="dest State", fg='black', bg='white')
    origin_state_label.grid(row=11, column=0, sticky='W')

    mileage_label = Label(root, text="Mileage", fg='black', bg='white')
    mileage_label.grid(row=12, column=0, sticky='W')

    origin_city_results_field = Entry(root, state='disabled', textvariable=mystr)
    origin_city_results_field.grid(row=8, column=1, ipadx="100")

    origin_state_results_field = Entry(root, state='disabled', textvariable=origin_state)
    origin_state_results_field.grid(row=9, column=1, ipadx="100")

    dest_city_results_field = Entry(root, state='disabled', textvariable=destination_city)
    dest_city_results_field.grid(row=10, column=1, ipadx="100")

    dest_state_results_field = Entry(root, state='disabled', textvariable=destination_state)
    dest_state_results_field.grid(row=11, column=1, ipadx="100")

    mileage_field = Entry(root, state='disabled', textvariable=mileage)
    mileage_field.grid(row=12, column=1, ipadx="100")

    button3 = Button(root, text="RESULT",
                     bg="red", fg="black",
                     command=get_trip_info)

    button3.grid(row=6, column=1)

    button4 = Button(root, text="CLEAR",
                     bg="red", fg="black",
                     command=clear_data)

    button4.grid(row=6, column=2)

    root.mainloop()
