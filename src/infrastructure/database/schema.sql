CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,

    password_hash TEXT NOT NULL,

    password_salt TEXT,

    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    last_login TEXT
);

CREATE TABLE vaults (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,

    name TEXT NOT NULL,

    created_at TEXT NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vault_id INTEGER NOT NULL,

    site TEXT NOT NULL,
    username TEXT NOT NULL,

    password_encrypted BLOB NOT NULL,

    notes TEXT,

    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT,

    FOREIGN KEY (vault_id) REFERENCES vaults(id)
        ON DELETE CASCADE
);

CREATE INDEX idx_users_username ON users(username);

CREATE INDEX idx_vaults_user_id ON vaults(user_id);

CREATE INDEX idx_credentials_vault_id ON credentials(vault_id);

CREATE INDEX idx_credentials_site ON credentials(site);