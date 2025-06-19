#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import Iterable


def normalize(ext: str) -> str:
    """'.' 유무와 대소문자를 정리해 '.xxx' 형태로 반환."""
    ext = ext.lower()
    return ext if ext.startswith(".") else f".{ext}"


def rename_file(path: Path, from_ext: str, to_ext: str) -> None:
    """단일 파일의 확장자를 변경."""
    if path.suffix.lower() != from_ext:
        return

    new_path = path.with_suffix(to_ext)

    if new_path.exists():
        print(f"⚠️  {new_path} already exists – skipped")
        return

    try:
        path.rename(new_path)
        print(f"✅  {path} → {new_path}")
    except OSError as e:
        print(f"❌  {path} rename failed: {e}")


def iter_target_files(target: Path, from_ext: str, recursive: bool) -> Iterable[Path]:
    """파일/디렉터리에서 대상 확장자 파일을 찾아 반환."""
    if target.is_file():
        yield target
    elif target.is_dir():
        pattern = f"**/*{from_ext}" if recursive else f"*{from_ext}"
        yield from target.glob(pattern)
    else:
        print(f"❓  {target} is not a file or directory – skipped")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="지정 확장자를 다른 확장자로 일괄 변경 (.js → .jsx 등)"
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="파일 또는 디렉터리 경로(공백으로 구분)",
    )
    parser.add_argument(
        "-f",
        "--from",
        dest="from_ext",
        default=".js",
        help="변경 전 확장자(기본: .js)",
    )
    parser.add_argument(
        "-t",
        "--to",
        dest="to_ext",
        default=".jsx",
        help="변경 후 확장자(기본: .jsx)",
    )
    parser.add_argument(
        "--non-recursive",
        action="store_false",
        dest="recursive",
        help="디렉터리 하위 폴더를 재귀적으로 검색하지 않음",
    )

    args = parser.parse_args()
    from_ext = normalize(args.from_ext)
    to_ext = normalize(args.to_ext)

    if from_ext == to_ext:
        parser.error("from-ext와 to-ext가 같습니다. 다른 확장자를 지정하세요.")

    for raw in args.paths:
        for file in iter_target_files(
            Path(raw).expanduser().resolve(), from_ext, args.recursive
        ):
            rename_file(file, from_ext, to_ext)


if __name__ == "__main__":
    main()
