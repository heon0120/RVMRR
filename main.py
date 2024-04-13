import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import time
from fpdf import FPDF

def collect_and_analyze_data(data_collection_time, csv_filename, pdf_filename):
    # 데이터 수집
    gen_results = []
    end_time = time.time() + data_collection_time
    while time.time() < end_time:
        process = subprocess.Popen(["python", "gen.py"], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        try:
            gen_result = float(output.decode("utf-8"))  # Handle both integers and decimals
        except ValueError:
            print("난수생성 코드에서 출력된값에의해 디코딩오류가 발생하였습니다.")
            continue
        gen_results.append(gen_result)

    # 데이터 저장
    df = pd.DataFrame({"gen_result": gen_results})
    df.to_csv(csv_filename, index=False)

    # 데이터 분석
    analyze_data(df, pdf_filename)

def analyze_data(df, pdf_filename):
    # 난수분포분석
    df["gen_result"].hist(bins=20)
    plt.xlabel("Random Number")
    plt.ylabel("Frequency")
    plt.title("Random Number Distribution")
#    plt.show()  # 히스토그램 표시- 보고서만 저장할거면 앞에주석을 삭제하세요.

    # 난수통계분석
    mean = df["gen_result"].mean()
    std_dev = df["gen_result"].std()

    # 빈도분석
    frequency_table = df["gen_result"].value_counts()
    most_frequent_number = frequency_table.idxmax()
    most_frequent_count = frequency_table.max()

    # PDF 보고서를 생성
    generate_pdf_report(pdf_filename, most_frequent_number, most_frequent_count, mean, std_dev, df)

def generate_pdf_report(pdf_filename, most_frequent_number, most_frequent_count, mean, std_dev, df):
    # FPDF 개체 생성 및 설정
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)

    pdf.cell(40, 10, "난수 분석 보고서")

    pdf.ln()

    # 복수랜덤 번호 정보 추가
    pdf.set_font("Arial", "", 12)
    pdf.cell(40, 10, "Most Frequent Number:")
    pdf.cell(0, 10, str(most_frequent_number))

    pdf.ln()

    pdf.cell(40, 10, "Frequency Count:")
    pdf.cell(0, 10, str(most_frequent_count))
    pdf.ln()

    # 통계정보 추가
    pdf.cell(40, 10, "Mean:")
    pdf.cell(0, 10, f"{mean:.2f}")

    pdf.ln()

    pdf.cell(40, 10, "Standard Deviation:")
    pdf.cell(0, 10, f"{std_dev:.2f}")

    pdf.ln()

    # 히스토그램 추가
    fig = plt.figure()
    df["gen_result"].hist(bins=20)
    plt.xlabel("Random Number")
    plt.ylabel("Frequency")
    plt.title("Random Number Distribution")
    fig.savefig("histogram.png")  # Save histogram to temporary file

    # PDF에 히스토그램 이미지 추가
    pdf.image("histogram.png", w=180, h=100)

    # mataplotlib 닫기
    plt.close(fig)

    # PDF 보고서 생성
    pdf.output(pdf_filename)

# 데이터 수집 시간(초) 
data_collection_time = 60  # 수집시간

# CSV 파일저장
csv_filename = "gen_results.csv"

# PDF 파일저장
pdf_filename = "random_number_analysis.pdf"

# 데이터 수집 및 분석
collect_and_analyze_data(data_collection_time, csv_filename, pdf_filename)

if __name__ == "__main__":
    # 스크립트를 직접 실행하는 경우 데이터 수집 및 분석
    collect_and_analyze_data(data_collection_time, csv_filename, pdf_filename)
