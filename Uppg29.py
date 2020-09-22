import webbrowser
from pathlib import Path
import requests

r=requests.get("https://api.adviceslip.com/advice")

api=r.json()
api_dict=api["slip"]
value=api_dict["advice"]

content=Path("uppg29 template.html").read_text()
fil=content.replace("QUOTE_TEXT", value)
p=Path("goat_quote.html")
p.write_text(fil,encoding="utf8")
webbrowser.open(str(p))