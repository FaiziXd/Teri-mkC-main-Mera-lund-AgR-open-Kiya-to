from flask import Flask, render_template_string, request

# Email credentials (add 30 email addresses)
EMAILS = [
    "sonpigmix@mbox.re", "faxbug474@via.tokyo.jp", "rughim31@mail4.uk", "faxcatnot@boxfi.uk", "topyou976@fanclub.pm",
    "liepubpad@quicksend.ch", "oweheypop@digdig.org", "dueawe272@fanclub.pm", "cryvanraw@owleyes.ch", "alecup@boxfi.uk",
    "huesowtar@magim.be", "digingear@instaddr.uk", "pop612@prin.be", "mowantbum@mirai.re", "tonvan619@nekosan.uk",
    "lietubwho@mirai.re", "ebbgym900@fanclub.pm", "zoolidpay@send4.uk", "canmatcry@mail4.uk", "rimher748@stayhome.li",
    "ahaoff630@stayhome.li", "waxallpie@send4.uk", "mayourbra@moimoi.re", "newand147@mofu.be", "ownpop639@svk.jp",
    "ragput368@haren.uk", "hogdiphug@eay.jp", "theatjar@heisei.be", "mrsadhot@ichigo.me", "ashlap24@instmail.uk"
]

# Password to be used for all accounts
PASSWORD = "FAIZU H3R2"

# Flask setup
app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generate Facebook Accounts</title>
    </head>
    <body>
        <h1>Facebook Account Generator</h1>
        <form action="/generate" method="POST">
            <button type="submit">Generate Accounts</button>
        </form>
    </body>
    </html>
    """)

@app.route('/generate', methods=['POST'])
def generate():
    created_accounts = [(email, PASSWORD) for email in EMAILS]
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generated Accounts</title>
    </head>
    <body>
        <h1>Generated Accounts</h1>
        <ul>
            {% for account in accounts %}
                <li>Email: {{ account[0] }}, Password: {{ account[1] }}</li>
            {% endfor %}
        </ul>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """, accounts=created_accounts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
