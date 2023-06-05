import math
from tkinter import *
from tkinter import filedialog, Tk, simpledialog, messagebox
from PIL import Image, ImageTk, ImageEnhance
import random
import matplotlib.pyplot as plt
import numpy as np

obrazek = None


def otworz_zdjecie():
    global obrazek
    sciezka = filedialog.askopenfilename(filetypes=[("Pliki obrazów", "*.jpg;*.jpeg;*.png")])
    if sciezka:
        img = Image.open(sciezka).convert("RGB")
        result_img = Image.new('RGB', img.size)
        result_img.putdata(list(img.getdata()))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def zapisz_zdjecie():
    global obrazek
    if obrazek:
        sciezka = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Pliki PNG", "*.png")])
        if sciezka:
            img = ImageTk.getimage(obrazek).convert("RGB")
            img.save(sciezka)


def zamknij_projekt():
    global obrazek
    obrazek = None
    wypisz_obrazek()


def wypisz_obrazek():
    global obrazek

    # if obrazek:
    #     img = ImageTk.getimage(obrazek)
    #     width, height = img.width, img.height
    #
    #     # Sprawdzenie, czy wymiary obrazka przekraczają limity
    #     if height > 800:
    #         proporcja = 800 / height
    #         width = int(width * proporcja)
    #         height = 800
    #
    #     # Skalowanie obrazka z zachowaniem proporcji
    #     img = img.resize((width, height), Image.LANCZOS)
    #
    #     # Aktualizacja obrazka w etykiecie
    #     obrazek = ImageTk.PhotoImage(img)
    etykieta.configure(image=obrazek)



def negujImg():
    global obrazek
    if obrazek:
        img = ImageTk.getimage(obrazek).convert("RGB")
        result_img = Image.new('RGB', img.size)
        w, h = img.size

        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                r = 255 - r
                g = 255 - g
                b = 255 - b
                result_img.putpixel((i, j), (r, g, b))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def jasnoscImg():
    global obrazek
    if obrazek:
        okno_wprowadzania = Tk()
        okno_wprowadzania.withdraw()

        jasnosc = simpledialog.askfloat("Wprowadź wartość jasności", "Wprowadź wartość jasności:")
        if jasnosc is None:
            return

        img = ImageTk.getimage(obrazek).convert("RGB")
        result_img = Image.new('RGB', img.size)
        w, h = img.size

        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                r /= 255
                g /= 255
                b /= 255

                r *= jasnosc
                if r > 1:
                    r = 1
                if r < 0:
                    r = 0

                g *= jasnosc
                if g > 1:
                    g = 1
                if g < 0:
                    g = 0

                b *= jasnosc
                if b > 1:
                    b = 1
                if b < 0:
                    b = 0

                r *= 255
                g *= 255
                b *= 255
                result_img.putpixel((i, j), (int(r), int(g), int(b)))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()
        okno_wprowadzania.destroy()


def potengaImg():
    global obrazek
    if obrazek:
        okno_wprowadzania = Tk()
        okno_wprowadzania.withdraw()

        x = simpledialog.askfloat("Wprowadź wartość potęgi", "Wprowadź wartość potęgi:")
        if x is None:
            return

        img = ImageTk.getimage(obrazek).convert("RGB")
        result_img = Image.new('RGB', img.size)
        w, h = img.size

        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                r /= 255
                g /= 255
                b /= 255

                r = pow(r, x)
                g = pow(g, x)
                b = pow(b, x)

                r *= 255
                g *= 255
                b *= 255

                result_img.putpixel((i, j), (int(r), int(g), int(b)))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()
        okno_wprowadzania.destroy()


def pierwiastekImg():
    global obrazek
    if obrazek:
        img = ImageTk.getimage(obrazek).convert("RGB")
        result_img = Image.new('RGB', img.size)
        w, h = img.size

        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                r /= 255
                g /= 255
                b /= 255

                r = math.sqrt(r)
                g = math.sqrt(g)
                b = math.sqrt(b)

                r *= 255
                g *= 255
                b *= 255

                result_img.putpixel((i, j), (int(r), int(g), int(b)))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def mieszajM1Img():
    global obrazek
    if obrazek:
        okno_wprowadzania = Tk()
        okno_wprowadzania.withdraw()

        obrazek2 = filedialog.askopenfilename(title="Wybierz drugi obrazek")
        if not obrazek2:
            okno_wprowadzania.destroy()
            return

        img1 = ImageTk.getimage(obrazek).convert("RGB")
        img2 = Image.open(obrazek2).convert("RGB")

        # Upewnij się, że oba obrazy mają takie same wymiary
        if img1.size != img2.size:
            messagebox.showerror("Błąd", "Obrazy muszą mieć takie same wymiary")
            okno_wprowadzania.destroy()
            return

        w, h = img1.size
        result_img = Image.new('RGB', (w, h))

        for i in range(w):
            for j in range(h):
                # Odczytaj piksele z obu obrazów i znormalizuj wartości do zakresu 0-1
                r1, g1, b1 = img1.getpixel((i, j))
                r1, g1, b1 = r1 / 255, g1 / 255, b1 / 255

                r2, g2, b2 = img2.getpixel((i, j))
                r2, g2, b2 = r2 / 255, g2 / 255, b2 / 255

                # Policz średnią wartość pikseli
                r = (r1 + r2) / 2
                g = (g1 + g2) / 2
                b = (b1 + b2) / 2

                # Ustaw piksel w obrazie wynikowym i znormalizuj wartości do zakresu 0-255
                result_img.putpixel((i, j), (int(r * 255), int(g * 255), int(b * 255)))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()
        okno_wprowadzania.destroy()


def mieszajImgLosowo():
    global obrazek
    if obrazek:
        img1 = ImageTk.getimage(obrazek).convert("RGB")

        okno_wprowadzania = Tk()
        okno_wprowadzania.withdraw()

        obrazek2 = filedialog.askopenfilename(title="Wybierz drugi obrazek")
        if not obrazek2:
            okno_wprowadzania.destroy()
            return

        img2 = Image.open(obrazek2).convert("RGB")

        # Upewnij się, że oba obrazy mają takie same wymiary
        if img1.size != img2.size:
            messagebox.showerror("Błąd", "Obrazy muszą mieć takie same wymiary")
            okno_wprowadzania.destroy()
            return

        w, h = img1.size
        result_img = Image.new('RGB', (w, h))

        # Tworzenie listy pikseli
        pixels = []
        for i in range(w):
            for j in range(h):
                pixels.append((i, j))

        # Mieszanie pikseli
        random.shuffle(pixels)

        for idx, (i, j) in enumerate(pixels):
            # Odczytaj piksele z obu obrazów
            r1, g1, b1 = img1.getpixel((i, j))
            r2, g2, b2 = img2.getpixel((i, j))

            # Interpolacja liniowa pikseli na podstawie indeksu mieszania
            alpha = idx / (w * h)
            r = (1 - alpha) * r1 + alpha * r2
            g = (1 - alpha) * g1 + alpha * g2
            b = (1 - alpha) * b1 + alpha * b2

            # Ustaw piksel w obrazie wynikowym
            result_img.putpixel((i, j), (int(r), int(g), int(b)))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()
        okno_wprowadzania.destroy()


def zmienKontrastImg():
    global obrazek
    if obrazek:
        okno_wprowadzania = Tk()
        okno_wprowadzania.withdraw()

        wspolczynnik = simpledialog.askfloat("Wprowadź wartość kontrastu", "Wprowadź wartość kontrastu:")
        if wspolczynnik is None:
            return

        img = ImageTk.getimage(obrazek).convert("RGB")
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(wspolczynnik)

        result_img = Image.new('RGB', img.size)
        result_img.putdata(list(img.getdata()))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()
        okno_wprowadzania.destroy()


def histogramRGB():
    global obrazek
    if obrazek:
        img = ImageTk.getimage(obrazek)
        mode = img.mode

        if mode in ['RGB', 'RGBA']:
            r, g, b = img.split()[:3]
        elif mode == 'L':
            r = g = b = img
        elif mode == 'P':
            img = img.convert('RGB')
            r, g, b = img.split()[:3]
        else:
            raise ValueError("Nieobsługiwany tryb obrazka")

        plt.figure(figsize=(15, 10))

        plt.subplot(411)
        plt.hist(np.divide(r.histogram(), 255), bins=256, color='red', alpha=0.5, histtype='stepfilled')
        plt.xlabel('Intensywność')
        plt.ylabel('Liczba pikseli')
        plt.title('Histogram kanału R')

        plt.subplot(412)
        plt.hist(np.divide(g.histogram(), 255), bins=256, color='green', alpha=0.5, histtype='stepfilled')
        plt.xlabel('Intensywność')
        plt.ylabel('Liczba pikseli')
        plt.title('Histogram kanału G')

        plt.subplot(413)
        plt.hist(np.divide(b.histogram(), 255), bins=256, color='blue', alpha=0.5, histtype='stepfilled')
        plt.xlabel('Intensywność')
        plt.ylabel('Liczba pikseli')
        plt.title('Histogram kanału B')

        plt.subplot(414)
        plt.hist([r.histogram(), g.histogram(), b.histogram()], bins=256, color=['red', 'green', 'blue'], alpha=0.5,
                 histtype='stepfilled', label=['R', 'G', 'B'])
        plt.legend()
        plt.xlabel('Intensywność')
        plt.ylabel('Liczba pikseli')
        plt.title('Połączony histogram')

        plt.subplots_adjust(hspace=0.4)
        plt.show()


def histogramR():
    global obrazek
    if obrazek:
        img = ImageTk.getimage(obrazek)
        mode = img.mode

        if mode in ['RGB', 'RGBA']:
            r, _, _ = img.split()[:3]
        elif mode == 'L':
            r = g = b = img
        elif mode == 'P':
            img = img.convert('RGB')
            r, _, _ = img.split()[:3]
        else:
            raise ValueError("Nieobsługiwany tryb obrazka")

        plt.hist(np.divide(r.histogram(), 255), bins=256, color='red', alpha=0.5, histtype='stepfilled')
        plt.xlabel('Intensywność')
        plt.ylabel('Liczba pikseli')
        plt.title('Histogram kanału R')
        plt.show()


def histogramG():
    global obrazek
    if obrazek:
        img = ImageTk.getimage(obrazek)
        mode = img.mode

        if mode in ['RGB', 'RGBA']:
            _, g, _ = img.split()[:3]
        elif mode == 'L':
            r = g = b = img
        elif mode == 'P':
            img = img.convert('RGB')
            _, g, _ = img.split()[:3]
        else:
            raise ValueError("Nieobsługiwany tryb obrazka")

        plt.hist(np.divide(g.histogram(), 255), bins=256, color='green', alpha=0.5, histtype='stepfilled')
        plt.xlabel('Intensywność')
        plt.ylabel('Liczba pikseli')
        plt.title('Histogram kanału G')
        plt.show()


def histogramB():
    global obrazek
    if obrazek:
        img = ImageTk.getimage(obrazek)
        mode = img.mode

        if mode in ['RGB', 'RGBA']:
            _, _, b = img.split()[:3]
        elif mode == 'L':
            r = g = b = img
        elif mode == 'P':
            img = img.convert('RGB')
            _, _, b = img.split()[:3]
        else:
            raise ValueError("Nieobsługiwany tryb obrazka")

        plt.hist(np.divide(b.histogram(), 255), bins=256, color='blue', alpha=0.5, histtype='stepfilled')
        plt.xlabel('Intensywność')
        plt.ylabel('Liczba pikseli')
        plt.title('Histogram kanału B')
        plt.show()


def filtrMinImg():
    global obrazek

    if obrazek:
        maska = simpledialog.askinteger("Wprowadź rozmiar maski", "Wprowadź rozmiar maski:")
        if maska is None:
            return

        img = ImageTk.getimage(obrazek).convert('RGB')
        result_img = Image.new('RGB', img.size)
        w, h = img.size
        r = int(maska / 2)

        for i in range(r, w - r):
            for j in range(r, h - r):
                pixel_vals = []
                for x in range(i - r, i + r + 1):
                    for y in range(j - r, j + r + 1):
                        pixel_vals.append(img.getpixel((x, y)))
                val = [min([p[k] for p in pixel_vals]) for k in range(3)]
                result_img.putpixel((i, j), tuple(val))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrMaxImg():
    global obrazek

    if obrazek:
        maska = simpledialog.askinteger("Wprowadź rozmiar maski", "Wprowadź rozmiar maski:")
        if maska is None:
            return

        img = ImageTk.getimage(obrazek).convert('RGB')
        result_img = Image.new('RGB', img.size)
        w, h = img.size
        r = int(maska / 2)

        for i in range(r, w - r):
            for j in range(r, h - r):
                pixel_vals = []
                for x in range(i - r, i + r + 1):
                    for y in range(j - r, j + r + 1):
                        pixel_vals.append(img.getpixel((x, y)))
                val = [max([p[k] for p in pixel_vals]) for k in range(3)]
                result_img.putpixel((i, j), tuple(val))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrMedImg():
    global obrazek

    if obrazek:
        maska = simpledialog.askinteger("Wprowadź rozmiar maski", "Wprowadź rozmiar maski:")
        if maska is None:
            return

        img = ImageTk.getimage(obrazek)
        result_img = Image.new('RGB', img.size)
        w, h = img.size
        r = int(maska / 2)

        for k in range(3):
            for i in range(r, w - r):
                for j in range(r, h - r):
                    pixel_vals = []
                    for x in range(i - r, i + r + 1):
                        for y in range(j - r, j + r + 1):
                            pixel_vals.append(img.getpixel((x, y))[k])
                    val = sorted(pixel_vals)[int(len(pixel_vals) / 2)]
                    result_img.putpixel((i, j), tuple(
                        list(result_img.getpixel((i, j)))[:k] + [val] + list(result_img.getpixel((i, j)))[k + 1:]))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrGornoprzepustowySobelaPionowy():
    global obrazek

    if obrazek:
        img = ImageTk.getimage(obrazek).convert('RGB')
        w, h = img.size

        mask_pionowa = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

        result_img = Image.new('RGB', (w - 2, h - 2))

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                temp_r_pion, temp_g_pion, temp_b_pion = 0, 0, 0

                for k in range(-1, 2):
                    for l in range(-1, 2):
                        r, g, b = img.getpixel((i + k, j + l))
                        temp_r_pion += r * mask_pionowa[k + 1][l + 1]
                        temp_g_pion += g * mask_pionowa[k + 1][l + 1]
                        temp_b_pion += b * mask_pionowa[k + 1][l + 1]

                result_r = int(math.sqrt(temp_r_pion ** 2))
                result_g = int(math.sqrt(temp_g_pion ** 2))
                result_b = int(math.sqrt(temp_b_pion ** 2))
                result_img.putpixel((i - 1, j - 1), (result_r, result_g, result_b))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrGornoprzepustowySobelaPoziomy():
    global obrazek

    if obrazek:
        img = ImageTk.getimage(obrazek).convert('RGB')
        w, h = img.size

        mask_pozioma = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

        result_img = Image.new('RGB', (w - 2, h - 2))

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                temp_r_poziom, temp_g_poziom, temp_b_poziom = 0, 0, 0

                for k in range(-1, 2):
                    for l in range(-1, 2):
                        r, g, b = img.getpixel((i + k, j + l))
                        temp_r_poziom += r * mask_pozioma[k + 1][l + 1]
                        temp_g_poziom += g * mask_pozioma[k + 1][l + 1]
                        temp_b_poziom += b * mask_pozioma[k + 1][l + 1]

                result_r = int(math.sqrt(temp_r_poziom ** 2))
                result_g = int(math.sqrt(temp_g_poziom ** 2))
                result_b = int(math.sqrt(temp_b_poziom ** 2))
                result_img.putpixel((i - 1, j - 1), (result_r, result_g, result_b))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrGornoprzepustowyRobertsaPionowy():
    global obrazek

    if obrazek:
        img = ImageTk.getimage(obrazek).convert('L')
        result_img = Image.new('L', (img.width, img.height))

        w, h = img.size

        mask = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]

        for i in range(w - 2):
            for j in range(h - 2):
                pixel_vals = [
                    img.getpixel((i, j)),
                    img.getpixel((i + 1, j + 1)),
                    img.getpixel((i + 2, j + 2)),
                    img.getpixel((i + 2, j + 1)),
                    img.getpixel((i + 2, j)),
                ]

                result_pixel = abs(sum([pixel_vals[k] * mask[k // 2][k % 2] for k in range(5)]))
                result_pixel = 255 - int(result_pixel * 255 / max(1, max(pixel_vals)))  # Odwrócenie wartości kolorów
                result_img.putpixel((i, j), result_pixel)

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrGornoprzepustowyRobertsaPoziomy():
    global obrazek

    if obrazek:
        img = ImageTk.getimage(obrazek).convert('L')
        result_img = Image.new('L', (img.width, img.height))

        w, h = img.size

        mask = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]

        for i in range(w - 2):
            for j in range(h - 2):
                pixel_vals = [
                    img.getpixel((i, j)),
                    img.getpixel((i + 1, j + 1)),
                    img.getpixel((i + 1, j + 2)),
                    img.getpixel((i, j + 2)),
                    img.getpixel((i + 2, j)),
                ]

                result_pixel = abs(sum([pixel_vals[k] * mask[k // 2][k % 2] for k in range(5)]))
                result_pixel = 255 - int(result_pixel * 255 / max(1, max(pixel_vals)))  # Odwrócenie wartości kolorów
                result_img.putpixel((i, j), result_pixel)

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrGornoprzepustowyPrewittaPionowy():
    global obrazek

    if obrazek:
        img = ImageTk.getimage(obrazek).convert('L')
        result_img = Image.new('L', (img.width, img.height))

        w, h = img.size

        mask = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                pixel_values = [
                    img.getpixel((i - 1, j - 1)), img.getpixel((i, j - 1)), img.getpixel((i + 1, j - 1)),
                    img.getpixel((i - 1, j)), img.getpixel((i, j)), img.getpixel((i + 1, j)),
                    img.getpixel((i - 1, j + 1)), img.getpixel((i, j + 1)), img.getpixel((i + 1, j + 1))
                ]

                gradient = sum([pixel_values[k] * mask[k // 3][k % 3] for k in range(9)])
                result_pixel = int(abs(gradient))
                result_img.putpixel((i, j), result_pixel)

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrGornoprzepustowyPrewittaPoziomy():
    global obrazek

    if obrazek:
        img = ImageTk.getimage(obrazek).convert('L')
        result_img = Image.new('L', (img.width, img.height))

        w, h = img.size

        mask = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                pixel_values = [
                    img.getpixel((i - 1, j - 1)), img.getpixel((i, j - 1)), img.getpixel((i + 1, j - 1)),
                    img.getpixel((i - 1, j)), img.getpixel((i, j)), img.getpixel((i + 1, j)),
                    img.getpixel((i - 1, j + 1)), img.getpixel((i, j + 1)), img.getpixel((i + 1, j + 1))
                ]

                gradient = sum([pixel_values[k] * mask[k // 3][k % 3] for k in range(9)])
                result_pixel = int(abs(gradient))
                result_img.putpixel((i, j), result_pixel)

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


def filtrGornoprzepustowyLaplace():
    global obrazek

    if obrazek:
        img = ImageTk.getimage(obrazek).convert('RGB')
        result_img = Image.new('RGB', img.size)

        w, h = img.size

        mask = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                r, g, b = 0, 0, 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        pixel = img.getpixel((i + x, j + y))
                        r += pixel[0] * mask[x + 1][y + 1]
                        g += pixel[1] * mask[x + 1][y + 1]
                        b += pixel[2] * mask[x + 1][y + 1]
                r, g, b = abs(r), abs(g), abs(b)
                result_img.putpixel((i, j), (r, g, b))

        obrazek = ImageTk.PhotoImage(result_img)
        wypisz_obrazek()


okno_glowne = Tk()
okno_glowne.title("Menu górne")
okno_glowne.minsize(800, 600)
# okno_glowne.state('zoomed')

menu = Menu(okno_glowne)
okno_glowne.config(menu=menu)

menu_pliki = Menu(menu, tearoff=0)
menu.add_cascade(label="Pliki", menu=menu_pliki)
menu_pliki.add_command(label="Otwórz", command=otworz_zdjecie)
menu_pliki.add_command(label="Zapisz", command=zapisz_zdjecie)
menu_pliki.add_separator()
menu_pliki.add_command(label="Zamknij projekt", command=zamknij_projekt)

menu_edycja = Menu(menu, tearoff=0)
menu.add_cascade(label="Barwy", menu=menu_edycja)
menu_edycja.add_command(label="Neguj", command=negujImg)
menu_edycja.add_command(label="Zmień Jasność", command=jasnoscImg)
menu_edycja.add_command(label="Potęga", command=potengaImg)
menu_edycja.add_command(label="Pierwiastek", command=pierwiastekImg)
menu_edycja.add_command(label="Kontrast", command=zmienKontrastImg)

menu_edycja = Menu(menu, tearoff=0)
menu.add_cascade(label="Mieszanie", menu=menu_edycja)
menu_edycja.add_command(label="Metoda 1", command=mieszajM1Img)
menu_edycja.add_command(label="Mieszanie Losowe", command=mieszajImgLosowo)

menu_edycja = Menu(menu, tearoff=0)
menu.add_cascade(label="Histogram", menu=menu_edycja)
menu_edycja.add_command(label="Histogram RGB", command=histogramRGB)
menu_edycja.add_command(label="Histogram R", command=histogramR)
menu_edycja.add_command(label="Histogram G", command=histogramG)
menu_edycja.add_command(label="Histogram B", command=histogramB)

menu_edycja = Menu(menu, tearoff=0)
menu.add_cascade(label="Filtry Statyczne", menu=menu_edycja)
menu_edycja.add_command(label="Minimim", command=filtrMinImg)
menu_edycja.add_command(label="Maksimum", command=filtrMaxImg)
menu_edycja.add_command(label="Mediana", command=filtrMedImg)

menu_edycja = Menu(menu, tearoff=0)
menu.add_cascade(label="Filtry Górnoprzepustowe", menu=menu_edycja)
menu_edycja.add_command(label="Sobela [Pionowy]", command=filtrGornoprzepustowySobelaPionowy)
menu_edycja.add_command(label="Sobela [Poziomy]", command=filtrGornoprzepustowySobelaPoziomy)
menu_edycja.add_separator()
menu_edycja.add_command(label="Robertsa [Pionowy]", command=filtrGornoprzepustowyRobertsaPionowy)
menu_edycja.add_command(label="Robertsa [Poziomy]", command=filtrGornoprzepustowyRobertsaPoziomy)
menu_edycja.add_separator()
menu_edycja.add_command(label="Prewitta [Pionowy]", command=filtrGornoprzepustowyPrewittaPionowy)
menu_edycja.add_command(label="Prewitta [Poziomy]", command=filtrGornoprzepustowyPrewittaPoziomy)
menu_edycja.add_separator()
menu_edycja.add_command(label="Laplaca", command=filtrGornoprzepustowyLaplace)

etykieta = Label(okno_glowne)
etykieta.pack()

okno_glowne.mainloop()
