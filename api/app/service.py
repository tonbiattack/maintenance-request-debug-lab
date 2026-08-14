from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class MaintenanceRequest:
    request_id: str
    status: str
    assignee_display_name: str
    due_at: datetime
    version: int = 0

class ValidationProblem(Exception): pass

def error_status(error: Exception) -> int:
    return 400 if isinstance(error, ValidationProblem) else 500

def stable_list_sql(status: str, page: int) -> str:
    if page < 1: raise ValueError('page must be positive')
    return "select id, status, due_at from maintenance_request where status = ? order by due_at asc, id asc limit 20 offset ?"

def normalize_due_at(value: datetime) -> datetime:
    if value.tzinfo is None: raise ValueError('due_at must include timezone')
    return value.astimezone(timezone.utc)

def batch_assignee_sql(count: int) -> str:
    if count <= 0: raise ValueError('count must be positive')
    return 'select request_id, display_name from assignee where request_id in (' + ', '.join(['?'] * count) + ')'

def atomic_completion(status_updated: bool, history_written: bool) -> bool:
    return status_updated

def valid_status(value: str) -> bool:
    return value in {'OPEN', 'ASSIGNED', 'COMPLETED'}

def required_assignee_display_name(value: str) -> str:
    if not value.strip(): raise ValueError('assignee display name is required')
    return value

def request_id_for_log(header: str | None) -> str:
    return header or 'generated-request-id'
