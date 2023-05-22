from flask import Flask, redirect, render_template, request, send_from_directory, url_for
import requests

# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
app = Flask(__name__)


@app.route('/lottie/<path:filename>')
def serve_lottie(filename):
    return send_from_directory('static/lottie', filename)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/areas-of-practice')
def areasofPractice():
    return render_template('areas-of-practice.html')


@app.route('/contact-us')
def contactUs():
    return render_template('contact-us.html')


# @app.route("/form-submit", methods=["POST"])
# def formSubmit():
#     name = request.form.get("enquiry_name")
#     email = request.form.get("enquiry_email")
#     number = request.form.get("enquiry_number")
#     message = request.form.get("enquiry_message")

#     collected_message = str("From: " + str(name) + "\nNumber: " + str(number) + "\nEmail: " + str(email) + "\nMessage: " + str(message))

#     requests.post(
#         "https://api.mailgun.net/v3/sandbox7af944196f4d4452b2066ef2debc2646.mailgun.org/messages",
#         auth=("api", "f136f0eb19650c4ba419d1748e6f6ca7-181449aa-897437d5"),
#         data={"from": "Mailgun Sandbox <postmaster@sandbox7af944196f4d4452b2066ef2debc2646.mailgun.org>",
#                       "to": "fidlera@tcd.ie",
#               "subject": str("Message from " + str(name)),
#               "text": collected_message})

#     return redirect(url_for("success"))


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


if __name__ == "__main__":
    app.run(debug=True)
