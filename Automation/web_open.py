import webbrowser
from Automation.Web_Data import websites

def openweb(webname):
    #* Convert the input website name to lowercase and split into words.
    website_name = webname.lower().split()
    
    #* Count the occurrences of each word in the input.
    counts = {}
    for name in website_name:
        counts[name] = counts.get(name, 0) + 1
    
    #* Prepare a list of URLs to open based on the counts of each website.
    urls_to_open = []
    for name, count in counts.items():
        if name in websites:
            urls_to_open.extend([f"https://{websites[name]}"] * count)
    
    #* Open the collected URLs in the default web browser.
    for url in urls_to_open:
        webbrowser.open(url) 
    
    #* Print a message if any URLs were opened.
    if urls_to_open:
        print("Opening...")


openweb("youtube")