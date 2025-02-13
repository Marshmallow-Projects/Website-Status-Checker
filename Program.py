import requests

# -------------------------------------------------------------------------
# Website Status Checker by Marshmallow.Projects 
# Checks the status code of a website to see if it is up and running.
# A Python Program To quickly check if a website or API is available and responsive.
#
# Developed and maintained by Marshmallow.Projects
# Website: https://github.com/Marshmallow-Projects
# -------------------------------------------------------------------------

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website '{url}' is up and running.")
        else:
            print(f"[Marshmallow.Projects] Website '{url}' returned status code {response.status_code}.")
    except requests.RequestException as Marshmallow:
        print(f"Marshmallow.Projects Failed to reach '{url}': {Marshmallow}")

# Program start
url = 'https://www.example.com'  # Change to your website's URL
print("""
========================================
Website Status Checker
Powered by Marshmallow.Projects
========================================
""")

check_website_status(url)
