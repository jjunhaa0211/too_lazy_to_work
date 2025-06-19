# 1️⃣ rename_type_to_type.py 매뉴얼
| 예시 명령                                                                                               | 동작 설명                                     |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `python rename_type_to_type.py src`                                                                     | `src` 폴더 **하위 전부** `.js → .jsx`         |
| `python rename_type_to_type.py pages -f .ts -t .tsx`                                                    | `pages` 안 `.ts` → `.tsx`                     |
| `python rename_type_to_type.py ./main.c -f .c -t .cpp`                                                  | 단일 파일 `.c` → `.cpp`                       |
| `python rename_type_to_type.py . --non-recursive -f txt -t md`                                          | 현재 폴더만 `.txt` → `.md`                    |
| `python rename_type_to_type.py "/Users/junha/Desktop/jjunhaa/too_lazy_to_work" -f .log -t .bak`         | 공백 포함 경로 처리, `.log` → `.bak`          |

## 옵션
| 옵션                | 설명                                   | 기본값 |
| ------------------- | -------------------------------------- | ------ |
| `-f`, `--from`      | 원본 확장자                            | `.js`  |
| `-t`, `--to`        | 대상 확장자                            | `.jsx` |
| `--non-recursive`   | 하위 폴더를 검색하지 않음              | 재귀   |

## 출력 메시지

- `✅ old.ext → new.ext` : 변경 성공  
- `⚠️  *.newext already exists – skipped` : 같은 이름 파일 존재, 건너뜀  
- `❌  path rename failed: …` : 오류 이유 출력
- `❓  skipped: …` : 못찾음

# 2️⃣ `file_compare.py` 매뉴얼 (초간단)

## 📌 예시 명령

| 예시 명령                                                                                                      | 생성 파일 (4개)                                                  | 비고                                |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------- |
| `python file_compare.py A.txt B.txt`                                                                          | `only_in_A.txt`<br>`only_in_B.txt`<br>`common.txt`<br>`report.md` | 현재 폴더에 저장                    |
| `python file_compare.py dev.sql prod.sql -o ./compare_out`                                                    | 위 4개 파일을 `./compare_out` 폴더에                             | `.sql`·`.csv`·`.json` 등 텍스트 OK  |
| `python file_compare.py "/Users/junha/aaa.txt" "/Users/junha/bbb.txt" -o ~/diff`                              | `~/diff` 폴더에 저장                                              | 공백·한글 경로 그대로 사용 가능     |

---

## ⚙️ 옵션

| 옵션 / 플래그        | 기능                             | 기본값  |
| -------------------- | -------------------------------- | ------- |
| `-o`, `--out-dir`    | 결과 파일을 저장할 디렉터리 지정 | `.`     |

---

## ⚙️ 작동 방식

1. **줄 단위 비교** (공백만 있는 줄은 제외)
2. `common.txt`   : 두 파일 모두에 존재
3. `only_in_A.txt` : A에만 존재
4. `only_in_B.txt` : B에만 존재
5. `report.md`   : 줄 수와 Jaccard 유사도 포함 요약

---

## 📦 인코딩 자동 처리

- 기본: `UTF-8`
- 실패 시 자동으로 `Latin-1` 재시도
- 별도 옵션 없이 `.sql`, `.json`, `.csv` 등 **모든 텍스트 형식** 지원

---

✅ 실행 후 메시지:  
> `결과가 '…/compare_out' 에 생성되었습니다.`  
뜨면 정상 완료입니다!
```예제
python file_compare.py \
    "/Users/junha/Desktop/jjunhaa/too_lazy_to_work/develop.md" \ 
    "/Users/junha/Desktop/jjunhaa/too_lazy_to_work/operation.md" \  
    -o "/Users/junha/Desktop/jjunhaa/too_lazy_to_work/compare_out"
```
