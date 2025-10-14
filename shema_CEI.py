#!/usr/bin/env python3
"""
Générateur de Schémas pour le Cadre d'Entraînement Intensif (C.E.I.)
Version: 7.0 "Maestro"

Ce module génère des visualisations du framework C.E.I. sous différents formats:
- Diagramme de flux complet (Mermaid → SVG/PNG)
- Arbre de compétences (Mermaid mindmap)
- Timeline d'un cycle (visualisation temporelle)
- Graphe de dépendances des concepts
"""

import os
import json
from matplotlib import pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

# Configuration des styles (cohérents avec le diagramme Mermaid)
STYLES = {
    'goal':     {'facecolor': '#c8e6c9', 'edgecolor': '#2e7d32', 'textcolor': '#1b5e20'},
    'actor':    {'facecolor': '#e1f5fe', 'edgecolor': '#0277bd', 'textcolor': '#01579b'},
    'quest':    {'facecolor': '#f3e5f5', 'edgecolor': '#6a1b9a', 'textcolor': '#4a148c'},
    'workflow': {'facecolor': '#e8eaf6', 'edgecolor': '#303f9f', 'textcolor': '#1a237e'},
    'trigger':  {'facecolor': '#fff3e0', 'edgecolor': '#ef6c00', 'textcolor': '#e65100'},
    'tool':     {'facecolor': '#f5f5f5', 'edgecolor': '#616161', 'textcolor': '#212121'},
}

class GenerateurSchemas:
    """Classe principale pour générer les différents schémas du C.E.I."""
    
    def __init__(self, output_dir='exports'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Charger la configuration JSON si disponible
        self.config = self._charger_config()
        
    def _charger_config(self):
        """Charge la configuration depuis C.E.I.json"""
        config_path = os.path.join(os.path.dirname(__file__), 'C.E.I.json')
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def generer_diagramme_flux_complet(self):
        """Génère le diagramme de flux complet du système C.E.I."""
        fig, ax = plt.subplots(figsize=(16, 12))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        # Positions des nœuds
        pos = {
            'A': (0.5, 0.94),
            'ARCHITECT': (0.15, 0.82),
            'SPARRING': (0.85, 0.82),
            'Q1': (0.20, 0.65),
            'Q2': (0.20, 0.57),
            'Q3': (0.20, 0.49),
            'W1': (0.60, 0.65),
            'W2': (0.60, 0.57),
            'W3': (0.60, 0.49),
            'W4': (0.60, 0.41),
            'W5': (0.60, 0.33),
            'T1': (0.88, 0.57),
            'T2': (0.88, 0.47),
            'T3': (0.88, 0.37),
            'JDB': (0.20, 0.15),
            'FR': (0.50, 0.15),
            'AC': (0.80, 0.15)
        }
        
        # Dessiner les groupes
        self._draw_group(ax, 0.40, 0.91, 0.20, 0.07, "GOAL [Projet Archon]", 'goal')
        self._draw_group(ax, 0.02, 0.77, 0.96, 0.12, "ACTORS [Acteurs]", 'actor')
        self._draw_group(ax, 0.02, 0.44, 0.38, 0.28, "QUEST_FRAMING [Phase A: Planification]", 'quest')
        self._draw_group(ax, 0.42, 0.28, 0.38, 0.48, "WORKFLOW [Phase B: Exécution]", 'workflow')
        self._draw_group(ax, 0.82, 0.32, 0.16, 0.32, "TRIGGERS [Protocoles Spéciaux]", 'trigger')
        self._draw_group(ax, 0.02, 0.08, 0.96, 0.14, "TOOLS [Outils & Artefacts]", 'tool')
        
        # Dessiner les nœuds
        nodes = {
            'A': ("Forger l'environnement\nHyprland parfait", 'goal', 0.18, 0.05),
            'ARCHITECT': ("Architecte (Sidix)\nDéfinit, pratique, verbalise", 'actor', 0.24, 0.08),
            'SPARRING': ("Sparring Partner (Gemini)\nGuide, valide, synthétise", 'actor', 0.24, 0.08),
            'Q1': ("1. Déclaration\nd'Intention", 'quest', 0.16, 0.06),
            'Q2': ("2. Déconstruction\ndes Concepts", 'quest', 0.16, 0.06),
            'Q3': ("3. Définition de la Quête\nObjectif clair & mesurable", 'quest', 0.16, 0.07),
            'W1': ("1. Exploration & Pratique\n(Mains sur le clavier)", 'workflow', 0.18, 0.06),
            'W2': ("2. Capitalisation\n(Génération de la Fiche)", 'workflow', 0.18, 0.06),
            'W3': ("3. Validation Finale\n(Défi Inverse)", 'workflow', 0.18, 0.06),
            'W4': ("4. Débriefing Méta-Cognitif\n(Analyse du Journal)", 'workflow', 0.18, 0.06),
            'W5': ("5. Mise à jour de la Maîtrise\n(Mise à jour de l'Arbre)", 'workflow', 0.18, 0.06),
            'T1': ("Leçon de\nl'Erreur", 'trigger', 0.12, 0.06),
            'T2': ("Sparring\nSpontané", 'trigger', 0.12, 0.06),
            'T3': ("Synthèse\nDynamique", 'trigger', 0.12, 0.06),
            'JDB': ("Journal de Bord\n(Input/Output)", 'tool', 0.16, 0.06),
            'FR': ("Fiche Récapitulative\n(Capitalisation)", 'tool', 0.16, 0.06),
            'AC': ("Arbre de Compétences\n(Carte de Maîtrise)", 'tool', 0.16, 0.06),
        }
        
        for key, (text, style, w, h) in nodes.items():
            x, y = pos[key]
            self._draw_node(ax, x, y, w, h, text, style)
        
        # Dessiner les flèches
        arrows = [
            ('ARCHITECT', 'Q1', 'solid', "Initie le cycle"),
            ('Q1', 'Q2', 'solid', None),
            ('Q2', 'Q3', 'solid', None),
            ('Q3', 'W1', 'solid', "Lance la quête"),
            ('W1', 'W2', 'solid', None),
            ('W2', 'W3', 'solid', None),
            ('W3', 'W4', 'solid', None),
            ('W4', 'W5', 'solid', None),
            ('W5', 'Q1', 'solid', "Boucle"),
            ('W1', 'ARCHITECT', 'solid', "Interaction\nconstante"),
            ('W1', 'SPARRING', 'solid', "Interaction\nconstante"),
            ('W1', 'T1', 'dashed', "Déclenche"),
            ('W1', 'T2', 'dashed', None),
            ('W1', 'T3', 'dashed', None),
            ('ARCHITECT', 'JDB', 'solid', "Tient à jour"),
            ('JDB', 'W4', 'solid', "Alimente"),
            ('W2', 'FR', 'solid', "Produit"),
            ('W5', 'AC', 'solid', "Met à jour"),
        ]
        
        for arrow in arrows:
            if len(arrow) == 4:
                src, dst, style, label = arrow
            else:
                src, dst, style = arrow
                label = None
            self._draw_arrow(ax, pos[src], pos[dst], style, label)
        
        # Titre
        ax.text(0.5, 0.99, "Cadre d'Entraînement Intensif (C.E.I.) v7.0 'Maestro'", 
                ha='center', va='top', fontsize=14, fontweight='bold')
        
        # Sauvegarder
        svg_path = os.path.join(self.output_dir, 'cei_flux_complet.svg')
        png_path = os.path.join(self.output_dir, 'cei_flux_complet.png')
        plt.savefig(svg_path, bbox_inches='tight', dpi=300)
        plt.savefig(png_path, bbox_inches='tight', dpi=150)
        plt.close(fig)
        
        print(f"✅ Diagramme de flux complet généré:")
        print(f"   SVG: {svg_path}")
        print(f"   PNG: {png_path}")
        
    def generer_arbre_competences_exemple(self):
        """Génère un exemple d'arbre de compétences pour Hyprland"""
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        # Structure hiérarchique de l'arbre
        tree = {
            'root': {'pos': (0.5, 0.9), 'text': 'Maîtrise Hyprland', 'level': 0},
            'config': {'pos': (0.25, 0.75), 'text': 'Configuration\nde Base', 'level': 1, 'parent': 'root'},
            'theming': {'pos': (0.5, 0.75), 'text': 'Theming &\nEsthétique', 'level': 1, 'parent': 'root'},
            'workflow': {'pos': (0.75, 0.75), 'text': 'Workflow &\nProductivité', 'level': 1, 'parent': 'root'},
            
            'monitors': {'pos': (0.15, 0.6), 'text': 'Gestion\nMoniteurs', 'level': 2, 'parent': 'config', 'status': 'acquired'},
            'input': {'pos': (0.35, 0.6), 'text': 'Clavier/Souris', 'level': 2, 'parent': 'config', 'status': 'acquired'},
            
            'waybar': {'pos': (0.4, 0.6), 'text': 'Waybar', 'level': 2, 'parent': 'theming', 'status': 'in_progress'},
            'dunst': {'pos': (0.5, 0.6), 'text': 'Dunst', 'level': 2, 'parent': 'theming', 'status': 'explored'},
            'hyprpaper': {'pos': (0.6, 0.6), 'text': 'Hyprpaper', 'level': 2, 'parent': 'theming', 'status': 'not_started'},
            
            'keybinds': {'pos': (0.7, 0.6), 'text': 'Keybindings', 'level': 2, 'parent': 'workflow', 'status': 'acquired'},
            'scripts': {'pos': (0.8, 0.6), 'text': 'Scripts\nAutomation', 'level': 2, 'parent': 'workflow', 'status': 'in_progress'},
        }
        
        # Dessiner les connexions
        for key, node in tree.items():
            if 'parent' in node:
                parent = tree[node['parent']]
                self._draw_tree_connection(ax, parent['pos'], node['pos'])
        
        # Dessiner les nœuds
        for key, node in tree.items():
            status = node.get('status', 'root')
            color_map = {
                'root': '#4CAF50',
                'acquired': '#2196F3',
                'in_progress': '#FF9800',
                'explored': '#9C27B0',
                'not_started': '#9E9E9E'
            }
            self._draw_tree_node(ax, node['pos'][0], node['pos'][1], 
                               node['text'], color_map.get(status, '#9E9E9E'))
        
        # Légende
        legend_elements = [
            mpatches.Patch(color='#2196F3', label='Acquis'),
            mpatches.Patch(color='#FF9800', label='En cours'),
            mpatches.Patch(color='#9C27B0', label='Exploré'),
            mpatches.Patch(color='#9E9E9E', label='Non commencé')
        ]
        ax.legend(handles=legend_elements, loc='lower right', fontsize=10)
        
        # Titre
        ax.text(0.5, 0.98, "Arbre de Compétences - Exemple Projet Archon", 
                ha='center', va='top', fontsize=14, fontweight='bold')
        
        # Sauvegarder
        svg_path = os.path.join(self.output_dir, 'cei_arbre_competences.svg')
        png_path = os.path.join(self.output_dir, 'cei_arbre_competences.png')
        plt.savefig(svg_path, bbox_inches='tight', dpi=300)
        plt.savefig(png_path, bbox_inches='tight', dpi=150)
        plt.close(fig)
        
        print(f"✅ Arbre de compétences généré:")
        print(f"   SVG: {svg_path}")
        print(f"   PNG: {png_path}")
    
    def generer_timeline_cycle(self):
        """Génère une timeline d'un cycle complet C.E.I."""
        fig, ax = plt.subplots(figsize=(16, 6))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        # Phases sur la timeline
        phases = [
            {'x': 0.05, 'width': 0.15, 'label': 'Phase A\nPlanification', 'color': '#f3e5f5'},
            {'x': 0.22, 'width': 0.50, 'label': 'Phase B\nExécution', 'color': '#e8eaf6'},
            {'x': 0.74, 'width': 0.10, 'label': 'Débriefing\nMéta-Cognitif', 'color': '#fff3e0'},
            {'x': 0.86, 'width': 0.10, 'label': 'Mise à jour\nMaîtrise', 'color': '#c8e6c9'},
        ]
        
        # Dessiner la ligne de temps
        ax.plot([0.02, 0.98], [0.5, 0.5], 'k-', linewidth=2, zorder=1)
        
        # Dessiner les phases
        for i, phase in enumerate(phases):
            rect = Rectangle((phase['x'], 0.35), phase['width'], 0.3,
                           facecolor=phase['color'], edgecolor='black', linewidth=2, zorder=2)
            ax.add_patch(rect)
            ax.text(phase['x'] + phase['width']/2, 0.5, phase['label'],
                   ha='center', va='center', fontsize=10, fontweight='bold', zorder=3)
        
        # Ajouter des marqueurs temporels
        markers = [
            (0.05, 'Intention'),
            (0.12, 'Déconstruction'),
            (0.19, 'Quête définie'),
            (0.30, 'Exploration'),
            (0.45, 'Capitalisation'),
            (0.55, 'Validation'),
            (0.65, 'Débriefing'),
            (0.79, 'Analyse Journal'),
            (0.91, 'Arbre mis à jour'),
        ]
        
        for x, label in markers:
            ax.plot([x, x], [0.5, 0.25], 'k--', linewidth=1, alpha=0.5)
            ax.text(x, 0.20, label, ha='center', va='top', fontsize=8, rotation=45)
        
        # Ajouter les Learning Triggers (peuvent survenir à tout moment)
        trigger_y = 0.75
        ax.text(0.5, trigger_y + 0.05, 'Learning Triggers (déclenchables à tout moment)', 
                ha='center', fontsize=10, style='italic', color='#ef6c00')
        
        triggers = [
            (0.35, 'Erreur'),
            (0.50, 'Sparring'),
            (0.60, 'Synthèse'),
        ]
        
        for x, label in triggers:
            circle = Circle((x, trigger_y), 0.02, facecolor='#fff3e0', 
                          edgecolor='#ef6c00', linewidth=2, zorder=4)
            ax.add_patch(circle)
            ax.text(x, trigger_y - 0.08, label, ha='center', fontsize=8)
        
        # Titre
        ax.text(0.5, 0.95, "Timeline d'un Cycle C.E.I. Complet", 
                ha='center', va='top', fontsize=14, fontweight='bold')
        
        # Sauvegarder
        svg_path = os.path.join(self.output_dir, 'cei_timeline.svg')
        png_path = os.path.join(self.output_dir, 'cei_timeline.png')
        plt.savefig(svg_path, bbox_inches='tight', dpi=300)
        plt.savefig(png_path, bbox_inches='tight', dpi=150)
        plt.close(fig)
        
        print(f"✅ Timeline du cycle généré:")
        print(f"   SVG: {svg_path}")
        print(f"   PNG: {png_path}")
    
    def generer_mermaid_code(self):
        """Génère le code Mermaid pour différentes visualisations"""
        mermaid_files = {}
        
        # 1. Arbre de compétences en mindmap
        mindmap = """mindmap
  root((Maîtrise Hyprland))
    Configuration de Base
      Gestion Moniteurs
      Clavier/Souris
      Workspaces
    Theming & Esthétique
      Waybar
      Dunst
      Hyprpaper
      GTK Theme
    Workflow & Productivité
      Keybindings
      Scripts Automation
      Window Rules
    Intégration Système
      Audio (Pipewire)
      Bluetooth
      Network Manager
"""
        mermaid_files['arbre_competences.mmd'] = mindmap
        
        # 2. Diagramme de séquence d'un cycle
        sequence = """sequenceDiagram
    participant A as Architecte
    participant S as Sparring Partner
    participant J as Journal de Bord
    participant F as Fiche Récap
    participant Ar as Arbre Compétences
    
    A->>S: Déclaration d'Intention
    S->>A: Questions de déconstruction
    A->>J: Note ses réflexions
    S->>A: Définition de la Quête
    
    rect rgb(232, 234, 246)
        Note over A,S: Phase d'Exploration
        loop Pratique Active
            A->>A: Expérimentation
            A->>J: Journalise résultats
            A->>S: Verbalise compréhension
            S->>A: Validation/Guidage
        end
    end
    
    A->>F: Génère Fiche Récapitulative
    S->>A: Défi Inverse (Validation)
    S->>A: Débriefing Méta-Cognitif
    A->>J: Insights sur le processus
    A->>Ar: Mise à jour compétences
    
    Note over A,Ar: Cycle terminé, prêt pour le suivant
"""
        mermaid_files['sequence_cycle.mmd'] = sequence
        
        # 3. Diagramme d'état des compétences
        state = """stateDiagram-v2
    [*] --> NonCommencé
    NonCommencé --> Exploré: Première exposition
    Exploré --> EnCours: Pratique active
    EnCours --> Acquis: Validation réussie
    Acquis --> Maîtrisé: Application répétée
    
    EnCours --> Exploré: Blocage/Confusion
    Exploré --> NonCommencé: Abandon temporaire
    
    Maîtrisé --> [*]: Intégré au workflow
    
    note right of Exploré
        Fiche créée
        Concepts identifiés
    end note
    
    note right of Acquis
        Défi Inverse réussi
        Ajouté à l'Arbre
    end note
"""
        mermaid_files['etat_competences.mmd'] = state
        
        # Sauvegarder tous les fichiers Mermaid
        for filename, content in mermaid_files.items():
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fichier Mermaid généré: {filepath}")
    
    # Méthodes utilitaires pour le dessin
    def _draw_node(self, ax, x, y, w, h, text, style_key):
        """Dessine un nœud avec style"""
        style = STYLES.get(style_key, STYLES['tool'])
        box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                            boxstyle="round,pad=0.01", linewidth=1.5,
                            facecolor=style['facecolor'], 
                            edgecolor=style['edgecolor'])
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=8,
                color=style['textcolor'], weight='bold')
    
    def _draw_group(self, ax, x0, y0, width, height, label, style_key):
        """Dessine un groupe avec style"""
        style = STYLES.get(style_key, STYLES['tool'])
        group = Rectangle((x0, y0), width, height, linewidth=2, fill=True,
                         facecolor=style['facecolor'], edgecolor=style['edgecolor'], 
                         alpha=0.2)
        ax.add_patch(group)
        ax.text(x0 + 0.01, y0 + height - 0.01, label, ha='left', va='top', 
                fontsize=9, fontweight='bold', color=style['textcolor'])
    
    def _draw_arrow(self, ax, start, end, style, label=None):
        """Dessine une flèche entre deux points"""
        arrow = FancyArrowPatch(start, end, arrowstyle='->', 
                               linestyle=('dashed' if style == 'dashed' else 'solid'),
                               linewidth=1.5, color='#424242', 
                               shrinkA=10, shrinkB=10, zorder=1)
        ax.add_patch(arrow)
        
        if label:
            mid_x = (start[0] + end[0]) / 2
            mid_y = (start[1] + end[1]) / 2
            ax.text(mid_x, mid_y, label, fontsize=7, ha='center', 
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                            edgecolor='none', alpha=0.8))
    
    def _draw_tree_node(self, ax, x, y, text, color):
        """Dessine un nœud d'arbre"""
        circle = Circle((x, y), 0.04, facecolor=color, edgecolor='black', 
                       linewidth=2, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y - 0.07, text, ha='center', va='top', fontsize=8, 
               weight='bold')
    
    def _draw_tree_connection(self, ax, start, end):
        """Dessine une connexion d'arbre"""
        ax.plot([start[0], end[0]], [start[1], end[1]], 'k-', 
               linewidth=2, alpha=0.5, zorder=2)
    
    def generer_tous_schemas(self):
        """Génère tous les schémas disponibles"""
        print("\n" + "="*60)
        print("🎨 GÉNÉRATEUR DE SCHÉMAS C.E.I. v7.0 'Maestro'")
        print("="*60 + "\n")
        
        self.generer_diagramme_flux_complet()
        print()
        self.generer_arbre_competences_exemple()
        print()
        self.generer_timeline_cycle()
        print()
        self.generer_mermaid_code()
        
        print("\n" + "="*60)
        print(f"✨ Tous les schémas ont été générés dans: {self.output_dir}/")
        print("="*60)


if __name__ == "__main__":
    generateur = GenerateurSchemas()
    generateur.generer_tous_schemas()
