__author__ = 'didzis'

import sys
import os
import re
import requests
import subprocess
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, 
    QProgressBar, QFileDialog, QMessageBox
)
from bs4 import BeautifulSoup


class DownloaderTab(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Webpage URL Input
        self.url_label = QLabel("Enter Webpage URL:")
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        # Button to Scrape M3U8
        self.scrape_btn = QPushButton("Find M3U8 Link")
        self.scrape_btn.clicked.connect(self.scrape_m3u8_link)
        layout.addWidget(self.scrape_btn)

        # Display Found M3U8 URL
        self.found_m3u8_label = QLabel("M3U8 Link:")
        layout.addWidget(self.found_m3u8_label)

        self.m3u8_display = QLineEdit()
        self.m3u8_display.setReadOnly(True)
        layout.addWidget(self.m3u8_display)

        # Format Selection
        self.format_label = QLabel("Select Format:")
        layout.addWidget(self.format_label)

        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4", "MKV", "TS"])
        layout.addWidget(self.format_combo)

        # Download Button
        self.download_btn = QPushButton("Download Video")
        self.download_btn.clicked.connect(self.download_video)
        self.download_btn.setEnabled(False)  # Initially disabled
        layout.addWidget(self.download_btn)

        # Progress Bar
        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        # Status Label
        self.status = QLabel("")
        layout.addWidget(self.status)

        self.setLayout(layout)

    def scrape_m3u8_link(self):
        """Extracts M3U8 URL from the given webpage."""
        webpage_url = self.url_input.text().strip()
        if not webpage_url:
            self.status.setText("Please enter a valid webpage URL.")
            return

        try:
            response = requests.get(webpage_url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()  # Raise error for failed requests
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract M3U8 links from the page
            m3u8_links = re.findall(r'https?://[^\s"]+\.m3u8', response.text)
            if not m3u8_links:
                self.status.setText("No M3U8 link found.")
                return

            # Take the first found M3U8 URL
            old_m3u8_url = m3u8_links[0]

            # Rename the M3U8 file while keeping the path the same
            dir_path = os.path.dirname(old_m3u8_url)
            new_m3u8_url = f"{dir_path}/index-f4-v1-a1.m3u8"

            # Display the new M3U8 link
            self.m3u8_display.setText(new_m3u8_url)
            self.status.setText("M3U8 link found and renamed.")
            self.download_btn.setEnabled(True)  # Enable download button

        except requests.RequestException as e:
            self.status.setText(f"Error fetching webpage: {e}")

    def download_video(self):
        """Downloads video using yt-dlp."""
        m3u8_url = self.m3u8_display.text().strip()
        if not m3u8_url:
            self.status.setText("No M3U8 link found.")
            return

        # Prompt user for output filename
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Video As", "", "Video Files (*.mp4 *.mkv *.ts)")
        if not save_path:
            self.status.setText("Download cancelled.")
            return

        format_map = {"MP4": "mp4", "MKV": "mkv", "TS": "ts"}
        selected_format = format_map[self.format_combo.currentText()]

        # Ensure correct file extension
        if not save_path.endswith(f".{selected_format}"):
            save_path += f".{selected_format}"

        self.status.setText("Downloading...")
        self.progress.setValue(50)

        # yt-dlp command
        yt_dlp_cmd = f'yt-dlp -f "best" -o "{save_path}" "{m3u8_url}"'

        process = subprocess.run(yt_dlp_cmd, shell=True)

        if process.returncode == 0:
            self.status.setText("Download complete!")
            self.progress.setValue(100)
        else:
            self.status.setText("Error during download.")
            self.progress.setValue(0)
            QMessageBox.critical(self, "Download Failed", "An error occurred while downloading the video.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DownloaderTab()
    window.show()
    sys.exit(app.exec())
