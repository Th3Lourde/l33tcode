class BrowserHistory:

    def __init__(self, homepage: str):
        self.backP = []
        self.forwards = []
        self.current = homepage


    def visit(self, url: str) -> None:
        self.backP.append(self.current)
        self.current = url
        self.forwards = []



    def back(self, steps: int) -> str:

        self.forwards.append(self.current)

        for i in range(steps-1):
            if self.backP == []:
                break

            else:

                self.forwards.append(self.backP.pop())

        self.current = self.forwards.pop()

        return self.current





    def forward(self, steps: int) -> str:

        self.backP.append(self.current)

        for i in range(steps-1):
            if self.forwards == []: break
            r = self.forwards.pop()
            self.backP.append(r)



        self.current = self.backP.pop()

        return self.current


if __name__ == '__main__':
    
