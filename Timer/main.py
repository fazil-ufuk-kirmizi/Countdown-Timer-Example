import time

class Timer:
    def __init__(self):
        self.run()

    def run(self):
        while True:
            self.start_countdown()
            if not self.ask_to_repeat():
                print("Program is exiting...")
                break

    @staticmethod
    def start_countdown():
        while True:
            try:
                duration = int(input("Enter countdown duration: "))
                if duration <= 0:
                    print("Please enter a number greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        for i in range(duration, 0, -1):
            print(f"Remaining: {i} seconds")
            time.sleep(1)

        print("0 - Time is up.")

    @staticmethod
    def ask_to_repeat():
        while True:
            answer = input("Do you want to start again? (y/n): ").strip().lower()
            if answer == 'y':
                return True
            elif answer == 'n':
                return False
            else:
                print("Please enter only 'y' or 'n'.")

Timer()
