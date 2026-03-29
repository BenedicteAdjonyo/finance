# 📊 Gestion familiale des dépenses

Application Python simple permettant de suivre, analyser et visualiser les dépenses mensuelles par utilisateur.

---

## 🚀 Fonctionnalités

* ➕ Ajouter une dépense (date, catégorie, montant)
* 📅 Résumé mensuel par catégorie
* 📊 Tableau des tendances (par mois et catégorie)
* 📈 Visualisation graphique des dépenses
* 📄 Génération automatique de rapport PDF
* 👤 Gestion multi-utilisateurs

---

## 🗂️ Structure du projet

```
gestion-depenses/
│
├── depenses.py            # Script principal
├── depenses.csv       # Base de données (créée automatiquement)
├── courbes.png        # Graphique généré (temporaire)
├── rapport_*.pdf      # Rapports générés
└── README.md
```

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/BenedicteAdjonyo/finance.git
```

### 2. Installer les dépendances

```bash
pip install pandas matplotlib reportlab
```

---

## ▶️ Utilisation

Lancer le programme :

```bash
python main.py
cd finance
```

---

## 🧭 Menu principal

```
1 - Entrer une dépense
2 - Résumé mensuel
3 - Tableau des tendances
4 - Courbes des tendances
5 - Générer un rapport PDF
0 - Quitter
```

---

## 📝 Format des données (CSV)

Le fichier `depenses.csv` contient :

```
utilisateur,date,categorie,montant
Eyram,2026-01-05,nourriture,1225.0
```

### ⚠️ Important

* Format date : `YYYY-MM-DD`
* Catégories autorisées :

  * loyer
  * deplacement
  * nourriture
  * electricite
  * internet
  * autres

---

## 📊 Analyses disponibles

### ✔️ Résumé mensuel

Affiche les dépenses par catégorie pour un mois donné.

### ✔️ Tableau des tendances

Affiche l’évolution des dépenses par mois et catégorie.

### ✔️ Courbes

Graphique des dépenses mensuelles par catégorie.

---

## 📄 Génération de rapport PDF

Le rapport contient :

* Total des dépenses
* Répartition par catégorie
* Graphique des tendances

Fichier généré :

```
rapport_<utilisateur>.pdf
```

---

## 🛠️ Technologies utilisées

* Python 3
* pandas (gestion des données)
* matplotlib (graphiques)
* reportlab (PDF)

---

## ⚠️ Problèmes connus

* Les données mal formatées dans le CSV peuvent causer :

  * "Aucune donnée" dans les analyses
* Les dates doivent être valides
* Les catégories doivent être correctes

---

## 💡 Améliorations possibles

* Interface graphique (Tkinter ou web)
* Export Excel
* Gestion des budgets
* Authentification utilisateurs
* Application mobile

---

## 👤 Auteur

Projet réalisé par **Olivier Adjonyo**

---

## 📌 Licence

Projet libre pour usage personnel et éducatif.
