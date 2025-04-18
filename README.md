**Eesmärk:**  
*Auto_Finants* on nutikas Django-põhine veebirakendus, mis võimaldab kasutajatel üles laadida oma kuludokumente (nt CSV-vormis pangaväljavõtteid), ning kasutab **OpenAI GPT-4** API-t, et:
- tuvastada kulumustreid,
- pakkuda säästusoovitusi,
- ja genereerida personaliseeritud finantsanalüüsi.

---

## 🧰 **Tehnoloogiad ja raamistikud**

| Tehnoloogia       | Kasutus                                             |
|-------------------|------------------------------------------------------|
| **Python 3**      | Põhikeel                                            |
| **Django**        | Veebiraamistik (admin, auth, forms, models)        |
| **Bootstrap 5**   | Kasutajaliidese kujundus                            |
| **OpenAI API (GPT-4)** | Finantsanalüüsi genereerimine AI toel         |
| **CSV**           | Pangaväljavõtete andmestruktuur                     |
| **Django Admin**  | Failide ja analüüside haldus                        |
| **SQLite/PostgreSQL** | Andmebaasi salvestus (kasutajad, failid, analüüsid) |

---

## 💡 **Peamised funktsioonid**

### 🔐 Kasutajahaldus
- Registreerimine (signup)
- Sisselogimine / väljalogimine
- Autentimise põhine ligipääs analüüsile

### 📤 Failide üleslaadimine
- Kasutaja saab laadida üles CSV-faili, mis sisaldab tehingute infot:
  - `Kuupäev, Kategooria, Kirjeldus, Summa`
- Failid salvestatakse andmebaasi (`UploadedDocument`)

### 🤖 AI finantsanalüüs
- OpenAI GPT-4 mudel analüüsib faili sisu:
  - 📊 **Suurimad kulukategooriad**
  - 💡 **Säästusoovitused**
  - 🔁 **Korduvad mustrid**
- Tulemus kuvatakse selgelt punktidena ja kategooriatena
- Analüüs salvestatakse (`AnalysisResult`) andmebaasi

### 📚 Minu analüüsid
- Kasutaja saab vaadata kõiki oma varasemaid analüüse
- Iga analüüs on seotud konkreetse failiga
- Bootstrap accordion-stiilis ülevaade

### 🧾 Django Admin
- Admin näeb kõiki üleslaaditud faile ja vastavaid analüüse
- Otsing, filtreerimine ja sorteerimine

---

## 📁 Kaustastruktuuri näide

```
Auto_Finants/
├── config/
│   ├── settings.py
│   ├── urls.py
├── analüüs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│   ├── forms.py
│   └── admin.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── logout.html
│   ├── upload.html
│   └── minu_analüüsid.html
├── media/uploads/
├── static/
├── .env
└── manage.py
```

---

## ✨ Tuleviku ideed (laiendusvõimalused)

| Laiendus                        | Kirjeldus |
|---------------------------------|-----------|
| 📈 Graafikud kulude visualiseerimiseks | Chart.js või Django Charts abil |
| 📤 Analüüsi PDF-eksport         | Kasutaja saab analüüsi alla laadida |
| 📬 E-maili teavitus peale analüüsi | Analüüsi tulemus saadetakse meiliga |
| 🗂 Töötlemine Excel (.xlsx) failidega | XLSX failitugi CSV kõrval |
| 🔒 Kaksikautentimine (2FA)      | Turvalisuse tõstmiseks |
| 🤝 Jagatavad lingid analüüsile  | Avalikud/privaatse lingiga vaated |
| 📱 Mobiilivaade (PWA)           | Telefonisõbralik vaade ja teavitused |
