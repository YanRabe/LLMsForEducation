---
title: "Rapport 1 - Yan Rabefaniraka"
author: 
- Yan Rabefaniraka, stagiaire de Meriem Ouederni et David Brunet
date: 13 Juin 2025
geometry: margin=2cm
output: pdf_document
---

**Remarques :** 
- Fichier engendré avec:
    ```
    pandoc -o ../pdfs/report1_yan_rabefaniraka.pdf report1_yan_rabefaniraka.md
    ```
- Par facilité d'écriture, on utilisera le masculin 'étudiant' pour qualifier les étudiant.es.
# Abstrait du sujet de stage

Pour ce stage, il m'est demandé en tant qu'étudiant en sciences du numérique d'établir une étude de cas approfondie sur l'utilisation actuelle par les étudiants de l'IA générative dans ce domaine--- en particulier des modèles de langage--- et d'en déduire une possible utilisation plus efficace pour l'apprentissage. Mon expérience personnelle et mon statut d'étudiant sont un bon apport de départ, accompagnés par ma tutrice qui enseigne directement aux concerné.es.

Cette mission n'a pas de filière cible et n'est pas seulement dirigée vers celles spécialisées en informatique, tout d'abord parce que l'aide que l'IA pourrait fournir dans les études s'applique à tous les domaines, mais aussi parce que l'importance grandissante des petits cas d'usage de l'informatique dans les études supérieures (e.g savoir mettre sur un graphe avec *Python/Matlab* ses données d'expérience pour un.e étudiant.e en agronomie ou en chimie, ou encore faire des statistiques sur *RStudio* à partir de sondages pour un.e étudiant.e en sociologie) permet de se questionner sur les facilitations que l'IA offre à celles et ceux dont le futur métier ne se trouve pas dans les sciences du numérique.

Ainsi, les tests effectués et les conclusions déduites de cette étude de cas--- spécifiquement pour les sciences du numérique--- doivent être applicables pour un niveau débutant, voire en particulier pour des langages haut niveau comme le *Python*.

Cependant, on peut aussi vérifier la puissance / les limites de l'utilisation de l'IA Générative dans l'apprentissage d'une matière complexe. Pour cela, **l'Ingénierie Dirigée par les Modèles**, enseignée (par Mme Ouederni aux 2ème années) à l'ENSEEIHT sera certainement choisie: C'est une matière suffisamment théorique mais avec des applications directes dans les différents processus de développement/industriels, avec une grande part de notions graphiques. Elle s'enseigne aussi avec 9 cours de *Travaux pratiques* sur machine, avec code et modélisation donc. On pourra ainsi vérifier ce que l'IA peut proposer à un étudiant qui cherche à l'utiliser pour travailler la matière en autonomie.

L'objectif final de cette étude de cas étant la création d'une formation / d'un module qui offrirait aux étudiants de tout horizon un set d'outils pour leur enseigner les bonnes pratiques, il n'est pas anodin de donner les bases de l'IA génératives à travers une courte vulgarisation du fonctionnement de la GenAI et des LLMs pour les non-initié.es.
Le public étant large il est aussi intéressant mentionner les impacts environnementaux en rappelant les coûts en énergie et en eau de l'apprentissage et de la maintenance des services, de la place des utilisateurs dans la boucle (apprentissage actif, données personnelles) mais aussi des limites de l'IA *i.e* les hallucinations, les erreurs, les biais causés par le *data set*, les biais de confirmation de ChatGPT, etc. 
Mais, il est aussi essentiel de leur montrer à quel point ces outils sont puissants, en parlant de tout ce qui est inclus avec ChatGPT (compilateur LateX, Python), la gratuité de Github Copilot pour tout étudiant avec au choix l'utilisation de modèles de Claude Sonnet, GPT, et Gemini, ainsi que les modèles *offline*. Cela inclut donc un comparatif des différents modèles de langage gratuits actuellement sur le marché, par tâche et *use cases* afin de comparer leur pertinence.

Enfin, cela implique donc d'établir des critères de qualité/validation de réponses selon le domaine, les prompts, l'IA, etc. Pour ce faire, plusieurs tests seront effectués et tabulés tout au long du stage. Des templates seront également préparés pour d'éventuels Jupyter Notebooks (à lancer sur Google Colab par exemple). Ces derniers facilitent l'interactivité et augmenteront donc l'accessibilité du projet.


# Intérêt de la mission en tant qu'étudiant avec une professeure pour tutrice

En tant qu'étudiant en sciences du numérique, je vais donc me servir de mes propres expériences avec l'IA Générative et vais partager l'usage que j'en fais ou que j'ai pu constater lors de ma $1^{ère}$ année, que ce soit pour y apporter un regard critique ou m'en servir de base pour développer la suite du projet.


# Ressenti - étudiant

Dans cette section, je vais donc étayer les différents usages de l'IA Générative que j'ai jusque là pu observer.

## Utilisation de l'IA par le cor apprenant

### Apprentissage

On constate plusieurs cas d'utilisation courants que font les étudiants de l'IA générative dans l'apprentissage, en particulier de ChatGPT:
- **Trouver des solutions à des problèmes** **spontanés** qu'ils rencontrent lors de l'apprentissage d'un cours ou la résolution d'exercices, quand aucun professeur n'est à disposition pour y répondre. Cette utilisation est de plus en plus courante quand les étudiants résolvent des exercices pour lesquels il n'y a pas de correction claire et où ils ne sont donc pas assurés d'avoir les bonnes réponses, voire d'avoir compris le cours. Cela peut aussi s'appliquer à la programmation, quand la documentation pour une librairie est difficile à trouver ou à lire et que son utilisation n'est qu'un outil et non pas l'objectif final. On peut par exemple penser aux différentes fonctions intégrées de *Matlab* dont la compréhension peut parfois être sinueuse; *Matlab* n'étant qu'un outil numérique pour appliquer un cours théorique (e.g avec le Traitement du Signal et les Télécommunications), les étudiants se permettent de l'utiliser pour comprendre comment l'implémenter.
- **Expliquer/résumer un cours** qu'ils n'ont pas compris ou dont ils veulent vérifier leur propre compréhension. Cela peut s'apparenter à de l'aide personnalisée, avec les étudiants qui fournissent la section du cours qu'ils n'ont pas comprise. De même, certains s'en servent pour générer des questions typiques ou des quiz, comme des équivalents à la plateforme *Quizlet*.

*AJOUTER IMAGES ICI pour illustrer avec Graphes python, code Matlab*.


### Facilitation des tâches pénibles

Une utilisation courante est aussi celle de la facilitation des tâches fastidieuses (répétitives, peu challengeantes) en passant par l'IA. On rencontre le plus ce cas d'utilisation lors de de TPs ou de projets qui nécessitent du code répétitif et peu demandant en réflexion technique pour les étudiants. On peut notamment penser aux méthodes répétitives en programmation orientée objet, comme des *getters* ou des *setters*, ou encore aux matières dont le code n'est pas le sujet principal mais un support d'application (mathématiques appliquées par exemple). 

### Triche

Cas où l'apprentissage est peu effiace. Comment changer ca ? A faire pour vendredi


# Ressenti - professeure

À demander à Meriem Ouederni.

# Pistes d'amélioration pour l'utilisation actuelle et mise en pratique

Partie à venir, avec test sur les IAs.