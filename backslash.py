from PyQt5.QtWidgets import QApplication, QLabel

lineList = [line.rstrip('\n') for line in open("Y:/Seagate_Backup_Plus_Drive/Playlists/holiday_1.m3u")]
outputList = open("Y:/Seagate_Backup_Plus_Drive/Playlists/holiday_1_output.m3u", 'w')

for i in lineList:
    j = i.replace (" ", "\ ")
    print(j)
    outputList.write(j+"\n")

outputList.close()
