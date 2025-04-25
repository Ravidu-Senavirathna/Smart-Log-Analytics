from collections import Counter


class AnalyticsEngine:

    @staticmethod
    def top_errors(logs):

        errors = [
            log.message
            for log in logs
            if log.level == "ERROR"
        ]

        return Counter(errors).most_common(5)

    @staticmethod
    def top_users(logs):

        users = [log.user for log in logs]

        return Counter(users).most_common(5)