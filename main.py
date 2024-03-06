import sys
from colorthief import ColorThief
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)


# dominant_color = ct.get_color(quality=1)
#
# plt.imshow([[dominant_color]])
# plt.show()


# plt.imshow([[palette[i] for i in range(5)]])
# plt.show()


@app.route('/', methods=["GET","POST"])
def main():
    hex_colors = []

    if request.method == "POST":


        image = request.form.get("image_address")
        ct = ColorThief(f"static/img/{image}")
        palette = ct.get_palette(color_count=5)
        for color in palette:

            hex_color = (f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
            hex_colors.append(hex_color)


    return render_template("index.html", hex_codes = hex_colors)

if __name__ == "__main__":
    app.run(debug=True)