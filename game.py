def anime_quiz():
    questions = [
        {
            "question": "What is the name of the main character in 'sabeer'?",
            "options": ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Kakashi Hatake"],
            "answer": "Naruto Uzumaki"
        },
        {
            "question": "In 'Dragon Ball Z', who is Goku's arch-rival?",
            "options": ["Vegeta", "Frieza", "Cell", "Majin Buu"],
            "answer": "Vegeta"
        },
        {
            "question": "Which anime features a notebook that can kill anyone whose name is written in it?",
            "options": ["Death Note", "Attack on Titan", "One Piece", "Fullmetal Alchemist"],
            "answer": "Death Note"
        },
        {
            "question": "Who is the main character of 'One Piece'?",
            "options": ["Monkey D. Luffy", "Roronoa Zoro", "Sanji", "Nami"],
            "answer": "Monkey D. Luffy"
        },
        {
            "question": "What is the name of the high school where 'My Hero Academia' takes place?",
            "options": ["UA High School", "Hogwarts", "Xavier's School for Gifted Youngsters", "Shinra High School"],
            "answer": "UA High School"
        }
    ]

    score = 0

    for idx, question in enumerate(questions):
        print(f"Question {idx + 1}: {question['question']}")
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

        answer = int(input("Enter the number of your answer: "))
        if question["options"][answer - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")

        print()

    print(f"You scored {score} out of {len(questions)}.")

anime_quiz()
