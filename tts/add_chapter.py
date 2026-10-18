#!/usr/bin/env python3
"""episodes.json に章を追加する（長さは音声ファイルから測る）。

使い方:
  python3 tts/add_chapter.py 02_ise "第2章　かなわぬ恋" 02-01:関守よ、眠っておくれ 02-02:月やあらぬ ...
同じ章名がすでにあれば、中身を置き換える。
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(ROOT / path)], capture_output=True, text=True, check=True)
    return round(float(out.stdout))


def main():
    program_id, chapter_title, *blocks = sys.argv[1:]
    path = ROOT / "episodes.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    program = next(p for p in data["programs"] if p["id"] == program_id)
    chapter = {"title": chapter_title, "blocks": []}
    for b in blocks:
        key, title = b.split(":", 1)
        f = f"audio/{program_id}/{key}.mp3"
        chapter["blocks"].append({"title": title, "file": f, "duration": duration(f)})
    chapters = program["chapters"]
    for i, c in enumerate(chapters):
        if c["title"] == chapter_title:
            chapters[i] = chapter
            break
    else:
        chapters.append(chapter)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(chapter_title, [b["duration"] for b in chapter["blocks"]])


if __name__ == "__main__":
    main()
