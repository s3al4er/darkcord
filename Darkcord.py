# Importing libs

from colorama import init, Fore, Style
import pyfiglet
import subprocess as sp

import os

# Setupping 0 to plugin name, and theme name vars

plname = 0
thname = 0

# Initing colorama with autoreset

init(autoreset=True)


def cls():
	os.system("cls")


# Printing menu

def menu():

	try:

		os.system("cls")

		# Printing client name and version

		f = pyfiglet.figlet_format("DARKCORD", font="banner4")
		print(Fore.GREEN + f)

		print("""
			|------------------|
			| 1. Load plugin   |
			| 2. Load theme    |
			| 3. Update repos  |
		        | 4. Info          |
			|------------------|
			""")

		# Creating option select

		menu_select = input(Fore.YELLOW + "Select option: ")

		# Load plugin

		if menu_select == "1":
			try:
				plname = input(Fore.YELLOW + "Enter plugin name: ")
				plugin_path = os.path.join(os.getcwd(), "plugins", plname + "_injector.py")
				sp.call(["python", plugin_path])

			except Exception as e:
				print(f"Произошла ошибка: {e}")
				exit(2)

			menu()

		# Load theme

		elif menu_select == "2":
			thname = input(Fore.GREEN + "Enter theme name: ")
			theme_path = os.path.join(os.getcwd(), "themes", thname + "_injector.py")
			sp.call(["python", theme_path])
			menu()

		# Updater

		elif menu_select == "3":
			os.system("rmdir /s  /q plugins")
			os.system("rmdir /s /q themes")
			os.system("git clone https://github.com/s3al4er/darkcord-plugins.git plugins")
			os.system("git clone https://github.com/s3al4er/darkcord-themes.git themes")
			menu()

		elif menu_select == "4":
			print(Fore.YELLOW + """
				DARKCORD 1.0
				Author: s3al4er
				Modifying the Discord client can get your account banned.
				The author is not responsible for your actions!
				""")
			menu()

	except KeyboardInterrupt:
		cls()
		print(Fore.RED + "Closing darkcord...")
		exit(0)

menu()

