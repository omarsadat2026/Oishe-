"""
Happy Birthday, My Love — a little website built just for her.

HOW TO RUN:
    1. pip install flask
    2. python app.py
    3. open http://localhost:5000 in your browser

HOW TO CUSTOMIZE (search for these in this file):
    - HER_NAME        -> Tasfiya Uzzal Oishe
    - BIRTHDAY_DATE    -> 2026/10/09
    - LOVE_LETTER      -> MRs Omar i loveeee youuuu kittyy,Happy Birthday
    - MEMORIES         -> a list of little memories/moments
    - Photos: drop your images into static/images/ and list the
      filenames in the PHOTOS list below (any order you like).
"""

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------
# ✏️  CUSTOMIZE EVERYTHING BELOW THIS LINE
# ---------------------------------------------------------------------

HER_NAME = "My Love"

# Format: "YYYY-MM-DD HH:MM:SS" (24-hour time, used for the countdown)
BIRTHDAY_DATE = "2026-09-14 00:00:00"

LOVE_LETTER = """
My darling,

Every year I get to watch you grow more beautiful, more brilliant, and
more wonderfully you — and every year I fall for you a little harder.
Today isn't just about celebrating the day you were born. It's about
celebrating every single day I get to spend beside you.

Thank you for your laugh that fills every room, for the way you make
even ordinary Tuesdays feel like an adventure, and for loving me the
way you do.

Here's to another year of us.

Forever yours.
"""

# A short list of memories — as many or as few as you like.
MEMORIES = [
    {"2023": "The Beginning", "text": "The first time I saw you smile, I knew I was in trouble."},
    {"2024": "Our First Meet", "text": "Getting lost together and laughing the whole time."},
    {"2025": "The Little Things", "text": "Everyday of us?, bad jokes, and always youre mine."},
    {"2026": "Today", "text": "Still the best decision I ever made, every single day."},
]

# Drop image files into static/images/ and list their filenames here.
# Leave empty and the page will show elegant placeholder frames instead.
PHOTOS = [
    # "IMG_4214.JPG",
    # "static/images//Users/omarsadad/Downloads/IMG_1448.JPG",
    # "/Users/omarsadad/Downloads/IMG_9915.HEIC",

]

# ---------------------------------------------------------------------
# You shouldn't need to touch anything below this line.
# ---------------------------------------------------------------------


@app.route("/")
def home():
    return render_template(
        "index.html",
        her_name=Tasfiya Oishe,
        birthday_date= 9/10/2026,
        love_letter=LOVE_LETTER.strip(),
        memories=MEMORIES,
        photos=PHOTOS,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
