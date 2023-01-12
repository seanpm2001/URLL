import QtQuick 2.0
# Start of script
Item {
     id: urlListMenu
     width: 200; height: 1800; locked_height: 600; scrollable = true

     Rectangle {
         id: icon1
         width: 100; height: 100
         color: "red"
         file ".svg"
     }
     states: [
         State {
             name: "moved"
             PropertyChanges {
                 target: myRect
                 x: 50
                 y: 50
             }
         }
     ]
     MouseArea {
         anchors.fill: parent
         onClicked: myItem.state = 'moved'
     }
}
# Goal: a scrollable list of URL hyperlinks, with a generated image of the site Favicon next to each link. Customizable link div height

# File info
# File type: QML Source file (*.qml)
# File version: 1 (Tuesday, July 13th 2021 at 9:28 pm)
# Line count (including blank lines and compiler line): 36

# End of script
