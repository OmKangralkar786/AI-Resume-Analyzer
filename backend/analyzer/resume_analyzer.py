def analyze_resume(skills):

    strengths = []

    weaknesses = []

    recommendations = []

    if len(skills) >= 5:

        strengths.append(
            "Strong technical skill set"
        )

    if "python" in skills:

        strengths.append(
            "Good programming foundation"
        )

    if "django" in skills:

        strengths.append(
            "Backend development knowledge"
        )

    if "react" not in skills:

        weaknesses.append(
            "React skill missing"
        )

        recommendations.append(
            "Learn React and build projects"
        )

    if "sql" not in skills:

        weaknesses.append(
            "Database knowledge not shown"
        )

        recommendations.append(
            "Add SQL projects"
        )

    if len(skills) < 3:

        weaknesses.append(
            "Limited technical skills"
        )

        recommendations.append(
            "Add more technical skills"
        )

    return {

        "strengths":
            strengths,

        "weaknesses":
            weaknesses,

        "recommendations":
            recommendations
    }