import requests, random, time, logging, os, ctypes
os.system("")
os.system("cls")
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;63m[\x1b[0m%(asctime)s\x1b[38;5;63m]\x1b[0m %(message)s",
    datefmt="%H:%M:%S"
)
Valid = 0
def UpdateTitle(): 
    ctypes.windll.kernel32.SetConsoleTitleW("[ThisPersonDoesNotExist Scraper] | Valid: %s" % (Valid))
if not os.path.exists('Images'): os.makedirs('Images')
while True:
    time.sleep (1)
    response = requests.get ("https://thispersondoesnotexist.com/image")
    if response.status_code == 200:
        Valid += 1
        logging.critical ("Successfully Scraped Image")
        UpdateTitle()
    else:
        logging.critical ("Failed to Scrape Image")
    chars = ("abcdefghijklmnopqrstuvwxyz")
    filename = "".join(random.choice(chars) for x in range(4))
    with open(f'Images/{filename}.{"png"}', 'wb') as f: f.write(response.content)
