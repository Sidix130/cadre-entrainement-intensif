class ProjetArchon:
    def __init__(self):
        self.nom = "Forger l'environnement Hyprland parfait"
        self.acteurs = [ArchitecteSidix(), SparringPartnerGemini()]
        self.phase_planification = PhasePlanification()
        self.phase_execution = PhaseExecution()
        self.protocoles = [LeconErreur(), SparringSpontane(), SyntheseDynamique()]
        self.outils = [JournalBord(), FicheRecapitulative(), ArbreCompetences()]
        self.cycle_actif = True
        
    def demarrer_projet(self):
        print(f"🚀 Démarrage du projet: {self.nom}")
        while self.cycle_actif:
            self.executer_cycle_complet()
            
    def executer_cycle_complet(self):
        """Exécute un cycle complet Planification -> Execution"""
        # Phase A: Planification
        intention = self.phase_planification.declarer_intention()
        concepts = self.phase_planification.deconstruire_concepts(intention)
        quete = self.phase_planification.definir_quete(concepts)
        
        # Phase B: Execution
        self.phase_execution.executer_workflow(quete, self.acteurs, self.outils)
        
        # Vérifier si on continue
        self.evaluer_continuation()

    def evaluer_continuation(self):
        """Détermine si le projet doit continuer"""
        # Logique pour décider de continuer ou arrêter
        if self.phase_execution.maitrise_atteinte:
            print("🎯 Maîtrise atteinte! Projet terminé.")
            self.cycle_actif = False

class ArchitecteSidix:
    def __init__(self):
        self.role = "Définit, pratique, verbalise"
        self.journal = JournalBord()
        self.expertise_actuelle = "Débutant"
        
    def declarer_intention(self):
        intention = input("🎯 Architecte Sidix - Quelle est votre intention? ")
        self.journal.ajouter_entree("Déclaration d'intention", intention)
        return intention
        
    def pratiquer_exploration(self, quete):
        print(f"👨‍💻 Architecte en exploration: {quete}")
        # Simulation de la pratique
        commandes_testees = ["hyprctl monitors", "hyprpaper config", "waybar settings"]
        resultats = {}
        
        for cmd in commandes_testees:
            print(f"  Testing: {cmd}")
            resultat = input(f"  Résultat pour {cmd}: ")
            resultats[cmd] = resultat
            self.journal.ajouter_entree(f"Pratique - {cmd}", resultat)
            
        return resultats
        
    def verbaliser_apprentissage(self, apprentissage):
        print(f"💭 Verbalisation: {apprentissage}")
        self.journal.ajouter_entree("Verbalisation", apprentissage)

class SparringPartnerGemini:
    def __init__(self):
        self.role = "Guide, valide, synthétise"
        
    def guider_exploration(self, intention_architecte):
        questions_guidage = [
            f"Quels aspects de '{intention_architecte}' souhaitez-vous explorer?",
            "Avez-vous considéré les implications système?",
            "Quels sont vos critères de succès?"
        ]
        return questions_guidage
        
    def valider_approche(self, approche_architecte):
        print(f"🔍 Validation Gemini: {approche_architecte}")
        validation = input("Gemini - Cette approche est-elle valide? (oui/non/amendements): ")
        return validation
        
    def synthetiser_connaissances(self, journal_entries):
        print("📊 Synthèse Gemini en cours...")
        themes_cles = ["Configuration", "Performance", "UX/UI", "Intégration"]
        synthese = f"Synthèse des apprentissages: {', '.join(themes_cles)}"
        return synthese

class PhasePlanification:
    def __init__(self):
        self.etapes = [
            "1. Déclaration d'Intention",
            "2. Déconstruction des Concepts", 
            "3. Définition de la Quête - Objectif clair et mesurable"
        ]
        
    def declarer_intention(self):
        print("\n" + "="*50)
        print("PHASE A: PLANIFICATION - Quest Framing Cycle")
        print("="*50)
        return self.etapes[0]
        
    def deconstruire_concepts(self, intention):
        print(f"\n🔨 Déconstruction des concepts pour: {intention}")
        concepts = intention.split()
        concepts_etendus = []
        
        for concept in concepts:
            sous_concepts = input(f"  Sous-concepts pour '{concept}': ").split(",")
            concepts_etendus.extend([sc.strip() for sc in sous_concepts])
            
        print(f"  Concepts déconstruits: {concepts_etendus}")
        return concepts_etendus
        
    def definir_quete(self, concepts):
        quete = f"Implémenter: {', '.join(concepts[:3])}"  # Prend les 3 premiers concepts
        print(f"🎯 Quête définie: {quete}")
        return quete

class PhaseExecution:
    def __init__(self):
        self.cycles = [
            "1. Exploration et Pratique (Mains sur le clavier)",
            "2. Capitalisation (Génération de la Fiche)",
            "3. Validation Finale (Défi Inverse)",
            "4. Débriefing Métacognitif (Analyse du Journal)",
            "5. Mise à jour de la Maîtrise (Mise à jour de l'Arbre)"
        ]
        self.maitrise_atteinte = False
        self.fiches_produites = []
        
    def executer_workflow(self, quete, acteurs, outils):
        print("\n" + "="*50)
        print("PHASE B: EXECUTION - Workflow Cycle")
        print("="*50)
        
        architecte = acteurs[0]
        sparring = acteurs[1]
        journal, fiche, arbre = outils
        
        # Cycle 1: Exploration et Pratique
        print(f"\n🔄 {self.cycles[0]}")
        resultats_pratique = architecte.pratiquer_exploration(quete)
        
        # Interactions avec Sparring Partner
        questions_guidage = sparring.guider_exploration(quete)
        for question in questions_guidage:
            print(f"  🤔 {question}")
            reponse = input("  Réponse: ")
            journal.ajouter_entree("Guidage", f"Q: {question} - R: {reponse}")
        
        # Cycle 2: Capitalisation
        print(f"\n📝 {self.cycles[1]}")
        fiche_creee = self.generer_fiche(quete, resultats_pratique, journal)
        self.fiches_produites.append(fiche_creee)
        
        # Cycle 3: Validation Finale
        print(f"\n✅ {self.cycles[2]}")
        validation = sparring.valider_approche(fiche_creee)
        journal.ajouter_entree("Validation", validation)
        
        # Cycle 4: Débriefing Métacognitif
        print(f"\n🧠 {self.cycles[3]}")
        self.debriefing_metacognitif(journal, architecte)
        
        # Cycle 5: Mise à jour Maîtrise
        print(f"\n🌱 {self.cycles[4]}")
        self.mettre_a_jour_maitrise(arbre, fiche_creee)
        
    def generer_fiche(self, quete, resultats, journal):
        fiche = {
            "quete": quete,
            "date": "2024-01-15",
            "resultats": resultats,
            "commandes_cles": list(resultats.keys()),
            "apprentissages": journal.dernieres_entrees(3)
        }
        print(f"  📄 Fiche générée: {fiche['quete']}")
        return fiche
        
    def debriefing_metacognitif(self, journal, architecte):
        entrees_recentes = journal.dernieres_entrees(5)
        print("  Analyse du journal:")
        for entree in entrees_recentes:
            print(f"    - {entree}")
        
        insight = input("  💡 Insight métacognitif: ")
        architecte.verbaliser_apprentissage(insight)
        
    def mettre_a_jour_maitrise(self, arbre, fiche):
        arbre.ajouter_competence(fiche["quete"], "Maîtrisé")
        print(f"  🌳 Arbre mis à jour: {fiche['quete']} → Maîtrisé")
        
        # Vérifier si la maîtrise globale est atteinte
        if len(arbre.competences) >= 3:  # Exemple de condition
            self.maitrise_atteinte = True

class ProtocoleSpecial:
    def __init__(self):
        self.est_actif = False
        
    def declencher(self, contexte):
        raise NotImplementedError

class LeconErreur(ProtocoleSpecial):
    def declencher(self, contexte):
        print("🚨 PROTOCOLE: Leçon de l'Erreur déclenché!")
        print("   Analysons cette erreur pour en tirer des enseignements...")
        analyse = input("   Quelle leçon tirez-vous de cette erreur? ")
        return f"Leçon: {analyse}"

class SparringSpontane(ProtocoleSpecial):
    def declencher(self, contexte):
        print("💬 PROTOCOLE: Sparring Spontané déclenché!")
        question_urgence = "Que se passe-t-il? Comment puis-je vous aider?"
        print(f"   Gemini: {question_urgence}")
        reponse = input("   Votre réponse: ")
        return f"Sparring spontané: {reponse}"

class SyntheseDynamique(ProtocoleSpecial):
    def declencher(self, contexte):
        print("🎯 PROTOCOLE: Synthèse Dynamique déclenché!")
        synthese = "Synthèse des patterns identifiés..."
        print(f"   {synthese}")
        return synthese

class Outil:
    def __init__(self):
        self.contenu = []

class JournalBord(Outil):
    def __init__(self):
        super().__init__()
        self.description = "Input/Output de l'Architecte"
        
    def ajouter_entree(self, type_entree, contenu):
        entree = f"[{type_entree}] {contenu}"
        self.contenu.append(entree)
        print(f"  📖 Journal: {entree}")
        
    def dernieres_entrees(self, n):
        return self.contenu[-n:] if self.contenu else []

class FicheRecapitulative(Outil):
    def __init__(self):
        super().__init__()
        self.description = "Livrable de Capitalisation"
        self.fiches = []

class ArbreCompetences(Outil):
    def __init__(self):
        super().__init__()
        self.description = "Carte de la Maîtrise"
        self.competences = {}
        
    def ajouter_competence(self, competence, niveau):
        self.competences[competence] = niveau

# Gestionnaire de déclencheurs
class GestionnaireDeclencheurs:
    def __init__(self, protocoles):
        self.protocoles = protocoles
        
    def verifier_declencheurs(self, contexte):
        """Vérifie si des protocoles spéciaux doivent être déclenchés"""
        declencheurs_actives = []
        
        # Simulation: 30% de chance de déclencher un protocole
        import random
        if random.random() < 0.3:
            protocole = random.choice(self.protocoles)
            resultat = protocole.declencher(contexte)
            declencheurs_actives.append(resultat)
            
        return declencheurs_actives

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialisation du projet
    projet = ProjetArchon()
    gestionnaire = GestionnaireDeclencheurs(projet.protocoles)
    
    print("🏛️  PROJET ARCHON - Environnement Hyprland Parfait")
    print("=" * 60)
    
    # Simulation d'un cycle
    contexte = {"phase": "exploration", "difficulte": "moyenne"}
    
    # Vérification des déclencheurs spéciaux
    declenchements = gestionnaire.verifier_declencheurs(contexte)
    
    # Démarrage manuel d'un cycle (pour test)
    projet.executer_cycle_complet()
    
    # Affichage des résultats
    print("\n" + "="*60)
    print("📊 ÉTAT FINAL DU PROJET")
    print(f"Fiches produites: {len(projet.phase_execution.fiches_produites)}")
    print(f"Entrées journal: {len(projet.outils[0].contenu)}")
    print(f"Compétences maîtrisées: {len(projet.outils[2].competences)}")