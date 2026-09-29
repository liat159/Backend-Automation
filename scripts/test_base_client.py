from core.api.base_client import BaseClient

client = BaseClient()

response = client.get("/health")

print(response.status_code)
print(response.text)
