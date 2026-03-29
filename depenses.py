import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ================== CONFIG ==================
FICHIER = "depenses.csv"
MONNAIE = "FCFA"

CATEGORIES = [
    "loyer",
    "deplacement",
    "nourriture",
    "electricite",
    "internet",
    "autres"
]

# ================== INIT CSV ==================
if not os.path.exists(FICHIER):
    pd.DataFrame(
        columns=["utilisateur", "date", "categorie", "montant"]
    ).to_csv(FICHIER, index=False)

# ================== DONNEES ==================
def charger_donnees():
    df = pd.read_csv(FICHIER)
    df["date"] = pd.to_datetime(
        df["date"].astype(str).str.strip(),
        format="mixed",
        errors="coerce"
    )
    return df

# ================== SAISIE ==================
def enregistrer_depense(utilisateur):
    print("\n--- Entrer une dépense ---")

    date = input("Date (YYYY-MM-DD) : ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ Date invalide.")
        return

    print("Catégories :", ", ".join(CATEGORIES))
    categorie = input("Catégorie : ").lower()
    if categorie not in CATEGORIES:
        print("❌ Catégorie invalide.")
        return

    try:
        montant = float(input(f"Montant ({MONNAIE}) : "))
        if montant <= 0:
            raise ValueError
    except ValueError:
        print("❌ Montant invalide.")
        return

    nouvelle = pd.DataFrame(
        [[utilisateur, date, categorie, montant]],
        columns=["utilisateur", "date", "categorie", "montant"]
    )

    df = charger_donnees()
    df = pd.concat([df, nouvelle], ignore_index=True)
    df.to_csv(FICHIER, index=False)

    print("✅ Dépense enregistrée.")

# ================== ANALYSES ==================
def resume_mensuel(utilisateur):
    mois = int(input("Mois (1-12) : "))
    annee = int(input("Année : "))

    df = charger_donnees()
    df = df[df["utilisateur"] == utilisateur]

    df = df[
        (df["date"].dt.month == mois) &
        (df["date"].dt.year == annee)
    ]

    if df.empty:
        print("Aucune donnée.")
        return None

    resume = df.groupby("categorie")["montant"].sum()
    print("\nRésumé mensuel :\n", resume)
    print(f"Total : {resume.sum():,.0f} {MONNAIE}")
    return resume

def tableau_tendances(utilisateur):
    df = charger_donnees()
    df = df[df["utilisateur"] == utilisateur]
    df["mois"] = df["date"].dt.to_period("M")

    tableau = (
        df.groupby(["mois", "categorie"])["montant"]
        .sum()
        .unstack(fill_value=0)
    )

    print("\nTableau des tendances :\n")
    print(tableau)
    return tableau

def courbes_tendances(utilisateur, sauvegarder=False):
    df = charger_donnees()
    df = df[df["utilisateur"] == utilisateur]
    df["mois"] = df["date"].dt.to_period("M")

    tendances = (
        df.groupby(["mois", "categorie"])["montant"]
        .sum()
        .unstack(fill_value=0)
    )

    if tendances.empty:
        return None

    plt.figure(figsize=(10, 6))
    for cat in tendances.columns:
        plt.plot(tendances.index.astype(str), tendances[cat], marker="o", label=cat)

    plt.xlabel("Mois")
    plt.ylabel(f"Dépenses ({MONNAIE})")
    plt.title(f"Tendances des dépenses – {utilisateur}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if sauvegarder:
        plt.savefig("courbes.png")
        plt.close()
    else:
        plt.show()

    return tendances

# ================== PDF ==================
def generer_pdf(utilisateur):
    print("\n📄 Génération du rapport PDF...")

    c = canvas.Canvas(f"rapport_{utilisateur}.pdf", pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, f"Rapport de dépenses – {utilisateur}")

    c.setFont("Helvetica", 11)
    y = height - 100

    df = charger_donnees()
    df = df[df["utilisateur"] == utilisateur]

    if df.empty:
        c.drawString(50, y, "Aucune donnée disponible.")
        c.save()
        return

    total = df["montant"].sum()
    c.drawString(50, y, f"Total des dépenses : {total:,.0f} {MONNAIE}")
    y -= 30

    resume = df.groupby("categorie")["montant"].Esum()
    for cat, val in resume.items():
        c.drawString(50, y, f"{cat} : {val:,.0f} {MONNAIE}")
        y -= 20

    courbes_tendances(utilisateur, sauvegarder=True)
    c.drawImage("courbes.png", 50, 100, width=500, preserveAspectRatio=True)

    c.save()
    print(f"✅ Rapport généré : rapport_{utilisateur}.pdf")

# ================== MENU ==================
def menu(utilisateur):
    while True:
        print("\n====== MENU ======")
        print("1 - Entrer une dépense")
        print("2 - Résumé mensuel")
        print("3 - Tableau des tendances")
        print("4 - Courbes des tendances")
        print("5 - Générer un rapport PDF")
        print("0 - Quitter")

        choix = input("Choix : ")

        if choix == "1":
            enregistrer_depense(utilisateur)
        elif choix == "2":
            resume_mensuel(utilisateur)
        elif choix == "3":
            tableau_tendances(utilisateur)
        elif choix == "4":
            courbes_tendances(utilisateur)
        elif choix == "5":
            generer_pdf(utilisateur)
        elif choix == "0":
            break
        else:
            print("❌ Choix invalide.")

# ================== MAIN ==================
if __name__ == "__main__":
    print("📊 Gestion familiale des dépenses")
    utilisateur = input("Entrez votre nom : ").strip().capitalize()
    menu(utilisateur)
