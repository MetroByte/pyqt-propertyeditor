from PySide6.QtCore import QObject


class TestClass(QObject):

    def __init__(self, parent=None):
        super(TestClass, self).__init__(parent)
        self.name = 'Czesc'
        self.number = 4
        self.radius = 0.00
        self._id = 5
        self.test = True
