from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox
from tkinter.font import Font

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

window = Tk()
window.title("HOME")
window.iconbitmap('wash.ico')
window.geometry("370x650")

def home():
    clear_window()
    window.title("HOME")

    # Gambar Utama
    window.img1 = PhotoImage(file="estetik.png")
    canvas1 = Canvas(window, width=366, height=240)
    canvas1.pack()
    canvas1.create_image(0, 0, anchor=NW, image=window.img1)

    window.img2 = PhotoImage(file="kurir.png")
    canvas2 = Canvas(window, width=569, height=240)
    canvas2.place(x=0, y=451)
    canvas2.create_image(0, 0, anchor=NW, image=window.img2)

    # Alamat, jam operational beserta Logo
    window.img3 = PhotoImage(file="location.png")
    canvas3 = Canvas(window, width=44, height=44)
    canvas3.place(x=70, y=320)
    canvas3.create_image(2, 7, anchor=NW, image=window.img3)
    Label(window, text="Jl.Soekarno-Hatta KM.15 No.64").place(x=130, y=330)

    window.img4 = PhotoImage(file="work.png")
    canvas4 = Canvas(window, width=24, height=44)
    canvas4.place(x=70, y=360)
    canvas4.create_image(2, 7, anchor=NW, image=window.img4)
    Label(window, text="Week Day     |    Week End").place(x=130, y=370)

    window.img5 = PhotoImage(file="jam.png")
    canvas5 = Canvas(window, width=24, height=44)
    canvas5.place(x=70, y=400)
    canvas5.create_image(2, 7, anchor=NW, image=window.img5)
    Label(window, text="08.00 - 19.00    |    09.00 - 18.00").place(x=130, y=410)

    window.img6 = PhotoImage(file="wa.png")
    canvas6 = Canvas(window, width=24, height=44)
    canvas6.place(x=10, y=610)
    canvas6.create_image(2, 7, anchor=NW, image=window.img6)
    Label(window, text="0895705277943").place(x=45, y=620)

    window.img7 = PhotoImage(file="ig.png")
    canvas7 = Canvas(window, width=24, height=34)
    canvas7.place(x=200, y=610)
    canvas7.create_image(2, 8, anchor=NW, image=window.img7)
    Label(window, text="@PremierLaundry.id").place(x=240, y=620)

    # Buttons
    Button(window, text='KILOAN', width="10", command=kiloan).place(x=70, y=270)
    Button(window, text='SATUAN', width="10", command=satuan).place(x=220, y=270)

def kiloan():
    clear_window()
    window.title('KILOAN')

    # Pilihan Paket Yang Ada Di Jenis Laundry Kiloan
    my_font = Font(family="Candara", size=16, weight="bold")
    Label(window, text="DAFTAR HARGA PAKET", font=my_font).place(x=70, y=20)

    # Kolom daftar Paket
    Label(window, text="---------------------------------------------------------------------").place(x=10, y=60)
    Label(window, text="KILOAN").place(x=50, y=80)
    Label(window, text="---------------------------------------------------------------------").place(x=10, y=95)
    Label(window, text="1. Reguler").place(x=40, y=110)
    Label(window, text="2. Oneday").place(x=40, y=130)
    Label(window, text="3. Express").place(x=40, y=150)
    Label(window, text="---------------------------------------------------------------------").place(x=10, y=170)

    # Kolom daftar Waktu Pengerjaan
    Label(window, text="PENGERJAAN").place(x=150, y=80)
    Label(window, text="2 Hari").place(x=170, y=110)
    Label(window, text="1 Hari").place(x=170, y=130)
    Label(window, text="5 Jam").place(x=170, y=150)

    # Kolom daftar Harga
    Label(window, text="HARGA").place(x=270, y=80)
    Label(window, text="Rp  8.000 / kg").place(x=260, y=110)
    Label(window, text="Rp 10.000 / kg").place(x=260, y=130)
    Label(window, text="Rp 15.000 / kg").place(x=260, y=150)

    # Mendifinisikan harga paket
    package_prices = {
        "Reguler": 8000,
        "Oneday": 10000,
        "Express": 15000
    }

    package = StringVar()
    berat = StringVar()
    total = StringVar()

    # Dropdown untuk memilih paket
    Label(window, text="Pilih Paket\t\t:").place(x=30, y=200)
    package_menu = Combobox(window, width=10, textvariable=package, values=list(package_prices.keys()))
    package_menu.place(x=200, y=200)

    # Input berat (Kg)
    Label(window, text="Masukkan Berat Pakaian\t:").place(x=30, y=230)
    Entry(window, width="10", textvariable=berat).place(x=200, y=230)

    # Menampilkan total harga
    Label(window, text="Total Harga\t\t:").place(x=30, y=260)
    Entry(window, width="10", textvariable=total, state=DISABLED).place(x=200, y=260)

    def input():
        selected_package = package.get()
        item2 = berat.get()
        if selected_package in package_prices and item2.isdigit():
            item3 = package_prices[selected_package] * int(item2)
            total.set(item3)
            return True
        else:
            tkinter.messagebox.showwarning('INVALID', 'Harap memilih paket dan memasukkan berat pakaian dengan benar')
            package.set("")
            berat.set("")
            total.set("")
            return False

    Button(window, text='HITUNG', width="8", command=input).place(x=290, y=210)

    # Registrasi
    def data():
        Label(window, text="Silahkan Melengkapi Data Diri Anda :").place(x=20, y=350)

        package = StringVar()
        nama = StringVar()
        alamat = StringVar()
        notelp = StringVar()

        Label(window, text="Paket\t: ").place(x=20, y=390)
        package_menu = Combobox(window, width=37, textvariable=package, values=list(package_prices.keys()))
        package_menu.place(x=100, y=390)

        Label(window, text="Nama\t: ").place(x=20, y=420)
        Entry(window, width="40", textvariable=nama).place(x=100, y=420)

        Label(window, text="Alamat\t: ").place(x=20, y=450)
        Entry(window, width="40", textvariable=alamat).place(x=100, y=450)

        Label(window, text="No.HP\t: ").place(x=20, y=480)
        Entry(window, width="40", textvariable=notelp).place(x=100, y=480)

        Label(window, text="*kami akan menghubungi anda untuk konfirmasi").place(x=20, y=510)

        def numberonly():
            if not nama.get() or not alamat.get() or not notelp.get():
                tkinter.messagebox.showwarning('INVALID', 'Harap mengisi semua data diri')
                return False

            item = notelp.get()
            if item.isdigit():
                ask = tkinter.messagebox.askquestion("PREMIER LAUNDRY", "Data yang anda masukkan sudah benar ?")
                if ask == 'yes':
                    tkinter.messagebox.showinfo('PREMIER LAUNDRY', 'Registrasi Berhasil\nBeberapa saat lagi kami akan menghubungi Anda')
                    nama.set("")
                    alamat.set("")
                    notelp.set("")
                    package.set("")
                    berat.set("")
                    total.set("")
                    return True
                if ask == 'no':
                    return True
            else:
                tkinter.messagebox.showwarning('INVALID', 'Harap memasukkan angka untuk No.HP')
                notelp.set("")
                return False

        Button(window, text='SUBMIT', command=numberonly).place(x=160, y=550)
        Button(window, text='CLOSE', width="10", command=home).place(x=260, y=610)

    Button(window, text='NEXT', width="10", command=data).place(x=150, y=310)

def satuan():
    clear_window()
    window.title('SATUAN')

    # Daftar Pilihan
    my_font = Font(family="Candara", size=16, weight="bold")

    Label(window, text="DAFTAR HARGA PAKAIAN", font=my_font).place(x=30, y=20)
    Label(window, text='---------------------------------------------------------------------').place(x=10, y=50)

    Label(window, text="1. Kaos\t\t\t\tRp.8.000").place(x=60, y=60)
    Label(window, text="2. Kemeja\t\t\tRp.12.000").place(x=60, y=80)
    Label(window, text="3. Sprei\t\t\t\tRp.15.000").place(x=60, y=100)
    Label(window, text="4. Selimut\t\t\tRp.13.000").place(x=60, y=120)
    Label(window, text="5. Sarung Bantal\t\tRp.17.000").place(x=60, y=140)
    Label(window, text="6. Handuk\t\t\tRp.10.000").place(x=60, y=160)
    Label(window, text="7. Blazer\t\t\t\tRp.13.000").place(x=60, y=180)
    Label(window, text="8. Jaket\t\t\t\tRp.13.000").place(x=60, y=200)
    Label(window, text="9. Jeans\t\t\t\tRp.12.000").place(x=60, y=220)
    Label(window, text="10. Gaun\t\t\t\tRp.25.000").place(x=60, y=240)
    Label(window, text="11. Kebaya\t\t\tRp.30.000").place(x=60, y=260)
    Label(window, text='---------------------------------------------------------------------').place(x=10, y=290)

    pilihan = StringVar()

    Label(window, text="Tentukan Pilihan Anda\t:").place(x=65, y=320)
    daftar = list(range(1, 12))
    Combobox(window, width=5, values=daftar, textvariable=pilihan).place(x=240, y=320)

    # Registrasi
    def data():
        if pilihan.get() == "":
            tkinter.messagebox.showwarning('INVALID', 'Harap memilih salah satu pilihan')
            return

        Label(window, text="Silahkan Melengkapi Data Diri Anda :").place(x=20, y=400)

        nama = StringVar()
        alamat = StringVar()
        notelp = StringVar()

        Label(window, text="Nama\t: ").place(x=20, y=440)
        Entry(window, width="40", textvariable=nama).place(x=100, y=440)

        Label(window, text="Alamat\t: ").place(x=20, y=470)
        Entry(window, width="40", textvariable=alamat).place(x=100, y=470)

        Label(window, text="No.HP\t: ").place(x=20, y=500)
        Entry(window, width="40", textvariable=notelp).place(x=100, y=500)

        Label(window, text="*kami akan menghubungi anda untuk konfirmasi").place(x=20, y=530)

        def numberonly():
            if not nama.get() or not alamat.get() or not notelp.get():
                tkinter.messagebox.showwarning('INVALID', 'Harap mengisi semua data diri')
                return False

            item = notelp.get()
            if item.isdigit():
                ask = tkinter.messagebox.askquestion("PREMIER LAUNDRY", "Data yang anda masukkan sudah benar ?")
                if ask == 'yes':
                    tkinter.messagebox.showinfo('PREMIER LAUNDRY', 'Registrasi Berhasil\nBeberapa saat lagi kami akan menghubungi Anda')
                    nama.set("")
                    alamat.set("")
                    notelp.set("")
                    pilihan.set("")
                    return True
                if ask == 'no':
                    return True
            else:
                tkinter.messagebox.showwarning('INVALID', 'Harap memasukkan angka untuk No.HP')
                notelp.set("")
                return False

        Button(window, text='SUBMIT', command=numberonly).place(x=120, y=570)
        Button(window, text='CLOSE', width="10", command=home).place(x=280, y=610)

    Button(window, text='NEXT', width="10", command=data).place(x=140, y=360)

home()
window.mainloop()
