# 🗺️ Roadmap d'Implémentation C.E.I. - 8 Heures

**Objectif** : Créer une application C.E.I. fonctionnelle avec interface TUI et agent Gemini.

---

## 📋 Vue d'Ensemble

```
┌─────────────┬──────────────────────────────────────┬──────────┐
│   Phase     │           Tâches                     │  Durée   │
├─────────────┼──────────────────────────────────────┼──────────┤
│ Phase 1     │ Setup Environnement                  │   1h     │
│ Phase 2     │ Core Agent Gemini                    │   2h     │
│ Phase 3     │ Interface TUI                        │   2h     │
│ Phase 4     │ Protocoles Spéciaux                  │   2h     │
│ Phase 5     │ Tests & Documentation                │   1h     │
└─────────────┴──────────────────────────────────────┴──────────┘
```

---

## 🚀 Phase 1 : Setup Environnement (1h)

### Objectif
Préparer l'environnement de développement et valider la connexion à l'API Gemini.

### Tâches

#### 1.1 Installation des Dépendances (15min)
```bash
# Créer environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer packages
pip install google-generativeai rich pyyaml python-dotenv
pip freeze > requirements.txt
```

**Checklist :**
- [ ] Environnement virtuel créé
- [ ] Packages installés
- [ ] requirements.txt généré

#### 1.2 Configuration API Gemini (15min)
```bash
# Obtenir clé API
# https://aistudio.google.com/app/apikey

# Créer .env
echo "GEMINI_API_KEY=votre_cle_ici" > .env
```

**Checklist :**
- [ ] Clé API obtenue
- [ ] Fichier .env créé
- [ ] .env ajouté au .gitignore

#### 1.3 Structure du Projet (15min)
```bash
mkdir -p cei_app/{core,ui,storage,tests,data/{journal,fiches}}
touch cei_app/{__init__.py,core/__init__.py,ui/__init__.py,storage/__init__.py}
```

**Structure finale :**
```
cei_app/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── agent.py          # Agent Gemini
│   └── protocols.py      # Protocoles spéciaux
├── ui/
│   ├── __init__.py
│   └── tui.py           # Interface TUI
├── storage/
│   ├── __init__.py
│   └── manager.py       # Gestion fichiers
├── data/
│   ├── journal/
│   ├── fiches/
│   ├── arbre.json
│   └── quetes.json
├── tests/
│   └── test_agent.py
├── config.yaml
├── main.py
├── .env
└── requirements.txt
```

**Checklist :**
- [ ] Dossiers créés
- [ ] Fichiers __init__.py créés
- [ ] Structure validée

#### 1.4 Test de Connexion (15min)
```python
# test_connection.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-2.0-flash-exp')
response = model.generate_content('Dis bonjour!')
print(response.text)
```

**Checklist :**
- [ ] Script de test créé
- [ ] Connexion réussie
- [ ] Réponse reçue

---

## 🤖 Phase 2 : Core Agent Gemini (2h)

### Objectif
Créer l'agent Gemini avec tous les prompts C.E.I.

### Tâches

#### 2.1 Classe CEIAgent de Base (30min)
**Fichier :** `cei_app/core/agent.py`

**Fonctionnalités :**
- Initialisation modèle Gemini
- Gestion historique conversation
- Méthode générique `generate()`

**Checklist :**
- [ ] Classe CEIAgent créée
- [ ] Connexion Gemini fonctionnelle
- [ ] Historique conversation implémenté
- [ ] Tests unitaires passent

#### 2.2 Prompts Phase A : Planification (30min)

**Méthodes à implémenter :**
```python
def declarer_intention(self, intention: str) -> dict
def deconstruire_concepts(self, intention: str) -> list[str]
def definir_quete(self, concepts: list[str]) -> dict
```

**Checklist :**
- [ ] Prompt déclaration d'intention
- [ ] Prompt déconstruction concepts
- [ ] Prompt définition quête
- [ ] Tests avec exemples réels

#### 2.3 Prompts Phase B : Exécution (30min)

**Méthodes à implémenter :**
```python
def guider_exploration(self, quete: dict, contexte: str) -> str
def generer_fiche(self, journal_entries: list) -> str
def defi_inverse(self, fiche: str) -> dict
def debriefing_metacognitif(self, journal: str) -> str
```

**Checklist :**
- [ ] Prompt guidage exploration
- [ ] Prompt génération fiche
- [ ] Prompt défi inverse
- [ ] Prompt débriefing
- [ ] Tests validation

#### 2.4 Gestion Contexte & Mémoire (30min)

**Fonctionnalités :**
- Injection journal dans contexte
- Résumé automatique si contexte > 100k tokens
- Sauvegarde/chargement conversation

**Checklist :**
- [ ] Injection contexte
- [ ] Résumé automatique
- [ ] Sauvegarde état
- [ ] Chargement état

---

## 🖥️ Phase 3 : Interface TUI (2h)

### Objectif
Créer une interface terminal intuitive avec Rich.

### Tâches

#### 3.1 Menu Principal (30min)
**Fichier :** `cei_app/ui/tui.py`

**Écrans :**
1. Accueil
2. Nouvelle Quête
3. Reprendre Quête
4. Consulter Arbre
5. Historique

**Checklist :**
- [ ] Menu avec Rich Panel
- [ ] Navigation clavier
- [ ] Affichage titre/version
- [ ] Sortie propre

#### 3.2 Interface Phase A (30min)

**Écrans :**
1. Saisie intention
2. Affichage questions déconstruction
3. Saisie réponses
4. Affichage quête définie
5. Confirmation

**Checklist :**
- [ ] Prompts formatés
- [ ] Affichage réponses Gemini
- [ ] Validation input
- [ ] Progression visible

#### 3.3 Interface Phase B (30min)

**Écrans :**
1. Zone exploration (input/output)
2. Journal temps réel (sidebar)
3. Commandes spéciales (/erreur, /sparring, /synthese)
4. Génération fiche
5. Défi inverse

**Checklist :**
- [ ] Layout 2 colonnes
- [ ] Journal live
- [ ] Commandes slash
- [ ] Affichage fiche
- [ ] Quiz interactif

#### 3.4 Visualisations (30min)

**Composants :**
- Arbre de compétences (Tree)
- Progression quête (Progress)
- Statistiques (Table)
- Timeline (Panel)

**Checklist :**
- [ ] Arbre affiché
- [ ] Barre progression
- [ ] Stats session
- [ ] Timeline cycles

---

## ⚡ Phase 4 : Protocoles Spéciaux (2h)

### Objectif
Implémenter les Learning Triggers adaptatifs.

### Tâches

#### 4.1 Protocole Leçon de l'Erreur (30min)
**Fichier :** `cei_app/core/protocols.py`

**Workflow :**
1. Détection erreur (regex, keywords)
2. Isolation contexte
3. Questions diagnostic
4. Résolution guidée
5. Capitalisation leçon

**Checklist :**
- [ ] Détection automatique
- [ ] Prompt diagnostic
- [ ] Guidage résolution
- [ ] Ajout au journal
- [ ] Tests avec erreurs réelles

#### 4.2 Protocole Sparring Spontané (30min)

**Workflow :**
1. Détection connexion (embeddings similaires)
2. Interruption contextuelle
3. Micro-défi
4. Validation compréhension
5. Reprise flux

**Checklist :**
- [ ] Détection connexions
- [ ] Prompt micro-défi
- [ ] Validation réponse
- [ ] Reprise fluide
- [ ] Tests scénarios

#### 4.3 Protocole Synthèse Dynamique (30min)

**Workflow :**
1. Détection complexité (nb concepts, confusion)
2. Proposition synthèse
3. Génération (texte ou Mermaid)
4. Validation utilisateur
5. Intégration

**Checklist :**
- [ ] Détection complexité
- [ ] Prompt synthèse
- [ ] Génération Mermaid
- [ ] Affichage formaté
- [ ] Tests

#### 4.4 Gestionnaire de Déclencheurs (30min)

**Fonctionnalités :**
- Écoute continue input utilisateur
- Analyse contexte en temps réel
- Déclenchement automatique protocoles
- Historique déclenchements

**Checklist :**
- [ ] Classe TriggerManager
- [ ] Analyse temps réel
- [ ] Déclenchement auto
- [ ] Logs déclenchements
- [ ] Tests intégration

---

## ✅ Phase 5 : Tests & Documentation (1h)

### Objectif
Valider le système complet et documenter l'usage.

### Tâches

#### 5.1 Tests Cycle Complet (30min)

**Scénarios de test :**
1. Cycle complet Hyprland (exemple)
2. Déclenchement erreur
3. Sparring spontané
4. Génération fiche
5. Mise à jour arbre

**Checklist :**
- [ ] Test cycle A→B complet
- [ ] Test chaque protocole
- [ ] Test sauvegarde/chargement
- [ ] Test erreurs/edge cases
- [ ] Tous les tests passent

#### 5.2 Documentation Utilisateur (20min)

**Fichiers à créer :**
- README_USAGE.md (guide utilisateur)
- EXAMPLES.md (exemples concrets)
- FAQ.md (questions fréquentes)

**Checklist :**
- [ ] Guide démarrage rapide
- [ ] Exemples commentés
- [ ] FAQ complète
- [ ] Screenshots/GIFs

#### 5.3 Optimisations (10min)

**Améliorations :**
- Cache réponses Gemini
- Logs structurés
- Gestion erreurs réseau
- Indicateurs performance

**Checklist :**
- [ ] Cache implémenté
- [ ] Logs configurés
- [ ] Retry logic
- [ ] Métriques ajoutées

---

## 🎯 Critères de Succès

À la fin des 8h, vous devez pouvoir :

✅ **Lancer l'application**
```bash
python main.py
```

✅ **Exécuter un cycle complet**
- Déclarer une intention
- Déconstruire les concepts
- Définir une quête
- Explorer et pratiquer
- Générer une fiche
- Passer le défi inverse
- Faire le débriefing
- Mettre à jour l'arbre

✅ **Déclencher les protocoles**
- Tester une erreur → Leçon de l'Erreur
- Faire une connexion → Sparring Spontané
- Atteindre complexité → Synthèse Dynamique

✅ **Consulter les artefacts**
- Journal de bord
- Fiches récapitulatives
- Arbre de compétences

---

## 📊 Métriques de Progression

| Phase | Tâches | Complété | Temps Réel |
|-------|--------|----------|------------|
| 1     | 4/4    | [ ]      | ___h___    |
| 2     | 4/4    | [ ]      | ___h___    |
| 3     | 4/4    | [ ]      | ___h___    |
| 4     | 4/4    | [ ]      | ___h___    |
| 5     | 3/3    | [ ]      | ___h___    |

**Total : 0/19 tâches complétées**

---

## 🚨 Points d'Attention

### Pièges à Éviter
1. **Over-engineering** : Restez simple, itérez plus tard
2. **Perfectionnisme** : Un système fonctionnel > un système parfait
3. **Scope creep** : Suivez la roadmap, notez les idées pour plus tard
4. **Blocages API** : Testez la connexion Gemini dès le début

### Si Vous Prenez du Retard
**Priorités (dans l'ordre) :**
1. Phase 1 + 2 (Agent fonctionnel)
2. Phase 3 (Interface basique)
3. Phase 4 (Au moins 1 protocole)
4. Phase 5 (Tests minimaux)

### Si Vous Avancez Vite
**Améliorations bonus :**
- Export fiches en PDF
- Visualisation graphique arbre
- Intégration Git auto
- Statistiques avancées

---

## 📚 Ressources

- **Documentation Gemini** : https://ai.google.dev/docs
- **Documentation Rich** : https://rich.readthedocs.io/
- **Cours détaillés** : Voir `Le_Comment/doc/`
- **Code de référence** : Voir `Le_Comment/code/`

---

## ✨ Prêt à Commencer ?

**Checklist pré-démarrage :**
- [ ] J'ai lu toute la roadmap
- [ ] J'ai consulté les cours dans `doc/`
- [ ] J'ai le code de référence sous les yeux
- [ ] J'ai ma clé API Gemini
- [ ] J'ai 8h devant moi
- [ ] Let's go! 🚀

---

**Dernière mise à jour** : 2025-01-14  
**Version** : 1.0  
**Auteur** : Sidix (avec assistance Cascade)
