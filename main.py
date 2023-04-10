from flask import Flask, jsonify , redirect
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route("/xpshort/<path:url>")
def xpshort(url):
    import time
    import requests
    from bs4 import BeautifulSoup 
    client = requests.session()
    DOMAIN = "https://xpshort.com/"
    url = url[:-1] if url[-1] == '/' else url
    code = url.split("/")[-1]
    final_url = f"{DOMAIN}/{code}"
    #ref = "https://b.finsurances.co/"
    ref = "https://www.jankarihoga.com/"
    h = {"referer": ref}
    resp = client.get(final_url,headers=h)
    soup = BeautifulSoup(resp.content, "html.parser")
    inputs = soup.find_all("input")
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }  
    time.sleep(8)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return redirect(r.json()['url'])
    except: 
        return "SomeThing went wrong"

    
 
@app.route("/test/<path:url>")
def xpshor1t(url):
    import time
    import requests
    from bs4 import BeautifulSoup 
    redirect("https://www.youtube.com/")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
