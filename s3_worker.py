#!/usr/bin/env python3
# poc2026dlpdetect
# Arquivo SINTETICO para validacao de Enterprise DLP - POC 2026 / Itau
# Todas as credenciais abaixo sao FALSAS (validas apenas em formato).

import boto3
import requests

# --- AWS service account credentials (sinteticas) ---
AWS_ACCESS_KEY_ID     = "AKIANRA82DCFXN8OQBLP"
AWS_SECRET_ACCESS_KEY = "vMblxEcDG6zxZORA0sUZdQ/gZzsKnxNqmgIzxdqx"
AWS_SESSION_TOKEN     = (
    "SxdSSEn+oCHj1omTLQw6xWhvl7wpCv+Zdp264sJryHNr3+9UTvciPHUmUArUP5QBU/5Cv4q4Fwu"
    "B8TYMgOIl0Y1I0d733zI7mBdBF+KhIQLNqD3g3fR5qZFPa83PRSLHwCO/gUlm4WG57Xls+9xD61"
    "oeCx66blom8KytUu/dWAbOxw2qmCibTrBac2S4yWIAiNQ4/pjJm+DW6iJ4Y74OPW6AhfmoYvoKZ"
    "khOfAQZbr1QIw/S"
)
AWS_REGION = "us-east-1"

# --- Service account bearer token (JWT sintetico) ---
SVC_ACCOUNT_TOKEN = (
    "eyJhbGciOiAiUlMyNTYiLCAidHlwIjogIkpXVCJ9."
    "eyJzdWIiOiAic3ZjLXBvYy1kbHBAaXRhdS5pbnRlcm5hbCIsICJpc3MiOiAicG9jIiwgInNjb3Bl"
    "IjogInN0b3JhZ2UucncifQ."
    "C819DKpOKB_WbRr5EsrEEWsYLx-t0DRf3Y9xiWMKEJ36WwSe-ZH668LQBQDLW8ELOKSH19tWNoYFXAkhJRzF8A"
)

# --- GitHub token (sintetico) ---
GITHUB_TOKEN = "ghp_HnXBb8YcYODkik6MvsLjntIktSBbnxqYXZQC"


def get_session():
    return boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=AWS_REGION,
    )


def sync_bucket(bucket: str):
    s3 = get_session().client("s3")
    for obj in s3.list_objects_v2(Bucket=bucket).get("Contents", []):
        print(obj["Key"])


def push_metrics(payload: dict):
    requests.post(
        "https://internal.metrics.itau/api/v1/ingest",
        headers={"Authorization": f"Bearer {SVC_ACCOUNT_TOKEN}"},
        json=payload,
        timeout=10,
    )


if __name__ == "__main__":
    sync_bucket("itau-poc-dlp-backup")
