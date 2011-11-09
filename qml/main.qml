import Qt 4.7
import com.nokia.meego 1.0

Page {
	orientationLock: PageOrientation.LockPortrait
	background: "#000"


	Text {
		text: "ja hej"
		color: "#000"
	}

	/*
	ListView {
		id: playerList
		width: 400
		height: 200

		model: listModel

		delegate: Component {
			Rectangle {
				width: playerList.width
				heihgt: 40
				color: ((index % 2 == 0) ? "#222" : "#111")
				Text {
					id: title
					elide: Text.ElideRight
					text: "model.player.name"
					color: "#fff"
					font.bold: true
					anchors.leftMargin: 10
					anchors.fill: parent
					verticalAlignment: Text.AlignVCenter
				}
				MouseArea {
					anchors.fill: parent
					onClicked: { controller.playerSelected(model.player) }
				}
			}
		}
	}
	*/
}
