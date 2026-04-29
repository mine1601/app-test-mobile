# 🏥 SANTÉ PLUS - Application de Collecte de Données Médicales

Une application Streamlit professionnelle pour la collecte, l'analyse et la gestion des données de santé.

## 📋 Fonctionnalités

### 1. 📝 Collecte des Données
- **Informations Personnelles** : Nom, âge, sexe, date de naissance
- **Constantes Vitales** : Tension artérielle, fréquence cardiaque, température
- **Anthropométrie** : Poids, taille, calcul automatique de l'IMC
- **Antécédents Médicaux** : Historique médical et médicaments actuels
- **Symptômes** : Description des plaintes actuelles
- **Habitudes de Vie** : Tabagisme, alcool, activité physique, sommeil
- **Observations** : Notes médicales supplémentaires

### 2. 📊 Analyse Descriptive
- Statistiques générales (nombre de patients, moyennes)
- Analyse des constantes vitales
- Distribution par sexe
- Tableau complet des données
- Export en CSV

### 3. ✏️ Modification des Entrées
- Sélection et modification des dossiers patients existants
- Mise à jour des informations en temps réel

## 🚀 Installation et Déploiement sur Streamlit Cloud

### Étape 1 : Préparer votre environnement local

```bash
# Cloner ou créer un dépôt GitHub
git clone https://github.com/votre-username/health-app.git
cd health-app
```

### Étape 2 : Créer les fichiers nécessaires

Les fichiers suivants doivent être dans votre dépôt :
- `app.py` (le fichier principal Streamlit)
- `requirements.txt` (les dépendances)
- `.streamlit/config.toml` (configuration optionnelle)

### Étape 3 : Pousser vers GitHub

```bash
git add .
git commit -m "Initial commit: Health data collection app"
git push origin main
```

### Étape 4 : Déployer sur Streamlit Cloud

1. Allez sur [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Cliquez sur "New app"
3. Connectez votre compte GitHub
4. Sélectionnez votre dépôt et la branche `main`
5. Sélectionnez le fichier `app.py`
6. Cliquez sur "Deploy"

### Étape 5 : Obtenir votre lien personnalisé

Après le déploiement, votre application sera accessible à :
```
https://[votre-username]-[nom-du-projet].streamlit.app/
```

Par exemple :
```
https://namegni-eric-dyvan24G2317.streamlit.app/
```

## 📦 Dépendances

- `streamlit==1.28.1`
- `pandas==2.0.3`

## 🔒 Sécurité

- Les données sont stockées localement en JSON
- Pour une utilisation en production, considérez une base de données sécurisée
- Respectez les normes de confidentialité des données médicales

## 📝 Structure des Données

Les données sont stockées en JSON avec la structure suivante :

```json
{
  "id": "20260428120000",
  "date_enregistrement": "2026-04-28T12:00:00",
  "nom_complet": "Jean Dupont",
  "age": 45,
  "sexe": "Masculin",
  "tension_systolique": 120,
  "tension_diastolique": 80,
  "frequence_cardiaque": 72,
  "temperature": 37.0,
  "poids": 75.5,
  "taille": 180,
  "imc": 23.29,
  "antecedents": ["Hypertension"],
  "medicaments": "Aspirine 100mg",
  "symptomes": "Aucun",
  "tabagisme": "Non-fumeur",
  "alcool": "Modérée",
  "activite_physique": "Modérée",
  "sommeil": 7,
  "observations": "Patient en bonne santé",
  "date_consultation": "2026-04-28"
}
```

## 🎨 Personnalisation

Vous pouvez personnaliser l'application en modifiant :
- Les couleurs dans `.streamlit/config.toml`
- Les champs du formulaire dans `app.py`
- Le titre et la description

## 📞 Support

Pour toute question ou problème, consultez la [documentation Streamlit](https://docs.streamlit.io/)

---

**Version:** 1.0  
**Créé:** 2026
