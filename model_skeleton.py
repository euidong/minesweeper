class Panel:
    def __init__(self):
        """
        패널 초기화
        1. isRevealed : False
        2. hasFlag : False
        """
        pass

    def toggleFlag(self):
        """
        깃발을 토글한다.
        현재 True라면, 실행 후 False
        현재 False라면, 실행 후 True
        """
        pass

    def unveil(self):
        """
        패널을 오픈한다.
        """
        pass


class EmptyPanel(Panel):
    def __init__(self, numOfNearMines):
        """
        빈 패널 초기화
        """
        pass

    def addNumOfNearMines(self):
        """
        주변 지뢰 개수를 1 증가시킨다.
        """
        pass

    def unveil(self):
        """
        패널을 오픈한다.
        """
        pass


class MinePanel(Panel):
    def unveil(self):
        """
        패널을 오픈한다.
        """
        pass


class Board:
    def reset(self, numMine, height, width):
        """
        Board를 초기화한다.
        1. panels를 초기화한다.
        2. 중복 없이 numMine개의 지뢰를 랜덤하게 배치한다.
        3. 나머지 패널들을 EmptyPanel로 초기화한다.
        """
        pass

    def getNumOfRevealedPanels(self):
        """
        오픈된 패널의 개수를 반환한다.
        """
        pass

    def unveil(self, y, x):
        """
        y, x 위치의 패널을 오픈한다.
        """
        pass

    def toggleFlag(self, y, x):
        """
        y, x 위치의 패널의 깃발을 토글한다.
        """
        pass

    def checkReveal(self, y, x):
        """
        y, x 위치의 패널이 오픈되었는지 확인한다.
        """
        pass

    def checkFlag(self, y, x):
        """
        y, x 위치의 패널에 깃발이 꽂혀있는지 확인한다.
        """
        pass

    def checkMine(self, y, x):
        """
        y, x 위치의 패널이 지뢰인지 확인한다.
        """
        pass

    def getNumOfNearMines(self, y, x):
        """
        y, x 위치의 패널의 주변 지뢰 개수를 반환한다.
        """
        pass
