from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .extract.ext_skl import extract_skills
from .extract.pickleUse import find_domain
from .extract.scrape import scrape_indeed
from .extract.matchbert import calc_and_sort_jobs
import os

@api_view(['POST'])
def postResume(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)
    
    uploaded_file = request.FILES['file']
    save_path = "C:/Users/keyur/Desktop/VIT/EDI/edi5/AutoJobSearch/resume/resume.pdf"
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    with open(save_path, 'wb') as file:
        for chunk in uploaded_file.chunks():
            file.write(chunk)
    
    resume_data = extract_skills()    
    domain = find_domain()
    
    return Response({
        "skills": resume_data,
        "domain_info": domain
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def postChosenSkills(request):
    data = request.data
    # print(data["title"])

    title = data['title']
    location = data['location']

    results = scrape_indeed(title, location)

    jobs = calc_and_sort_jobs(data['skills'])

    return Response(jobs, status=status.HTTP_200_OK)
