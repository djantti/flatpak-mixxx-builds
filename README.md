# Flatpak Mixxx builds

This repository produces daily Flatpak development builds from [Mixxx](https://www.mixxx.org) main branch. Builds are available as single-file Flatpak bundles and the latest successful build can always be downloaded from the GitHub Pages links below. An optional debug extension bundle is also provided.

Please note that these are **unstable**, **untested** and **unofficial** builds. They should be used for development and testing purposes only. For a stable DJing experience, please install the official Mixxx Flatpak from [Flathub](https://flathub.org/apps/org.mixxx.Mixxx) or use distribution specific packages.

# Downloads

Latest builds for x86-64 and AArch64 architectures are listed here. Check the [Actions](https://github.com/djantti/flatpak-mixxx-builds/actions) page to download artifacts from past workflow runs.

### *x86-64*

- 📦 [Mixxx-Devel_x86_64.flatpak](https://djantti.github.io/flatpak-mixxx-builds/Mixxx-Devel_x86_64.flatpak)
- 🪲 [Mixxx-Devel_x86_64.Debug.flatpak](https://djantti.github.io/flatpak-mixxx-builds/Mixxx-Devel_x86_64.Debug.flatpak)

### *AArch64*

- 📦 [Mixxx-Devel_aarch64.flatpak](https://djantti.github.io/flatpak-mixxx-builds/Mixxx-Devel_aarch64.flatpak)
- 🪲 [Mixxx-Devel_aarch64.Debug.flatpak](https://djantti.github.io/flatpak-mixxx-builds/Mixxx-Devel_aarch64.Debug.flatpak)

# Examples

- 💻 `flatpak install --user Mixxx-Devel_x86_64.flatpak`
- 🎚️ `flatpak run org.mixxx.Mixxx.Devel`
- 🧹 `flatpak uninstall --user org.mixxx.Mixxx.Devel`
- 🔎 `flatpak run --command=sh --devel org.mixxx.Mixxx.Devel`

# Build

1. `git clone https://github.com/djantti/flatpak-mixxx-builds.git`
2. `cd flatpak-mixxx-builds`
3. `git clone --single-branch --branch main https://github.com/mixxxdj/mixxx.git`
4. `python3 scripts/update_metainfo.py`
5. `flatpak-builder --force-clean --repo=repo build org.mixxx.Mixxx.Devel.json`

# Notes

These builds use a custom application ID (*org.mixxx.Mixxx.Devel*), so it's possible to have the official Mixxx Flatpak and a development build installed at the same time. All application data, configuration files and settings are kept separate.

# Links

- 🗃️ [Official Mixxx Flathub repository](https://github.com/flathub/org.mixxx.Mixxx)
- 🏗️ [Flatpak Builder documentation](https://docs.flatpak.org/en/latest/flatpak-builder.html)
- ✨ [Flatpak GitHub Actions](https://github.com/flatpak/flatpak-github-actions)
