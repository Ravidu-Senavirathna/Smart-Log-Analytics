from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: str
    level: str
    user: str
    message: str
    server: str


class LogParser:

    @staticmethod
    def parse_line(line: str):
        parts = line.strip().split()

        return LogEntry(
            timestamp=parts[0],
            level=parts[1],
            user=parts[2],
            message=parts[3],
            server=parts[4]
        )

    @staticmethod
    def load_logs(filepath):
        logs = []

        with open(filepath, "r") as f:
            for line in f:
                logs.append(LogParser.parse_line(line))

        return logs