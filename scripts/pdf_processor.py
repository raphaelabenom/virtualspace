import PyPDF2
from sentence_transformers import SentenceTransformer
from milvus_config import setup_milvus
import json

# Configuração do modelo de embedding
model = SentenceTransformer('all-MiniLM-L6-v2')

# Configuração do Milvus
collection = setup_milvus()

def process_pdf(pdf_path):
    # Extrair texto do PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Criar embedding
    embedding = model.encode(text).tolist()

    # Armazenar no Milvus
    collection.insert([
        [pdf_path],  # id
        [embedding],  # embedding
        [text],  # text
        [json.dumps({"source": pdf_path})]  # metadata
    ])

    # Garantir que os dados sejam persistidos
    collection.flush()

    print(f"Processado e armazenado: {pdf_path}")

# Exemplo de uso
process_pdf("caminho/para/seu/arquivo.pdf")

# Função para buscar documentos similares
def search_similar_documents(query_text, top_k=5):
    query_embedding = model.encode(query_text).tolist()
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["text", "metadata"]
    )

    for hits in results:
        for hit in hits:
            print(f"ID: {hit.id}, Distance: {hit.distance}")
            print(f"Text: {hit.entity.get('text')}")
            print(f"Metadata: {hit.entity.get('metadata')}")
            print("---")

# Exemplo de uso da busca
# search_similar_documents("Texto de consulta aqui")

