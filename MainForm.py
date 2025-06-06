# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1568, 1077)
        self.centralwidget = QtWidgets.QWidget(parent=MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1568, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInput = QtWidgets.QMenu(parent=self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuAnalyze = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainForm)
        self.toolBar.setObjectName("toolBar")
        MainForm.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(parent=MainForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionPoint_Polygon = QtGui.QAction(parent=MainForm)
        self.actionPoint_Polygon.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/pointpol.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPoint_Polygon.setIcon(icon2)
        self.actionPoint_Polygon.setObjectName("actionPoint_Polygon")
        self.actionClear_results = QtGui.QAction(parent=MainForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_results.setIcon(icon3)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionClear_all = QtGui.QAction(parent=MainForm)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/clear_all.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_all.setIcon(icon4)
        self.actionClear_all.setObjectName("actionClear_all")
        self.actionWinding_number = QtGui.QAction(parent=MainForm)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/winding.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWinding_number.setIcon(icon5)
        self.actionWinding_number.setObjectName("actionWinding_number")
        self.actionRay_crossing = QtGui.QAction(parent=MainForm)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icons/ray.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRay_crossing.setIcon(icon6)
        self.actionRay_crossing.setObjectName("actionRay_crossing")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuInput.addAction(self.actionPoint_Polygon)
        self.menuInput.addSeparator()
        self.menuInput.addAction(self.actionClear_results)
        self.menuInput.addAction(self.actionClear_all)
        self.menuAnalyze.addAction(self.actionWinding_number)
        self.menuAnalyze.addAction(self.actionRay_crossing)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPoint_Polygon)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionWinding_number)
        self.toolBar.addAction(self.actionRay_crossing)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_results)
        self.toolBar.addAction(self.actionClear_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        
        # Connect components and slots
        self.actionOpen.triggered.connect(self.openClick)
        self.actionExit.triggered.connect(self.exitClick)
        self.actionRay_crossing.triggered.connect(self.rayCrossingClick)
        self.actionWinding_number.triggered.connect(self.windingNumberClick)
        self.actionPoint_Polygon.triggered.connect(self.switchClick)
        self.actionClear_all.triggered.connect(self.clearAllClick)
        self.actionClear_results.triggered.connect(self.clearClick)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Analyze point and polygon position"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuInput.setTitle(_translate("MainForm", "Input"))
        self.menuAnalyze.setTitle(_translate("MainForm", "Analyze"))
        self.toolBar.setWindowTitle(_translate("MainForm", "toolBar"))
        self.actionOpen.setText(_translate("MainForm", "Open"))
        self.actionOpen.setToolTip(_translate("MainForm", "Open file"))
        self.actionExit.setText(_translate("MainForm", "Exit"))
        self.actionExit.setToolTip(_translate("MainForm", "Close application"))
        self.actionPoint_Polygon.setText(_translate("MainForm", "Point/Polygon"))
        self.actionPoint_Polygon.setToolTip(_translate("MainForm", "Input point or polygon vertex"))
        self.actionClear_results.setText(_translate("MainForm", "Clear results"))
        self.actionClear_all.setText(_translate("MainForm", "Clear all"))
        self.actionClear_all.setToolTip(_translate("MainForm", "Clear all data"))
        self.actionWinding_number.setText(_translate("MainForm", "Winding number"))
        self.actionWinding_number.setToolTip(_translate("MainForm", "Winding number algorithm"))
        self.actionRay_crossing.setText(_translate("MainForm", "Ray crossing"))
        self.actionRay_crossing.setToolTip(_translate("MainForm", "Ray crossing algorithm"))

    def openClick(self):
        self.Canvas.openFile()
        
    def exitClick(self):
        self.Canvas.exit()
        
    def clearAllClick(self):
        self.Canvas.clearAll()
        
    def clearClick(self):
        self.Canvas.clearRes()
   
        
    def getRes(self,method):
        """
        Analyze point and polygon position
        """
        
        # Get input data
        q = self.Canvas.getQ()
        a = Algorithms()
        result = 0
        num_pols = 0
        for pol in self.Canvas.getPol():
            # Analyze position
            in_bb = a.in_min_max_box(q, pol)
            if in_bb == 0:
                continue
            
            if method == "rc":
                result = a.ray_crossing(q, pol)                
            if method == "wn":
                result = a.winding_number(q, pol)
                
            if result == -1:
                self.Canvas.paintRes(pol)
                num_pols += 1
            if result == 1:
                self.Canvas.paintRes(pol) 
                break    
    
        # Show results
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle('Analyze point and polygon position')
        
        # Point q inside pol
        if result == 1:
            dialog.setText('The point is inside one of the polygons.')
        
        # Point q outside pol
        elif result == 0:
            dialog.setText('The point is outside all polygons.')
            
        # Point q between pol
        elif result == -1 and num_pols == 1:
            dialog.setText("The point is on the boundary of a polygon.")
            
        elif result == -1:
            dialog.setText(f"The point is shared by {num_pols} polygons.")

        # Show dialog
        dialog.exec()
        
    def windingNumberClick(self):
        # Use winding number algorithm to analyze point and polygon position
        self.getRes("wn")
        
    def rayCrossingClick(self):
        # Use ray crossing algorithm to analyze point and polygon position
        self.getRes("rc")
        
            
    def switchClick(self):
        """
        Switch source, point or polygon
        """
        ui.Canvas.switchInput()
        
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())