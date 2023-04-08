import os

#Menu
menu = """
    -- MENU OF PATHS --

    1. Portfolio
    2. Personal folder
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
portfolio = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Documents\Projects\Jorge Sarricolea\GitHub\Portfolio 2.0"
itmPath = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Instituto Tecnológico de Mérida"
personalFolder = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Documents\Projects\Jorge Sarricolea"
projects = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Documents\Projects"
downloads = "C:/Users/jorge/Downloads"
multimedia = "C:/Users/jorge/OneDrive - INSTITUTO TECNOLOGICO DE MERIDA\Multimedia"

while activeMenu == 1:
    print(menu)
    option = int(input("    Select an option by typing the number: "))
    if option == 1:
        os.startfile(portfolio)
    if option == 2:
        os.startfile(personalFolder)
    if option == 3:
        os.startfile(itmPath)
    if option == 4:
        os.startfile(projects)
    if option == 5:
        os.startfile(downloads)
    if option == 6:
        os.startfile(multimedia)
    if option == 7:
        os.startfile(personalFolder)
        os.startfile(itmPath)
        os.startfile(projects)
    if option == 8:
        activeMenu = 0
        print("\nBYE BYE 👋")

