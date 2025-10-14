# 🏗️ Architecture du Système C.E.I.

**Documentation complète de l'architecture logicielle du Cadre d'Entraînement Intensif**

---

## 📊 Vue d'Ensemble

Le système C.E.I. est organisé en **5 couches principales** qui communiquent entre elles :

```
┌─────────────────────────────────────────────────────────┐
│  1. Interface Utilisateur (TUI)                         │
│     ↓ Interactions utilisateur                          │
├─────────────────────────────────────────────────────────┤
│  2. Cœur du Système (Agent CEI)                         │
│     ↓ Orchestration & Logique métier                    │
├─────────────────────────────────────────────────────────┤
│  3. Protocoles Adaptatifs (Learning Triggers)           │
│     ↓ Détection & Déclenchement automatique             │
├─────────────────────────────────────────────────────────┤
│  4. Stockage Local (Fichiers)                           │
│     ↓ Persistance des données                           │
├─────────────────────────────────────────────────────────┤
│  5. Services Externes (API Gemini)                      │
│     ↓ Génération de contenu IA                          │
└─────────────────────────────────────────────────────────┘
```

**Voir le diagramme complet :** `sys_architectureCEI.mmd`

---

## 🖥️ Couche 1 : Interface Utilisateur (TUI)

### Responsabilités
- Afficher les menus et interfaces
- Capturer les inputs utilisateur
- Formatter et présenter les données
- Gérer la navigation entre phases

### Composants

#### **Menu Principal**
```python
# cei_app/ui/tui.py
class CEITUI:
    def menu_principal(self) -> str:
        # Affiche menu avec Rich
        # Retourne choix: 'nouvelle', 'reprendre', 'arbre', 'historique', 'quitter'
```

**Options :**
- Nouvelle Quête → Lance Phase A
- Reprendre Quête → Charge session existante
- Consulter Arbre → Affiche arbre de compétences
- Historique → Liste quêtes passées
- Quitter → Sauvegarde et quitte

#### **Interface Phase A (Planification)**
```python
def phase_a_planification(self, agent) -> Dict:
    # 1. Capture intention utilisateur
    # 2. Affiche questions de clarification
    # 3. Présente concepts identifiés
    # 4. Affiche quête définie
    # 5. Demande confirmation
```

**Affichage :**
- Panels Rich pour sections
- Prompts interactifs
- Trees pour concepts hiérarchiques
- Tables pour critères de succès

#### **Interface Phase B (Exécution)**
```python
def phase_b_execution(self, agent, quete) -> None:
    # 1. Journal en temps réel
    # 2. Guidage socratique
    # 3. Génération fiche
    # 4. Quiz interactif
    # 5. Débriefing
```

**Affichage :**
- Live updates pour journal
- Markdown rendering pour fiches
- Progress bars pour étapes
- Panels colorés pour feedback

#### **Affichage Rich**
```python
class Display:
    def afficher_panel(self, titre, contenu, style)
    def afficher_table(self, data)
    def afficher_tree(self, arbre)
    def afficher_markdown(self, md_text)
    def afficher_progress(self, steps)
```

### Technologies
- **Rich** : Composants TUI (Panel, Table, Tree, Progress)
- **Prompt** : Inputs utilisateur interactifs
- **Console** : Affichage formaté et coloré

### Flux de Données
```
Utilisateur → Menu → Agent → Display → Utilisateur
```

---

## 🧠 Couche 2 : Cœur du Système (Agent CEI)

### Responsabilités
- Orchestrer les phases A et B
- Gérer le contexte et l'historique
- Communiquer avec Gemini
- Générer les artefacts (fiches, quiz)
- Coordonner les protocoles

### Composants

#### **Agent Gemini**
```python
# cei_app/core/agent.py
class CEIAgent:
    def __init__(self, api_key, model_name):
        self.model = genai.GenerativeModel(model_name)
        self.conversation_history = []
        self.context = {
            "journal_entries": [],
            "current_quest": None,
            "competences": []
        }
```

**Attributs :**
- `model` : Instance du modèle Gemini
- `conversation_history` : Historique complet
- `context` : Contexte actuel (journal, quête, compétences)

**Méthodes principales :**
- `generate(prompt, system_context)` : Génération avec contexte
- `_build_context_prompt()` : Construction contexte
- `_add_to_history(role, content)` : Ajout historique

#### **Phase A : Planification**

##### **A.1 Déclaration d'Intention**
```python
def declarer_intention(self, intention: str) -> Dict:
    # Prompt socratique pour analyser l'intention
    # Retourne: reformulation, concepts, questions
```

**Entrée :** Intention brute de l'utilisateur  
**Sortie :** JSON avec reformulation + questions  
**Prompt :** Socratique, questions ouvertes

##### **A.2 Déconstruction des Concepts**
```python
def deconstruire_concepts(self, intention: str, reponses: List[str]) -> List[Dict]:
    # Décompose en concepts atomiques
    # Retourne: liste de concepts avec prérequis
```

**Entrée :** Intention + réponses clarification  
**Sortie :** Liste concepts techniques  
**Prompt :** Analyse technique, dépendances

##### **A.3 Définition de la Quête**
```python
def definir_quete(self, intention: str, concepts: List[Dict]) -> Dict:
    # Transforme en quête SMART
    # Retourne: titre, objectif, critères, durée, livrables
```

**Entrée :** Intention + concepts  
**Sortie :** Quête SMART structurée  
**Prompt :** Pédagogique, objectifs mesurables

#### **Phase B : Exécution**

##### **B.1 Exploration & Pratique**
```python
def guider_exploration(self, action_utilisateur: str) -> str:
    # Pose questions socratiques
    # Retourne: question de guidage
```

**Mode :** Continu pendant exploration  
**Déclencheur :** Chaque action utilisateur  
**Prompt :** Socratique, approfondissement

##### **B.2 Capitalisation (Fiche)**
```python
def generer_fiche(self, journal_entries: List[str]) -> str:
    # Génère fiche Markdown structurée
    # Retourne: fiche complète
```

**Entrée :** Journal de session  
**Sortie :** Fiche Markdown  
**Structure :** Objectif, Concepts, Commandes, Pièges, Connexions

##### **B.3 Défi Inverse (Quiz)**
```python
def defi_inverse(self, fiche: str) -> Dict:
    # Génère quiz de validation
    # Retourne: questions + critères
```

**Entrée :** Fiche générée  
**Sortie :** 3 questions (conceptuelle, pratique, transfert)  
**Format :** JSON avec réponses attendues

##### **B.4 Débriefing Métacognitif**
```python
def debriefing_metacognitif(self, journal_entries: List[str]) -> str:
    # Analyse processus de réflexion
    # Retourne: analyse métacognitive
```

**Entrée :** Journal complet  
**Sortie :** Analyse Markdown  
**Focus :** Certitudes, doutes, stratégies, patterns

##### **B.5 Mise à Jour Arbre**
```python
def mettre_a_jour_arbre(self, quete: Dict, validation: bool) -> Dict:
    # Met à jour statut compétences
    # Retourne: arbre mis à jour
```

**Entrée :** Quête + résultat validation  
**Sortie :** Arbre JSON mis à jour  
**Statuts :** "exploré" ou "maîtrisé"

### Technologies
- **google-generativeai** : SDK Gemini
- **JSON** : Parsing réponses structurées
- **Prompts engineering** : Templates optimisés

### Flux de Données
```
UI → Agent → Gemini → Agent → Storage → UI
```

---

## ⚡ Couche 3 : Protocoles Adaptatifs (Learning Triggers)

### Responsabilités
- Détecter contextes spécifiques
- Déclencher protocoles automatiquement
- Enrichir l'apprentissage en temps réel

### Composants

#### **Détecteur de Contexte**
```python
# cei_app/core/protocols.py
class ContextDetector:
    def __init__(self, config):
        self.error_keywords = ["error", "erreur", "failed", "échec"]
        self.similarity_threshold = 0.7
        self.complexity_threshold = 5
    
    def detect_error(self, text: str) -> bool:
        # Détecte mots-clés d'erreur
    
    def detect_similarity(self, current, history) -> bool:
        # Détecte concepts similaires
    
    def detect_complexity(self, concepts: List) -> bool:
        # Détecte complexité excessive
```

**Méthodes de détection :**
- Keywords matching (erreurs)
- Similarité sémantique (concepts)
- Comptage de complexité (nombre concepts)

#### **P.1 Leçon de l'Erreur**
```python
class LeconErreur:
    def declencher(self, erreur: str, contexte: str) -> str:
        # 1. Identifier cause racine
        # 2. Expliquer pourquoi
        # 3. Proposer solution
        # 4. Généraliser leçon
```

**Déclenchement :** Détection mot-clé erreur  
**Prompt :** Analyse cause racine, généralisation  
**Sortie :** Leçon structurée Markdown

#### **P.2 Sparring Spontané**
```python
class SparringSpontane:
    def declencher(self, concept_actuel: str, historique: List) -> str:
        # 1. Identifier concept similaire passé
        # 2. Poser question connexion
        # 3. Approfondir différences
        # 4. Synthétiser
```

**Déclenchement :** Similarité > seuil  
**Prompt :** Questions comparatives  
**Sortie :** Question de connexion

#### **P.3 Synthèse Dynamique**
```python
class SyntheseDynamique:
    def declencher(self, concepts: List[str]) -> str:
        # 1. Identifier concepts clés
        # 2. Créer carte mentale
        # 3. Clarifier relations
        # 4. Simplifier
```

**Déclenchement :** Complexité > seuil  
**Prompt :** Synthèse visuelle  
**Sortie :** Carte mentale Markdown

### Configuration
```yaml
# config.yaml
protocols:
  error_detection:
    enabled: true
    keywords: ["error", "erreur", "failed", "échec"]
  
  sparring:
    enabled: true
    similarity_threshold: 0.7
  
  synthesis:
    enabled: true
    complexity_threshold: 5
```

### Flux de Données
```
B.1 Exploration → Detector → Protocole → Agent → UI
```

---

## 💾 Couche 4 : Stockage Local

### Responsabilités
- Persister les données
- Charger les sessions
- Versionner les artefacts
- Gérer la configuration

### Composants

#### **Journal (Markdown)**
```
cei_app/data/journal/
├── 2025-01-14_waybar.md
├── 2025-01-15_hyprland.md
└── 2025-01-16_neovim.md
```

**Format :**
```markdown
# Journal - [Titre Quête]
**Date :** 2025-01-14 10:30
**Durée :** 2h

## Actions
- 10:30 : Testé commande X
- 10:45 : Erreur Y rencontrée
- 11:00 : Solution trouvée

## Réflexions
- Concept X plus complexe que prévu
- Connexion avec concept Y
```

#### **Fiches (Markdown)**
```
cei_app/data/fiches/
├── waybar_configuration.md
├── hyprland_keybindings.md
└── neovim_plugins.md
```

**Format :** Structure standardisée (voir B.2)

#### **Arbre de Compétences (JSON)**
```json
{
  "competences": [
    {
      "nom": "Hyprland",
      "sous_competences": [
        {
          "nom": "Configuration",
          "statut": "maîtrisé",
          "date_acquisition": "2025-01-14",
          "quetes_liees": ["hyprland_setup"]
        },
        {
          "nom": "Keybindings",
          "statut": "exploré",
          "date_acquisition": "2025-01-15",
          "quetes_liees": ["hyprland_keys"]
        }
      ]
    }
  ]
}
```

#### **Historique Quêtes (JSON)**
```json
[
  {
    "id": "quest_001",
    "titre": "Configurer Waybar",
    "date_debut": "2025-01-14T10:00:00",
    "date_fin": "2025-01-14T12:30:00",
    "statut": "complétée",
    "validation_reussie": true,
    "concepts_acquis": ["waybar", "css", "json"],
    "fichiers": {
      "journal": "journal/2025-01-14_waybar.md",
      "fiche": "fiches/waybar_configuration.md"
    }
  }
]
```

#### **Configuration (YAML)**
```yaml
# config.yaml
gemini:
  model: "gemini-2.0-flash-exp"
  temperature: 0.7
  max_tokens: 8000

storage:
  data_dir: "cei_app/data"
  journal_dir: "cei_app/data/journal"
  fiches_dir: "cei_app/data/fiches"
  arbre_file: "cei_app/data/arbre.json"
  quetes_file: "cei_app/data/quetes.json"
```

#### **Storage Manager**
```python
# cei_app/storage/manager.py
class StorageManager:
    def sauvegarder_journal(self, quete_id, entries)
    def charger_journal(self, quete_id)
    def sauvegarder_fiche(self, titre, contenu)
    def charger_fiche(self, titre)
    def mettre_a_jour_arbre(self, competences)
    def charger_arbre(self)
    def ajouter_quete(self, quete)
    def charger_quetes(self)
```

### Technologies
- **Pathlib** : Gestion chemins
- **JSON** : Données structurées
- **Markdown** : Documents texte
- **YAML** : Configuration

### Flux de Données
```
Agent → StorageManager → Fichiers
Fichiers → StorageManager → Agent/UI
```

---

## 🌐 Couche 5 : Services Externes

### Responsabilités
- Générer contenu IA
- Gérer authentification
- Respecter rate limits

### Composants

#### **API Gemini**
```python
import google.generativeai as genai

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash-exp')

response = model.generate_content(prompt)
text = response.text
```

**Modèle :** `gemini-2.0-flash-exp`  
**Paramètres :**
- `temperature` : 0.7 (créativité modérée)
- `max_tokens` : 8000 (réponses longues)

**Rate Limits :**
- 60 requêtes/minute (gratuit)
- 1500 requêtes/jour (gratuit)

#### **Variables d'Environnement**
```bash
# .env
GEMINI_API_KEY=votre_cle_api_ici
```

**Chargement :**
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
```

### Gestion d'Erreurs
```python
try:
    response = model.generate_content(prompt)
except Exception as e:
    if "quota" in str(e).lower():
        # Rate limit atteint
        time.sleep(60)
        retry()
    elif "invalid" in str(e).lower():
        # API key invalide
        raise ConfigError("Vérifiez GEMINI_API_KEY")
    else:
        # Autre erreur
        log_error(e)
```

### Technologies
- **google-generativeai** : SDK officiel
- **python-dotenv** : Variables env
- **requests** : HTTP (sous le capot)

### Flux de Données
```
Agent → SDK Gemini → API Gemini → SDK → Agent
```

---

## 🔄 Flux de Données Complets

### Cycle Complet d'une Quête

```
1. DÉMARRAGE
   UI (Menu) → Agent (init)

2. PHASE A (Planification)
   UI (intention) → Agent (A.1) → Gemini → Agent → UI (questions)
   UI (réponses) → Agent (A.2) → Gemini → Agent → UI (concepts)
   Agent (A.3) → Gemini → Agent → UI (quête) → Storage (save)

3. PHASE B (Exécution)
   UI (actions) → Agent (B.1) → Detector → Protocoles → Gemini → Agent → UI
   Agent (journal) → Storage (save)
   
   Agent (B.2) → Gemini → Agent → UI (fiche) → Storage (save)
   Agent (B.3) → Gemini → Agent → UI (quiz)
   UI (réponses) → Agent (validation)
   
   Agent (B.4) → Gemini → Agent → UI (débriefing)
   Agent (B.5) → Storage (arbre) → UI (confirmation)

4. FIN
   Agent → Storage (save all) → UI (résumé)
```

### Communication entre Couches

```
┌─────────┐
│   UI    │ ←→ Display (Rich)
└────┬────┘
     │ Commandes/Inputs
     ↓
┌─────────┐
│  Agent  │ ←→ Context, History
└────┬────┘
     │ Prompts
     ↓
┌─────────┐
│ Gemini  │ ←→ API Key
└────┬────┘
     │ Réponses
     ↓
┌─────────┐
│ Storage │ ←→ Fichiers
└─────────┘
```

---

## 🎯 Patterns Architecturaux

### 1. **MVC Adapté**
- **Model** : Storage (données)
- **View** : UI/Display (affichage)
- **Controller** : Agent (logique)

### 2. **Observer Pattern**
- Detector observe B.1 (Exploration)
- Déclenche protocoles automatiquement

### 3. **Strategy Pattern**
- Protocoles = stratégies interchangeables
- Configuration active/désactive

### 4. **Facade Pattern**
- Agent = facade pour Gemini
- StorageManager = facade pour fichiers

### 5. **Template Method**
- Phase A/B = templates de workflow
- Étapes définies, implémentation flexible

---

## 🔒 Sécurité & Bonnes Pratiques

### Gestion des Secrets
```python
# ✅ BON
api_key = os.getenv('GEMINI_API_KEY')

# ❌ MAUVAIS
api_key = "AIzaSy..."  # Hardcodé
```

### Gestion d'Erreurs
```python
# ✅ BON
try:
    response = agent.generate(prompt)
except APIError as e:
    logger.error(f"API error: {e}")
    fallback_response()

# ❌ MAUVAIS
response = agent.generate(prompt)  # Pas de try/except
```

### Validation des Données
```python
# ✅ BON
if not intention or len(intention) < 10:
    raise ValueError("Intention trop courte")

# ❌ MAUVAIS
# Pas de validation
```

### Logging
```python
# ✅ BON
import logging
logging.info(f"Quête démarrée: {quete_id}")

# ❌ MAUVAIS
print(f"Quête démarrée: {quete_id}")  # Pas de log structuré
```

---

## 📈 Évolutivité

### Extensions Possibles

#### **1. Support Multi-LLM**
```python
class LLMFactory:
    @staticmethod
    def create(provider: str):
        if provider == "gemini":
            return GeminiAgent()
        elif provider == "openai":
            return OpenAIAgent()
        elif provider == "claude":
            return ClaudeAgent()
```

#### **2. Base de Données**
```python
# Remplacer JSON par SQLite/PostgreSQL
class DatabaseStorage:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
```

#### **3. Interface Web**
```python
# Ajouter FastAPI + React
@app.post("/api/quete/nouvelle")
async def nouvelle_quete(intention: str):
    result = agent.declarer_intention(intention)
    return result
```

#### **4. Collaboration**
```python
# Partage de fiches entre utilisateurs
class FicheRepository:
    def publier(self, fiche, public=False)
    def rechercher(self, query)
    def importer(self, fiche_id)
```

---

## 🧪 Tests

### Tests Unitaires
```python
# tests/test_agent.py
def test_declarer_intention():
    agent = CEIAgent()
    result = agent.declarer_intention("Configurer Waybar")
    assert "reformulation" in result
    assert len(result["questions"]) == 3
```

### Tests d'Intégration
```python
def test_cycle_complet():
    agent = CEIAgent()
    storage = StorageManager()
    
    # Phase A
    quete = agent.definir_quete(...)
    
    # Phase B
    fiche = agent.generer_fiche(...)
    storage.sauvegarder_fiche(fiche)
    
    assert os.path.exists(fiche_path)
```

### Tests E2E
```python
def test_workflow_complet():
    # Simuler utilisateur complet
    ui = CEITUI()
    agent = CEIAgent()
    
    # Nouvelle quête
    choix = "nouvelle"
    intention = "Test"
    # ... workflow complet
    
    assert quete_completed
```

---

## 📚 Ressources

### Documentation Technique
- **Gemini API** : https://ai.google.dev/docs
- **Rich** : https://rich.readthedocs.io/
- **Python Pathlib** : https://docs.python.org/3/library/pathlib.html

### Patterns
- **Design Patterns** : https://refactoring.guru/design-patterns
- **Clean Architecture** : Robert C. Martin

### Diagrammes
- **Mermaid** : https://mermaid.js.org/
- **Visualisation** : `sys_architectureCEI.mmd`

---

## ✅ Checklist Architecture

Avant d'implémenter, vérifiez :

- [ ] Comprendre les 5 couches
- [ ] Identifier les responsabilités de chaque composant
- [ ] Connaître les flux de données
- [ ] Comprendre les patterns utilisés
- [ ] Savoir où ajouter des fonctionnalités
- [ ] Connaître les points d'extension

---

**Version** : 1.0  
**Dernière mise à jour** : 2025-01-14  
**Auteur** : Sidix (avec assistance Cascade)
