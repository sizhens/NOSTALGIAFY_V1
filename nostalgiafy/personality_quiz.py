import re
import inquirer

def personality_quiz():
    print("This is an easy quiz for you to determine what genres of music you like.")

    questions = [
    inquirer.List('genre',
                    message="What's your favorite music genre?",
                    choices=['Rock & Alternative', 'Hip-Hop', 'Pop', 'Electronic', 'I like everything'],
                ),
    ]
    answers = inquirer.prompt(questions)
    stripped_answer = answers["genre"]
    if stripped_answer == 'Pop':
        return "pop-songs"
    elif stripped_answer == "Rock & Alternative":
        return "alternative-songs"
    elif stripped_answer == "Hip-Hop":
        return "hip-hop-songs"
    elif stripped_answer == "Electronic":
        return "dance-songs"
    elif stripped_answer == "I like everything":
        return "hot-100"
    else:
        print("Error! For some reason!")