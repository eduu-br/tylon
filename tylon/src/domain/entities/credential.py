from dataclasses import dataclass
from datetime import datetime


@dataclass
class Credential:
    id: int
    vault_id: int
    title: str
    username: str
    password_encrypted: str
    notes: str
    created_at: datetime
    updated_at: datetime

    def to_tuple(self):
        return (
            self.id,
            self.vault_id,
            self.title,
            self.username,
            self.password_encrypted,
            self.notes,
            self.created_at,
            self.updated_at,
        )
