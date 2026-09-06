class Content:
    def display(self,title):
        print('Title:',title)

class Movie(Content):
    def display(self,title,year):
        print("Title:",title,"Year:",year)

m = Movie()
m.display("Moon Light by Yo Yo Honey Singh",2026)