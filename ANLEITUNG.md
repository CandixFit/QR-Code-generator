# 🚀 Implementierungsanleitung — TDA QR-Code Generator

**Projekt:** Visitenkarten QR-Generator  
**Technologie:** Reines HTML/CSS/JavaScript (kein Backend nötig)  
**Hosting:** GitHub Pages (kostenlos)

---

## Schritt 1 — Voraussetzungen installieren

### 1.1 Git installieren
Falls noch nicht vorhanden: https://git-scm.com/download/win  
→ Installer herunterladen und durchklicken (alle Standardoptionen lassen)

Danach prüfen ob Git funktioniert — Terminal in VS Code öffnen (`Strg + ö`) und eingeben:
```bash
git --version
```
Ausgabe sollte sein: `git version 2.x.x`

### 1.2 GitHub-Konto anlegen
Falls noch nicht vorhanden: https://github.com/signup  
→ Konto erstellen (kostenlos)

---

## Schritt 2 — Projekt in VS Code einrichten

### 2.1 Projektordner erstellen
Erstelle einen neuen Ordner auf deinem PC, z.B.:
```
C:\Projekte\tda-qr-generator\
```

### 2.2 Ordner in VS Code öffnen
- VS Code starten
- `Datei → Ordner öffnen` → deinen neuen Ordner auswählen

### 2.3 Datei einfügen
- Die heruntergeladene `index.html` in den Projektordner kopieren
- Die Datei sollte jetzt im VS Code Explorer (linke Seitenleiste) erscheinen

> ⚠️ **Wichtig:** Die Datei muss zwingend `index.html` heißen,  
> damit GitHub Pages sie automatisch als Startseite erkennt.

### 2.4 Lokal testen (empfohlen)
Installiere die VS Code Extension **Live Server**:
- Linke Seitenleiste → Extensions-Icon (oder `Strg+Shift+X`)
- Suche: `Live Server` von Ritwick Dey → Installieren
- Rechtsklick auf `index.html` → **"Open with Live Server"**
- Browser öffnet sich automatisch unter `http://127.0.0.1:5500`

---

## Schritt 3 — Git-Repository einrichten

### 3.1 Git in VS Code initialisieren
Terminal in VS Code öffnen (`Strg + ö`) und folgende Befehle nacheinander ausführen:

```bash
# 1. Git-Repository initialisieren
git init

# 2. Deinen Namen und E-Mail hinterlegen (einmalig)
git config --global user.name "Dein Name"
git config --global user.email "deine@email.de"

# 3. Alle Dateien zum Staging hinzufügen
git add .

# 4. Ersten Commit erstellen
git commit -m "Erster Commit: TDA QR-Code Generator"
```

---

## Schritt 4 — Repository auf GitHub erstellen

### 4.1 Neues Repository anlegen
1. GitHub öffnen → https://github.com
2. Oben rechts auf **"+"** klicken → **"New repository"**
3. Einstellungen:
   - **Repository name:** `tda-qr-generator`
   - **Description:** `Visitenkarten QR-Generator für TDA Mitarbeiter` (optional)
   - **Visibility:** `Public` ✅ ← muss Public sein für kostenloses Hosting
   - **NICHT** ankreuzen: "Add a README file" (wir haben bereits Dateien)
4. Auf **"Create repository"** klicken

### 4.2 Lokales Repo mit GitHub verbinden
GitHub zeigt dir nach der Erstellung automatisch die Befehle an.  
Füge diese im VS Code Terminal ein (URL anpassen mit deinem Benutzernamen):

```bash
# Verbindung zu GitHub herstellen
git remote add origin https://github.com/DEIN-USERNAME/tda-qr-generator.git

# Branch umbenennen (moderner Standard)
git branch -M main

# Code zu GitHub hochladen (pushen)
git push -u origin main
```

> 💡 Beim ersten Push wirst du nach deinen GitHub-Zugangsdaten gefragt.  
> Alternativ kannst du in VS Code unter `Konten → GitHub anmelden` dich vorab einloggen.

---

## Schritt 5 — GitHub Pages aktivieren (Hosting)

### 5.1 Pages einschalten
1. Auf GitHub dein Repository öffnen
2. Oben auf **"Settings"** klicken
3. Linke Seitenleiste: **"Pages"** auswählen
4. Unter **"Branch"** → `main` auswählen → Ordner `/root` lassen
5. Auf **"Save"** klicken

### 5.2 Warten & aufrufen
- GitHub braucht ca. 1–2 Minuten zum Deployen
- Deine App ist dann erreichbar unter:
```
https://DEIN-USERNAME.github.io/tda-qr-generator/
```

> ✅ Diese URL kannst du intern an alle Mitarbeiter weitergeben — fertig!

---

## Schritt 6 — Änderungen vornehmen & aktualisieren

Wenn du später Anpassungen am Code machst (z.B. Logo hinzufügen, Farben ändern):

```bash
# 1. Geänderte Dateien zum Staging hinzufügen
git add .

# 2. Commit mit Beschreibung erstellen
git commit -m "Logo hinzugefügt"

# 3. Zu GitHub pushen
git push
```

→ GitHub Pages aktualisiert sich automatisch nach ca. 1 Minute.

---

## Kurzübersicht: Wichtigste Git-Befehle

| Befehl | Bedeutung |
|--------|-----------|
| `git init` | Neues lokales Repository erstellen |
| `git add .` | Alle Änderungen zum Staging hinzufügen |
| `git commit -m "Nachricht"` | Snapshot der Änderungen speichern |
| `git push` | Lokale Commits zu GitHub hochladen |
| `git pull` | Änderungen von GitHub herunterladen |
| `git status` | Zeigt welche Dateien geändert wurden |
| `git log` | Zeigt die Commit-Historie |

---

## Nächste Schritte (optional)

Sobald dein Chef die Web-Version für andere Unternehmen anbieten möchte:

1. **Backend hinzufügen** — z.B. mit Python (FastAPI) oder Node.js
2. **Datenbank** — QR-Codes und Mitarbeiterdaten speichern
3. **Login-System** — Jedes Unternehmen bekommt eigenen Bereich (Mandantenfähigkeit)
4. **Custom Branding** — Logo und Farben pro Unternehmen konfigurierbar
5. **Bezahltes Hosting** — z.B. Hetzner (DE), Netlify oder AWS statt GitHub Pages

---

*Erstellt für TDA-HR-Software-Entwicklungs GmbH*
