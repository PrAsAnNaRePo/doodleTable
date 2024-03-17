import requests

# The base URL of your API
API_BASE_URL = 'http://localhost:8000'

# The HTML table you want to convert to an Excel file
html_table = '<table><tr><td>Example</td></tr></table>'

# Step 1: Send the HTML table to your API to create the Excel file
create_response = requests.post(f'{API_BASE_URL}/setFile', json={'html_table': html_table})
print(create_response.text)