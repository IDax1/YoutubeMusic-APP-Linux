import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage

class YouTubeMusicApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Music")
        self.resize(1400, 900)

        profile = QWebEngineProfile("YouTubeMusic", self)

        profile.setPersistentStoragePath(
            "/home/max/.config/YouTubeMusic"
        )

        profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
        )

        page = QWebEnginePage(profile, self)

        self.browser = QWebEngineView()
        self.browser.setPage(page)

        self.browser.setUrl(QUrl("https://music.youtube.com"))

        self.setCentralWidget(self.browser)

app = QApplication(sys.argv)

window = YouTubeMusicApp()
window.show()

sys.exit(app.exec())