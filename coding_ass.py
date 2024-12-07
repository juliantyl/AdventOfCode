import requests
from bs4 import BeautifulSoup


def print_table(rows):
    x_pos = -1
    y_pos = -1
    char_pos = -1

    # get pos of each column first
    pos_cell = [cell.get_text() for cell in rows[0].find_all('td')]
    for i, cell in enumerate(pos_cell):
        if cell == 'x-coordinate':
            x_pos = i
        elif cell == 'y-coordinate':
            y_pos = i
        elif cell == 'Character':
            char_pos = i

    # exiting if incorrect format of table
    if any([x_pos < 0, y_pos < 0, char_pos < 0]):
        print(f"Couldn't identify names of the columns. Ensure that the first columns in a table has x-position, y-position and Character columns.")
        return

    chars_dict = {}
    for row in rows[1:]:
        cells = [cell.get_text() for cell in row.find_all('td')]
        chars_dict[(int(cells[x_pos]), int(cells[y_pos]))] = cells[char_pos]

    max_x = 0
    max_y = 0
    for key in chars_dict.keys():
        # print(key)
        if key[0] > max_x:
            max_x = key[0]
        if key[1] > max_y:
            max_y = key[1]
    max_x += 1
    max_y += 1

    output = [[" " for _ in range(max_x)] for _ in range(max_y)]
    for i in range(max_y):
        for j in range(max_x):
            if (i, j) in chars_dict:
                output[j][i] = chars_dict[(i, j)]

    for i in range(len(output) - 1, -1, -1):
        print(''.join(output[i]))



def display_google_doc_table(url):
    # Fetch the document content
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch the document. Ensure the URL is correct and the document is shared publicly.")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate tables in the Google Doc content
    tables = soup.find_all('table')

    if not tables:
        print("No tables found in the document.")
        return

    for table_idx, table in enumerate(tables):
        # print(f"Printing Result for Table {table_idx + 1}:")
        rows = table.find_all('tr')
        print_table(rows)



# Example URL of a public Google Doc
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
display_google_doc_table(url)
