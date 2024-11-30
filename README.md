# Basic-Blogpost-Template
A simple blog application built using Flask. It fetches blog posts from an external API and displays them on a homepage with individual blog pages for each post.

---

## Features
- Homepage displaying a list of blog posts.
- Individual pages for each blog post.
- Clean and modular code with routes for home and blog pages.

---

## Project Structure
Basic Blogpost Template/
├── static/            # Static files folder                                                                                                                           
│   └── css/           # CSS styles                                                                                                                                   
│       └── styles.css # Styling for the application                                                                                                                   
├── templates/         # HTML templates folder                                                                                                                         
│   ├── index.html     # Homepage template                                                                                                                             
│   └── post.html      # Individual post template                                                                                                                      
├── .env               # Environment file for sensitive data (not included in repo)                                                                                    
├── main.py            # Main application logic                                                                                                                        

---

## Prerequisites
- Python 3.8+
- Flask

---

## Installation
1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies: pip install flask, requests, dotenv
4. Make your API with the info you want to be displayed in your Blogspot and replace it in .env and main.py
5. Run the application: python main.py
