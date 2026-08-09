import re

COMMON_SKILLS = [

    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "Git",
    "Machine Learning",
    "Deep Learning",
    "Flask",
    "Django",
    "MongoDB",
    "MySQL",
    "REST API",
    "Docker",
    "AWS",
    "Excel",
    "Arduino",
    "ESP32"

]


def extract_skills(text):

    found = []

    for skill in COMMON_SKILLS:

        if re.search(r"\b" + re.escape(skill) + r"\b", text, re.IGNORECASE):

            found.append(skill)

    return found