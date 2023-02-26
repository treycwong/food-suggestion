import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        food = request.form["food"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(food),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(food):
    return """Suggest three Malaysian food based from my favourite food

Food: Pasta
Names: Mee Goreng, Laksa, Curry Mee
Food: Chicken
Names: Nasi Lemak, Ayam Goreng, Satay
Food: {}
Names:""".format(
        food.capitalize()
    )
