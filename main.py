import qrcode

vorname = "Can"
nachname = "Cingöz"
firma = "TDA-HR-Software-Entwicklungs GmbH"
position = "Team Projekte"
telefon = "+49 155 65684307"
email = "can.cingoez@tda-hr.de"
website = "https://tda-hr.de"
strasse = "Schloss Hülchrath 1"
plz = "41516"
ort = "Grevenbroich"
land = "Deutschland"

vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{nachname};{vorname}
FN:{vorname} {nachname}
ORG:{firma}
TITLE:{position}
TEL;TYPE=WORK,VOICE:{telefon}
EMAIL;TYPE=INTERNET:{email}
URL:{website}
ADR;TYPE=WORK:;;{strasse};{ort};;{plz};{land}
END:VCARD"""

img = qrcode.make(vcard)
img.save("can_cingoez_vcard_qr.png")

print("QR-Code erfolgreich erstellt.")
print()
print(vcard)