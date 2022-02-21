import json

from config import CANDIDATES_PATH, SETTINGS_PATH


def get_settings():
    """
    обрабатывает Json Settings
    return: словарь настроек
    """
    with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_candidates():
    """
    Обрабатывает Json список кандидатов
    return: список кандидатов
    """
    with open(CANDIDATES_PATH, "r", encoding="utf-8") as f:
        data2 = json.load(f)
    return data2


def candidate_by_cid(cid):
    """
    ;param cid: id кандидата
    return: словарь с данными кандидата
    """

    candidates = get_candidates()

    for candidate in candidates:
        if candidate.get("id") == cid:
            return candidate


def search_candidates_by_name(name):
    """
    param name: Имя по которому выполняется поиск
    return: Cписок подходящих людей
    """

    settings = get_settings()
    case_sensitive = settings.get("case_sensitive", False)

    candidates = get_candidates()
    candidates_match = []

    for candidate in candidates:

        if name in candidate.get("name"):
            candidates_match.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate.get("name").lower():
                candidates_match.append(candidate)

    return candidates_match


def get_candidate_by_skill(skill_name):

    settings = get_settings()
    limit = settings.get("limit, 3")
    candidates = get_candidates()
    candidates_match = []

    skill_name = skill_name.lower()

    for candidate in candidates:

        skills = candidate["skills"].lower().split(", ")

        if skill_name in skills:
            candidates_match.append(candidate)

    return candidates_match[:limit]

