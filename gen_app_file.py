#!/usr/bin/env python3

import os

name = input("Enter app name: ")
desc = input("Enter app description: ")
icon = input("Drag and drop icon: ").split("'")[1]
exec = input("Drag and drop executable: ").split("'")[1]
term = input("Is this a terminal program? (y/n): ")
term = "true" if term == "y" else "false";
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
Exec={exec}
Terminal={term}
Categories={tags}"""

name = f"{name}.desktop"
path = os.path.expanduser("~") + f"/.local/share/applications/{name}"

with open(path, "w") as desktop_file:
	desktop_file.write(file)

print(f"Entry complete! Desktop file written to {path}")
