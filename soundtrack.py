import pyglet

class Soundtrack:
    def __init__(self) -> None:
        """Initializes a MediaFiles instance with loaded sound files for game 
        feedback."""
        self.correct_answer_sound = pyglet.media.load(
            "media/correct_answer.wav", streaming=False)
        self.incorrect_answer_sound = pyglet.media.load(
            "media/incorrect_answer.wav", streaming=False)
        self.high_score_sound = pyglet.media.load(
            "media/high_score_sound.wav", streaming=False)
        self.low_score_sound = pyglet.media.load("media/low_score_sound.wav",
                                                 streaming=False)
        self.click_button_sound = pyglet.media.load("media/click_button.wav", 
                                                    streaming=False)
        self.startup_sound = pyglet.media.load(
            "media/startup_sound.wav", streaming=False)
        
    def play_sound(self, sound: str) -> None:
        """Takes a string as an argument and plays the corresponding sound."""
        match sound:
            case "correct_answer":
                self.correct_answer_sound.play()
            case "incorrect_answer":
                self.incorrect_answer_sound.play()
            case "high_score":
                self.high_score_sound.play()
            case "low_score":
                self.low_score_sound.play()
            case "click_button":
                self.click_button_sound.play()
            case "startup":
                self.startup_sound.play()
