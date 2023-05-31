from flask import Flask, redirect, render_template, request, send_from_directory, url_for
import requests

# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
app = Flask(__name__)


@app.route('/lottie/<path:filename>')
def serve_lottie(filename):
    return send_from_directory('static/lottie', filename)


@app.route('/')
def index():
    body_style = "body-black"
    return render_template('index.html', body_style=body_style)


@app.route('/team')
def team():
    body_style = "body-black"
    return render_template('team.html', body_style=body_style)


@app.route('/work')
def work():
    body_style = "body-white"
    return render_template('work.html', body_style=body_style)


@app.route('/2023/irish-defence-forces')
def irishDefenceForce():
    body_style = "body-white"
    title = "Irish Defence Forces"
    subtitle = "A lack of interest and understanding in what the Defence Forces can offer led to falling recruitment rates across all three strands of the Defence Forces."
    heading = "Be More"
    desc_text = "Our Be More strategic and creative platform presents a career option which trains you in a trade and gives you life skills which any future employer will want."
    video_url = "https://aalasa.online/static/images/index/armed-forces-helicopter.jpg"
    carousel_text = "Egit. Ora videlis; nit. Si inatum dius, Catam prox sedi il cons in Ita, ces cam in viuscior audes postem, ublium sentem ute, nem perum cerissimis, nuntem, nonvo, noverev irmante mus"
    carousel_img_1 = "https://aalasa.online/static/images/work/idf/idf-carousel-1.jpg"
    carousel_img_2 = "https://aalasa.online/static/images/work/idf/idf-carousel-2.jpg"
    carousel_img_3 = "https://aalasa.online/static/images/work/idf/idf-carousel-1.jpg"
    social_header = "Cadetship"
    social_copy = "Egit. Ora videlis nit. Si inatum dius, Catam prox sedi il cons in Ita, ces cam in viuscior audes postem, ublium sentem ute, nem perum cerissimis, nuntem, nonvo, noverev irmante mus"
    social_img_url = "https://aalasa.online/static/images/work/idf/social-1.png"

    return render_template('/work_items/work-item-idf.html',
                           body_style=body_style, title=title, subtitle=subtitle, heading=heading,
                           desc_text=desc_text, video_url=video_url, carousel_text=carousel_text,
                           carousel_img_1=carousel_img_1, carousel_img_2=carousel_img_2, carousel_img_3=carousel_img_3,
                           social_header=social_header, social_copy=social_copy, social_img_url=social_img_url)


@app.route('/contact')
def contact():
    body_style = "body-black"
    return render_template('contact-us.html', body_style=body_style)


@app.route("/form-submit", methods=["POST"])
def formSubmit():
    name = request.form.get("enquiry_name")
    email = request.form.get("enquiry_email")
    number = request.form.get("enquiry_number")
    message = request.form.get("enquiry_message")
    if '.ru' in email:
        return redirect(url_for("errorRedirect"))
    elif ' ' not in message:
        return redirect(url_for("errorRedirect"))
    elif '0' not in number:
        return redirect(url_for("errorRedirect"))
    else:
        collected_message = str("From: " + str(name) + "\nNumber: " + str(number) +
                                "\nEmail: " + str(email) + "\nMessage: " + str(message))
        requests.post(
            "https://api.mailgun.net/v3/sandbox7af944196f4d4452b2066ef2debc2646.mailgun.org/messages",
            # auth=("api", "f136f0eb19650c4ba419d1748e6f6ca7-181449aa-897437d5"),
            auth=("api", "key-30d0d276a40ad456cc0f854f71d59925"),
            data={"from": "Mailgun Sandbox <postmaster@sandbox7af944196f4d4452b2066ef2debc2646.mailgun.org>",
                  "to": "fidlera@tcd.ie",
                  "subject": str("KICK Dublin - Message from " + str(name)),
                  "text": collected_message})

        return redirect(url_for("success"))


@app.route('/success')
def success():
    body_style = "body-black"
    return render_template('success.html', body_style=body_style)


@app.errorhandler(404)
def page_not_found(e):
    body_style = "body-white"
    # note that we set the 404 status explicitly
    return render_template('error-redirect.html', body_style=body_style), 404


if __name__ == "__main__":
    app.run(debug=True, port=6150)
