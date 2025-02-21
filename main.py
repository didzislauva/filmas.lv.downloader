__author__ = 'didzis'
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from downloader_tab import DownloaderTab

class M3U8DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("M3U8 Video Downloader")
        self.setGeometry(100, 100, 600, 250)

        # Create Tab Widget
        self.tabs = QTabWidget(self)

        # Create downloader tab
        self.downloader_tab = DownloaderTab()
        self.tabs.addTab(self.downloader_tab, "Download M3U8")

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = M3U8DownloaderApp()
    window.show()
    sys.exit(app.exec())
