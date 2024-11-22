import re
from pdfminer.high_level import extract_text

def extract_skills():
    def extract_text_from_pdf(pdf_path):
        return extract_text(pdf_path)


    resume_path = "C:/Users/keyur/Desktop/VIT/EDI/edi5/AutoJobSearch/resume/resume.pdf"
    text = extract_text_from_pdf(resume_path)

    def extract_skills_from_resume(text, skills_list):
        skills = []

        for skill in skills_list:
            pattern = r"\b{}\b".format(re.escape(skill))
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                skills.append(skill)

        return skills

    skills_list = [
        # Core Engineering and Sciences
        'Computer Science', 'Information Technology', 'Software Engineering', 'Electrical Engineering', 
        'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering', 'Biomedical Engineering', 
        'Aerospace Engineering', 'Nuclear Engineering', 'Industrial Engineering', 'Systems Engineering',
        'Environmental Engineering', 'Petroleum Engineering', 'Geological Engineering', 'Marine Engineering', 
        'Robotics Engineering', 'Biotechnology', 'Biochemistry', 'Microbiology', 'Genetics', 'Molecular Biology', 
        'Bioinformatics', 'Neuroscience', 'Biophysics', 'Biostatistics', 'Pharmacology', 'Physiology', 'Anatomy',
        'Pathology', 'Immunology', 'Epidemiology', 'Public Health', 'Health Administration', 'Nursing', 'Medicine', 
        'Dentistry', 'Pharmacy', 'Veterinary Medicine', 'Medical Technology', 'Radiography', 'Physical Therapy', 
        'Occupational Therapy', 'Speech Therapy', 'Nutrition', 'Sports Science', 'Kinesiology', 'Exercise Physiology',
        'Sports Medicine', 'Rehabilitation Science',

        # Emerging Technologies
        'Artificial Intelligence', 'Machine Learning', 'Deep Learning', 'Natural Language Processing', 
        'Computer Vision', 'Augmented Reality', 'Virtual Reality', 'Mixed Reality', 'Blockchain Technology', 
        'Cryptocurrency', 'Quantum Computing', 'Edge Computing', 'Cloud Computing', 'IoT (Internet of Things)', 
        '5G Technology', 'Digital Twin', 'Big Data', 'Data Mining', 'Data Engineering', 'Predictive Analytics',
        'Prescriptive Analytics', 'Business Intelligence', 'Smart Cities', 'Autonomous Vehicles', 'Smart Grids',
        'Renewable Energy', 'Energy Storage Systems', 'Cybersecurity', 'Information Security', 'Digital Forensics',

        # Software Development and IT
        'Programming Languages', 'Python', 'Java', 'JavaScript', 'C++', 'C#', 'GoLang', 'R', 'Ruby', 'Swift', 'Kotlin', 'PHP', 'Perl', 'Shell Scripting', 'SQL', 'NoSQL', 'MongoDB', 'PostgreSQL', 'Redis', 'Elasticsearch', 'DevOps', 'CI/CD', 'Kubernetes', 'Docker', 'Terraform', 'Jenkins', 'AWS', 'Azure', 'Google Cloud Platform', 'Linux Administration', 'Monitoring Tools', 'Prometheus', 'Grafana', 'Nagios', 'Load Balancing', 'Infrastructure as Code', 'Microservices', 'Agile Methodology', 'Scrum', 'Kanban', 'Jira', 'Confluence', 'Git', 'GitHub', 'GitLab', 'Version Control', 'Automation Testing', 'Selenium', 'Cypress', 'JUnit', 'Load Testing', 'Performance Optimization', 'Spring', 'Spring Boot', 'Maven', 'React', 'HTML', 'CSS', 'TypeScript', 'HTML5', 'CSS3', 'Angular', 'Vue.js', 'Node.js', 'Express.js', 'Django', 'Flask', 'RESTful APIs', 'MySQL', 'Oracle', 'SQLite', 'Linux/Unix', 'Windows Server', 'macOS', 'Bitbucket', 'Ansible', 'Android Development (Java/Kotlin)', 'iOS Development (Swift)', 'Network Security', 'Ethical Hacking', 'Cryptography', 'Security Protocols', 'Penetration Testing', 'NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn', 'TensorFlow', 'PyTorch', 'Data Analysis', 'Natural Language Processing (NLP)', 'Sorting Algorithms', 'Searching Algorithms', 'Graph Theory', 'Dynamic Programming', 'Object-Oriented Programming (OOP)', 'Functional Programming', 'Event-Driven Programming', 'WebSockets', 'GraphQL', 'WebAssembly', 'Apache', 'Nginx', 'Tomcat', 'Jest', 'Continuous Integration', 'Continuous Deployment', 'OpenAPI', 'Postman', 'TCP/IP', 'DNS', 'HTTP/HTTPS', 'VPN', 'Ruby on Rails', 'Visual Studio Code', 'IntelliJ IDEA', 'Eclipse', 'Trello', 'GUI',
        # 'Python', 'Java', 'C++', 'JavaScript', 'C#', 'Ruby', 'Swift', 'Kotlin', 'Go', 'TypeScript', 'HTML5', 'CSS3', 'React', 'Angular', 'Vue.js', 'Node.js', 'Express.js', 'Django', 'Flask', 'RESTful APIs', 'SQL', 'MySQL', 'PostgreSQL', 'MongoDB', 'Oracle', 'SQLite', 'NoSQL', 'Linux/Unix', 'Windows Server', 'macOS', 'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Docker', 'Kubernetes', 'Jenkins', 'Ansible', 'Terraform', 'Amazon Web Services (AWS)', 'Microsoft Azure', 'Google Cloud Platform (GCP)', 'Android Development (Java/Kotlin)', 'iOS Development (Swift)', 'Network Security', 'Ethical Hacking', 'Cryptography', 'Security Protocols', 'Penetration Testing', 'NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn', 'TensorFlow', 'PyTorch', 'Data Analysis', 'Natural Language Processing (NLP)', 'Sorting Algorithms', 'Searching Algorithms', 'Graph Theory', 'Dynamic Programming', 'Agile', 'Scrum', 'Kanban', 'Object-Oriented Programming (OOP)', 'Functional Programming', 'Event-Driven Programming', 'WebSockets', 'GraphQL', 'WebAssembly', 'Apache', 'Nginx', 'Tomcat', 'JUnit', 'Selenium', 'Jest', 'Continuous Integration', 'Continuous Deployment', 'OpenAPI', 'Postman', 'TCP/IP', 'DNS', 'HTTP/HTTPS', 'VPN', 'Spring (Java)', 'Django (Python)', 'Ruby on Rails', 'Flask (Python)', 'Visual Studio Code', 'IntelliJ IDEA', 'Eclipse', 'Jira', 'Trello',  'GUI',

        # Management and Business
        'Project Management', 'Risk Management', 'Strategic Management', 'Business Administration', 
        'Marketing', 'Finance', 'Accounting', 'Entrepreneurship', 'Supply Chain Management', 'Logistics', 
        'Operations Management', 'Human Resources', 'Organizational Behavior', 'Corporate Communications',
        'Public Relations', 'Digital Marketing', 'SEO (Search Engine Optimization)', 'Content Marketing',
        'Affiliate Marketing', 'Brand Management', 'Customer Relationship Management (CRM)', 'Salesforce',
        'SAP', 'ERP Systems', 'Agile Project Management', 'Six Sigma', 'Lean Management', 'Process Improvement',
        
        # Social Sciences and Design
        'Psychology', 'Counseling', 'Social Work', 'Sociology', 'Anthropology', 'Political Science', 
        'International Relations', 'Urban Planning', 'Architecture', 'Interior Design', 'Landscape Architecture',
        'Graphic Design', 'User Experience (UX)', 'User Interface (UI)', 'UI', 'UX', 'UI/UX', 'UX/UI', 'User Experience' , 'User Interface', 'Digital Media', 'Animation',
        'Game Development', 'Film Studies', 'Media Production', 'Creative Writing', 'English Literature',
        'History', 'Philosophy', 'Theology', 'Religious Studies',

        # Environmental Sciences and Sustainability
        'Environmental Science', 'Climate Science', 'Meteorology', 'Geography', 'GIS (Geographic Information Systems)',
        'Remote Sensing', 'Green Technology', 'Ecology', 'Conservation Biology', 'Wildlife Biology', 
        'Zoology', 'Sustainability Studies', 'Renewable Energy Sources', 'Carbon Footprinting', 
        'Climate Modeling', 'Natural Resource Management', 'Biodiversity Studies',

        # Data and Analytics
        'Data Science', 'Data Analytics', 'Big Data Analytics', 'Hadoop', 'Spark', 'Kafka', 
        'Business Analytics', 'Data Warehousing', 'ETL Processes', 'Data Visualization', 'Tableau', 'Power BI',
        'Statistical Analysis', 'Regression Analysis', 'Machine Learning Algorithms', 'Deep Learning Frameworks',
        'TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn', 'Natural Language Toolkit (NLTK)', 
        'SpaCy', 'Data Preprocessing', 'Feature Engineering', 'Model Deployment',

        # Others
        'Library Science', 'Education Technology', 'E-learning Systems', 'Instructional Design', 
        'Curriculum Development', 'Health Informatics', 'Geoinformatics', 'Cartography', 'Fire Science',
        'Emergency Management', 'Forensic Science', 'Crime Scene Investigation', 'Telecommunications',
        'Optical Networks', 'Nanotechnology', 'Material Science', 'Space Exploration', 'Astronomy', 
        'Astrophysics', 'Oceanography', 'Marine Biology', 'Hydrology',
        'Computer Science', 'Information Technology', 'Software Engineering', 'Electrical Engineering', 
        'Mechanical Engineering', 'Civil Engineering', 'Chemical Engineering', 'Biomedical Engineering', 
        'Aerospace Engineering', 'Nuclear Engineering', 'Industrial Engineering', 'Systems Engineering',
        'Environmental Engineering', 'Petroleum Engineering', 'Geological Engineering', 'Marine Engineering', 
        'Robotics Engineering', 'Biotechnology', 'Biochemistry', 'Microbiology', 'Genetics', 'Molecular Biology', 
        'Bioinformatics', 'Neuroscience', 'Biophysics', 'Biostatistics', 'Pharmacology', 'Physiology', 'Anatomy',
        'Pathology', 'Immunology', 'Epidemiology', 'Public Health', 'Health Administration', 'Nursing', 'Medicine', 
        'Dentistry', 'Pharmacy', 'Veterinary Medicine', 'Medical Technology', 'Radiography', 'Physical Therapy', 
        'Occupational Therapy', 'Speech Therapy', 'Nutrition', 'Sports Science', 'Kinesiology', 'Exercise Physiology',
        'Sports Medicine', 'Rehabilitation Science'
    ]

    extracted_skills = extract_skills_from_resume(text, skills_list)

    if extracted_skills:
        print("Skills:", extracted_skills)
    else:
        print("No skills found")


    def extract_education_from_resume(text):
        education = []

        # List of education keywords to match against
        education_keywords = [
            'Computer Science', 'Information Technology', 'Software Engineering', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering',
            'Chemical Engineering', 'Biomedical Engineering', 'Aerospace Engineering', 'Nuclear Engineering', 'Industrial Engineering', 'Systems Engineering',
            'Environmental Engineering', 'Petroleum Engineering', 'Geological Engineering', 'Marine Engineering', 'Robotics Engineering', 'Biotechnology',
            'Biochemistry', 'Microbiology', 'Genetics', 'Molecular Biology', 'Bioinformatics', 'Neuroscience', 'Biophysics', 'Biostatistics', 'Pharmacology',
            'Physiology', 'Anatomy', 'Pathology', 'Immunology', 'Epidemiology', 'Public Health', 'Health Administration', 'Nursing', 'Medicine', 'Dentistry',
            'Pharmacy', 'Veterinary Medicine', 'Medical Technology', 'Radiography', 'Physical Therapy', 'Occupational Therapy', 'Speech Therapy', 'Nutrition',
            'Sports Science', 'Kinesiology', 'Exercise Physiology', 'Sports Medicine', 'Rehabilitation Science', 'Psychology', 'Counseling', 'Social Work',
            'Sociology', 'Anthropology', 'Criminal Justice', 'Political Science', 'International Relations', 'Economics', 'Finance', 'Accounting', 'Business Administration',
            'Management', 'Marketing', 'Entrepreneurship', 'Hospitality Management', 'Tourism Management', 'Supply Chain Management', 'Logistics Management',
            'Operations Management', 'Human Resource Management', 'Organizational Behavior', 'Project Management', 'Quality Management', 'Risk Management',
            'Strategic Management', 'Public Administration', 'Urban Planning', 'Architecture', 'Interior Design', 'Landscape Architecture', 'Fine Arts',
            'Visual Arts', 'Graphic Design', 'Fashion Design', 'Industrial Design', 'Product Design', 'Animation', 'Film Studies', 'Media Studies',
            'Communication Studies', 'Journalism', 'Broadcasting', 'Creative Writing', 'English Literature', 'Linguistics', 'Translation Studies',
            'Foreign Languages', 'Modern Languages', 'Classical Studies', 'History', 'Archaeology', 'Philosophy', 'Theology', 'Religious Studies',
            'Ethics', 'Early Childhood Education', 'Elementary Education', 'Secondary Education', 'Special Education', 'Higher Education',
            'Adult Education', 'Distance Education', 'Online Education', 'Instructional Design', 'Curriculum Development'
            'Library Science', 'Information Science', 'Computer Engineering', 'Software Development', 'Cybersecurity', 'Information Security',
            'Network Engineering', 'Data Science', 'Data Analytics', 'Business Analytics', 'Operations Research', 'Decision Sciences',
            'Human-Computer Interaction', 'User Experience Design', 'User Interface Design', 'Digital Marketing', 'Content Strategy',
            'Brand Management', 'Public Relations', 'Corporate Communications', 'Media Production', 'Digital Media', 'Web Development',
            'Mobile App Development', 'Game Development', 'Virtual Reality', 'Augmented Reality', 'Blockchain Technology', 'Cryptocurrency',
            'Digital Forensics', 'Forensic Science', 'Criminalistics', 'Crime Scene Investigation', 'Emergency Management', 'Fire Science',
            'Environmental Science', 'Climate Science', 'Meteorology', 'Geography', 'Geomatics', 'Remote Sensing', 'Geoinformatics',
            'Cartography', 'GIS (Geographic Information Systems)', 'Environmental Management', 'Sustainability Studies', 'Renewable Energy',
            'Green Technology', 'Ecology', 'Conservation Biology', 'Wildlife Biology', 'Zoology']

        for keyword in education_keywords:
            pattern = r"(?i)\b{}\b".format(re.escape(keyword))
            match = re.search(pattern, text)
            if match:
                education.append(match.group())

        return education

    extracted_education = extract_education_from_resume(text)
    if extracted_education:
        print("Education:", extracted_education)
    else:
        print("No education information found")

    import pickle

    resume_data = { 
        "skill":extracted_skills , "education":extracted_education
    }

    with open("resume_data.pkl","wb") as f:
        pickle.dump(text,f)

    return resume_data

if __name__ == "__main__":
    extract_skills()