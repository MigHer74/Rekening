CREATE TABLE IF NOT EXISTS 'company' (
    id_com INTEGER PRIMARY KEY,
    com_name VARCHAR(50) NOT NULL,
    com_init_rec INTEGER NOT NULL,
    com_init_doc VARCHAR(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS 'receiver' (
    id_rec VARCHAR(6) PRIMARY KEY,
    rec_name VARCHAR(50),
    rec_active BOOL DEFAULT 1
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