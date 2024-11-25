from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("index.html")  # Renders the HTML template

# API Route to handle a POST request
@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.get("user_input")
    if data:
        response = {
            "message": f"You submitted: {data}",
            "length": len(data)
        }
        return jsonify(response)
    else:
        return jsonify({"error": "No input received!"}), 400

if __name__ == "__main__":
    app.run(debug=True)
