import csv
import openai
import os
from io import TextIOWrapper

# Loo kindlus, et API võti laetakse .env failist
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_csv(uploaded_file):
    """
    Võtab Django InMemoryUploadedFile või TemporaryUploadedFile objekti
    ning tagastab hästi vormindatud tekstiväljundi, mis sobib analüüsiks.
    """
    try:
        uploaded_file.seek(0)  # Oluline: loe alati algusest
        text_file = TextIOWrapper(uploaded_file.file, encoding='utf-8')
        reader = csv.DictReader(text_file)

        lines = []
        for row in reader:
            date = row.get("Kuupäev", "").strip()
            category = row.get("Kategooria", "").strip()
            description = row.get("Kirjeldus", "").strip()
            amount = row.get("Summa", "").strip()
            lines.append(f"{date} | {category} | {description} | {amount}")

        if not lines:
            return "FAIL TÜHI: CSV ei sisaldanud ühtegi rida."

        return "\n".join(lines)
    except Exception as e:
        return f"Viga CSV lugemisel: {e}"

def analyze_expense_text(text):
    """
    Saadab kasutaja CSV sisu OpenAI GPT-4 API-le ja palub vastust struktureerituna:
    kategooriate kaupa ja punktidena.
    """
    if not text.strip():
        return "Sisend oli tühi – ei saa analüüsida."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Oled professionaalne finantsanalüütik. Sinu ülesanne on analüüsida CSV-vormis "
                        "pangatehingute andmeid ja koostada selge kokkuvõte, jagatuna kategooriatesse. "
                        "Esita iga osa punktidena ja kasuta emotikone pealkirjades: "
                        "\n\n📊 Suurimad kulukategooriad\n💡 Säästusoovitused\n🔁 Korduvad mustrid"
                    )
                },
                {
                    "role": "user",
                    "content": f"Siin on kasutaja pangaväljavõte:\n{text}"
                }
            ],
            temperature=0.4
        )

        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Viga OpenAI API päringul: {e}"
