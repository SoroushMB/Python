from tkinter import Tk,Label,Button
from tkinter.ttk import Combobox,Style
from tkinter.messagebox import showinfo
from speedtest import Speedtest

def actor():
    selected_option : str = options_cbx.get()
    match selected_option:
        case "Download Speed":
            download_speed = (int(internet_info.download())/(10e5))/8
            showinfo(title="Download Speed" , message=f"Download Speed : {download_speed:.2f} MB/s")
        case "Upload Speed":
            upload_speed = (int(internet_info.upload())/(10e5))/8
            showinfo(title="Upload Speed" , message=f"Upload Speed : {upload_speed:.2f} MB/s")
        case "Ping":
            internet_info.get_best_server
            ping_delay = internet_info.results.ping
            showinfo(title="Ping" , message=f"Ping : {ping_delay} ms")

internet_info = Speedtest()
main_page = Tk()
main_page.title(string="Speedtest!")
main_page.config(background="#031926")

style = Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground = "#031926", background="#031926")

options = ["Download Speed" , "Upload Speed" , "Ping"]
choosing_lbl = Label(master=main_page,text="Options : ",bg="#031926",fg="#7678ed",font=("Product Sans Medium",16))
options_cbx = Combobox(master=main_page,values=options,font=("Product Sans Medium",16),foreground="#7678ed",state="normal")
show_btn = Button(master=main_page,text="Press to show!",bg="#bdb2ff",fg="#03045e",font=("Product Sans Medium",16),command=lambda:actor())

choosing_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
options_cbx.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
show_btn.grid(row=1,column=0,padx=10,pady=10,columnspan=2,sticky="nsew")

main_page.mainloop()