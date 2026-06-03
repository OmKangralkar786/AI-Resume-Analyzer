def recommend_career(skills):

    roles = []

    learning = []

    skills = [skill.lower() for skill in skills]

    if 'python' in skills:

        roles.append(
            'Python Developer'
        )

        learning.extend([
            'Advanced Python',
            'Design Patterns'
        ])

    if 'django' in skills:

        roles.append(
            'Django Developer'
        )

        learning.extend([
            'REST APIs',
            'Docker'
        ])

    if 'react' in skills:

        roles.append(
            'Frontend Developer'
        )

        learning.extend([
            'Redux',
            'Next.js'
        ])

    if (
        'react' in skills and
        'django' in skills
    ):

        roles.append(
            'Full Stack Developer'
        )

    if 'sql' in skills:

        learning.extend([
            'Database Optimization',
            'System Design'
        ])

    return {

        'roles':
            list(set(roles)),

        'learning':
            list(set(learning))
    }