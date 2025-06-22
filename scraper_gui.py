# Final Scraper GUI Application - Version 1.0

import tkinter as tk
from tkinter import ttk
import sv_ttk
import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading

# --- Scraper Functions ---

def fetch_page(url):
    """Downloads the HTML content of a webpage, returning a BeautifulSoup object."""
    try:
        page = requests.get(url)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_jobs(soup):
    """Parses the soup object to find and extract job details."""
    if soup is None: return []

    job_container = soup.find('ol', class_='list-recent-jobs')
    if not job_container:
        print("Could not find the main job container.")
        return []

    job_elements = job_container.find_all('li')
    extracted_jobs = []

    print(f"Found {len(job_elements)} potential job listings. Extracting details...")

    for job_element in job_elements:
        try:
            title_element = job_element.find('h2').find('a')
            company_span = job_element.find('span', class_='listing-company-name')
            location_element = job_element.find('span', class_='listing-location')

            title = title_element.text.strip() if title_element else "N/A"
            link = "https://www.python.org" + title_element['href'] if title_element else "N/A"
            location = location_element.text.strip() if location_element else "N/A"
            
            company = "N/A"
            if company_span:
                # Get all text from the span, then remove the job title's text.
                # What remains is the company name.
                all_text_in_span = company_span.get_text(separator=' ', strip=True)
                job_title_in_span = title_element.text.strip()
                company = all_text_in_span.replace(job_title_in_span, '').strip()

            # Only add the job if we found a valid title
            if title != "N/A":
                extracted_jobs.append([title, company, location, link])
        except Exception as e:
            # This will catch any errors on malformed listings and just skip them
            print(f"Skipping a malformed job listing due to error: {e}")
            continue
            
    return extracted_jobs

# --- GUI Functions ---

def perform_search():
    """This function runs the scraper and updates the table. It's run in a separate thread."""
    print("Scraping started...")
    
    # 1. Clear any old results from the table
    for item in tree.get_children():
        tree.delete(item)

    # 2. Fetch and parse the data
    URL = "https://www.python.org/jobs/"
    page_soup = fetch_page(URL)
    jobs_data = parse_jobs(page_soup)

    # 3. Insert new data into the table
    if jobs_data:
        for job in jobs_data:
            tree.insert('', tk.END, values=job)
        print(f"Scraping complete! Found {len(jobs_data)} jobs.")
    else:
        print("No jobs found or an error occurred.")

def search_jobs_threaded():
    """Starts the scraping process in a new thread to keep the GUI responsive."""
    # Create and start a new thread that will run the perform_search function
    thread = threading.Thread(target=perform_search)
    thread.start()

# --- Window and Widgets Setup ---
root = tk.Tk()
sv_ttk.set_theme("dark")
root.title("Python Job Scraper")
root.geometry("1100x700")

top_frame = ttk.Frame(root, padding="10")
top_frame.pack(fill=tk.X)

search_label = ttk.Label(top_frame, text="Source:")
search_label.pack(side=tk.LEFT, padx=5)

# For now, the source is fixed, but we'll make this a dropdown later.
source_label = ttk.Label(top_frame, text="python.org/jobs", font="-weight bold")
source_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

# We now connect the button to our new threaded search function
search_button = ttk.Button(top_frame, text="Fetch Jobs", command=search_jobs_threaded)
search_button.pack(side=tk.LEFT, padx=5)

tree_frame = ttk.Frame(root, padding="10")
tree_frame.pack(expand=True, fill=tk.BOTH)

columns = ('Job Title', 'Company', 'Location', 'Link')
tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

tree.heading('Job Title', text='Job Title')
tree.heading('Company', text='Company')
tree.heading('Location', text='Location')
tree.heading('Link', text='Link')

tree.column('Job Title', width=400)
tree.column('Company', width=200)
tree.column('Location', width=200)
tree.column('Link', width=250)

tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()