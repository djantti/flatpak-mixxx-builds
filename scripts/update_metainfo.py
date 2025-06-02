#!/usr/bin/env python3

import xml.etree.ElementTree as ET

# Read the Mixxx MetaInfo file
mixxx_tree = ET.parse("mixxx/res/linux/org.mixxx.Mixxx.metainfo.xml")
mixxx_root = mixxx_tree.getroot()

# First development release tag contains main branch version info
mixxx_release = mixxx_root.find(".//release[@type='development']")
print("Release: " + mixxx_release.attrib['version'])
print("Date: " + mixxx_release.attrib['date'])

# Read Flatpak packaging MetaInfo file
flatpak_tree = ET.parse("org.mixxx.Mixxx.Devel.metainfo.xml.in")
flatpak_root = flatpak_tree.getroot()

# Add a new tags and attributes based on Mixxx release
flatpak_releases = ET.SubElement(flatpak_root, "releases")

flatpak_release = ET.SubElement(flatpak_releases, "release")
flatpak_release.attrib['version'] = mixxx_release.attrib['version']
flatpak_release.attrib['date'] = mixxx_release.attrib['date']

flatpak_url = ET.SubElement(flatpak_release, "url")
flatpak_url.attrib['type'] = "details"
flatpak_url.text = "https://github.com/mixxxdj/mixxx/blob/main/CHANGELOG.md"

# Indent the XML tree
ET.indent(flatpak_tree, "  ")

# Convert the tree into a formatted string with proper header and newline
flatpak_metainfo = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    + ET.tostring(flatpak_root, encoding="utf_8", xml_declaration=False).decode() + "\n")

# Write the new Flatpak MetaInfo file
with open("org.mixxx.Mixxx.Devel.metainfo.xml", "wb") as f:
    f.write(flatpak_metainfo.encode())
