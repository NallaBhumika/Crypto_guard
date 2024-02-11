from flask import Flask, request, render_template
import string

app = Flask(__name__)

def shift_text(text, shift):
    # Implement the Caesar cipher shift logic here
    alphabet = string.ascii_lowercase
    shifted_text = ""
    for char in text:
        if char.isalpha():
            base_index = alphabet.index(char.lower())
            shifted_index = (base_index + shift) % 26
            shifted_char = alphabet[shifted_index]
            shifted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            shifted_text += char
    return shifted_text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt_info.html")
def encrypt_info():
    return render_template("encrypt_info.html")

@app.route("/decrypt_info.html")
def decrypt_info():
    return render_template("decrypt_info.html")

@app.route("/application.html")
def application():
    return render_template("application.html")


@app.route("/encrypt", methods=["POST"])
def encrypt():
    shift = int(request.form["shift"])
    file = request.files["file"]
    
    # Ensure the file is not empty
    if file.filename == '':
        return "No file selected", 400
    
    # Read the contents of the file
    text = file.read().decode("utf-8")
    
    # Encrypt the text
    encrypted_text = shift_text(text, shift)
    
    # Return the encrypted text
    return encrypted_text

@app.route("/decrypt", methods=["POST"])
def decrypt():
    shift = int(request.form["shift"])
    encrypted_text = request.form["encrypted_text"]
    decrypted_text = shift_text(encrypted_text, -shift)
    return decrypted_text
    #return render_template("index.html", decrypted_text=decrypted_text)


if __name__ == "__main__":
    app.run(debug=True)





