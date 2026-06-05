import sys
from pathlib import Path

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView


class YouTubeMusicApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carpeta donde está el script
        base_dir = Path(__file__).resolve().parent

        # Icono de la aplicación
        icon_path = base_dir / "icon.png"

        self.setWindowTitle("YouTube Music")
        self.setWindowIcon(QIcon(str(icon_path)))
        self.resize(1400, 900)

        # Carpeta para guardar sesión, cookies y datos
        storage_path = Path.home() / ".config" / "YouTubeMusic"
        storage_path.mkdir(parents=True, exist_ok=True)

        # Perfil persistente
        profile = QWebEngineProfile("YouTubeMusic", self)
        profile.setPersistentStoragePath(str(storage_path))
        profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
        )

        # Página web con perfil persistente
        page = QWebEnginePage(profile, self)

        # Navegador
        self.browser = QWebEngineView()
        self.browser.setPage(page)
        self.browser.setUrl(QUrl("https://music.youtube.com"))

        self.setCentralWidget(self.browser)


def main():
    app = QApplication(sys.argv)

    window = YouTubeMusicApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
