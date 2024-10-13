from typing import Dict

def parse_query_dict(query_dict: Dict) -> Dict:
    query = {}
    for key, value in query_dict.items():
        query[key] = value[0]
    return query
