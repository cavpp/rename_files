# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lpsdesk/PycharmProjects/rename_files/rename_files/gui_datafiles/rename.ui'
#
# Created: Wed Jul 22 17:14:21 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1024, 725)
        Form.setMinimumSize(QtCore.QSize(1024, 680))
        Form.setMaximumSize(QtCore.QSize(2024, 16777215))
        self.gridLayout_3 = QtGui.QGridLayout(Form)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frameBackground = QtGui.QFrame(Form)
        self.frameBackground.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameBackground.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBackground.setObjectName(_fromUtf8("frameBackground"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameBackground)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(-1, -1, 12, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frameTitle = QtGui.QFrame(self.frameBackground)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameTitle.sizePolicy().hasHeightForWidth())
        self.frameTitle.setSizePolicy(sizePolicy)
        self.frameTitle.setMinimumSize(QtCore.QSize(0, 50))
        self.frameTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameTitle.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameTitle.setFrameShadow(QtGui.QFrame.Raised)
        self.frameTitle.setObjectName(_fromUtf8("frameTitle"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frameTitle)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_title = QtGui.QLabel(self.frameTitle)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.verticalLayout_3.addWidget(self.label_title)
        self.verticalLayout_2.addWidget(self.frameTitle)
        self.frameSetup = QtGui.QFrame(self.frameBackground)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSetup.sizePolicy().hasHeightForWidth())
        self.frameSetup.setSizePolicy(sizePolicy)
        self.frameSetup.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameSetup.setFrameShadow(QtGui.QFrame.Plain)
        self.frameSetup.setObjectName(_fromUtf8("frameSetup"))
        self.gridLayout = QtGui.QGridLayout(self.frameSetup)
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_2 = QtGui.QFrame(self.frameSetup)
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineEdit_validStatus = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_validStatus.sizePolicy().hasHeightForWidth())
        self.lineEdit_validStatus.setSizePolicy(sizePolicy)
        self.lineEdit_validStatus.setReadOnly(True)
        self.lineEdit_validStatus.setObjectName(_fromUtf8("lineEdit_validStatus"))
        self.gridLayout_4.addWidget(self.lineEdit_validStatus, 4, 1, 1, 3)
        self.lineEdit_OID_startNum = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_OID_startNum.sizePolicy().hasHeightForWidth())
        self.lineEdit_OID_startNum.setSizePolicy(sizePolicy)
        self.lineEdit_OID_startNum.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_OID_startNum.setObjectName(_fromUtf8("lineEdit_OID_startNum"))
        self.gridLayout_4.addWidget(self.lineEdit_OID_startNum, 3, 3, 1, 1)
        self.lineEdit_PID_startNum = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_PID_startNum.sizePolicy().hasHeightForWidth())
        self.lineEdit_PID_startNum.setSizePolicy(sizePolicy)
        self.lineEdit_PID_startNum.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_PID_startNum.setObjectName(_fromUtf8("lineEdit_PID_startNum"))
        self.gridLayout_4.addWidget(self.lineEdit_PID_startNum, 2, 3, 1, 1)
        self.label_validStatus = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_validStatus.sizePolicy().hasHeightForWidth())
        self.label_validStatus.setSizePolicy(sizePolicy)
        self.label_validStatus.setObjectName(_fromUtf8("label_validStatus"))
        self.gridLayout_4.addWidget(self.label_validStatus, 4, 0, 1, 1)
        self.label_PID_startNum = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_PID_startNum.sizePolicy().hasHeightForWidth())
        self.label_PID_startNum.setSizePolicy(sizePolicy)
        self.label_PID_startNum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_PID_startNum.setObjectName(_fromUtf8("label_PID_startNum"))
        self.gridLayout_4.addWidget(self.label_PID_startNum, 2, 2, 1, 1)
        self.label_PID_prefix = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_PID_prefix.sizePolicy().hasHeightForWidth())
        self.label_PID_prefix.setSizePolicy(sizePolicy)
        self.label_PID_prefix.setObjectName(_fromUtf8("label_PID_prefix"))
        self.gridLayout_4.addWidget(self.label_PID_prefix, 2, 0, 1, 1)
        self.lineEdit_PID_prefix = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_PID_prefix.sizePolicy().hasHeightForWidth())
        self.lineEdit_PID_prefix.setSizePolicy(sizePolicy)
        self.lineEdit_PID_prefix.setObjectName(_fromUtf8("lineEdit_PID_prefix"))
        self.gridLayout_4.addWidget(self.lineEdit_PID_prefix, 2, 1, 1, 1)
        self.label_OID_startNum = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_OID_startNum.sizePolicy().hasHeightForWidth())
        self.label_OID_startNum.setSizePolicy(sizePolicy)
        self.label_OID_startNum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_OID_startNum.setObjectName(_fromUtf8("label_OID_startNum"))
        self.gridLayout_4.addWidget(self.label_OID_startNum, 3, 2, 1, 1)
        self.pushButton_sourceBrowse = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sourceBrowse.sizePolicy().hasHeightForWidth())
        self.pushButton_sourceBrowse.setSizePolicy(sizePolicy)
        self.pushButton_sourceBrowse.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_sourceBrowse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_sourceBrowse.setAutoFillBackground(False)
        self.pushButton_sourceBrowse.setCheckable(False)
        self.pushButton_sourceBrowse.setChecked(False)
        self.pushButton_sourceBrowse.setObjectName(_fromUtf8("pushButton_sourceBrowse"))
        self.gridLayout_4.addWidget(self.pushButton_sourceBrowse, 0, 6, 1, 1)
        self.lineEdit_OID_MARC = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_OID_MARC.sizePolicy().hasHeightForWidth())
        self.lineEdit_OID_MARC.setSizePolicy(sizePolicy)
        self.lineEdit_OID_MARC.setObjectName(_fromUtf8("lineEdit_OID_MARC"))
        self.gridLayout_4.addWidget(self.lineEdit_OID_MARC, 3, 1, 1, 1)
        self.lbl_searchType = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_searchType.sizePolicy().hasHeightForWidth())
        self.lbl_searchType.setSizePolicy(sizePolicy)
        self.lbl_searchType.setObjectName(_fromUtf8("lbl_searchType"))
        self.gridLayout_4.addWidget(self.lbl_searchType, 4, 5, 1, 1)
        self.cb_searchType = QtGui.QComboBox(self.frame_2)
        self.cb_searchType.setObjectName(_fromUtf8("cb_searchType"))
        self.cb_searchType.addItem(_fromUtf8(""))
        self.cb_searchType.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.cb_searchType, 4, 6, 1, 1)
        self.pushButton_load_filles = QtGui.QPushButton(self.frame_2)
        self.pushButton_load_filles.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load_filles.sizePolicy().hasHeightForWidth())
        self.pushButton_load_filles.setSizePolicy(sizePolicy)
        self.pushButton_load_filles.setObjectName(_fromUtf8("pushButton_load_filles"))
        self.gridLayout_4.addWidget(self.pushButton_load_filles, 6, 6, 1, 1)
        self.label_OID_MARC = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_OID_MARC.sizePolicy().hasHeightForWidth())
        self.label_OID_MARC.setSizePolicy(sizePolicy)
        self.label_OID_MARC.setObjectName(_fromUtf8("label_OID_MARC"))
        self.gridLayout_4.addWidget(self.label_OID_MARC, 3, 0, 1, 1)
        self.pushButton_destinationBrowse = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_destinationBrowse.sizePolicy().hasHeightForWidth())
        self.pushButton_destinationBrowse.setSizePolicy(sizePolicy)
        self.pushButton_destinationBrowse.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_destinationBrowse.setObjectName(_fromUtf8("pushButton_destinationBrowse"))
        self.gridLayout_4.addWidget(self.pushButton_destinationBrowse, 1, 6, 1, 1)
        self.lineEdit_source = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_source.setObjectName(_fromUtf8("lineEdit_source"))
        self.gridLayout_4.addWidget(self.lineEdit_source, 0, 1, 1, 5)
        self.lineEdit_destination = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_destination.setObjectName(_fromUtf8("lineEdit_destination"))
        self.gridLayout_4.addWidget(self.lineEdit_destination, 1, 1, 1, 5)
        self.label_destination = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_destination.sizePolicy().hasHeightForWidth())
        self.label_destination.setSizePolicy(sizePolicy)
        self.label_destination.setObjectName(_fromUtf8("label_destination"))
        self.gridLayout_4.addWidget(self.label_destination, 1, 0, 1, 1)
        self.label_source = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_source.sizePolicy().hasHeightForWidth())
        self.label_source.setSizePolicy(sizePolicy)
        self.label_source.setObjectName(_fromUtf8("label_source"))
        self.gridLayout_4.addWidget(self.label_source, 0, 0, 1, 1)
        self.pushButton_add_complex = QtGui.QPushButton(self.frame_2)
        self.pushButton_add_complex.setObjectName(_fromUtf8("pushButton_add_complex"))
        self.gridLayout_4.addWidget(self.pushButton_add_complex, 7, 6, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 4)
        self.verticalLayout_2.addWidget(self.frameSetup)
        self.frameFiles = QtGui.QFrame(self.frameBackground)
        self.frameFiles.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameFiles.setFrameShadow(QtGui.QFrame.Raised)
        self.frameFiles.setObjectName(_fromUtf8("frameFiles"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frameFiles)
        self.horizontalLayout_2.setContentsMargins(12, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame_3 = QtGui.QFrame(self.frameFiles)
        self.frame_3.setFrameShape(QtGui.QFrame.Panel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_5.setMargin(8)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_group = QtGui.QPushButton(self.frame_4)
        self.pushButton_group.setEnabled(False)
        self.pushButton_group.setAutoFillBackground(False)
        self.pushButton_group.setFlat(False)
        self.pushButton_group.setObjectName(_fromUtf8("pushButton_group"))
        self.gridLayout_2.addWidget(self.pushButton_group, 3, 1, 1, 1)
        self.pushButton_include = QtGui.QPushButton(self.frame_4)
        self.pushButton_include.setEnabled(False)
        self.pushButton_include.setObjectName(_fromUtf8("pushButton_include"))
        self.gridLayout_2.addWidget(self.pushButton_include, 3, 2, 1, 1)
        self.pushButton_update = QtGui.QPushButton(self.frame_4)
        self.pushButton_update.setObjectName(_fromUtf8("pushButton_update"))
        self.gridLayout_2.addWidget(self.pushButton_update, 3, 5, 1, 1)
        self.checkBox_preview = QtGui.QCheckBox(self.frame_4)
        self.checkBox_preview.setMaximumSize(QtCore.QSize(150, 16777215))
        self.checkBox_preview.setChecked(True)
        self.checkBox_preview.setObjectName(_fromUtf8("checkBox_preview"))
        self.gridLayout_2.addWidget(self.checkBox_preview, 3, 6, 1, 1)
        self.frame_preview = QtGui.QFrame(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_preview.sizePolicy().hasHeightForWidth())
        self.frame_preview.setSizePolicy(sizePolicy)
        self.frame_preview.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_preview.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_preview.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_preview.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_preview.setObjectName(_fromUtf8("frame_preview"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_preview)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(self.frame_preview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 9999999))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_5 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setMargin(2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.preview_image = QtGui.QLabel(self.frame_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_image.sizePolicy().hasHeightForWidth())
        self.preview_image.setSizePolicy(sizePolicy)
        self.preview_image.setMinimumSize(QtCore.QSize(150, 0))
        self.preview_image.setText(_fromUtf8(""))
        self.preview_image.setObjectName(_fromUtf8("preview_image"))
        self.verticalLayout_5.addWidget(self.preview_image)
        self.verticalLayout.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_7 = QtGui.QFrame(self.frame_preview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lbl_fileName = QtGui.QLabel(self.frame_7)
        self.lbl_fileName.setObjectName(_fromUtf8("lbl_fileName"))
        self.gridLayout_6.addWidget(self.lbl_fileName, 0, 0, 1, 1)
        self.le_fileName = QtGui.QLineEdit(self.frame_7)
        self.le_fileName.setReadOnly(True)
        self.le_fileName.setObjectName(_fromUtf8("le_fileName"))
        self.gridLayout_6.addWidget(self.le_fileName, 0, 1, 1, 1)
        self.lbl_fileSize = QtGui.QLabel(self.frame_7)
        self.lbl_fileSize.setObjectName(_fromUtf8("lbl_fileSize"))
        self.gridLayout_6.addWidget(self.lbl_fileSize, 1, 0, 1, 1)
        self.le_fileSize = QtGui.QLineEdit(self.frame_7)
        self.le_fileSize.setEnabled(True)
        self.le_fileSize.setReadOnly(True)
        self.le_fileSize.setObjectName(_fromUtf8("le_fileSize"))
        self.gridLayout_6.addWidget(self.le_fileSize, 1, 1, 1, 1)
        self.lbl_resolution = QtGui.QLabel(self.frame_7)
        self.lbl_resolution.setObjectName(_fromUtf8("lbl_resolution"))
        self.gridLayout_6.addWidget(self.lbl_resolution, 2, 0, 1, 1)
        self.le_resolution = QtGui.QLineEdit(self.frame_7)
        self.le_resolution.setReadOnly(True)
        self.le_resolution.setObjectName(_fromUtf8("le_resolution"))
        self.gridLayout_6.addWidget(self.le_resolution, 2, 1, 1, 1)
        self.lbl_colorDepth = QtGui.QLabel(self.frame_7)
        self.lbl_colorDepth.setObjectName(_fromUtf8("lbl_colorDepth"))
        self.gridLayout_6.addWidget(self.lbl_colorDepth, 3, 0, 1, 1)
        self.le_color = QtGui.QLineEdit(self.frame_7)
        self.le_color.setReadOnly(True)
        self.le_color.setObjectName(_fromUtf8("le_color"))
        self.gridLayout_6.addWidget(self.le_color, 3, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.gridLayout_2.addWidget(self.frame_preview, 2, 8, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 3, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tree_files = QtGui.QTreeWidget(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_files.sizePolicy().hasHeightForWidth())
        self.tree_files.setSizePolicy(sizePolicy)
        self.tree_files.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tree_files.setObjectName(_fromUtf8("tree_files"))
        self.tree_files.header().setVisible(True)
        self.horizontalLayout_5.addWidget(self.tree_files)
        self.tree_filesView = QtGui.QTreeView(self.frame_4)
        self.tree_filesView.setObjectName(_fromUtf8("tree_filesView"))
        self.horizontalLayout_5.addWidget(self.tree_filesView)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 1, 1, 6)
        self.gridLayout_5.addWidget(self.frame_4, 0, 1, 1, 8)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frameFiles)
        self.frameActions = QtGui.QFrame(self.frameBackground)
        self.frameActions.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameActions.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameActions.setFrameShadow(QtGui.QFrame.Plain)
        self.frameActions.setObjectName(_fromUtf8("frameActions"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frameActions)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.checkBox_IncludeReport = QtGui.QCheckBox(self.frameActions)
        self.checkBox_IncludeReport.setEnabled(True)
        self.checkBox_IncludeReport.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_IncludeReport.setChecked(True)
        self.checkBox_IncludeReport.setObjectName(_fromUtf8("checkBox_IncludeReport"))
        self.horizontalLayout.addWidget(self.checkBox_IncludeReport)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonRename = QtGui.QPushButton(self.frameActions)
        self.buttonRename.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRename.sizePolicy().hasHeightForWidth())
        self.buttonRename.setSizePolicy(sizePolicy)
        self.buttonRename.setMinimumSize(QtCore.QSize(150, 0))
        self.buttonRename.setMaximumSize(QtCore.QSize(400, 16777215))
        self.buttonRename.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonRename.setObjectName(_fromUtf8("buttonRename"))
        self.horizontalLayout.addWidget(self.buttonRename)
        self.verticalLayout_2.addWidget(self.frameActions)
        self.frame_6 = QtGui.QFrame(self.frameBackground)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.progressBar = QtGui.QProgressBar(self.frame_6)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.gridLayout_3.addWidget(self.frameBackground, 0, 0, 1, 1)
        self.label_validStatus.setBuddy(self.lineEdit_validStatus)
        self.label_PID_startNum.setBuddy(self.lineEdit_PID_startNum)
        self.label_PID_prefix.setBuddy(self.lineEdit_PID_prefix)
        self.label_OID_startNum.setBuddy(self.lineEdit_OID_startNum)
        self.lbl_searchType.setBuddy(self.cb_searchType)
        self.label_OID_MARC.setBuddy(self.lineEdit_OID_MARC)
        self.label_destination.setBuddy(self.lineEdit_destination)
        self.label_source.setBuddy(self.lineEdit_source)
        self.lbl_fileName.setBuddy(self.le_fileName)
        self.lbl_fileSize.setBuddy(self.le_fileSize)
        self.lbl_resolution.setBuddy(self.le_resolution)
        self.lbl_colorDepth.setBuddy(self.le_color)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_source, self.lineEdit_destination)
        Form.setTabOrder(self.lineEdit_destination, self.lineEdit_PID_prefix)
        Form.setTabOrder(self.lineEdit_PID_prefix, self.lineEdit_PID_startNum)
        Form.setTabOrder(self.lineEdit_PID_startNum, self.lineEdit_OID_MARC)
        Form.setTabOrder(self.lineEdit_OID_MARC, self.lineEdit_OID_startNum)
        Form.setTabOrder(self.lineEdit_OID_startNum, self.lineEdit_validStatus)
        Form.setTabOrder(self.lineEdit_validStatus, self.cb_searchType)
        Form.setTabOrder(self.cb_searchType, self.pushButton_load_filles)
        Form.setTabOrder(self.pushButton_load_filles, self.pushButton_group)
        Form.setTabOrder(self.pushButton_group, self.pushButton_include)
        Form.setTabOrder(self.pushButton_include, self.checkBox_preview)
        Form.setTabOrder(self.checkBox_preview, self.checkBox_IncludeReport)
        Form.setTabOrder(self.checkBox_IncludeReport, self.buttonRename)
        Form.setTabOrder(self.buttonRename, self.le_resolution)
        Form.setTabOrder(self.le_resolution, self.le_color)
        Form.setTabOrder(self.le_color, self.le_fileName)
        Form.setTabOrder(self.le_fileName, self.le_fileSize)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "CAPS Renaming Script", None))
        self.label_title.setText(_translate("Form", "CAPS Image Renaming and Conversion Script", None))
        self.lineEdit_OID_startNum.setText(_translate("Form", "1", None))
        self.lineEdit_PID_startNum.setText(_translate("Form", "1", None))
        self.label_validStatus.setText(_translate("Form", "Status:", None))
        self.label_PID_startNum.setText(_translate("Form", "Start Number:", None))
        self.label_PID_prefix.setText(_translate("Form", "Project ID Prefix:", None))
        self.lineEdit_PID_prefix.setText(_translate("Form", "caps", None))
        self.label_OID_startNum.setText(_translate("Form", "Start Number:", None))
        self.pushButton_sourceBrowse.setText(_translate("Form", "Browse", None))
        self.lbl_searchType.setText(_translate("Form", "Search type", None))
        self.cb_searchType.setItemText(0, _translate("Form", "Smart", None))
        self.cb_searchType.setItemText(1, _translate("Form", "All", None))
        self.pushButton_load_filles.setText(_translate("Form", "Load Files", None))
        self.label_OID_MARC.setText(_translate("Form", "Object ID MARC:", None))
        self.pushButton_destinationBrowse.setText(_translate("Form", "Browse", None))
        self.label_destination.setText(_translate("Form", "Destination:", None))
        self.label_source.setText(_translate("Form", "Source:", None))
        self.pushButton_add_complex.setText(_translate("Form", "Add Complex Object", None))
        self.pushButton_group.setText(_translate("Form", "Group/Ungroup", None))
        self.pushButton_include.setText(_translate("Form", "Include/Exclude", None))
        self.pushButton_update.setText(_translate("Form", "Update", None))
        self.checkBox_preview.setText(_translate("Form", "Preview", None))
        self.lbl_fileName.setText(_translate("Form", "File Name", None))
        self.lbl_fileSize.setText(_translate("Form", "File Size", None))
        self.lbl_resolution.setText(_translate("Form", "Resolution", None))
        self.lbl_colorDepth.setText(_translate("Form", "Color", None))
        self.tree_files.headerItem().setText(0, _translate("Form", "#", None))
        self.tree_files.headerItem().setText(1, _translate("Form", "queueNumber", None))
        self.tree_files.headerItem().setText(2, _translate("Form", "fileNumber", None))
        self.tree_files.headerItem().setText(3, _translate("Form", "Project ID", None))
        self.tree_files.headerItem().setText(4, _translate("Form", "Simple/Complex", None))
        self.tree_files.headerItem().setText(5, _translate("Form", "Original Name", None))
        self.tree_files.headerItem().setText(6, _translate("Form", "New Name", None))
        self.tree_files.headerItem().setText(7, _translate("Form", "Included/Excluded", None))
        self.tree_files.headerItem().setText(8, _translate("Form", "Status", None))
        self.checkBox_IncludeReport.setText(_translate("Form", "Include Report", None))
        self.buttonRename.setText(_translate("Form", "Rename", None))

