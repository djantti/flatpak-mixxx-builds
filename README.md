# Flatpak Mixxx builds

This repository produces daily Flatpak development builds from [Mixxx](https://www.mixxx.org) main branch. Builds are available as single-file Flatpak bundles and the latest successful build can always be downloaded from the link below. Check the [Actions page](https://github.com/djantti/flatpak-mixxx-builds/actions) to download (GitHub account required) zipped artifacts from past workflow runs.

Please note that these are **unstable**, **untested** and **unofficial** builds. They should be used for development and testing purposes only. For a stable DJing experience, please install the official Mixxx Flatpak from [Flathub](https://flathub.org/apps/org.mixxx.Mixxx) or use distribution specific packages.

# Download

- 📦 [Mixxx-Devel.flatpak](https://djantti.github.io/flatpak-mixxx-builds/Mixxx-Devel.flatpak) (~18 MB)

# Usage

- 🎚️ `flatpak install --user Mixxx-Devel.flatpak`
- 🧹 `flatpak uninstall --user org.mixxx.Mixxx.Devel`
- 🧱 `flatpak-builder --force-clean --repo=repo build org.mixxx.Mixxx.Devel.json`

# Notes

These builds use a custom application ID (*org.mixxx.Mixxx.Devel*), so it's possible to have the official Mixxx Flatpak and a development build installed at the same time. All application data, configuration files and settings are kept separate.

# Links

- 🗃️ [Official Mixxx Flathub repository](https://github.com/flathub/org.mixxx.Mixxx)
- 🏗️ [Flatpak Builder documentation](https://docs.flatpak.org/en/latest/flatpak-builder.html)
- ✨ [Flatpak GitHub Actions](https://github.com/flathub-infra/flatpak-github-actions)