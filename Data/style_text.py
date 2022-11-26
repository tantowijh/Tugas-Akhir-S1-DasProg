
def ascii_style(The_Text, The_Style, The_App):
    import os
    while True:
        try: import pyfiglet; break
        except: os.system("python3 -m pip install pyfiglet &> /dev/null")
    with open(The_App + '.txt', 'w') as f:
        text = pyfiglet.figlet_format(The_Text, font = The_Style)
        text = text.rstrip()
        f.write(text)
    with open(The_App + '.txt', 'r') as f:
        for line in f: 
            line = line.rstrip() + "\t"
            print(line.center(72))
    
    os.system("python3 -m pip uninstall pyfiglet -y &> /dev/null")

ascii_style("APOTEK G3", "standard", "app")
