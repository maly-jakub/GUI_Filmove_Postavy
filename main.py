from datetime import datetime
from decimal import Decimal
import tkinter as tk

postavy = []


with open("postavy.txt", "r", encoding="utf-8") as soubor, \
     open("oblibene-postavy.txt", "w", encoding="utf-8") as vystup:
        for radek in soubor:
            udaje = radek.strip().split("#")
            
            jmeno = udaje[0]
            vek = int(udaje[1])
            pohlavi = udaje[2]
            je_zvire = udaje[3] == "ano"
            datum_promitani = datetime.strptime(udaje[4], '%Y-%m-%d')
            oblibenost = Decimal(udaje[5])

            postava = {
                "jmeno": jmeno,
                "vek": vek,
                "pohlavi": pohlavi,
                "je_zvire": je_zvire,
                "datum_promitani": datum_promitani,
                "oblibenost": oblibenost,
            }
            postavy.append(postava)

            if oblibenost > Decimal("2.5") and not je_zvire:
                
                print(f"Jméno: {jmeno}")
                print(f"Věk: {vek}")
                print(f"Pohlaví: {pohlavi}")
                
                print(f"Je zvíře: {je_zvire}")
                print(f"Poslední promítání: {datum_promitani.strftime('%Y-%m-%d')}")
                print(f"Oblíbenost u diváků: {oblibenost}")
                print("---------------------------------")
                
                vystup.write(f"{jmeno}\t{vek}\t{pohlavi}\t{je_zvire}\t{datum_promitani.strftime('%Y-%m-%d')}\t{oblibenost}\n")

aktualni = 0


def zobraz_postavu():
    postava = postavy[aktualni]
    popisek_jmeno.config(text=f"Jméno: {postava['jmeno']}")
    popisek_vek.config(text=f"Věk: {postava['vek']}")
    popisek_pohlavi.config(text=f"Pohlaví: {postava['pohlavi']}")
    if postava["je_zvire"]:
        popisek_zvire.config(text="Je zvíře: ano")
    else:
        popisek_zvire.config(text="Je zvíře: ne")
    popisek_datum.config(text=f"Poslední promítání: {postava['datum_promitani'].strftime('%d. %m. %Y')}")
    popisek_oblibenost.config(text=f"Oblíbenost u diváků: {postava['oblibenost']}")


def dalsi():
    global aktualni
    if aktualni < len(postavy) - 1:
        aktualni += 1
        zobraz_postavu()


def predchozi():
    global aktualni
    if aktualni > 0:
        aktualni -= 1
        zobraz_postavu()


okno = tk.Tk()
okno.title("Filmové postavy")
okno.geometry("300x200")

nadpis = tk.Label(okno, text="Filmové postavy")
nadpis.pack()

popisek_jmeno = tk.Label(okno)
popisek_jmeno.pack()
popisek_vek = tk.Label(okno)
popisek_vek.pack()
popisek_pohlavi = tk.Label(okno)
popisek_pohlavi.pack()
popisek_zvire = tk.Label(okno)
popisek_zvire.pack()
popisek_datum = tk.Label(okno)
popisek_datum.pack()
popisek_oblibenost = tk.Label(okno)
popisek_oblibenost.pack()

tlacitko_predchozi = tk.Button(okno, text="< Předchozí", command=predchozi)
tlacitko_predchozi.pack(side="left")
tlacitko_dalsi = tk.Button(okno, text="Další >", command=dalsi)
tlacitko_dalsi.pack(side="right")

if postavy:
    zobraz_postavu()
else:
    nadpis.config(text="Žádné postavy k zobrazení")

okno.mainloop()