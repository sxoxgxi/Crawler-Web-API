from urllib.parse import urlparse


def subdomain(url: str) -> str:
    try:
        return urlparse(url).netloc
    except Exception as uwu:
        return ""


def domain(url: str) -> str:
    try:
        res = subdomain(url)
        output = res.split('.')
        return f"{output[-2]}.{output[-1]}"
    except Exception as uwu:
        return ""
