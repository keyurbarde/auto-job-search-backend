from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Initialize the BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Function to get the BERT embedding for a given text
def get_bert_embedding(text):
    # Tokenize and encode the text
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    # Get the model's output (the hidden states)
    with torch.no_grad():
        outputs = model(**inputs)
    # Get the embeddings of the [CLS] token (the first token in BERT)
    return outputs.last_hidden_state[:, 0, :].squeeze()

# Function to calculate cosine similarity between two texts
def calculate_similarity(text1, text2):
    # Get the BERT embeddings for both texts
    embedding1 = get_bert_embedding(text1)
    embedding2 = get_bert_embedding(text2)
    # Compute cosine similarity
    similarity = cosine_similarity([embedding1.numpy()], [embedding2.numpy()])
    return similarity[0][0]

# Function to get the most relevant job listings based on resume and job descriptions
def get_most_relevant_jobs(resume_data, job_listings, top_n=10):
    job_scores = []

    # Process each job listing
    for job in job_listings:
        job_title = job['Title']
        job_description = job['Description']

        # Access skills and education from resume_data dictionary
        resume_skills = ' '.join(resume_data.get('skill', []))  # Get skills from resume
        resume_education = ' '.join(resume_data.get('education', []))  # Get education from resume

        # Combine skills and education into a single resume description
        resume_full = resume_skills + ' ' + resume_education

        # Calculate similarity between the resume and the job title/description
        title_similarity = calculate_similarity(job_title, resume_full)
        description_similarity = calculate_similarity(job_description, resume_full)

        # Average the similarity scores for title and description
        total_similarity = (title_similarity + description_similarity) / 2
        job_scores.append((total_similarity, job))
        job['Score'] = total_similarity

    # Sort jobs by similarity score in descending order
    job_listings.sort(key=lambda x: x['Score'], reverse=True)

    # Return the top N jobs
    return job_listings

def calc_and_sort_jobs(skills):

    with open('resume_data.pkl', 'rb') as f:
        resume_data = pickle.load(f)

    resume_data['skill'] = skills

    with open('scraped_data.pkl', 'rb') as u:
        job_listings = pickle.load(u)

    top_jobs = get_most_relevant_jobs(resume_data, job_listings, top_n=10)

    print("Top 10 most relevant jobs:")
    for i, job in enumerate(top_jobs, start=1):
        print(f"{i}. {job['Score']}")

    return top_jobs

if __name__ == "__main__":
    calc_and_sort_jobs(['Machine Learning', 'Java', 'JavaScript', 'R', 'SQL', 'Git', 'GitHub', 'Spring', 'Spring Boot', 'Maven', 'React', 'HTML', 'CSS', 'Java', 'JavaScript', 'R', 'SQL', 'Git', 'GitHub', 'Spring', 'Spring Boot', 'Maven', 'React', 'HTML', 'CSS', 'MySQL', 'UI', 'UX', 'UI/UX', 'User Experience', 'Data Science', 'Machine Learning Algorithms', 'Data Preprocessing'])