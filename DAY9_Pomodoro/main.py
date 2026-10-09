import time

class Pomodoro:
    def __init__(self , duration_mins: int = 20):
        self.total_duration: int = duration_mins*60
        self.time_accumulated: float = 0.0
        self.start_time: float | None = None
        self.is_running: bool = False
        self.is_paused: bool = False

    def get_current_elapsed(self):
        if self.is_running and self.start_time is not None:
            return self.time_accumulated + (time.time() - self.start_time)
        return self.time_accumulated
    def start(self):
        if self.is_running:
            print("The timer is already running! ")
            return
        if self.is_paused:
            print("Timer is currently paused . Press '3' to resume")
            return
        self.start_time = time.time()
        self.time_accumulated = 0.0
        self.is_running = True
        self.is_paused = False
        print("Pomodoro started!")

    def pause(self):
        if not self.is_running:
            print("Timer is not currently running.")
            return

        self.time_accumulated += time.time() - self.start_time
        self.start_time = None
        self.is_running = False
        self.is_paused = True
        print(f"Pomodoro Paused at {self.format_time(self.get_current_elapsed())}.")

    def resume(self):
        if not self.is_paused:
            print("The timer is not paused , so you cant resume it T_T.")
            return

        self.start_time = time.time()
        self.is_running = True
        self.is_paused = False
        print("Pomodoro Resumed!")

    def stop(self):
        if not self.is_running and not self.is_paused:
            print("No active timer exists to stop T_T .")
            return
        total_elapsed = self.get_current_elapsed()
        self.is_running = False
        self.is_paused = False
        self.start_time = None
        self.time_accumulated = 0.0
        print(f"Pomodoro stopped! Total focus time : {self.format_time(total_elapsed)}.")

    def show_elapsed(self):
        if not self.is_running and not self.is_paused:
            print("No timer has been started yet to show T_T . ")
            return
        elapsed = self. get_current_elapsed()
        remaining = max(0.0 , self.total_duration - elapsed)

        status = "Running..." if self.is_running else "Paused."

        print(f"\n+=+=+= Status: {status} =+=+=+\nElapsed Time: {self.format_time(elapsed)}\nTime Remaining: {self.format_time(remaining)}")

        if elapsed >= self.total_duration:
            print("Goal duration reached!")

    @staticmethod
    def format_time(seconds):
        secs = int(seconds)
        mins = secs // 60
        secs = secs % 60
        return f"{mins:02d}:{secs:02d}"

    def run(self):
        while True:
            print("\n+=+=+= Pomodoro =+=+=+")
            print("1. Start timer\n2. Pause timer\n3. Resume Timer\n4. Stop timer\n5. Show elapsed time\n6. Exit")

            choice = input("Choose an option(1-6) : ").strip()

            if choice == "1":
                self.start()
            elif choice == "2":
                self.pause()
            elif choice == "3":
                self.resume()
            elif choice == "4":
                self.stop()
            elif choice == "5":
                self.show_elapsed()
            elif choice == "6":
                print("Sayonara ~ ~")
                break
            else:
                print("Invalid option. Enter a number between 1-6.")

timer = Pomodoro(duration_mins=25)
timer.run()