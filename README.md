# Flowify

Port macOS de FlowFrames avec optimisations Metal et IA spécialisée gaming.

## Description

Flowify est un outil d'interpolation vidéo spécialement conçu pour optimiser les vidéos de jeux vidéo. Le projet vise à développer un modèle d'IA personnalisé capable de différencier l'interface utilisateur (HUD) du contenu de jeu pour une interpolation plus précise.

## Fonctionnalités

- Interpolation vidéo basée sur RIFE-NCNN-Vulkan
- Support des formats MP4, MOV, AVI, MKV
- Multiplication configurable des frames
- Contrôle du ralentissement vidéo
- Préservation de l'audio original
- Interface en ligne de commande interactive

## Installation

```bash
# Installer les dépendances
pip install -r requirements.txt

# Rendre RIFE exécutable
chmod +x rife-ncnn-vulkan/rife-ncnn-vulkan
```

## Utilisation

```bash
python Flowify.py
```

## Roadmap

- **Phase 1** : Port macOS avec optimisations Metal
- **Phase 2** : Modèle IA spécialisé gaming (détection HUD/Gameplay)  
- **Phase 3** : Extension multiplateforme (Windows DirectX, Linux Vulkan)

## Architecture

```
src/flowify/           # Modules principaux
├── video_processor.py # Traitement vidéo/audio
├── rife_engine.py    # Moteur d'interpolation
└── config_manager.py # Gestion configuration
```
