# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mlock.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setEnabled(True)
        Main.resize(930, 788)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Main.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/guiResources/lock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setAutoFillBackground(False)
        Main.setStyleSheet("")
        Main.setSizeGripEnabled(False)
        Main.setModal(False)
        self.subLogo = QtWidgets.QLabel(Main)
        self.subLogo.setGeometry(QtCore.QRect(430, 60, 361, 41))
        self.subLogo.setAutoFillBackground(False)
        self.subLogo.setObjectName("subLogo")
        self.labelAuthor = QtWidgets.QLabel(Main)
        self.labelAuthor.setGeometry(QtCore.QRect(40, 60, 71, 21))
        self.labelAuthor.setObjectName("labelAuthor")
        self.entryTitle = QtWidgets.QLineEdit(Main)
        self.entryTitle.setGeometry(QtCore.QRect(120, 30, 261, 20))
        self.entryTitle.setStyleSheet("font: italic 12pt \"Arial\";")
        self.entryTitle.setObjectName("entryTitle")
        self.entryAuthor = QtWidgets.QLineEdit(Main)
        self.entryAuthor.setGeometry(QtCore.QRect(120, 60, 261, 20))
        self.entryAuthor.setStyleSheet("font: italic 12pt \"Arial\";")
        self.entryAuthor.setObjectName("entryAuthor")
        self.labelTitle = QtWidgets.QLabel(Main)
        self.labelTitle.setGeometry(QtCore.QRect(40, 30, 71, 21))
        self.labelTitle.setObjectName("labelTitle")
        self.entryProduct = QtWidgets.QLineEdit(Main)
        self.entryProduct.setGeometry(QtCore.QRect(120, 90, 261, 20))
        self.entryProduct.setStyleSheet("font: italic 12pt \"Arial\";")
        self.entryProduct.setObjectName("entryProduct")
        self.labelProduct = QtWidgets.QLabel(Main)
        self.labelProduct.setGeometry(QtCore.QRect(30, 90, 81, 21))
        self.labelProduct.setObjectName("labelProduct")
        self.logo = QtWidgets.QLabel(Main)
        self.logo.setGeometry(QtCore.QRect(431, 30, 361, 31))
        self.logo.setText("")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.mainWidget = QtWidgets.QTabWidget(Main)
        self.mainWidget.setEnabled(True)
        self.mainWidget.setGeometry(QtCore.QRect(40, 130, 761, 611))
        self.mainWidget.setStyleSheet("")
        self.mainWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mainWidget.setDocumentMode(False)
        self.mainWidget.setObjectName("mainWidget")
        self.tabInfo = QtWidgets.QWidget()
        self.tabInfo.setObjectName("tabInfo")
        self.boxProductType = QtWidgets.QGroupBox(self.tabInfo)
        self.boxProductType.setGeometry(QtCore.QRect(30, 20, 691, 101))
        self.boxProductType.setFlat(False)
        self.boxProductType.setCheckable(False)
        self.boxProductType.setObjectName("boxProductType")
        self.radioButton_6 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_6.setEnabled(False)
        self.radioButton_6.setGeometry(QtCore.QRect(540, 50, 91, 16))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_10 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_10.setEnabled(False)
        self.radioButton_10.setGeometry(QtCore.QRect(540, 30, 111, 16))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_7 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_7.setEnabled(False)
        self.radioButton_7.setGeometry(QtCore.QRect(160, 30, 111, 16))
        self.radioButton_7.setAcceptDrops(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_3 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_9 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_9.setEnabled(False)
        self.radioButton_9.setGeometry(QtCore.QRect(160, 70, 121, 16))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioSafe = QtWidgets.QRadioButton(self.boxProductType)
        self.radioSafe.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.radioSafe.setObjectName("radioSafe")
        self.radioButton_4 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setGeometry(QtCore.QRect(360, 30, 141, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_8 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_8.setEnabled(False)
        self.radioButton_8.setGeometry(QtCore.QRect(160, 50, 161, 16))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioPadlock = QtWidgets.QRadioButton(self.boxProductType)
        self.radioPadlock.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.radioPadlock.setObjectName("radioPadlock")
        self.radioButton_5 = QtWidgets.QRadioButton(self.boxProductType)
        self.radioButton_5.setEnabled(False)
        self.radioButton_5.setGeometry(QtCore.QRect(360, 50, 131, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.featPad = QtWidgets.QGroupBox(self.tabInfo)
        self.featPad.setGeometry(QtCore.QRect(30, 130, 691, 211))
        self.featPad.setVisible(False)
        self.featPad.setObjectName("featPad")
        self.chkLogo = QtWidgets.QCheckBox(self.featPad)
        self.chkLogo.setGeometry(QtCore.QRect(20, 140, 70, 17))
        self.chkLogo.setObjectName("chkLogo")
        self.chkCable = QtWidgets.QCheckBox(self.featPad)
        self.chkCable.setGeometry(QtCore.QRect(20, 80, 70, 17))
        self.chkCable.setObjectName("chkCable")
        self.chkOutdoor = QtWidgets.QCheckBox(self.featPad)
        self.chkOutdoor.setGeometry(QtCore.QRect(20, 100, 70, 17))
        self.chkOutdoor.setObjectName("chkOutdoor")
        self.chkDial = QtWidgets.QCheckBox(self.featPad)
        self.chkDial.setGeometry(QtCore.QRect(20, 40, 70, 17))
        self.chkDial.setObjectName("chkDial")
        self.chkElectronics = QtWidgets.QCheckBox(self.featPad)
        self.chkElectronics.setGeometry(QtCore.QRect(20, 120, 91, 17))
        self.chkElectronics.setObjectName("chkElectronics")
        self.chkShackle = QtWidgets.QCheckBox(self.featPad)
        self.chkShackle.setGeometry(QtCore.QRect(20, 60, 70, 17))
        self.chkShackle.setObjectName("chkShackle")
        self.chkKey = QtWidgets.QCheckBox(self.featPad)
        self.chkKey.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.chkKey.setTristate(False)
        self.chkKey.setObjectName("chkKey")
        self.featSafe = QtWidgets.QGroupBox(self.tabInfo)
        self.featSafe.setGeometry(QtCore.QRect(30, 130, 691, 211))
        self.featSafe.setVisible(False)
        self.featSafe.setObjectName("featSafe")
        self.chkSafeDoor = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeDoor.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.chkSafeDoor.setObjectName("chkSafeDoor")
        self.chkSafeCashBox = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeCashBox.setGeometry(QtCore.QRect(20, 40, 101, 17))
        self.chkSafeCashBox.setObjectName("chkSafeCashBox")
        self.chkSafeFireProof = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeFireProof.setGeometry(QtCore.QRect(20, 60, 121, 17))
        self.chkSafeFireProof.setObjectName("chkSafeFireProof")
        self.chkSafeWaterProof = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeWaterProof.setGeometry(QtCore.QRect(20, 80, 141, 17))
        self.chkSafeWaterProof.setObjectName("chkSafeWaterProof")
        self.chkSafeDial = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeDial.setGeometry(QtCore.QRect(20, 140, 70, 17))
        self.chkSafeDial.setObjectName("chkSafeDial")
        self.chkSafeElectronics = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeElectronics.setGeometry(QtCore.QRect(20, 120, 101, 17))
        self.chkSafeElectronics.setObjectName("chkSafeElectronics")
        self.chkSafeKey = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeKey.setGeometry(QtCore.QRect(20, 100, 70, 17))
        self.chkSafeKey.setObjectName("chkSafeKey")
        self.chkSafeShelf = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafeShelf.setGeometry(QtCore.QRect(20, 160, 70, 17))
        self.chkSafeShelf.setObjectName("chkSafeShelf")
        self.chkSafePowdercoated = QtWidgets.QCheckBox(self.featSafe)
        self.chkSafePowdercoated.setGeometry(QtCore.QRect(20, 180, 121, 17))
        self.chkSafePowdercoated.setObjectName("chkSafePowdercoated")
        self.groubDoorFeat = QtWidgets.QGroupBox(self.featSafe)
        self.groubDoorFeat.setEnabled(False)
        self.groubDoorFeat.setGeometry(QtCore.QRect(170, 20, 151, 91))
        self.groubDoorFeat.setFlat(True)
        self.groubDoorFeat.setObjectName("groubDoorFeat")
        self.chkSafeHandle = QtWidgets.QCheckBox(self.groubDoorFeat)
        self.chkSafeHandle.setGeometry(QtCore.QRect(30, 20, 70, 17))
        self.chkSafeHandle.setObjectName("chkSafeHandle")
        self.chkSafeVerticalHinge = QtWidgets.QCheckBox(self.groubDoorFeat)
        self.chkSafeVerticalHinge.setGeometry(QtCore.QRect(30, 60, 111, 21))
        self.chkSafeVerticalHinge.setObjectName("chkSafeVerticalHinge")
        self.chkSafePlastic = QtWidgets.QCheckBox(self.groubDoorFeat)
        self.chkSafePlastic.setEnabled(False)
        self.chkSafePlastic.setGeometry(QtCore.QRect(60, 40, 70, 17))
        self.chkSafePlastic.setObjectName("chkSafePlastic")
        self.groupElectronicsFeat = QtWidgets.QGroupBox(self.featSafe)
        self.groupElectronicsFeat.setEnabled(False)
        self.groupElectronicsFeat.setGeometry(QtCore.QRect(340, 20, 171, 131))
        self.groupElectronicsFeat.setFlat(True)
        self.groupElectronicsFeat.setObjectName("groupElectronicsFeat")
        self.chkSafeBatteries = QtWidgets.QCheckBox(self.groupElectronicsFeat)
        self.chkSafeBatteries.setGeometry(QtCore.QRect(30, 20, 70, 17))
        self.chkSafeBatteries.setObjectName("chkSafeBatteries")
        self.chkSafeSensors = QtWidgets.QCheckBox(self.groupElectronicsFeat)
        self.chkSafeSensors.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.chkSafeSensors.setObjectName("chkSafeSensors")
        self.chkSafeTemperature = QtWidgets.QCheckBox(self.groupElectronicsFeat)
        self.chkSafeTemperature.setEnabled(False)
        self.chkSafeTemperature.setGeometry(QtCore.QRect(60, 80, 101, 17))
        self.chkSafeTemperature.setObjectName("chkSafeTemperature")
        self.chkSafeHumidity = QtWidgets.QCheckBox(self.groupElectronicsFeat)
        self.chkSafeHumidity.setEnabled(False)
        self.chkSafeHumidity.setGeometry(QtCore.QRect(60, 100, 101, 17))
        self.chkSafeHumidity.setObjectName("chkSafeHumidity")
        self.chkSafeSolenoid = QtWidgets.QCheckBox(self.groupElectronicsFeat)
        self.chkSafeSolenoid.setGeometry(QtCore.QRect(30, 40, 91, 17))
        self.chkSafeSolenoid.setObjectName("chkSafeSolenoid")
        self.clearButton = QtWidgets.QPushButton(self.tabInfo)
        self.clearButton.setGeometry(QtCore.QRect(500, 530, 111, 41))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.clearButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.clearButton.setFont(font)
        self.clearButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clearButton.setStyleSheet("QPushButton {\n"
"   \n"
"    font: 87 9pt \"Arial Black\";\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4c4c4c, stop: 1 #363636);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #838383, stop: 1 #515151);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: gray; /* make the default button prominent */\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/guiResources/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setIconSize(QtCore.QSize(25, 25))
        self.clearButton.setAutoDefault(True)
        self.clearButton.setDefault(False)
        self.clearButton.setFlat(False)
        self.clearButton.setObjectName("clearButton")
        self.acceptButton = QtWidgets.QPushButton(self.tabInfo)
        self.acceptButton.setGeometry(QtCore.QRect(630, 530, 111, 41))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.acceptButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.acceptButton.setFont(font)
        self.acceptButton.setStyleSheet("QPushButton {\n"
"   \n"
"    font: 87 9pt \"Arial Black\";\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4c4c4c, stop: 1 #363636);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #838383, stop: 1 #515151);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: gray; /* make the default button prominent */\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/guiResources/okay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acceptButton.setIcon(icon2)
        self.acceptButton.setIconSize(QtCore.QSize(25, 25))
        self.acceptButton.setObjectName("acceptButton")
        self.mainWidget.addTab(self.tabInfo, "")
        self.tabTests = QtWidgets.QWidget()
        self.tabTests.setObjectName("tabTests")
        self.endDateBox = QtWidgets.QGroupBox(self.tabTests)
        self.endDateBox.setGeometry(QtCore.QRect(380, 20, 341, 231))
        self.endDateBox.setObjectName("endDateBox")
        self.endDate = QtWidgets.QCalendarWidget(self.endDateBox)
        self.endDate.setGeometry(QtCore.QRect(10, 20, 321, 201))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.endDate.setFont(font)
        self.endDate.setAutoFillBackground(True)
        self.endDate.setStyleSheet("/* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); }\n"
"QCalendarWidget QToolButton {\n"
"    height: 24px;\n"
"    width: 150px;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    icon-size:  27px, 27px;\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QCalendarWidget QMenu {\n"
"    width: 150px;\n"
"    left: 20px;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    background-color: rgb(100, 100, 100);\n"
"}\n"
"QCalendarWidget QSpinBox { \n"
"    width: 150px; \n"
"    font-size:24px; \n"
"    color: white; \n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"    selection-background-color: rgb(136, 136, 136);\n"
"    selection-color: rgb(255, 255, 255);\n"
"}\n"
"QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; }\n"
"QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;}\n"
"QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; }\n"
"QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; }\n"
" \n"
"/* header row */\n"
"QCalendarWidget QWidget { alternate-background-color: rgb(200, 200, 200); }\n"
" \n"
"/* normal days */\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"    font-size:12px;  \n"
"    color: rgb(0, 0, 0);  \n"
"    background-color: white;  \n"
"    selection-background-color: rgb(64, 64, 64); \n"
"    selection-color: rgb(0, 255, 0); \n"
"}\n"
" \n"
"/* days in other months */\n"
"QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")
        self.endDate.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.endDate.setGridVisible(False)
        self.endDate.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.endDate.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.endDate.setNavigationBarVisible(True)
        self.endDate.setDateEditEnabled(True)
        self.endDate.setObjectName("endDate")
        self.endDateBox_2 = QtWidgets.QGroupBox(self.tabTests)
        self.endDateBox_2.setGeometry(QtCore.QRect(30, 20, 341, 231))
        self.endDateBox_2.setObjectName("endDateBox_2")
        self.endDate_2 = QtWidgets.QCalendarWidget(self.endDateBox_2)
        self.endDate_2.setGeometry(QtCore.QRect(10, 20, 321, 201))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.endDate_2.setFont(font)
        self.endDate_2.setAutoFillBackground(True)
        self.endDate_2.setStyleSheet("/* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); }\n"
"QCalendarWidget QToolButton {\n"
"    height: 24px;\n"
"    width: 150px;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    icon-size:  27px, 27px;\n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QCalendarWidget QMenu {\n"
"    width: 150px;\n"
"    left: 20px;\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    background-color: rgb(100, 100, 100);\n"
"}\n"
"QCalendarWidget QSpinBox { \n"
"    width: 150px; \n"
"    font-size:24px; \n"
"    color: white; \n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"    selection-background-color: rgb(136, 136, 136);\n"
"    selection-color: rgb(255, 255, 255);\n"
"}\n"
"QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; }\n"
"QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;}\n"
"QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; }\n"
"QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; }\n"
" \n"
"/* header row */\n"
"QCalendarWidget QWidget { alternate-background-color: rgb(200, 200, 200); }\n"
" \n"
"/* normal days */\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"    font-size:12px;  \n"
"    color: rgb(0, 0, 0);  \n"
"    background-color: white;  \n"
"    selection-background-color: rgb(64, 64, 64); \n"
"    selection-color: rgb(0, 255, 0); \n"
"}\n"
" \n"
"/* days in other months */\n"
"QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")
        self.endDate_2.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.endDate_2.setGridVisible(False)
        self.endDate_2.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.endDate_2.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.endDate_2.setNavigationBarVisible(True)
        self.endDate_2.setDateEditEnabled(True)
        self.endDate_2.setObjectName("endDate_2")
        self.testWindow = QtWidgets.QGroupBox(self.tabTests)
        self.testWindow.setGeometry(QtCore.QRect(30, 260, 691, 291))
        self.testWindow.setObjectName("testWindow")
        self.listWidget = QtWidgets.QListWidget(self.testWindow)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 481, 261))
        self.listWidget.setStyleSheet("font: 11pt \"Arial\";")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.genReport = QtWidgets.QPushButton(self.testWindow)
        self.genReport.setGeometry(QtCore.QRect(510, 240, 161, 41))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.genReport.setPalette(palette)
        self.genReport.setStyleSheet("QPushButton {\n"
"   \n"
"    font: 87 9pt \"Arial Black\";\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4c4c4c, stop: 1 #363636);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #838383, stop: 1 #515151);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: gray; /* make the default button prominent */\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/guiResources/genRep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genReport.setIcon(icon3)
        self.genReport.setIconSize(QtCore.QSize(30, 30))
        self.genReport.setAutoRepeat(False)
        self.genReport.setAutoExclusive(False)
        self.genReport.setAutoDefault(True)
        self.genReport.setDefault(False)
        self.genReport.setFlat(False)
        self.genReport.setObjectName("genReport")
        self.genReport_2 = QtWidgets.QPushButton(self.testWindow)
        self.genReport_2.setGeometry(QtCore.QRect(510, 190, 161, 41))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 76, 76))
        gradient.setColorAt(1.0, QtGui.QColor(54, 54, 54))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.genReport_2.setPalette(palette)
        self.genReport_2.setStyleSheet("QPushButton {\n"
"   \n"
"    font: 87 9pt \"Arial Black\";\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4c4c4c, stop: 1 #363636);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #838383, stop: 1 #515151);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: gray; /* make the default button prominent */\n"
"}")
        self.genReport_2.setInputMethodHints(QtCore.Qt.ImhNone)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/guiResources/CSV.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genReport_2.setIcon(icon4)
        self.genReport_2.setIconSize(QtCore.QSize(30, 30))
        self.genReport_2.setObjectName("genReport_2")
        self.mainWidget.addTab(self.tabTests, "")
        self.tabHelp = QtWidgets.QWidget()
        self.tabHelp.setObjectName("tabHelp")
        self.label = QtWidgets.QLabel(self.tabHelp)
        self.label.setGeometry(QtCore.QRect(40, 40, 671, 501))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setObjectName("label")
        self.mainWidget.addTab(self.tabHelp, "")
        self.labelAuthor.setBuddy(self.entryAuthor)
        self.labelTitle.setBuddy(self.entryTitle)
        self.labelProduct.setBuddy(self.entryProduct)

        self.retranslateUi(Main)
        self.mainWidget.setCurrentIndex(0)
        self.radioPadlock.toggled['bool'].connect(self.featPad.setVisible)
        self.chkSafeHandle.clicked['bool'].connect(self.chkSafePlastic.setEnabled)
        self.radioSafe.toggled['bool'].connect(self.featSafe.setVisible)
        self.chkSafeDoor.clicked['bool'].connect(self.groubDoorFeat.setEnabled)
        self.chkSafeElectronics.clicked['bool'].connect(self.groupElectronicsFeat.setEnabled)
        self.chkSafeSensors.clicked['bool'].connect(self.chkSafeTemperature.setEnabled)
        self.chkSafeSensors.clicked['bool'].connect(self.chkSafeHumidity.setEnabled)
        self.clearButton.clicked['bool'].connect(self.chkSafeDoor.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeCashBox.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeFireProof.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeWaterProof.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeKey.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeDial.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeShelf.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafePowdercoated.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeHandle.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafePlastic.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeVerticalHinge.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeBatteries.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeSolenoid.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeSensors.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeTemperature.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeHumidity.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkSafeElectronics.setChecked)
        self.clearButton.clicked['bool'].connect(self.groubDoorFeat.setEnabled)
        self.clearButton.clicked['bool'].connect(self.groupElectronicsFeat.setEnabled)
        self.clearButton.clicked['bool'].connect(self.chkKey.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkDial.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkShackle.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkCable.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkOutdoor.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkElectronics.setChecked)
        self.clearButton.clicked['bool'].connect(self.chkLogo.setChecked)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "TestGen 0.1a"))
        self.subLogo.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">QA Testing Center<br/></span><span style=\" font-size:12pt;\">Test Plan Generator</span></p></body></html>"))
        self.labelAuthor.setText(_translate("Main", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; text-decoration: underline; color:#57575a;\">___Author</span></p><p align=\"right\"><span style=\" font-weight:600; color:#57575a;\"><br/></span></p></body></html>"))
        self.labelTitle.setText(_translate("Main", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; text-decoration: underline; color:#54575a;\">_____Title</span></p><p align=\"right\"><span style=\" font-weight:600; color:#54575a;\"><br/></span></p></body></html>"))
        self.labelProduct.setText(_translate("Main", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; text-decoration: underline; color:#57575a;\">__Product</span></p><p align=\"right\"><span style=\" font-weight:600; color:#57575a;\"><br/></span></p></body></html>"))
        self.boxProductType.setTitle(_translate("Main", "Product Type"))
        self.radioButton_6.setText(_translate("Main", "Bike Lock"))
        self.radioButton_10.setText(_translate("Main", "Access Control"))
        self.radioButton_7.setText(_translate("Main", "Luggage Lock"))
        self.radioButton_3.setText(_translate("Main", "LO/TO"))
        self.radioButton_9.setText(_translate("Main", "Trailer Reciever"))
        self.radioSafe.setText(_translate("Main", "Safe"))
        self.radioButton_4.setText(_translate("Main", "Built In Locker Lock"))
        self.radioButton_8.setText(_translate("Main", "Trailer Pin/Coupler Lock"))
        self.radioPadlock.setText(_translate("Main", "Padlock"))
        self.radioButton_5.setText(_translate("Main", "Built in Door Lock"))
        self.featPad.setTitle(_translate("Main", "Padlock Features"))
        self.chkLogo.setText(_translate("Main", "Logo"))
        self.chkCable.setText(_translate("Main", "Cable"))
        self.chkOutdoor.setText(_translate("Main", "Outdoor"))
        self.chkDial.setText(_translate("Main", "Dial."))
        self.chkElectronics.setText(_translate("Main", "Electronics"))
        self.chkShackle.setText(_translate("Main", "Shackle"))
        self.chkKey.setText(_translate("Main", "Key"))
        self.featSafe.setTitle(_translate("Main", "Safe Features"))
        self.chkSafeDoor.setText(_translate("Main", "Door"))
        self.chkSafeCashBox.setText(_translate("Main", "Cash Box"))
        self.chkSafeFireProof.setText(_translate("Main", "Fire Resistance"))
        self.chkSafeWaterProof.setText(_translate("Main", "Water Resistance"))
        self.chkSafeDial.setText(_translate("Main", "Dial"))
        self.chkSafeElectronics.setText(_translate("Main", "Electronics"))
        self.chkSafeKey.setText(_translate("Main", "Key"))
        self.chkSafeShelf.setText(_translate("Main", "Shelf"))
        self.chkSafePowdercoated.setText(_translate("Main", "Powdercoated"))
        self.groubDoorFeat.setTitle(_translate("Main", "Door Features"))
        self.chkSafeHandle.setText(_translate("Main", "Handle"))
        self.chkSafeVerticalHinge.setText(_translate("Main", "Vertical Hinge"))
        self.chkSafePlastic.setText(_translate("Main", "Plastic"))
        self.groupElectronicsFeat.setTitle(_translate("Main", "Electronics Detail"))
        self.chkSafeBatteries.setText(_translate("Main", "Batteries"))
        self.chkSafeSensors.setText(_translate("Main", "Sensors"))
        self.chkSafeTemperature.setText(_translate("Main", "Temperature"))
        self.chkSafeHumidity.setText(_translate("Main", "Humidity"))
        self.chkSafeSolenoid.setText(_translate("Main", "Solenoid"))
        self.clearButton.setText(_translate("Main", "Clear"))
        self.acceptButton.setText(_translate("Main", "Accept"))
        self.mainWidget.setTabText(self.mainWidget.indexOf(self.tabInfo), _translate("Main", "Product Info"))
        self.endDateBox.setTitle(_translate("Main", "End Date"))
        self.endDateBox_2.setTitle(_translate("Main", "Start Date"))
        self.testWindow.setTitle(_translate("Main", "Required Tests"))
        self.genReport.setText(_translate("Main", "Generate Report"))
        self.genReport_2.setText(_translate("Main", "Export to CSV"))
        self.mainWidget.setTabText(self.mainWidget.indexOf(self.tabTests), _translate("Main", "Testing Info"))
        self.mainWidget.setTabText(self.mainWidget.indexOf(self.tabHelp), _translate("Main", "Help"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

