# CS551P (2025-26): Advanced Programming - Class Assignment

## Project Overview

The **Music Streaming App** is a simple object-oriented Python application that allows users to:

* Browse songs and artistes
* Stream music with a countdown timer
* Rate songs

The system is designed using core Object-Oriented Programming (OOP) principles and provides a command-line interface for interaction.

---

## Project Structure

The application is built using three main classes:

### 1. `Song`

Represents a music track.

**Attributes:**

* `title` – Name of the song
* `duration` – Length of the song (in seconds)
* `genre` – Music genre
* `ratings` – List of user ratings (integers)

**Key Methods:**

* `add_rating(rating)` – Adds a rating (1–5)
* `average_rating()` – Calculates average rating
* `formatted_rating()` – Returns formatted rating or "N/A"
* `__str__()` – Displays song details

---

### 2. `Artiste`

Represents a music artist.

**Attributes:**

* `name` – Artist name
* `songs` – List of songs by the artist

**Key Methods:**

* `add_song(song)` – Adds a song to the artist
* `find_song(title)` – Finds a song (case-insensitive)
* `__str__()` – Displays artist and their songs

---

### 3. `MusicServer`

Acts as the main controller of the application.

**Attributes:**

* `artistes` – Dictionary storing artistes (case-insensitive keys)

**Key Methods:**

* `add_artiste(artiste)` – Adds an artist to the system
* `display_songs()` – Shows all songs
* `display_artistes()` – Shows all artists
* `stream_song(input)` – Streams a song based on user input

---

## How It Works

1. The system loads a sample catalogue of songs and artists.
2. A menu is displayed to the user:

   ```
   1. Display available songs
   2. Display available artistes
   3. Stream a song
   4. Exit
   ```
3. To stream a song, the user enters:

   ```
   <song title> by <artiste name>
   ```

---

## Streaming Feature

* Songs are streamed using a **countdown timer**.
* The duration is shortened using a multiplier:

  ```python
  Streaming_timer = 20
  ```
* Example output:

  ```
  Now streaming 'Waka Waka' by Shakira...
  5 seconds remaining...
  4 seconds remaining...
  ...
  Finished streaming.
  ```

---

## Rating System

After streaming, users can rate a song:

* Accepts: `yes`, `y`, `no`, `n`
* Ratings must be between **1 and 5**
* Invalid inputs are handled gracefully

---

## Sample Data

The system includes preloaded artists and songs:

* Shakira → *Waka Waka*, *Deja Vu*
* John Lennon → *Hey Jude*, *Imagine*
* 2pac → *Hail Mary*, *By Mama*

---

## Known Limitations

* Input format must strictly follow:

  ```
  <song title> by <artiste name>
  ```
* The separator `" by "` is **case-sensitive**

  * Example: `"BY"` will not work
* Extra spacing or missing spaces may cause parsing errors

---

## How to Run

1. Ensure Python is installed (Python 3.10+ recommended)
2. Save the file (e.g., `streamer.py`)
3. Run:

   ```bash
   python streamer.py
   ```

---

## Concepts Demonstrated

* Object-Oriented Programming (OOP)
* Encapsulation and modular design
* Input validation and error handling
* Basic simulation using `time.sleep`
* String parsing and case-insensitive matching

---

## Future Improvements

* Improve input parsing (handle "BY", missing spaces, etc.)
* Add a graphical user interface (GUI)
* Implement playlists and user accounts
* Add search and filtering features
* Replace countdown with progress bar


---

## UNit Testing

I have included a unit testing file to ensure that:
* Songs are correctly added to artistes
* Multiple songs can be stored properly
* Multiple artistes can be added to the music server
* The system correctly handles song titles containing the word "by"
* The system supports case-insensitive artiste storage
* The streaming function returns correct results.

Run the following command in your terminal:

  ```bash
   python -m unittest
   ```

Or directly:

  ```bash
   python test_streamer.py
   ```

---

## Author

Developed as part of a programming project to demonstrate OOP concepts in Python.
Author Name: Theodulph Sekyi Quainoo
Student ID:  52536877
Course:      Advanced Programming
Lecturer:    Dr. Miles Everett
---
