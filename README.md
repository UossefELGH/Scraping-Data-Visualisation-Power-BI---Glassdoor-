# Scraping Data & Visualisation Power BI - Glassdoor Project  

## 📝 Description  
Ce projet est divisé en deux parties :  
1. **Data Scraping** : Extraction de données des offres d'emploi sur Glassdoor à l'aide de Selenium et BeautifulSoup.
2. **Data Cleaning & Preparing** : Nettoyer et préparer les données dans Excel pour l'analyse.  
3. **Power BI** : Analyse et visualisation des données extraites sous forme de tableau de bord interactif.  

---

## 🚀 Fonctionnalités  
### Data Scraping  
- Extraction des informations sur les offres d'emploi (titre, entreprise, localisation, salaire, type de contrat).  
- Gestion des erreurs et pauses aléatoires pour éviter les détections de bot.  
- Résultats enregistrés au format CSV.
- 
### MICROSOFT Excel 
-  Suppression des valeurs manquantes.
-  Ajouter de colonnes pertinentes.
-  Structuration des données pour l'analyse.  

### Power BI  
- Visualisation des tendances d'emploi (types de contrat, salaires, etc.).  
- Tableau de bord interactif pour explorer les données extraites.  

---

## 📁 Structure des Dossiers  
- **`data/`** : Contient les données brutes et nettoyées.  
- **`scraping/`** : Scripts Python pour l'extraction des données.  
- **`powerbi/`** : Fichier Power BI et captures d'écran du tableau de bord.  
- **`docs/`** : Guides et documentations complémentaires.  

---

## 🛠️ Installation et Utilisation  

### Pré-requis  
- Python 3.x
- Chromedriver 
- Selenium et BeautifulSoup
- Microsoft Excel
- Power BI Desktop  


---

## 🛠️ Étapes du Projet  

### **1. Scraping des Données**  
**Outils et bibliothèques utilisés** :  
- `Python`, `Jupyter Notebook`  
- `Selenium`, `BeautifulSoup`, `Pandas`  
- `Chromedriver`  

**Étapes suivies** :  
1. **Configuration de Selenium** :  
   - Utilisation de *Chromedriver* pour automatiser la navigation.  
   - Ajout d’un *user-agent* et désactivation de la détection d'automatisation.  

2. **Extraction des URL à scraper** :  
   - Génération des URLs dynamiquement pour différents intitulés de poste et types de contrat (CDI, CDD).  

3. **Développement du script de scraping** :  
   - Collecte des données suivantes pour chaque offre :  
     - **Titre du poste**  
     - **Nom de l'entreprise**  
     - **Localisation**  
     - **Salaire estimé**  
     - **Type de contrat (CDI, CDD)**  

4. **Gestion des erreurs et pauses aléatoires** :  
   - Ajout de pauses pour simuler une navigation humaine.  
   - Enregistrement des erreurs dans un fichier log (`scraping_errors.log`).  

5. **Enregistrement des données** :  
   - Sauvegarde des données dans un fichier CSV nommé `glassdoor_jobs_dataset.csv`.  

### Commandes pour exécuter le script :  
```bash
# Installer les dépendances
pip install -r requirements.txt

# Exécuter le script
python main.py
