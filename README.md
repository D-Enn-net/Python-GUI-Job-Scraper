# Python GUI Job Scraper

A desktop GUI application built with Python and Tkinter that scrapes job listings from python.org/jobs and displays them in a clean, searchable table.

This project was built to showcase skills in GUI development, web scraping, and data handling.

## 🚀 Features
- Simple, dark-themed GUI built with Tkinter and the `sv-ttk` theme.
- Fetches live job data from `python.org/jobs` with a single click.
- Displays results in a clean, sortable table with a scrollbar.
- Built with professional practices like virtual environments and robust, error-handling functions.

## 🛠️ Technologies Used
- **Python**
- **Tkinter** (for the GUI)
- **sv-ttk** (for the dark theme)
- **Requests & BeautifulSoup4** (for web scraping)
- **Pandas** (for data handling)

## 🖼️ Screenshots

### Application on Launch ("Before")
*(Here you will drag-and-drop your 'before' screenshot)*

### Application After Fetching Data ("After")
*(Here you will drag-and-drop your 'after' screenshot)*


## ⚙️ How to Use

1.  Clone the repository to your local machine.
2.  Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Install the necessary libraries:
    ```sh
    pip install requests beautifulsoup4 pandas sv-ttk
    ```
4.  Run the script:
    ```sh
    python scraper_gui.py
    ```
