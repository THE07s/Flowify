# 🌊 Flowify

**Port macOS de FlowFrames avec optimisations spécialisées pour les vidéos de gaming**

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Description

Flowify est un outil d'interpolation vidéo haute performance spécialement conçu pour optimiser les vidéos de jeux vidéo. Utilisant RIFE-NCNN-Vulkan, il offre une interpolation intelligente pour augmenter le framerate tout en préservant la qualité.

## ✨ Fonctionnalités

- 🚀 **Interpolation vidéo basée sur RIFE-NCNN-Vulkan**
- 📹 **Support multi-formats** : MP4, MOV, AVI, MKV
- ⚡ **Multiplication configurable des frames** (2x, 4x, etc.)
- 🎛️ **Contrôle du ralentissement vidéo**
- 🔊 **Préservation de l'audio original**
- 💻 **Interface en ligne de commande interactive**
- 🖼️ **Support des séquences d'images**

## 🛠️ Installation

### Prérequis
- Python 3.8+
- FFmpeg installé sur le système
- macOS (optimisé pour Apple Silicon)

### Installation rapide
```bash
# Cloner le dépôt
git clone https://github.com/votre-username/flowify.git
cd flowify

# Installer les dépendances
pip install -r requirements.txt

# Rendre RIFE exécutable
chmod +x rife-ncnn-vulkan/rife-ncnn-vulkan
```

## 🎯 Utilisation

### Interface interactive
```bash
python Flowify.py
```

Suivez les instructions à l'écran pour :
1. Sélectionner votre dossier de vidéos
2. Choisir le multiplicateur de frames
3. Configurer les paramètres d'interpolation
4. Sélectionner le modèle RIFE

### Modèles disponibles
- **rife-v4.6** : Modèle général le plus récent (recommandé)
- **rife-anime** : Optimisé pour l'animation
- **rife-UHD** : Optimisé pour les hautes résolutions

## 📁 Structure du projet

```
Flowify/
├── Flowify.py              # Script principal
├── requirements.txt        # Dépendances Python
├── README.md              # Documentation
├── rife-ncnn-vulkan/      # Binaires et modèles RIFE
│   ├── rife-ncnn-vulkan   # Exécutable principal
│   ├── rife-anime/        # Modèle anime
│   ├── rife-UHD/          # Modèle UHD
│   └── rife-v4.6/         # Modèle v4.6
└── test files/            # Vidéos de test
```

## 🚀 Roadmap

- **Phase 1** ✅ : Port macOS avec optimisations Metal
- **Phase 2** 🔄 : Modèle IA spécialisé gaming (détection HUD/Gameplay)  
- **Phase 3** 📋 : Extension multiplateforme (Windows DirectX, Linux Vulkan)
- **Phase 4** 📋 : Interface graphique moderne
- **Phase 5** 📋 : Traitement par lots automatisé

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir des issues pour signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## ⚡ Performance

- **Accélération GPU** : Utilise Vulkan pour l'accélération matérielle
- **Optimisations macOS** : Tire parti de Metal Performance Shaders
- **Mémoire optimisée** : Traitement par chunks pour les grandes vidéos

## 🙏 Remerciements

- [RIFE](https://github.com/megvii-research/ECCV2022-RIFE) pour l'algorithme d'interpolation
- [RIFE-NCNN-Vulkan](https://github.com/nihui/rife-ncnn-vulkan) pour l'implémentation optimisée
