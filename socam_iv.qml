import QtQuick 1.0
import Qt.labs.folderlistmodel 1.0
 
ListView {
    id: view
    width: 854
    height: 480
    anchors.centerIn: parent
    model: FolderListModel {
        nameFilters: [ "*.JPG", "*.jpg", "*.png" ]
        folder: "~/shared/ConvertedMedia"
        sortField: FolderListModel.Name
    }
    delegate: Image {
        source: filePath
        width: view.width
        height: view.height
        smooth: true
    }
    snapMode: ListView.SnapToItem

}
