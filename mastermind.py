import random

class Mastermind:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.ans = ""
        self.user = ""
        self.num_attempt = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_inp):
        if 0 > x_inp < 8:
            self.__x = x_inp

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y_inp):
        y_inp = int(input(""))
        if 0 > y_inp < 10:
            self.__y = y_inp


    def user_input(self):
        self.user = str(input("What is your guess? "))
        return self.user


    def random_ans(self):
        answer = ""
        for i in range(self.__y):
            ans1 = random.randrange(1,self.__x+1)
            self.ans += str(ans1)
        for j in self.ans:
            answer += str(j)
        return answer




    def check_hint(self):
        string = ""
        for i in range(len(self.ans)):
            if self.user[i] == self.ans[i]:
                string += "*"
            elif self.user[i] in self.ans:
                string += "o"
        return string


    def play(self):
        answer = self.random_ans()
        print(answer)
        while True:
            print(f"Playing Mastermind {self.x} colors and {self.__y} positions")
            guess = self.user_input()
            if answer == guess:
                break
            print(f"Your guess is {guess}")
            print(f"{self.check_hint()}")
            self.num_attempt += 1
            print()
        print(f"You solve it after {self.num_attempt} rounds")










game1 = Mastermind(6,4)
game1.play()


