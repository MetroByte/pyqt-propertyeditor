from PySide6 import QtWidgets

from PropertyModel import PropertyModel
from TypeDelegate import TypeDelegate


class PropertyEditorWidget(QtWidgets.QTreeView):
    """ Subclassed QTreeView that displays property name & value in tidy manner."""

    def __init__(self, parent=None):
        super(PropertyEditorWidget, self).__init__(parent)
        self._model = PropertyModel(self)
        self.setModel(self._model)
        self.setItemDelegate(TypeDelegate(self))

    def addObject(self, propertyObject):
        self._model.add_property_object(propertyObject)
        self.expandToDepth(0)

    def setObject(self, propertyObject):
        self._model.clear()
        if propertyObject:
            self._model.addItem(propertyObject)
        self.expandToDepth(0)
