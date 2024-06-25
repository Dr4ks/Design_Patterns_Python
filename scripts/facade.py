# Subsystem1
class Amplifier:
    def on(self):
        print("Amplifier is on")

    def off(self):
        print("Amplifier is off")

    def set_volume(self, volume):
        print(f"Amplifier volume set to {volume}")

# Subsystem2
class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def off(self):
        print("DVD Player is off")

    def play(self, movie):
        print(f"DVD Player is playing {movie}")

# Subsystem3
class Projector:
    def on(self):
        print("Projector is on")

    def off(self):
        print("Projector is off")

    def wide_screen_mode(self):
        print("Projector in widescreen mode")

# Facade
class HomeTheaterFacade:
    def __init__(self, amp, dvd, projector):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.amp.on()
        self.amp.set_volume(10)
        self.dvd.on()
        self.dvd.play(movie)
        self.projector.on()
        self.projector.wide_screen_mode()
        print("Movie is playing")

    def end_movie(self):
        print("Shutting movie theater down...")
        self.projector.off()
        self.dvd.off()
        self.amp.off()
        print("Movie theater is off")

# Client code
def client_code():
    amp = Amplifier()
    dvd = DVDPlayer()
    projector = Projector()

    home_theater = HomeTheaterFacade(amp, dvd, projector)

    home_theater.watch_movie("Inception")
    print("\n")
    home_theater.end_movie()

# Usage
client_code()

## Output
# Get ready to watch a movie...
# Amplifier is on
# Amplifier volume set to 10
# DVD Player is on
# DVD Player is playing Inception
# Projector is on
# Projector in widescreen mode
# Movie is playing


# Shutting movie theater down...
# Projector is off
# DVD Player is off
# Amplifier is off
# Movie theater is off
