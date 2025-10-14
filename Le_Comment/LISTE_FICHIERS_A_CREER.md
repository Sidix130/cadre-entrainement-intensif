# 📋 Liste Complète des Fichiers à Créer

**Suivez cette checklist pour implémenter le système C.E.I. demain.**

Tous les codes détaillés sont dans `Le_Comment/code/` - copiez-collez directement.

---

## ✅ Checklist d'Implémentation

### Phase 1 : Setup (1h)

- [ ] `requirements.txt` - Dépendances Python
- [ ] `.env` - Clé API Gemini  
- [ ] `config.yaml` - Configuration système
- [ ] Test connexion Gemini

### Phase 2 : Core Agent (2h)

- [ ] `cei_app/__init__.py` - Package principal
- [ ] `cei_app/core/__init__.py` - Package core
- [ ] `cei_app/core/agent.py` - Agent Gemini (300 lignes)
- [ ] `cei_app/core/protocols.py` - Learning Triggers
- [ ] Tests agent

### Phase 3 : Interface TUI (2h)

- [ ] `cei_app/ui/__init__.py` - Package UI
- [ ] `cei_app/ui/tui.py` - Interface Rich (200 lignes)
- [ ] `cei_app/storage/__init__.py` - Package storage
- [ ] `cei_app/storage/manager.py` - Gestion fichiers
- [ ] Tests interface

### Phase 4 : Protocoles (2h)

- [ ] Protocole Leçon de l'Erreur
- [ ] Protocole Sparring Spontané
- [ ] Protocole Synthèse Dynamique
- [ ] Gestionnaire déclencheurs
- [ ] Tests protocoles

### Phase 5 : Finalisation (1h)

- [ ] `main.py` - Point d'entrée
- [ ] Tests cycle complet
- [ ] Documentation usage
- [ ] Commit & Push

---

## 📁 Arborescence Complète

```
cei_app/
├── __init__.py                    ← Vide
├── core/
│   ├── __init__.py                ← Vide
│   ├── agent.py                   ← 300 lignes (PRIORITÉ 1)
│   └── protocols.py               ← 150 lignes
├── ui/
│   ├── __init__.py                ← Vide
│   └── tui.py                     ← 200 lignes (PRIORITÉ 2)
├── storage/
│   ├── __init__.py                ← Vide
│   └── manager.py                 ← 100 lignes
├── data/
│   ├── journal/                   ← Créer dossier
│   ├── fiches/                    ← Créer dossier
│   ├── arbre.json                 ← Créer vide {}
│   └── quetes.json                ← Créer vide []
├── tests/
│   └── test_agent.py              ← 50 lignes
├── config.yaml                    ← 30 lignes
├── main.py                        ← 100 lignes (PRIORITÉ 1)
├── .env                           ← 1 ligne
└── requirements.txt               ← 4 lignes (PRIORITÉ 1)
```

---

## 🔥 Fichiers Prioritaires (À faire en premier)

### 1. requirements.txt
```txt
google-generativeai==0.3.2
rich==13.7.0
pyyaml==6.0.1
python-dotenv==1.0.0
```

### 2. .env
```env
GEMINI_API_KEY=votre_cle_ici
```

### 3. config.yaml
Voir `Le_Comment/code/config.yaml`

### 4. cei_app/core/agent.py
Voir `Le_Comment/code/cei_app/core/agent.py` (fichier complet avec tous les prompts)

### 5. main.py
Voir `Le_Comment/code/main.py`

---

## 📚 Documentation Disponible

### Cours Techniques
- `Le_Comment/doc/01_setup_environnement.md` - Installation
- `Le_Comment/doc/02_api_gemini.md` - Utilisation Gemini
- `Le_Comment/doc/03_interface_tui.md` - Rich/TUI
- `Le_Comment/doc/04_stockage_local.md` - Gestion fichiers
- `Le_Comment/doc/05_architecture.md` - Patterns
- `Le_Comment/doc/06_prompts_cei.md` - Bibliothèque prompts

### Guides
- `Le_Comment/GUIDE_DEMARRAGE_RAPIDE.md` - Quick start
- `Le_Comment/roadmap.md` - Roadmap 8h détaillée
- `Le_Comment/plan.md` - Architecture technique

---

## 🎯 Ordre d'Implémentation Recommandé

### Heure 1 : Setup
1. Créer structure dossiers
2. Installer dépendances
3. Configurer API Gemini
4. Tester connexion

### Heures 2-3 : Agent Core
1. Créer `agent.py` avec méthodes de base
2. Implémenter Phase A (planification)
3. Implémenter Phase B (exécution)
4. Tests unitaires

### Heures 4-5 : Interface
1. Créer `tui.py` avec menu principal
2. Interface Phase A
3. Interface Phase B
4. Tests navigation

### Heures 6-7 : Protocoles
1. Implémenter Leçon de l'Erreur
2. Implémenter Sparring Spontané
3. Implémenter Synthèse Dynamique
4. Tests intégration

### Heure 8 : Finalisation
1. `main.py` orchestration
2. Tests cycle complet
3. Documentation
4. Commit

---

## 💡 Conseils d'Implémentation

### Si Vous Bloquez
1. **Consultez les cours** dans `doc/`
2. **Regardez le code de référence** dans `code/`
3. **Simplifiez** : Version minimale d'abord
4. **Testez souvent** : Chaque fonction

### Raccourcis Possibles
- Phase 1 : Utilisez des valeurs par défaut au lieu de config.yaml
- Phase 2 : Commencez avec 1-2 méthodes agent
- Phase 3 : Interface basique sans Rich au début
- Phase 4 : Implémentez 1 seul protocole

### Points de Sauvegarde
Après chaque phase, commitez :
```bash
git add .
git commit -m "Phase X terminée"
```

---

## 🚀 Commandes Rapides

### Créer Structure
```bash
mkdir -p cei_app/{core,ui,storage,tests,data/{journal,fiches}}
touch cei_app/{__init__.py,core/__init__.py,ui/__init__.py,storage/__init__.py}
echo '{}' > cei_app/data/arbre.json
echo '[]' > cei_app/data/quetes.json
```

### Installer
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Tester
```bash
python3 -m pytest cei_app/tests/
python3 cei_app/core/agent.py  # Tests intégrés
```

### Lancer
```bash
python3 main.py
```

---

## ✅ Critères de Succès

À la fin, vous devez pouvoir :

1. ✅ Lancer `python3 main.py`
2. ✅ Déclarer une intention
3. ✅ Voir Gemini poser des questions
4. ✅ Obtenir une quête définie
5. ✅ Explorer avec guidage
6. ✅ Générer une fiche
7. ✅ Passer un quiz
8. ✅ Voir le débriefing
9. ✅ Arbre mis à jour

---

**Tous les codes complets sont dans `Le_Comment/code/` - Copiez-collez et adaptez !**

**Bonne implémentation ! 🚀**
