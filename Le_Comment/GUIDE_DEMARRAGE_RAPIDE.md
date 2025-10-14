# 🚀 Guide de Démarrage Rapide - C.E.I.

**Temps estimé : 30 minutes**

Ce guide vous permet de lancer votre première session C.E.I. rapidement.

---

## ⚡ Installation Express (10 min)

### 1. Prérequis
```bash
# Vérifier Python 3.10+
python3 --version

# Vérifier pip
pip --version
```

### 2. Installation
```bash
# Cloner le repo
cd ~/dev
git clone https://github.com/Sidix130/cadre-entrainement-intensif.git
cd cadre-entrainement-intensif

# Créer environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer dépendances
pip install -r requirements.txt
```

### 3. Configuration API Gemini
```bash
# 1. Obtenir clé API gratuite
# → https://aistudio.google.com/app/apikey

# 2. Créer fichier .env
echo "GEMINI_API_KEY=votre_cle_api_ici" > .env

# 3. Tester connexion
python3 test_connection.py
```

**✅ Si vous voyez une réponse de Gemini, c'est bon !**

---

## 🎯 Premier Cycle C.E.I. (20 min)

### Lancer l'Application
```bash
python3 main.py
```

### Workflow Guidé

#### **Phase A : Planification (5 min)**

1. **Déclaration d'Intention**
   ```
   Exemple : "Je veux configurer Waybar sur Hyprland"
   ```

2. **Déconstruction** (Gemini pose des questions)
   ```
   - Quels modules Waybar voulez-vous ?
   - Quel style visuel ?
   - Intégration avec quels outils ?
   ```

3. **Définition de la Quête**
   ```
   Gemini génère : "Configurer Waybar avec modules CPU, RAM, 
   réseau et horloge, style Dracula, intégration Hyprland"
   ```

#### **Phase B : Exécution (15 min)**

4. **Exploration & Pratique**
   ```bash
   # Vous testez des commandes
   waybar --version
   cat ~/.config/waybar/config
   
   # Le journal enregistre automatiquement
   ```

5. **Capitalisation**
   ```
   Gemini génère une fiche récapitulative avec :
   - Concepts clés
   - Commandes importantes
   - Pièges évités
   - Prochaines étapes
   ```

6. **Défi Inverse**
   ```
   Quiz interactif pour valider la compréhension
   ```

7. **Débriefing**
   ```
   Analyse de votre processus de réflexion
   ```

8. **Mise à Jour Arbre**
   ```
   Votre arbre de compétences est mis à jour
   ```

---

## 📁 Structure des Fichiers Générés

```
cei_app/data/
├── journal/
│   └── 2025-01-14_waybar.md          # Votre journal
├── fiches/
│   └── waybar_configuration.md       # Fiche générée
├── arbre.json                         # Arbre de compétences
└── quetes.json                        # Historique quêtes
```

---

## 🎨 Commandes Spéciales

Pendant l'exploration, utilisez :

- `/erreur` → Déclenche "Leçon de l'Erreur"
- `/sparring` → Déclenche "Sparring Spontané"
- `/synthese` → Déclenche "Synthèse Dynamique"
- `/fiche` → Génère fiche immédiatement
- `/quit` → Sauvegarde et quitte

---

## 💡 Conseils pour Démarrer

### ✅ À Faire
- **Commencez petit** : Une quête simple (15-30 min)
- **Verbalisez** : Expliquez ce que vous faites
- **Notez tout** : Le journal est votre mémoire
- **Testez les protocoles** : Provoquez une erreur pour voir

### ❌ À Éviter
- Quêtes trop ambitieuses au début
- Sauter le débriefing métacognitif
- Ne pas consulter les fiches générées
- Oublier de mettre à jour l'arbre

---

## 🆘 Dépannage Rapide

### Problème : "API Key invalide"
```bash
# Vérifier le fichier .env
cat .env

# Régénérer la clé sur
# https://aistudio.google.com/app/apikey
```

### Problème : "Module not found"
```bash
# Réinstaller dépendances
pip install -r requirements.txt --force-reinstall
```

### Problème : "Connexion timeout"
```bash
# Vérifier connexion internet
ping google.com

# Vérifier proxy si nécessaire
export HTTP_PROXY=...
```

---

## 📚 Prochaines Étapes

Une fois votre premier cycle terminé :

1. **Consultez la roadmap complète** : `Le_Comment/roadmap.md`
2. **Lisez les cours** : `Le_Comment/doc/`
3. **Explorez le code** : `Le_Comment/code/`
4. **Personnalisez** : Adaptez les prompts à votre style

---

## 🎯 Exemple Complet

### Quête : "Comprendre les keybindings Hyprland"

**Temps : ~20 min**

```bash
# 1. Lancer
python3 main.py

# 2. Intention
"Je veux maîtriser les keybindings Hyprland"

# 3. Gemini déconstruit
- Syntaxe bind
- Modificateurs (SUPER, ALT, etc.)
- Actions disponibles
- Conflits potentiels

# 4. Quête définie
"Créer 10 keybindings personnalisés pour Hyprland 
avec SUPER comme modificateur principal"

# 5. Exploration
bind = SUPER, Q, exec, kitty
bind = SUPER, W, killactive
bind = SUPER, F, fullscreen
# ... tester chaque binding

# 6. Fiche générée
✅ Concepts : bind, modificateurs, exec
✅ Commandes : hyprctl reload
✅ Pièges : Conflits avec keybindings système
✅ Next : Créer des submaps

# 7. Défi Inverse
Q: Comment créer un binding avec 2 modificateurs ?
R: bind = SUPER_SHIFT, Q, exec, ...

# 8. Débriefing
"J'ai d'abord testé sans réfléchir, puis j'ai 
compris la logique de la syntaxe..."

# 9. Arbre mis à jour
Hyprland > Configuration > Keybindings ✅ Maîtrisé
```

---

## ✨ Vous êtes Prêt !

**Checklist finale :**
- [ ] Python 3.10+ installé
- [ ] Dépendances installées
- [ ] Clé API Gemini configurée
- [ ] Test de connexion réussi
- [ ] Premier cycle lu

**🚀 Lancez `python3 main.py` et commencez votre première quête !**

---

**Support** : Si vous rencontrez des problèmes, consultez `Le_Comment/doc/` ou ouvrez une issue sur GitHub.

**Version** : 1.0  
**Dernière mise à jour** : 2025-01-14
