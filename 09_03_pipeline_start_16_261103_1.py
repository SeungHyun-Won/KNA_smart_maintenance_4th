"""ICT 검사 CSV 처리 파이프라인 — 교육생 실습 시작 코드.

1단계부터 6단계까지 완성할 때마다 RUN_TO_STEP을 하나씩 올리세요.
PPT의 실습 1~6과 함수가 대응합니다. 추가 패키지는 필요하지 않습니다.
"""
import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "09_ict_inspection_dirty_15_261102_2.csv"
REPORT_PATH = BASE / "09_03_pipeline_report.txt"
RUN_TO_STEP = 6  # 실습 1 완성 후 2, ... 6으로 변경


def read_csv_data(path):
    """[실습 1] (헤더 리스트, 데이터 행 리스트) 반환. 파일이 없으면 ([], [])."""
    # TODO: try / with open / csv.reader / next / list 사용
    # 파일이 없으면 FileNotFoundError를 처리하세요.
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = list(reader)
    except FileNotFoundError:
        print("파일없음: ", path)
        rows = []
        header = []
    return header, rows

def group_by_part(rows):
    """[실습 2] ({부품명: [행, ...]}, 부품명 빈 행의 수) 반환."""
    by_part = {} ### 빈 딕셔너리 생성
    dropped = 0
    for row in rows:
        try:
            part = row[1].strip() ### csv파일에서 부품명 가져옴
        except IndexError:
            dropped += 1
            continue
        if part == "":
            dropped += 1
            continue
        # by_part.setdefault(part, []).append(row) >>> 아래 if문 + append문과 동일한 내용임.
        if part not in by_part:
            by_part[part] = [] ### {"part" : []} 생성
        by_part[part].append(row) ### []에 row를 넣음, if문 안에 있을경우 부품명이 처음 나올때만 row 넣음.
                                  ### append사용이유: list안에 row를 넣는거니까
    return by_part, dropped



def calc_stats(rows, column=2):
    """[실습 3] {'count', 'mean', 'max', 'min'} 딕셔너리 또는 None 반환."""
    # TODO: float(row[column])로 숫자를 모으고 변환 실패/짧은 줄은 제외
    # 숫자가 없다면 None을 반환하세요.
    values = []
    for row in rows:
        try:
            values.append(float(row[column]))
        except (IndexError, ValueError):
            continue
    if len(values) == 0:
        return None  ### 함수(cal_stats())의 결과가 None이 되는거임.
    return {"count" : len(values), "mean" : round(sum(values) / len(values), 2), 
            "max" : max(values), "min" : min(values)}


def filter_valid_rows(rows, lo=0.0, hi=5000.0):
    """[실습 4] (유효 행 리스트, [(CSV 줄 번호, 검사ID, 사유), ...]) 반환."""
    # TODO: 0~5000 범위 검증, -999는 직접 raise ValueError
    # float 변환 오류와 IndexError를 처리하고 줄 번호/사유를 남기세요.
    # enumerate(rows, start=2)로 헤더 다음 줄부터 세어보세요.
    valid = []
    rejected = []
    for line_no, row in enumerate(rows, start=2):  ### enumerate >> line_number, 값을 함께 꺼내는 함수
                                                   ### start=2는 번호를 2부터 매기라는 뜻(header라인은 rows에서 제외됐음) 
        try:
            value = float(row[2])
            if value < lo or value > hi:
                raise ValueError(f"범위 밖 값 {value}") ### raise >> 해당 except로 이동 >> continue 필요없음.
                                                       ### 괄호 안 >> 오류메시지(내가 적은게 e로 저장되는방식)
        except ValueError as e:
            rejected.append((line_no, row[0], str(e)))  ### as e 없이는 오류메시지 출력 불가.
            continue
        except IndexError:
            rejected.append((line_no, row[0], "측정값 열 없음"))
            continue
        valid.append(row)
    return valid, rejected


def save_report(path, total_rows, valid_rows, rejected, stats):
    """[실습 5] 리포트 텍스트 파일 저장."""
    # TODO: 전체/유효/제외 건수, 측정값 평균/최대/최소를 lines에 모으고
    # with open(path, 'w', encoding='utf-8')로 저장하세요.
    # 원본에 측정값의 물리 단위가 없으므로 임의로 '도'를 붙이지 마세요.
    
    # lines = ["ICT 검사 데이터 리포트", 
    #          f"전체 {total_rows}행 / 유효 {len(valid_rows)}건 / 제외 {len(rejected)}건", 
    #          f"측정값 평균 {stats['mean']} / 최대 {stats['max']} / 최소 {stats['min']}"]
    lines = []
    lines.append("ICT 검사 데이터 리포트")
    lines.append(f"전체 {total_rows}행 / 유효 {len(valid_rows)}건 / 제외 {len(rejected)}건")
    if stats is None:
        lines.append("측정값 통계: 유효한 숫자 없음")
    else:
        lines.append(f"측정값 평균 {stats['mean']} / 최대 {stats['max']} / 최소 {stats['min']}")
    lines.append("제외 내역:")
    for line_no, inspect_id, reason in rejected:  ### 튜플 3개를 언패킹
        lines.append(f"  {line_no}행 / 검사ID {inspect_id} / {reason}") ### "20행 / 검사ID 9004 / 측정값 열 없음"의
                                                                       ### 문자열 형태로 lines에 저장됨
    with open(path, "w", encoding="utf-8") as f: ### UTF-8 텍스트로 저장
        f.write("\n".join(lines))  ### lines의 문자열 사이에 "\n"을 끼워서 이어 붙인다. <<< "\n".join(lines)


def verify_part_counts(valid_rows):
    """[실습 6] 유효 행을 부품별로 다시 묶고 합계가 전체와 같은지 확인."""
    # TODO: group_by_part(valid_rows)를 재사용하고
    # 각 부품에 calc_stats(part_rows, 2)를 적용해 건수를 합산하세요.
    by_part, dropped = group_by_part(valid_rows)        # ② 정제된 valid로 다시 분류 (실습 2 재사용)
    check_sum = 0
    for part, part_rows in by_part.items():             # 부품명, 그 부품의 행 목록
        stats = calc_stats(part_rows, 2)                # ③ 부품별 통계 (실습 3 재사용)
        if stats is None:                               # 숫자가 없는 부품 대비
            continue
        print(f"    {part}: {stats['count']}건 / 평균 {stats['mean']}")
        check_sum += stats["count"]                     # ④ count 합산
    result = check_sum == len(valid_rows)               # ⑤ 합계와 전체 비교 → True / False
    print(f"[6단계] 부품별 합계 {check_sum} = 유효 {len(valid_rows)} → {result}")
    return result


def main():
    header, rows = read_csv_data(DATA_PATH)
    print(f"[1단계] 헤더 {len(header)}개 / 데이터 {len(rows)}행")
    if RUN_TO_STEP == 1:
        return

    by_part, dropped = group_by_part(rows)
    print(f"[2단계] 부품 {len(by_part)}종 / 부품명 누락 {dropped}행")
    if RUN_TO_STEP == 2:
        return

    before = calc_stats(rows, 2)
    print(f"[3단계] 범위 검증 전 통계: {before}")
    if RUN_TO_STEP == 3:
        return

    valid, rejected = filter_valid_rows(rows)
    after = calc_stats(valid, 2)
    print(f"[4단계] 유효 {len(valid)}건 / 제외 {len(rejected)}건")
    for item in rejected:
        print("    제외:", item)
    if RUN_TO_STEP == 4:
        return

    save_report(REPORT_PATH, len(rows), valid, rejected, after)
    print(f"[5단계] 리포트 생성: {REPORT_PATH.name}")
    if RUN_TO_STEP == 5:
        return

    verify_part_counts(valid)


if __name__ == "__main__":
    main()
