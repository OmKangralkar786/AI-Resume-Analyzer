def calculate_breakdown(skills):

    skills_score = min(
        len(skills) * 5,
        40
    )

    project_score = 20

    experience_score = 20

    education_score = 15

    formatting_score = 5

    total_score = (

        skills_score +

        project_score +

        experience_score +

        education_score +

        formatting_score
    )

    return {

        "skills_score":
            skills_score,

        "project_score":
            project_score,

        "experience_score":
            experience_score,

        "education_score":
            education_score,

        "formatting_score":
            formatting_score,

        "total_score":
            total_score
    }