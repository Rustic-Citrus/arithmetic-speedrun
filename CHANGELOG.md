# Changelog
## [0.4.0] - 2023-07-20
### Added
- Added colours to the application.
- Added docstrings to some functions.

### Changed
- Adjusted the difficulty settings to include more arithmetic concepts in the equations, such as decimal and negative numbers.
- Fixed the view graph button so that the x-axis appears properly labelled.

## [0.3.3] - 2023-07-19
### Changed
- Moved the authorship label on the main menu frame so that it is at the bottom.
- Repositioned some of the buttons in the frames.

## [0.3.2] - 2023-07-17
### Changed
- Changed the text in several of the prompts so that it is split across multiple lines.
- Changed the fonts from "MS Gothic" to "OCR A Extended" and "Lucida Console".
- Fixed division so that Easy and Basic problems no longer show equations where the solution is not an integer.

## [0.3.1] - 2023-07-16
### Added
- Added an error message box that informs the user their username cannot be empty.
- Added an information message box that informs the user that division solutions are calculated to 2 decimal places.
- Added an information message box that tells the user their score was successfully saved.
- Added docstrings to several methods and functions.

### Changed
- Changed the widgets to Tk themed widgets for a more modern-looking aesthetic.
- Fixed the division questions so that the answers would be floating-point numbers, not integers, and that the solutions would be rounded to 2 decimal places.
- Changed the score calculation formula so that elapsed time carries less weight in comparison to difficulty, accuracy and number of problems.

    score = ((total_problems ** (difficulty + 1)) / elapsed_time) * (correct_ratio * 100)

## [0.3.0] - 2023-07-15
### Added
- Added a GUI using the tkinter module.
- Added click_button.wav.
- Added startup_sound.wav.

### Changed
- Changed classes.py to app.py.
- Changed the name of the MediaFiles class to Soundtrack.
- Moved the Soundtrack class to a separate file called soundtrack.py.

### Removed
- Removed setup.py.
- Removed difficulty.txt.

## [0.2.2] - 2023-07-11
### Changed
- Fixed the field order in leaderboard.csv.
- Changed score formula in classes.py to account for number of problems solved.
- Improved exception handling in setup.py.
- Changed the name of a few attributes in the Game class.
- Fixed the same equation appearing more than once in a round.

## [0.2.1] - 2023-07-10
### Added
- Added other arithmetic operations: division, addition and subtraction.
- Added some exception handling.

## [0.2.0] - 2023-07-07
### Added
- Added classes.py.
- Added the MediaFiles and Game classes.

### Changed
- Changed the scoring system.

### Removed
- Removed problems.py.

## [0.1.1] - 2023-07-06
### Added
- Added some scores to leaderboard.csv.
- Added comments.
- Added get_progress() function to problems.py.
- Added matplotlib to requirements.txt.

### Removed
- Removed emojis from README.md.

### Changed
- Changed difficulty levels.

## [0.1.0] - 2023-07-05
### Added
- Initial commit.