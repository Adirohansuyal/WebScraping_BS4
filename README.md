🚀 Movie Data Scraping Project 🎬

I’m excited to share my recent project where I scraped movie data for Hindi films of 2024 from Wikipedia! Here’s a breakdown of the technologies I used and the steps I followed to get the data and save it in an Excel format.

🛠 Technologies Used:
Python: The core programming language for this project.
BeautifulSoup: Used for web scraping, helping me parse HTML content from the webpage.
Requests: For sending HTTP requests and fetching the webpage content.
Openpyxl: Used to write the scraped data into an Excel sheet.
📌 Steps Involved:
Fetching the Webpage: I used the requests library to send a GET request to the Wikipedia page for Hindi films of 2024. This gave me access to the raw HTML content of the page.
Parsing the HTML: With the help of BeautifulSoup, I parsed the HTML content to extract the information from the table containing the movie details.
Identifying the Relevant Table: After inspecting the HTML structure, I identified the <table> tag with the class wikitable, which contains the list of movies, production companies, and distributors.
Extracting Data: I then looped through the rows of the table (excluding the header row) to extract:
Title: The name of the movie.
Production Company: The company responsible for producing the movie.
Distributor: The company distributing the movie.
Writing Data to Excel: Using openpyxl, I created an Excel workbook, added headers to the sheet, and appended the extracted data row by row.
Saving the Data: Finally, I saved the data into an Excel file named Hindi_Films_2024.xlsx, making it easy to access and analyze later.
🎯 Why This Project?
This project allowed me to practice web scraping, data extraction, and automation. It’s a great example of how Python can be used to automate data collection and manage it efficiently in an Excel format.

Looking forward to sharing more such projects and learning new ways to leverage data in my journey! 🌟

#Python #WebScraping #DataScience #BeautifulSoup #Openpyxl #Requests #Automation #TechProjects #DataAnalysis #MovieData