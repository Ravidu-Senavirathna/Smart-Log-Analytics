import heapq
from collections import Counter


def top_k_users(logs, k=3):

    counts = Counter(
        log.user
        for log in logs
    )

    return heapq.nlargest(
        k,
        counts.items(),
        key=lambda x: x[1]
    )