#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import Set

def safe_read_text(path: Path, encoding: str = "utf-8") -> str:
    """`encoding` 으로 읽되 실패하면 latin-1 로 재시도."""
    try:
        return path.read_text(encoding=encoding)
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def read_lines(path: Path) -> Set[str]:
    """파일을 읽어 공백 없는 줄 집합 반환."""
    return {ln.strip() for ln in safe_read_text(path).splitlines() if ln.strip()}


def write_list(path: Path, lines: Set[str]) -> None:
    path.write_text("\n".join(sorted(lines)), encoding="utf-8")


def write_report(
    path: Path,
    a_name: str,
    b_name: str,
    a_len: int,
    b_len: int,
    common_cnt: int,
    uniq_a: int,
    uniq_b: int,
) -> None:
    union_cnt = common_cnt + uniq_a + uniq_b
    jaccard = 0 if union_cnt == 0 else common_cnt / union_cnt
    md = f"""# 파일 비교 결과

| 항목 | 값 |
|------|----|
| 파일 A | `{a_name}` |
| 파일 B | `{b_name}` |
| A 줄 수 | {a_len} |
| B 줄 수 | {b_len} |
| 공통 줄 수 | {common_cnt} |
| A 전용 줄 수 | {uniq_a} |
| B 전용 줄 수 | {uniq_b} |
| **Jaccard 유사도** | **{jaccard:.4f}** |

> *생성: `file_compare.py`*
"""
    path.write_text(md, encoding="utf-8")


# ───────────────────────────── main ──────────────────────────────
def main() -> None:
    ap = argparse.ArgumentParser(
        description="두 텍스트(형식) 파일을 비교해 차이·공통·리포트 생성"
    )
    ap.add_argument("file_a", help="첫 번째 파일 경로")
    ap.add_argument("file_b", help="두 번째 파일 경로")
    ap.add_argument(
        "-o", "--out-dir", default=".", help="결과 파일 저장 폴더 (기본: 현재 폴더)"
    )
    args = ap.parse_args()

    a_path, b_path, out_dir = Path(args.file_a), Path(args.file_b), Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    set_a, set_b = read_lines(a_path), read_lines(b_path)

    common = set_a & set_b
    only_a = set_a - set_b
    only_b = set_b - set_a

    write_list(out_dir / "only_in_A.txt", only_a)
    write_list(out_dir / "only_in_B.txt", only_b)
    write_list(out_dir / "common.txt", common)
    write_report(
        out_dir / "report.md",
        a_path.name,
        b_path.name,
        len(set_a),
        len(set_b),
        len(common),
        len(only_a),
        len(only_b),
    )
    print(f"✅ 결과가 '{out_dir.resolve()}' 에 생성되었습니다.")


if __name__ == "__main__":
    main()
