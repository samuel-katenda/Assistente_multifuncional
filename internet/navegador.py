import webbrowser

def abrir_site(site):
    if site in links:
        webbrowser.open(links[site])
        return True
    else:
    	pass
    return None
links = {
    "1": "https://www.google.com",
    "2": "https://gemini.google.com",
    "3": "https://chat.openai.com",
    "4": "https://github.com",
    "5": "https://www.youtube.com",
    "6": "https://snapsave.app",
    "7": "https://www.facebook.com",
    "8": "https://claude.ai",
    "9": "https://www.canva.com",
    "10": "https://drive.google.com"}