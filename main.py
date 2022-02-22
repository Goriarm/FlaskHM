from flask import Flask, request, render_template

from utils import get_settings, candidate_by_cid,  get_candidates,\
    search_candidates_by_name, get_candidate_by_skill

app = Flask(__name__)


@app.route("/")
def index():

    settings = get_settings()
    online = settings.get("online", True)
    if online:
        return render_template("index.html")

    return "Приложение не работает"


@app.route("/candidate/<int:cid>")
def page_candidate(cid):

    candidate = candidate_by_cid(cid)

    return render_template("candidate.html", candidate=candidate)


@app.route("/list")
def page_list_of_candidates():

    candidates = get_candidates()

    return render_template("list.html", candidates=candidates)


@app.route("/search")
def page_search_by_name():

    name = request.args.get("name", "")

    candidates = search_candidates_by_name(name)
    candidates_count = len(candidates)

    return render_template("search.html", candidates=candidates, candidates_count=candidates_count)


@app.route("/skill/<skill_name>")
def page_search_by_skils(skill_name):

    candidates = get_candidate_by_skill(skill_name)
    candidates_count = len(candidates)

    return render_template("skill.html", candidates=candidates,  candidates_count=candidates_count)


if __name__ == "__main__":
    app.run()

