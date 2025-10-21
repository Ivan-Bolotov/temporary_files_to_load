import requests
from pathlib import Path


def to_csv(what, to, index=False, sep=',') -> Path:
    url = "https://example.com/file.zip"
    dest = to
    chunk_size = 8192
    timeout = 10
    dest_path = Path(dest)
    dest_path.parent.mkdir(parents=True, exist_ok=True) if dest_path.suffix else dest_path.mkdir(parents=True, exist_ok=True)
    if dest_path.is_dir() or not dest_path.suffix:
        filename = Path(url.split("?")[0]).name or "downloaded.file"
        dest_path = dest_path / filename if dest_path.is_dir() else Path(dest) / filename

    try:
        with requests.get(url, stream=True, timeout=timeout) as r:
            r.raise_for_status()
            total = int(r.headers.get("content-length", 0))
            downloaded = 0
            with open(dest_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if not chunk:
                        continue
                    f.write(chunk)
                    downloaded += len(chunk)
        return dest_path
    except requests.RequestException as e:
        if dest_path.exists():
            try:
                dest_path.unlink()
            except Exception:
                pass
        raise RuntimeError(f"Ошибка при скачивании {url}: {e}") from e
