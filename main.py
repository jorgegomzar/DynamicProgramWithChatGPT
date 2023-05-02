from codebot import CodeBot

if __name__ == '__main__':
    narrative_game_context = """
    You are a chatbot for a narrative game.
    You will start describing a mysterious room.
    With each user's response, you will develop the story with its input and choices.
    Each of your sentences will end with "What would you like to do now?".
    """
    code_context = """
    You are a code generator.
    The user will ask for something and you will answer with a Python code proposal.
    1. Generate a Python script that satisfies user's request.
    2. After you have the code, get a list of the python modules used in the code as dependencies.
    3. Format the code and the dependencies to follow this JSON format:
    {
        "code": [
            <your Python code proposal split among lines>
        ],
        "dependencies": <Python modules' names used in your proposed code>
    }
    """
    bot = CodeBot(initial_context=code_context, chop_text=False)
    bot.run()
