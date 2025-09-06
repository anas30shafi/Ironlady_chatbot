from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "").lower()

    faqs = {
        "programs": "Iron Lady offers leadership programs focused on confidence, communication, negotiation, and executive presence.",
        "duration": "Programs vary from short workshops (2-3 days) to long-term cohorts (8-12 weeks).",
        "mode": "Most programs are online, with some offline workshops in major cities.",
        "certificate": "Yes, certificates are provided after successful completion.",
        "mentors": "Mentors include senior industry leaders, certified coaches, and experienced women professionals."
    }

    answer = "Sorry, I can only answer about programs, duration, mode, certificates, or mentors."

    for key in faqs:
        if key in user_message:
            answer = faqs[key]
            break

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
