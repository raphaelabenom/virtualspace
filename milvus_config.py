from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType

def setup_milvus():
    # Conectar ao Milvus
    connections.connect(
        alias="default", 
        host="localhost",  # Ajuste conforme necessário
        port="19530"  # Porta padrão do Milvus
    )

    # Definir o schema da coleção
    fields = [
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),  # 384 é a dimensão do modelo 'all-MiniLM-L6-v2'
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
        FieldSchema(name="metadata", dtype=DataType.JSON)
    ]
    schema = CollectionSchema(fields, "Coleção de embeddings de PDFs")

    # Criar a coleção
    collection = Collection("pdf_embeddings", schema)

    # Criar um índice para buscas eficientes
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 1024}
    }
    collection.create_index(field_name="embedding", index_params=index_params)

    return collection

