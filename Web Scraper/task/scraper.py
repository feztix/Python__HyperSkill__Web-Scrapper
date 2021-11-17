import requests


class MainApp():
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)

        # Handling user input
        self.receive_user_input()

    def receive_user_input(self):
        self.user_input = str(input("Input the URL:\n"))
        print(self.user_input)


if __name__ == '__main__':
    web_scrapper = MainApp()
