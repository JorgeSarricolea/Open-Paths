import os
import time

#Menu
menu = """
        -- MENU OF PATHS --

        1. Personal folder
        2. ITM Folder
        3. Projects
        4. Downloads
        5. Multimedia
        6. open the first 3 paths
        7. Exit
        """
option = 0
activeMenu=1

#Paths
itmPath = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Instituto Tecnológico de Mérida"
personalFolder = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Documents\Projects\Jorge Sarricolea"
projects = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Documents\Projects"
downloads = "C:/Users/jorge/Downloads"
multimedia = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Multimedia"

while activeMenu == 1:
    print(menu)
    option = int(input("Select an option by typing the number: "))
    if option == 1:
        os.startfile(personalFolder)
    if option == 2:
        os.startfile(itmPath)
    if option == 3:
        os.startfile(projects)
    if option == 4:
        os.startfile(downloads)
    if option == 5:
        os.startfile(multimedia)
    if (option == 6):
        os.startfile(personalFolder)
        os.startfile(itmPath)
        os.startfile(projects)
    if option == 7:
        activeMenu = 0
        print("\nBYE BYE 👋")

