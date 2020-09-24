
class FileListWidget(QListWidget):
    """这个列表控件可以拖入文件"""
    signal = pyqtSignal(list)

    def __init__(self, type, parent=None):
        super(FileListWidget, self).__init__(parent)
        self.setAcceptDrops(True)

    def enterEvent(self, a0: QEvent) -> None:
        mainWindow.status.showMessage(self.tr('双击列表项可以清空文件列表'))

    def leaveEvent(self, a0: QEvent) -> None:
        mainWindow.status.showMessage('')

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.signal.emit(links)
        else:
            event.ignore()
