# M3U8 Video Downloader

**Author:** Didzis  

## Overview

**M3U8 Video Downloader** is a user-friendly desktop application built with Python and PyQt6 that allows users to effortlessly extract and download videos from webpages containing `.m3u8` streaming URLs. Utilizing powerful tools like `requests`, `BeautifulSoup`, and `yt-dlp`, the app simplifies video downloading into just a few clicks.

## Features

- **Intuitive GUI**: Simple and clean interface built with PyQt6.
- **Automatic M3U8 Extraction**: Enter a webpage URL, and the app automatically locates and retrieves the `.m3u8` link.
- **Format Selection**: Supports downloading in MP4, MKV, or TS formats.
- **Progress Tracking**: Built-in progress bar and status updates.
- **Easy Save Options**: Choose the destination and filename for the downloaded video.

## Requirements

- Python 3.7 or higher
- PyQt6
- requests
- BeautifulSoup4
- yt-dlp

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/didzislauva/filmas.lv.downloader.git
cd filmas.lv.downloader
```

2. **Install dependencies**:

```bash
pip install PyQt6 requests beautifulsoup4 yt-dlp
```

## Usage

1. **Launch the Application**:

```bash
python main.py
```

2. **Download Video**:
   - Enter the URL of the webpage containing the video.
   - Click "Find M3U8 Link".
   - Select the desired video format (MP4, MKV, TS).
   - Click "Download Video" and choose the save location.

3. **Monitor Progress**:
   - Track the download progress through the progress bar.
   - Check status updates displayed in the application window.

## Screenshots

![image](https://github.com/user-attachments/assets/194657e3-fb66-4c32-9944-8016bd46d733)


## Contributions

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is open-source and licensed under the [MIT License](LICENSE).

---

**Enjoy effortless video downloading with M3U8 Video Downloader!**

