# TED Insight Engine

TED Insight Engine is a content-based recommendation system designed to suggest relevant TED Talks using natural language processing techniques. The system analyzes textual content such as transcripts, descriptions, and tags to identify semantic similarities between talks and provide meaningful recommendations.

---

## Overview

This project implements an intelligent recommendation pipeline that combines textual similarity with audience engagement metrics. By leveraging TF-IDF vectorization and cosine similarity, the system identifies related talks and ranks them based on both content relevance and popularity.

---

## Key Features

- Content-based recommendation using NLP techniques  
- TF-IDF vectorization for feature extraction  
- Cosine similarity for measuring semantic closeness  
- Weighted ranking incorporating view counts  
- Interactive web interface built with Streamlit  
- Structured output displaying title, speaker, and views  

---

## Methodology

1. **Data Preparation**  
   The dataset includes TED Talk metadata such as titles, descriptions, transcripts, tags, speakers, and view counts. Relevant textual features are combined into a unified representation.

2. **Text Preprocessing**  
   Text data is cleaned by converting to lowercase, removing special characters, eliminating stopwords, and applying lemmatization.

3. **Feature Engineering**  
   The processed text is transformed into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency).

4. **Similarity Computation**  
   Cosine similarity is used to compute similarity scores between talks based on their vector representations.

5. **Ranking Strategy**  
   A weighted scoring mechanism is applied to balance content similarity (80%) and popularity based on views (20%).


## Installation and Setup

1. Clone the repository:

git clone https://github.com/your-username/ted-insight-engine.git

cd ted-insight-engine

2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

streamlit run app.py

2. Usage

This explains how to use your app after running it.

## Usage

- Open the application in your browser  
- Select a TED Talk from the dropdown menu  
- Click on "Generate Recommendations"  
- The system will display a list of similar talks  
3. System Design ← THIS is what makes you stand out

Most people skip this. That’s why most projects look weak.

## System Design

The system follows a content-based recommendation approach:

- Text data from transcripts, descriptions, and tags is combined  
- TF-IDF vectorization converts text into numerical vectors  
- Cosine similarity measures similarity between talks  
- A weighted scoring system ranks results using similarity and views  

This ensures both relevance and practical ranking of recommendations.
4. Technologies Used
## Technologies Used

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- Natural Language Processing (NLP)
5. Limitations ← THIS makes you look honest and smart
## Limitations

- Does not consider user preferences or personalization  
- Popularity bias due to view-based ranking  
- TF-IDF cannot capture deep semantic meaning  
6. Future Improvements
## Future Improvements

- Use advanced models like BERT or embeddings  
- Deploy as a public web application  
- Add thumbnails and richer UI  
- Combine with collaborative filtering  
7. Conclusion
## Conclusion

This project demonstrates how NLP techniques can be applied to build an effective recommendation system for content discovery.
