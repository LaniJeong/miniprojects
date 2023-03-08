# Qt Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverAPI import NaverApi
from urllib.request import urlopen
import webbrowser   # 웹브라우저 모듈


class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApi_movie.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/newspaper.png'))          # 아이콘

        # 검색버튼 클릭시그널 / 슬롯함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 검색어 입력 후 엔터를 치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        # self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)       # 더블 클릭했을때
    
    def tblResultDoubleClicked(self):
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text()       # url 링크컬럼 변경
        webbrowser.open(url)   # 네이버 영화 웹

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self, '경고', '영화명을 입력하세요!')
            return
        else:
            api = NaverApi() # NaverAPI 클래스 객체 생성
            node = 'movie'    # movie로 변경하면 영화검색
            display = 100

            result = api.get_naver_search(node, search, 1, display)
            print(result)
            # 리스트뷰에서 출력
            items = result['items'] # json결과 중 items 아래 배열만 추출
            self.makeTable(items)   # 테이블위젯에 데이터들을 할당 함수

    # 테이블 위젯에 데이터 표시 -- 네이버 영화 결과에 맞춰
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)      # 단일선택
        self.tblResult.setColumnCount(7)        # 컬럼갯수 변경
        self.tblResult.setRowCount(len(items))      # 현재 100개 행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 60)
        self.tblResult.setColumnWidth(4, 50)
        # 컬럼 데이터를 수정금지
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)


        for i, post in enumerate(items):     # 0, 뉴스 ...
            num = i + 1     # 뉴스번호
            title = self.replaceHtmlTag(post['title'])  # HTML 특수문자 변환
            pubDate = post['pubDate']
            director = post['director']
            actor = post['actor']
            useRating = post['useRating']
            link = post['link']
            # imgData = urlopen(post['image']).read()
            #  # image = QImage(requests.get(post['image'], stream=True))
            # imageUrl = urlopen(post['image']).read()
            # image = QPixmap()
            # image.loadFromData(imageUrl)
            # imgLabel = QPixmap()
            # imgLabel.setPixmap(QPixmap.fronImage(image))
            # imgLabel.setGeometry(0, 0, 60, 100)
            # imgLabel.resize(60, 10)
            # setItem(행, 열, 넣을 데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))        # link넣기
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))        # link넣기
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))        # link넣기
            self.tblResult.setItem(i, 4, QTableWidgetItem(useRating))        # link넣기
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))        # link넣기
            self.tblResult.setCellWidget(i, 6, imgLabel)

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>', '').replace('&apos', "'").replace('&quot', '"')
        return result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())