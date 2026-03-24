import requests
import time


VIRUSTOTAL_API_KEY = 'XXXXXXXXXXXXXXXXXXXXX' 
VIRUSTOTAL_BASE_URL = 'https://www.virustotal.com/api/v3'

class VirusTotalService:
    def __init__(self):
        self.headers = {"x-apikey":VIRUSTOTAL_API_KEY}
        self.base_url = VIRUSTOTAL_BASE_URL

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
        for _ in range(10):  # numero de tentativas
            response = requests.get(
                f"{self.base_url}/analyses/{analysis_id}",
                headers=self.headers
            )
            response.raise_for_status()
            result = response.json()

            status = result["data"]["attributes"]["status"]
            if status == "completed":
                return result
            
            time.sleep(2)

        return result 