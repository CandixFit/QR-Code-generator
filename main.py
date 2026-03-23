import qrcode

vorname = ""
nachname = ""
firma = ""
position = ""
telefon = ""
email = ""
website = ""
strasse = ""
plz = ""
ort = ""
land = ""

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
img.save("vcard_qr.png")

print("QR-Code erfolgreich erstellt.")
print()
print(vcard)