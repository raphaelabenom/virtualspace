from transformers import AutoTokenizer, AutoModel
import torch
from PyPDF2 import PdfReader
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Função para extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Função para gerar embedding
def get_embedding(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# Lista de modelos para comparar
models_to_compare = [
    "neuralmind/bert-base-portuguese-cased",
    "ricardo-filho/bert-portuguese-cased-nli-assin-2",
    "xlm-roberta-large",
    "bert-base-multilingual-cased"
]

# Carregar contratos de exemplo
contract1 = extract_text_from_pdf("contrato1.pdf")
contract2 = extract_text_from_pdf("contrato2.pdf")
query = "Cláusula de rescisão"

results = {}

for model_name in models_to_compare:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    
    # Gerar embeddings
    embedding1 = get_embedding(contract1, model, tokenizer)
    embedding2 = get_embedding(contract2, model, tokenizer)
    query_embedding = get_embedding(query, model, tokenizer)
    
    # Calcular similaridade
    similarity1 = cosine_similarity([query_embedding], [embedding1])[0][0]
    similarity2 = cosine_similarity([query_embedding], [embedding2])[0][0]
    
    results[model_name] = {
        "similarity_contract1": similarity1,
        "similarity_contract2": similarity2
    }

# Imprimir resultados
for model_name, result in results.items():
    print(f"Modelo: {model_name}")
    print(f"Similaridade com Contrato 1: {result['similarity_contract1']:.4f}")
    print(f"Similaridade com Contrato 2: {result['similarity_contract2']:.4f}")
    print("---")

