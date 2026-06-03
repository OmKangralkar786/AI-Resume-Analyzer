def calculate_ats(resume_skills, jd_skills):

    if len(jd_skills) == 0:

        jd_skills = [
            'python',
            'react',
            'django',
            'sql'
        ]

    matched_skills = list(
        set(resume_skills).intersection(
            set(jd_skills)
        )
    )

    missing_skills = list(
        set(jd_skills) - set(resume_skills)
    )

    score = (
        len(matched_skills)
        / len(jd_skills)
    ) * 100

    suggestions = []

    if score < 50:

        suggestions.append(
            "Add more technical skills"
        )

        suggestions.append(
            "Include more projects"
        )

    if 'react' not in resume_skills:

        suggestions.append(
            "Add React projects"
        )

    if 'django' not in resume_skills:

        suggestions.append(
            "Mention Django backend experience"
        )

    if 'sql' not in resume_skills:

        suggestions.append(
            "Add database related skills"
        )

    return {

        'score': round(score),

        'matched_skills': matched_skills,

        'missing_skills': missing_skills,

        'suggestions': suggestions
    }