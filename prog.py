import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mlock import Ui_Main

class MyFirstGuiProgram(Ui_Main):
    from checks import checkBoxChecker
    from cleaner import listCleaner
    from csvGen import csvGen
    from reportGen import reportGen
    def __init__(self, dialog):
        Ui_Main.__init__(self)
        self.setupUi(dialog)
        self.acceptButton.clicked.connect(self.checkBoxChecker)
        self.clearButton.clicked.connect(self.listCleaner)
        self.genReport_2.clicked.connect(self.csvGen)
        self.genReport.clicked.connect(self.reportGen)
                        
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = MyFirstGuiProgram(dialog)

	dialog.show()
	sys.exit(app.exec_())
