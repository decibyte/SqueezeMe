#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *
from PySide.QtOpenGL import *

class PlayerWrapper(QObject):
	def __init__(self, player):
		QObject.__init__(self)
		self.player = player
	
	def _name(self):
		return self.player.name

	changed = Signal()

	name = Property(unicode, _name, notify=changed)

class PlayerListModel(QAbstractListModel):
	COLUMNS = ('player',)

	def __init__(self, players):
		QAbstractListModel.__init__(self)
		self.players = players
		self.setRoleNames(dict(enumerate(PlayerListModel.COLUMNS)))
	
	def rowCount(self, parent=QModelIndex()):
		return len(self.players)

	def data(self, index, role):
		if index.isValid() and role == PlayerListModel.COLUMNS.index('player'):
			return self.players[index.row()]
		return None

class Controller(QObject):
	@Slot(QObject)
	def playerSelected(self, wrapper):
		print 'player selected: ', wrapper.player.name

class Player(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Player:', self.name

players = [PlayerWrapper(player) for player in [
	Player('northern'),
	Player('suothern'),
	Player('radio'),
]]

app = QApplication(sys.argv)
m = QMainWindow()
view = QDeclarativeView()
glw = QGLWidget()
view.setViewport(glw)
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

controller = Controller()
player_list = PlayerListModel(players)
rc = view.rootContext()
rc.setContextProperty('controller', controller)
rc.setContextProperty('listModel', player_list)

view.setSource('qml/main.qml')
m.setCentralWidget(view)
m.show()

app.exec_()
