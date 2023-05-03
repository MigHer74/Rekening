CREATE TABLE IF NOT EXISTS 'names' (
    id VARCHAR(6) PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS 'documents' (
    id_doc VARCHAR(6) PRIMARY KEY,
    doc_document VARCHAR(6),
    doc_date DATE,
    doc_amount FLOAT
);

CREATE TABLE IF NOT EXISTS 'vault' (
    id_vault INTEGER PRIMARY KEY AUTOINCREMENT,
    val_id VARCHAR(6),
    val_document VARCHAR(6),
    val_date DATE,
    val_amount FLOAT
);