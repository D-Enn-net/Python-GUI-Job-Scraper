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
![before scraping](https://github.com/user-attachments/assets/1814c03b-ed3e-43d7-a42a-d70699c3b0ba)


### Application After Fetching Data ("After")
![after scraping](https://github.com/user-attachments/assets/75df5701-b0c1-4330-a2f9-11b990c850fc)



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
