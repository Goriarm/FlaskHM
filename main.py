from flask import Flask, request, render_template

from utils import get_settings, candidate_by_cid,  get_candidates, search_candidates_by_name, get_candidate_by_skill

app = Flask(__name__)


@app.route("/")
def index():

    settings = get_settings()
    online = settings.get("online", False)
    if online:
        return f"""Приложение работает <br>
        <form action="/list"> 
        <input type = "submit" value="Перейти к кандидатам">
        """, render_template("index.html")

    return "Приложение не работает"


@app.route("/candidate/<int:cid>")
def page_candidate(cid):

    candidate = candidate_by_cid(cid)
    page_content = f"""
    <h1>{candidate["name"]}</h1>
    <p>{candidate["position"]}</p>
    <img src="{candidate["picture"]}" width=200/>
    <p>{candidate["skills"]}</p>
    """

    return page_content, render_template("candidate.html")


@app.route("/list")
def page_list_of_candidates():

    candidates = get_candidates()
    page_content = "<h1>Все кандидаты</h1"

    for candidate in candidates:
        page_content += f"""
            <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
            """
    return page_content, render_template("list.html")


@app.route("/search")
def page_search_by_name():

    name = request.args.get("name", "")

    candidates = search_candidates_by_name(name)
    candidates_count = len(candidates)

    page_content = f"<h1>найдено кандидатов {candidates_count} </h2>"

    for candidate in candidates:
        page_content += f"""
            <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
            """
    return page_content, render_template("search.html")


@app.route("/skill/<skill_name>")
def page_search_by_skils(skill_name):

    candidates = get_candidate_by_skill(skill_name)
    candidates_count = len(candidates)

    page_content = f"<h1>Найдено со скиллом {skill_name}: {candidates_count} </h2>"

    for candidate in candidates:
        page_content += f"""
            <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
            """
    return page_content, render_template("skill.html")


if __name__ == "__main__":
    app.run()