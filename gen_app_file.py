#!/usr/bin/env python3

import os

name = input("Enter app name: ")
desc = input("Enter app description: ")
icon = input("Drag and drop icon path: ").split("'")[1]
path = input("Drag and drop executable path: ")

tags = []

while True:
	tag = input("Enter tag (enter quit when done): ")
	
	if tag != "quit":
		tags.append(tag.strip())
	else:
		break

tags = ";".join(tags)

file = f"""
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name={name}
Comment={desc}
Icon={icon}
Exec={path}
Terminal=false
Categories={tags}"""

with open(f"{name}.desktop", "w") as desktop_file:
	desktop_file.write(file)

os.system(f"mv {name}.desktop ~/.local/share/applications")

print("Entry complete!")
