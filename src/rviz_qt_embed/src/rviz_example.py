#! /usr/bin/env python3
import sys
import rospy
import rospkg
from rviz import bindings as rviz
#from python_qt_binding import QtGui, QtCore,QtWidgets
from PyQt5 import uic, QtGui, QtCore,QtWidgets
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseWithCovarianceStamped


class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MyWindow,self).__init__()
		uic.loadUi('/home/aashith/Documents/arm/src/rviz_qt_embed/ui/designer.ui',self)
		self.map_widget=MyViz()
		self.gridLayout.addWidget(self.map_widget)
		

class MyViz(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.frame = rviz.VisualizationFrame()
		self.frame.setSplashPath( "" )
		self.frame.initialize()
		reader = rviz.YamlConfigReader()
		config = rviz.Config()

		#reader.readFile( config, "/home/aashith/Documents/arm/src/rviz_qt_embed/rviz/arm3.rviz" )
		reader.readFile( config, "/home/aashith/Documents/arm/src/rviz_qt_embed/rviz/arm2.rviz" )
		self.frame.load( config )
				
		self.setWindowTitle( config.mapGetChild( "Title" ).getValue() )
		self.frame.setMenuBar( None )
		self.frame.setStatusBar( None )
		self.frame.setHideButtonVisibility( True )
		self.manager = self.frame.getManager()
		self.grid_display = self.manager.getRootDisplayGroup().getDisplayAt( 0 )
		layout = QtWidgets.QVBoxLayout()
		layout.addWidget( self.frame )
		self.setLayout( layout )

if __name__ == '__main__':
	rospy.init_node('talker')
	rospy.loginfo("Node initialised")
	app = QtWidgets.QApplication(sys.argv)
	myWindow = MyWindow()
	myWindow.show()
	app.exec_()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

