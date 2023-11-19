import datetime
import pandas 
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dags_bash_operator",  #airflow 화면에서 보이는 이름들(파이썬 파일명과 상관없지만 일치시키는것이 좋음)
    schedule="0 0 * * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),      #UTC는 세계표준시간으로 우리나라보다 9시간 느림
    catchup=False,      #False일 경우 현재날짜부터, True일경우 start_date부터 시작. but 사이 구간은 차례로 돌지 않고 한꺼번에 돌게 됨(보통 False)
    #dagrun_timeout=datetime.timedelta(minutes=60),     #일정시간 이상 경과하면 실패 처리
    #tags=["example", "example2"],      #airflow 화면 리스트에서 밑에 파란색박스에 보이는 값들. 특정 태그만 화면에 나오게 할 수도 있음.
    #params={"example_key": "example_value"},       #태스크에 공통적으로 넘겨줄 파라미터?
) as dag:
		#task 객체명
    bash_t1 = BashOperator(
        task_id="bash_t1",       #dag 그래프에 표현되는 ID, 객체명과 일치하도록
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",       #dag 그래프에 표현되는 ID, 객체명과 일치하도록
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2