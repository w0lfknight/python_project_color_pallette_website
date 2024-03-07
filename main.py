import sys
from colorthief import ColorThief
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
app = Flask(__name__)


# dominant_color = ct.get_color(quality=1)
#
# plt.imshow([[dominant_color]])
# plt.show()


# plt.imshow([[palette[i] for i in range(5)]])
# plt.show()
file_path = None

@app.route('/', methods=["GET","POST"])
def main():

    global file_path
    hex_colors = []

    if request.method == "POST":
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        # Save the uploaded file
        file_path = 'static/uploads/' + file.filename
        file.save(file_path)

        # Get the URL of the uploaded file


        ct = ColorThief(file_path)
        palette = ct.get_palette(color_count=5)
        for color in palette:

            hex_color = (f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
            hex_colors.append(hex_color)


    return render_template("index.html", hex_codes = hex_colors, file_url=file_path, uploaded=True)

if __name__ == "__main__":
    app.run(debug=True)