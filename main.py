from app.parser.log_parser import LogParser

logs = LogParser.load_logs("data/sample_log.txt")

for log in logs:
    print(log)