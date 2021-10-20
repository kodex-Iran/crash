from firstWindowsUi import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from options import instaBotOptions
app = QtWidgets.QApplication([])


users = instaBotOptions.users_list()



print(__name__)
if __name__ == "__main__":
    import sys
    # app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_()) 