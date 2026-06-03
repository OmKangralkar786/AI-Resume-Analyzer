from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Avg, Max

from .models import Resume
from .serializers import ResumeSerializer
from .parser import extract_text
from .skills import extract_skills
from .ats import calculate_ats
from .question_generator import generate_questions
from .resume_analyzer import analyze_resume
from .score_breakdown import calculate_breakdown
from .career_recommender import recommend_career


@api_view(['POST'])
def upload_resume(request):

    file = request.FILES['resume']

    resume = Resume.objects.create(
        name=request.data['name'],
        email=request.data['email'],
        resume=file
    )

    text = extract_text(
        resume.resume.path
    )

    resume_skills = extract_skills(text)

    job_description = request.data.get(
        'job_description',
        ''
    )

    jd_skills = extract_skills(
        job_description
    )

    ats_result = calculate_ats(
        resume_skills,
        jd_skills
    )

    questions = generate_questions(
        resume_skills
    )

    analysis = analyze_resume(
        resume_skills
    )

    breakdown = calculate_breakdown(
        resume_skills
    )

    career = recommend_career(
        resume_skills
    )

    resume.ats_score = ats_result['score']

    resume.save()

    return Response({

        'message': 'Resume Uploaded Successfully',

        'skills': resume_skills,

        'ats_score': ats_result['score'],

        'matched_skills':
            ats_result['matched_skills'],

        'missing_skills':
            ats_result['missing_skills'],

        'suggestions':
            ats_result['suggestions'],

        'hr_questions':
            questions['hr_questions'],

        'technical_questions':
            questions['technical_questions'],

        'project_questions':
            questions['project_questions'],

        'strengths':
            analysis['strengths'],

        'weaknesses':
            analysis['weaknesses'],

        'recommendations':
            analysis['recommendations'],

        'breakdown':
            breakdown,

        'career_roles':
            career['roles'],

        'learning_paths':
            career['learning']
    })


@api_view(['GET'])
def resume_history(request):

    resumes = Resume.objects.all().order_by(
        '-created_at'
    )

    serializer = ResumeSerializer(
        resumes,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def analytics(request):

    total_resumes = Resume.objects.count()

    average_ats = Resume.objects.aggregate(
        Avg('ats_score')
    )['ats_score__avg']

    highest_ats = Resume.objects.aggregate(
        Max('ats_score')
    )['ats_score__max']

    return Response({

        'total_resumes': total_resumes,

        'average_ats': round(
            average_ats if average_ats else 0,
            2
        ),

        'highest_ats':
            highest_ats if highest_ats else 0
    })