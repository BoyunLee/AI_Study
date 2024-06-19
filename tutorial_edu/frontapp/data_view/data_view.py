import seaborn as sns
import matplotlib.pyplot as plt

class Data_View :
    ### 클래스가 생성되는 시점에 아래 함수를 순서대로 실행하여 최종 이미지를 저장까지 해놓기
    # 클래스 생성자 정의하기
    def __init__(self) :
        self.initDataset_Load()
        self.data_preprocess()
        self.initVisualivation()
        self.saveFig()
        
    ### 데이터 읽어들이는 함수 정의
    def initDataset_Load(self) :
        self.ans = sns.load_dataset("anscombe")
        
    ### 데이터 분리하는 함수 정의
    def data_preprocess(self) :
        self.data1 = self.ans[self.ans["dataset"] == "I"]
        self.data2 = self.ans[self.ans["dataset"] == "II"]
        self.data3 = self.ans[self.ans["dataset"] == "III"]
        self.data4 = self.ans[self.ans["dataset"] == "IV"]
        
    ### 데이터 시각화 함수 정의
    def initVisualivation(self) :
        ### 한글처리
        plt.rc("font", family="Malgun Gothic")

        ### 마이너스 기호처리
        plt.rcParams["axes.unicode_minus"] = False
        
        ### 그래프 상위객체 변수 정의
        self.fig = plt.figure()
        
        ### 4개의 각 그래프가 들어갈 공간 만들기
        # add_subplot(행, 열, 순번)
        ax1 = self.fig.add_subplot(2, 2, 1)
        ax2 = self.fig.add_subplot(2, 2, 2)
        ax3 = self.fig.add_subplot(2, 2, 3)
        ax4 = self.fig.add_subplot(2, 2, 4)

        ### 각 그래프에 제목 넣기
        ax1.set_title("data1")
        ax2.set_title("data2")
        ax3.set_title("data3")
        ax4.set_title("data4")

        ### 각각의 그래프에 데이터 넣기
        ax1.plot(self.data1["x"], self.data1["y"], "o", c="b")
        ax2.plot(self.data2["x"], self.data2["y"], "o", c="r")
        ax3.plot(self.data3["x"], self.data3["y"], "o", c="g")
        ax4.plot(self.data4["x"], self.data4["y"], "o", c="y")

        ### 전체 제목 넣기
        self.fig.suptitle("Anscombe Data")

        ### 겹치는 부분에 대해서는 그래프 재정렬
        # 그래프를 모두 완성 후 가장 마지막에 한번만 수행
        self.fig.tight_layout()
        
    ### 시각화 그래프를 이미지로 저장하기
    def saveFig(self) :
        save_path = "./frontapp/static/frontapp/data_img/anscombe.png"
        self.fig.savefig(save_path)