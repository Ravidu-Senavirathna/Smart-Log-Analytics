from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: str
    level: str
    user: str
    message: str
    server: str

