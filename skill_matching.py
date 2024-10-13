from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_skills(user_skills, job_descriptions):
    # Combine user skills into a single string
    user_skills_str = " ".join(user_skills)

    # Check for empty descriptions
    if not job_descriptions or len(job_descriptions) == 0:
        print("No job descriptions found.")
        return []

    # Add user skills to job descriptions for TF-IDF analysis
    all_descriptions = job_descriptions + [user_skills_str]
    

    # Create TF-IDF vectorizer and fit_transform the combined descriptions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_descriptions)

    # Check the shape of the tfidf_matrix
    print("TF-IDF Matrix shape:", tfidf_matrix.shape)

    # Ensure that the user skills are not empty before computing similarity
    if user_skills_str.strip() == "":
        print("No user skills extracted.")
        return []

    # Calculate cosine similarity between user skills and job descriptions
    similarity_scores = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1]).flatten()
    
    return similarity_scores
