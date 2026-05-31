from dataclasses import dataclass
from typing import overload
from tylon.src.domain.value_objects.vault_id import VaultID
from tylon.src.domain.value_objects.user_id import UserID
from datetime import datetime


@dataclass
class Vault:
    id: VaultID
    user_id: UserID
    name: str
    created_at: datetime
