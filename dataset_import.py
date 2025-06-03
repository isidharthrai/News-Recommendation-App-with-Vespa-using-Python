import requests, json

data = json.loads(
    requests.get("https://thigm85.github.io/data/mind/mind_demo_fields_parsed.json").text
)

print(data)