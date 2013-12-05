from PySide import QtGui, QtCore

class cycleList(QtGui.QWidget):
    def __init__(self):
        super(cycleList, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        lo = QtGui.QHBoxLayout()
        self.setLayout(lo)
        
        entry = QtGui.QLineEdit()
        startFrameInfo = QtGui.QSpinBox()
        dash = QtGui.QLabel("-")
        endFrameInfo = QtGui.QSpinBox()
        expButton = QtGui.QPushButton("Export")
        
        lo.addWidget(entry)
        lo.addWidget(startFrameInfo)
        lo.addWidget(dash)
        lo.addWidget(endFrameInfo)
        lo.addWidget(expButton)
        

class animaCycleSplitter(QtGui.QWidget):
    def __init__(self):
        super(animaCycleSplitter, self).__init__()
        
        self.setGeometry(300, 300, 450, 65)
        self.setWindowTitle("Animation Cycle Splitter")
        self.initUI()
    
    def initUI(self):
        lo = QtGui.QVBoxLayout()
        self.setLayout(lo)
        
        #lw = QtGui.QListWidget()
        listObj = cycleList()
        #lw.addItem(listObj)
        expAllButton = QtGui.QPushButton("New Cycle")
        
        lo.addWidget(listObj)
        lo.addWidget(expAllButton)
        
        self.show()

win = animaCycleSplitter()