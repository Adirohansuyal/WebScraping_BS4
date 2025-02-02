from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

try:
    # Fetch the webpage content
    source = requests.get("https://en.wikipedia.org/wiki/List_of_Hindi_films_of_2024")
    source.raise_for_status()
    soup = BeautifulSoup(source.text, "html.parser")
    
    # Find the table with class 'wikitable'
    table = soup.find('table', class_='wikitable')

    # Find all rows in the table (excluding the header row)
    rows = table.find_all('tr')[1:]

    # Debugging: print the number of rows to ensure all data is being fetched
    print(f"Total number of rows: {len(rows)}")

    # Create a new workbook and active sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Hindi Films of 2024"

    # Set headers for the Excel sheet
    ws.append(["Title", "Production Company", "Distributor"])

    # Loop through each row and extract the relevant data
    for row in rows:
        cols = row.find_all('td')
        
        # Ensure that the row has more than 2 columns (some rows might be empty)
        if len(cols) >= 3:
            title = cols[0].get_text(strip=True)
            production_company = cols[1].get_text(strip=True)
            distributor = cols[2].get_text(strip=True)
            
            # Append the extracted data as a new row in the Excel sheet
            ws.append([title, production_company, distributor])

    # Save the workbook to a file
    wb.save("Hindi_Films_2024.xlsx")

    print("Data has been successfully saved to 'Hindi_Films_2024.xlsx'.")

except Exception as e:
    print(f"An error occurred: {e}")
