import random
import subprocess
from PIL import UnidentifiedImageError
import customtkinter
import PyPDF2
import PIL.Image as img
import PIL.ImageTk as imgtk
from customtkinter import *
from tkinter.filedialog import askopenfilenames as fd
from tkinter import messagebox as msg
from tkinter import PhotoImage

# get pc username

pc_user = subprocess.run("cmd.exe /c echo %USERNAME%", capture_output=True)

pc_user = pc_user.stdout.decode("utf-8").replace("\r", "").replace("\n", "")

# creating gui


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("900x500+400+200")
        self.title("CONVERTER-CODE_DEM")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        # var

        self.pdf_list = []

        # frame one

        self.frame_1 = CTkFrame(master=self, width=300, fg_color="brown4")
        self.frame_1.pack(side=LEFT, fill="both", padx=20, pady=20, expand=True)

        # run frame 1 section function

        self.frame_1_section()

        # frame two

        self.frame_2 = CTkFrame(master=self, fg_color="tan3")
        self.frame_2.pack(side=LEFT, fill="both", padx=20, pady=20, expand=True)

        self.frame_2_section()

    def frame_2_section(self):

        # main label

        self.pdf_merger = CTkLabel(master=self.frame_2, text="PDF MERGER", font=CTkFont("Chaparral Pro Light",
                                                                                        35, weight="bold",
                                                                                        underline=True),
                                         text_color="black")

        self.pdf_merger.pack(anchor="n", pady=5)

        # option side

        self.pdf_option = CTkOptionMenu(master=self.frame_2, values=["PDF BİRLEŞTİRİCİ"])

        self.pdf_option.pack(padx=20, pady=30, fill="x")

        # choose file button

        self.choose_button = CTkButton(master=self.frame_2, text_color="snow", text="DOSYALARI SEÇ", fg_color="navy",
                                       hover_color="slate blue", command=self.choose_file_function)

        self.choose_button.pack(padx=20, pady=20, fill="x")

        # merge

        self.merge_button = CTkButton(master=self.frame_2, text_color="snow", text="DÖNÜŞTÜR", fg_color="magenta4",
                                       hover_color="magenta2", command=self.merge_pdf_files)

        self.merge_button.pack(padx=20, pady=35, fill="x")

        # iamge merger

        merger_image = CTkImage(dark_image=img.open("media_converter/merger.png"), size=(170, 170))

        merger_label = CTkLabel(master=self.frame_2, text="", image=merger_image)
        merger_label.pack(anchor="s", fill="x", padx=20, pady=5)

    # frame 2 choosing file

    def choose_file_function(self):

        msg.showinfo("ÖNEMLİ", "PDFLERİ SEÇERKEN HANGİ SIRA İLE BİRLEŞTİRMEK İSTİYORSANIZ O SIRA İLE SEÇİNİZ")

        # clear the list

        self.pdf_list = []

        # choose file

        pdf_file = fd(filetypes=(("PDF", "*.pdf"), ("PDF", "*.pdf")), initialdir="/", title="PDF SEÇ")

        # append the list

        for pdf in pdf_file:

            self.pdf_list.append(pdf)

    # frame 2 merge the files

    def merge_pdf_files(self):

        # create merger object

        merger = PyPDF2.PdfMerger()

        # every pdf with sıra

        for pdf in self.pdf_list:

            merger.append(pdf)

        # merge and save it and close the merger

        merger.write(f"C:/users/{pc_user}/Desktop/Birleştirilmiş_pdf.pdf")

        merger.close()

        msg.showinfo("BAŞARILI", "PDFLER BİRLEŞTİRİLDİ VE MASAÜSTÜNE KAYDEDİLDİ")

    # frame 1 section function

    def frame_1_section(self):
        # frame one section convert png to ico

        self.png_to_ico_label = CTkLabel(master=self.frame_1, text="PNG-To-ICON", font=CTkFont("Chaparral Pro Light",
                                                                                               35, weight="bold",
                                                                                               underline=True),
                                         text_color="black")

        self.png_to_ico_label.pack(anchor="n", pady=5)

        # dropdown menu

        self.dropdown_menu = CTkOptionMenu(master=self.frame_1, values=["png to-->icon", "icon to-->png"])

        self.dropdown_menu.pack(anchor="nw", padx=20, pady=30, fill="x")

        # spinboxes

        self.spinbox_x = CTkEntry(placeholder_text="X boyutunu giriniz (icon-->png için)", master=self.frame_1)
        self.spinbox_x.pack(anchor="w", fill="x", padx=20, pady=5)

        self.spinbox_y = CTkEntry(placeholder_text="Y boyutunu giriniz (icon-->png için)", master=self.frame_1)
        self.spinbox_y.pack(anchor="w", fill="x", padx=20, pady=5)

        # button one

        self.button_png_to_ico = CTkButton(master=self.frame_1, text="Dönüştür/Convert",
                                           command=self.convert_png_to_ico, fg_color="DarkSeaGreen")
        self.button_png_to_ico.pack(padx=20, pady=30, fill="x")

        # image label

        image = CTkImage(dark_image=img.open("media_converter/png_to_ico-removebg-preview.png"), size=(270, 270))

        image_label = CTkLabel(master=self.frame_1, image=image, text="")
        image_label.pack(anchor="s", fill="x", padx=20, pady=10)

    # frame 1 command

    def convert_png_to_ico(self):

        # get file path

        file_path = fd(filetypes=(("Png Dosyaları", "*.png"),("Icon Dosyaları", "*.ico")),
                       title="DOSYA SEÇ", initialdir="/")

        # get option

        option = self.dropdown_menu.get()

        # converting to png to ico into desktop

        if option == "png to-->icon":

            try:

                # with pil convert png to ico

                image = img.open(file_path[0])

                image.save(f"C:/users/{pc_user}/Desktop/yeni_{random.randint(0,999)}.ico", format="ICO")

                msg.showinfo("BAŞARILI", "DOSYA BAŞARILI BİR ŞEKİLDE MASAÜSTÜNE KAYDEDİLDİ!!")

            except UnidentifiedImageError:

                # invalid file

                msg.showerror("HATA", "LÜTFEN GEÇERLİ BİR PNG DOSYASI SEÇİN")

        else:

            # if we choose the icon to png,it would be resizeable

            try:
                image = img.open(file_path[0])

                # get sizes

                resize_shape_x = int(self.spinbox_x.get())

                resize_shape_y = int(self.spinbox_y.get())

                # reshape and save it desktop

                image = image.resize((resize_shape_x, resize_shape_y))

                image.save(f"C:/users/{pc_user}/Desktop/yeni_.png", format="PNG")

                msg.showinfo("BAŞARILI", "DOSYA BAŞARILI BİR ŞEKİLDE MASAÜSTÜNE KAYDEDİLDİ!!")

            except (ValueError, TypeError):

                msg.showerror("HATA", "BOYUT KISMI BOŞ BIRAKLILAMAZ")


c= MainWindow()
c.mainloop()




