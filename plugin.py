def Credits():
    global version, developer
    version = "v1.0.1"
    developer = "YT*Toaster (James Mc'Douglas)"
    return version, developer
Credits()

def ReadMod():
    from os.path import exists
    from os import getcwd
    print(f"PLUGIN: New Plugin Folder '{getcwd()}\\plugins'.")
    print(" ")
    print(f"==== Better-Plugin-Folder Dialogue ====")

    if exists(f'{plugin_path}\\plugin0.py'):
        import plugin0
        print(f"PLUGIN: Plugin Version - {plugin0.version}")
        print(f"PLUGIN: Created By - {plugin0.developer}")
        print(" ")
        plugin0.MainApp()
        print("=================== ===================")
    
    if exists(f'{plugin_path}\\plugin1.py'):
        import plugin1
        print(f"PLUGIN: Plugin Version - {plugin1.version}")
        print(f"PLUGIN: Created By - {plugin1.developer}")
        print(" ")
        plugin1.MainApp()
        print("=================== ===================")
    
    if exists(f'{plugin_path}\\plugin2.py'):
        import plugin2
        print(f"PLUGIN: Plugin Version - {plugin2.version}")
        print(f"PLUGIN: Created By - {plugin2.developer}")
        print(" ")
        plugin2.MainApp()
        print("=================== ===================")
    
    if exists(f'{plugin_path}\\plugin3.py'):
        import plugin3
        print(f"PLUGIN: Plugin Version - {plugin3.version}")
        print(f"PLUGIN: Created By - {plugin3.developer}")
        print(" ")
        plugin3.MainApp()
        print("=================== ===================")

    if exists(f'{plugin_path}\\plugin4.py'):
        import plugin4
        print(f"PLUGIN: Plugin Version - {plugin4.version}")
        print(f"PLUGIN: Created By - {plugin4.developer}")
        print(" ")
        plugin4.MainApp()
        print("=================== ===================")
    
    if exists(f'{plugin_path}\\plugin5.py'):
        import plugin5
        print(f"PLUGIN: Plugin Version - {plugin5.version}")
        print(f"PLUGIN: Created By - {plugin5.developer}")
        print(" ")
        plugin5.MainApp()
        print("=================== ===================")


def copy_plugins():
    from os import remove
    from os.path import join, basename, exists
    from shutil import copytree

    file_name = basename(__file__)
    
    if exists(f"{plugin_path}") == False:
        copytree(old_path,f"{directory}\\plugins")
        remove(f"{plugin_path}\\{file_name}")
    else:
        try:
            remove(f"{plugin_path}\\{file_name}")
        except FileNotFoundError:
            pass

    for i in range(4):
        file_paths = join(old_path, f"plugin{i}.py")
        try:
            remove(file_paths)
        except FileNotFoundError:
            pass
        except Exception as e:
            pass
    ReadMod()

def MainApp():
    global plugin_path, directory, old_path
    from sys import path
    from os.path import join, basename, exists
    from os import getcwd, system
    from time import sleep

    directory = getcwd()
    old_path = join(directory,'_dat','MMplugins')
    plugin_path = join(directory,'plugins')
    path.insert(0, plugin_path)

    if exists(f"{old_path}\\settings"):
        file0 = open(f"{old_path}\\settings",'r')
        read_data = file0.read()
        
        if read_data == "overwrite_warning=1":
            copy_plugins()

    if basename(__file__) != "plugin.py":
        print("PLUGIN WARNING: This plugin requires the name 'plugin'.")
        print("PLUGIN WARNING: Continuing may result in but not limited to the Following:")
        print("PLUGIN WARNING: 'Random ISZ & ISZ-ModMenu Crashing', 'Corrupted Insalls', and 'Performance Impacts'.")
        input("NOTICE: Please confirm you understand by pressing the 'Enter' Key.")
        input("NOTICE: Are you sure you want to continue? This will be your Last Warning.")

        
        with open(f'{old_path}\\settings','w') as file1:
            file1.write("overwrite_warning=1")
            file1.close()

    system('clear')
    copy_plugins()