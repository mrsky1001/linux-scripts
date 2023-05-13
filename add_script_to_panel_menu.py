import sys
from time import sleep
log="/home/mrsky1001/devel/github/linux-scripts/add_script_to_panel_menu.log"

# with open(log, "a") as f:
#     f.write(sys.argv.__str__())

folderApps="/usr/share/applications/"
pathScript = sys.argv[1]
fileNameScript = sys.argv[2].split('.')[0]
pathToIconScript = sys.argv[1].split('.sh')[0]+".png"

# with open(log, "a") as f:
#     f.write(pathScript)
#     f.write(fileNameScript)
#     f.write(pathToIconScript)

bodyItemMenu="""
[Desktop Entry]
Name="""+fileNameScript+""" 
GenericName=Program
Comment=Program
Exec="""+pathScript+"""
Terminal=false
Type=Application
Icon="""+pathToIconScript+"""
Categories=Other
Keywords="""+fileNameScript+"""
"""

# with open(log, "a") as f:
#     f.write(bodyItemMenu)
#     f.write(folderApps+fileNameScript+'.desktop')

with open(folderApps+fileNameScript+'.desktop', "w") as f:
    long_description = f.write(bodyItemMenu)
