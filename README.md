# LLMsForEducation
(*ANITI Internship*)

## Architecture du projet

Ce projet `LLMsForEducation` est une étude de cas sur l'utilisation de l'IA générative dans l'enseignement supérieur des sciences du numérique, organisé comme suit :

### Dossiers

- **`allumettes/`** : Cas d'étude principal - implémentation du jeu des 13 allumettes
  - `docs/` : Documents en Markdown-- avant export en pdf
    - `subject.md` : Spécifications du jeu avec affichage attendu
    - `prompts.md` : Tests de prompts avec ChatGPT et GitHub Copilot
  - `pdfs` : Documents exportés en pdf.
  - `src/` : Code source avec différentes approches d'utilisation de l'IA
    - `passive_code/` : Code généré par consommation passive d'IA
    - `creation_code/` : Code créé en collaboration avec l'IA

- **`docs/`** : Documentation et rapports
  - `report1_yan_rabefaniraka.md` : Rapport principal sur l'utilisation de l'IA par les étudiants
  - `model_comparison_for_langchain_api.md` : Comparatif des modèles IA par tâche
  - `Ppai6_creative_use_cases.md` : Grille d'évaluation des usages créatifs de l'IA

- **`pdfs/`** : Export en pdf des documents
  - `report1_yan_rabefaniraka.pdf` : Export en pdf du rapport global

- **`notebooks/`** : Jupyter notebooks interactifs
  - `Main_notebook.ipynb` : Notebook principal avec vulgarisation des LLMs et code Python interactible.
  - `langchainSimpleLLM.ipynb` : Test de micro-implémentation LangChain pour de futures usages

- **`copilot_chats/`** : Historique des conversations avec GitHub Copilot
  - `passive_iter_1.md` : Session de consommation passive
  - `creative_iter_2.md` : Session de création collaborative

- **`CR/`** : Comptes-rendus de réunions
- **`templates/`** : Modèles pour les tests sur notebook (*IMCOMPLET ET MIS EN PAUSE*)

### Objectif

Le projet vise à **évaluer et améliorer l'utilisation de l'IA générative** (en faire une formation/module éducatif ) par les étudiants en sciences du numérique, en réalisant dans un premier lieu une étude de cas où on évalue la capacité de l'IA à aider un étudiant; On se base pour ¢a sur une grille d'évaluation éducative qui sépare les différentes interactions Humain-IA selon leur pertinence et potentiel de créativité. Ensuite, on peut en déduire des *notebooks* Jupyter pour enseigner-- outre la base technique de l'IA gńeŕative-- les techniques de prompt permettant de travailler plus efficacement avec l'IA.

Ce projet tente d'inclure dans sa démarche des questions éthiques liées à l'utilisation de cette technologie par les étudiants et les enseignants: En connaissant l'impact écologique de l'apprentissage et du maintien des services d'IA générative, en ayant eu vent des récentes observations du MIT sur [les baisses de capacité cognitive causées par l'utilisation passive au long terme de ChatGPT par des étudiants](https://www.media.mit.edu/publications/your-brain-on-chatgpt/), tout en sachant que la quasi-hégémonie de l'IA générative est inévitable, le mieux à faire et d'apprendre aux étudiants à s'en servir *mieux*, plus efficacement. L'objectif est de trouver une généralisation à la relation de co-création, où l'utilisateur et l'IA produisent un résultat qu'aucun des deux n'auraient pu faire sans l'autre. 