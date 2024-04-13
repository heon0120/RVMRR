# RVMRR
Random Value Mean and Rule Report
## 프로그램 구성:


main.py: 생성된 난수를 이용하여 통계보고서를 생성합니다.




## 선행 조건

아래 사항들이 설치가 되어있어야합니다.

    python



## 사용 방법

1. 이 저장소를 GitHub에 복제합니다.

2. requirements.txt에 있는 라이브러리를 설치합니다.:


       pip install -r requirements.txt


3. main.py를 실행하여 생성된 난수들의 통계보고서를 생성합니다.:

       python main.py



## 기본값 설정
#### 난수생성 프로그램 연결

사용전, 아래 코드의 gen.py를 난수생성프로그램의 이름으로 변경합니다.:

    process = subprocess.Popen(["python", "gen.py"], stdout=subprocess.PIPE)
> [!Warning]
> 프로그램은 반드시 python이나 python3로 실행이 가능해야합니다.
> 
> python3로 실행해야한다면 위 코드의 python을 python3로 변경후 사용해야합니다.

#### 데이터수집시간 변경



    data_collection_time = 60

60은 1분을 의미하며, 이것을 수정하면 데이터 수집시간을 변경할수있습니다.
## 라이브러리

subprocess(기본설치)

time(기본설치)

matplotlib

fpdf

pandas


## 기여
소스 수정사항이 있다면 Pull requests 로 열어주세요.

## 라이센스
이 프로젝트는 MIT라이선스가 적용됩니다.
