# Implementation without Langchain

#### LOADER

#* This is just a web based loader, 
#* need to implement other loaders


from bs4 import BeautifulSoup
import requests
from typing import List

def parse_page(url:str)-> List[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = [p.get_text() for p in soup.find_all('p')] 
    return paragraphs

pages = parse_page('https://lilianweng.github.io/posts/2023-06-23-agent/')

## TEXT SPLITTER
'''

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
)

texts = text_splitter.split_documents(pages)


'''

from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
# Load the Sentence Transformer model

model = SentenceTransformer('all-MiniLM-L6-v2')
# Encoding the texts
embeddings = model.encode(pages)

# Calculate distortions for a range of number of clusters
inertias = []
K = range(1, 10)
for k in K:
    kmeanModel = KMeans(n_clusters=k, random_state=42).fit(embeddings)
    inertias.append(kmeanModel.inertia_)
    print(kmeanModel.inertia_)

import numpy as np


def find_elbow(inertias):
    # Convert the inertia values to an array
    n_points = len(inertias)
    all_coords = np.vstack((range(n_points), inertias)).T
    
    # Get the line from the first to the last point
    first_point = all_coords[0]
    last_point = all_coords[-1]
    line_vec = last_point - first_point
    line_vec_norm = line_vec / np.sqrt(np.sum(line_vec**2))
    
    # Calculate the distance to the line for each point
    vec_from_first = all_coords - first_point
    scalar_product = np.sum(vec_from_first * line_vec_norm, axis=1)
    vec_from_first_parallel = np.outer(scalar_product, line_vec_norm)
    vec_to_line = vec_from_first - vec_from_first_parallel
    dist_to_line = np.sqrt(np.sum(vec_to_line ** 2, axis=1))
    
    # The point with the maximum distance to the line is the elbow
    idx_of_elbow = np.argmax(dist_to_line)
    
    return idx_of_elbow


elbow_index = find_elbow(inertias)
print("The optimal number of clusters (elbow point) is at index:", elbow_index)

def split_pages(pages:List[str], model)-> List[str]:
    embeddings = model.encode(pages)
    kmeans = KMeans(n_clusters=elbow_index, random_state=42)
    clusters = kmeans.fit_predict(embeddings)
    return [kmeans.cluster_centers_[i] for i in clusters]

splits = split_pages(pages, model)

import chromadb
client = chromadb.Client()

collection = client.get_or_create_collection("test_splits_2", metadata={"name": "test_splits_2"})

collection.add(
    documents = splits,
    metadatas=[{"source": "page"} for _ in splits],  # Create a metadata dict for each split
    ids = [f"split_{index}" for index ,_ in enumerate(splits)],
    embeddings=embeddings
)
results = collection.query(
    query_texts=["agents are"],
    n_results=2
)

#print out results between delimeters
print([doc for doc in results])
