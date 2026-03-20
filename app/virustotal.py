import requests
from django.conf import settings

class VirusTotalService:
    def __init__(self):
        self.headers = {"x-apikey": settings.VIRUSTOTAL_API_KEY}
        self.base_url = settings.VIRUSTOTAL_BASE_URL

    def scan_url(self, url):
        response = requests.post(
            f"{self.base_url}/urls",
            headers=self.headers,
            data={"url": url}
        )
        response.raise_for_status()
        analysis_id = response.json()["data"]["id"]
        return self.get_report(analysis_id)

    def get_report(self, analysis_id):
        response = requests.get(
            f"{self.base_url}/analyses/{analysis_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()