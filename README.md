| 일하기 싫으니까 자동화 돌려야지~~

# rename_type_to_type.py 간단 매뉴얼

## 사용 예시

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
