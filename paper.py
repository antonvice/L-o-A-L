from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("paper.pdf", extract_images=True)
pages = loader.load()


from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
full = ''.join(page.page_content for page in pages)


from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

texts = text_splitter.create_documents([full])
print(len(texts))

for text in texts[:3]:
    print(text.page_content + "\n"+ "--****"*42 + "\n")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

text_splitter = SemanticChunker(embeddings)

docs = text_splitter.create_documents([''.join(page.page_content for page in texts)])

print(len(docs))

for doc in docs[:3]:
    print(doc.page_content + "\n"+ "==="*42 + "\n")