def generate_questions(skills):

    hr_questions = [

        "Tell me about yourself.",

        "Why should we hire you?",

        "What are your strengths?",

        "Describe a difficult situation you handled."
    ]

    technical_questions = []

    project_questions = [

        "Explain your most recent project.",

        "What challenges did you face?",

        "How did you overcome those challenges?"
    ]

    question_bank = {

        "python": [

            "What are Python decorators?",

            "Difference between List and Tuple?",

            "What are generators in Python?"
        ],

        "react": [

            "What are React Hooks?",

            "Difference between State and Props?",

            "Explain useEffect Hook."
        ],

        "django": [

            "What is Django ORM?",

            "Explain Django MVT architecture.",

            "What are Django middleware?"
        ],

        "sql": [

            "Difference between DELETE and TRUNCATE?",

            "Explain JOIN types.",

            "What is normalization?"
        ],

        "javascript": [

            "What is closure?",

            "Difference between let and var?",

            "Explain promises."
        ],

        "html": [

            "What is semantic HTML?",

            "Difference between div and span?"
        ],

        "css": [

            "What is Flexbox?",

            "Difference between Grid and Flexbox?"
        ]
    }

    for skill in skills:

        skill = skill.lower()

        if skill in question_bank:

            technical_questions.extend(
                question_bank[skill]
            )

    return {

        "hr_questions":
            hr_questions,

        "technical_questions":
            technical_questions,

        "project_questions":
            project_questions
    }