import pyautogui
import time
import pyperclip
# from openai import OpenAI

def is_last_message_from_sender(chat_log, sender_name="Papa"):
    """
    Check if the last message in the chat log is from the specified sender.

    Args:
    - chat_log (str): The chat log containing multiple messages.
    - sender_name (str): The sender's name to compare against (default: "Gracey").

    Returns:
    - bool: True if the last message is from the specified sender, False otherwise.
    """
    # Split the chat log by lines
    lines = chat_log.strip().split('\n')

    # Find the last message line
    for line in reversed(lines):
        if "] " in line:
            sender = line.split("] ")[1].split(":")[0]
            return sender == sender_name
    
    return False


# client = OpenAI(
#   api_key="",
# )


#     First, make sure pyperclip is installed
# pip install pyperclip

# Coordinates for the icon and selection area
icon_x, icon_y = 1374,1573 #brave icon
start_x, start_y = 1630,295
end_x, end_y = 2485,1380

# Click on the icon
pyautogui.click(icon_x, icon_y)

# Pause to ensure the click is registered and the application is ready
time.sleep(2)

while True:

    # Click and drag to select the area
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=1, button='left')

    # Copy the selected text to the clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.leftClick(2456,1363)

    # Pause to ensure the text is copied
    time.sleep(2)

    # Get the text from the clipboard
    chat_history = pyperclip.paste()

    # Print the text
    print("Copied Text:")
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):

        # completion = client.chat.completions.create(
        #   model="gpt-3.5-turbo",
        #   messages=[
        #     {"role": "system", "content": "You are a real person named Adarsh Raj who speaks hindi and english and from India. You have to analyze the messages or contents and have to give response to it or reply to it like Adarsh Raj. The reply should be like Adarsh Raj response only!"},
        #     {"role": "user", "content": chat_history}
        #   ]
        # )

        # response = completion.choices[0].message
        response = "hi, this is a test message from AUTO_BOT"
        # Copy the content to the clipboard
        pyperclip.copy(response)

        # Click on the box
        pyautogui.click(1610, 1456)

        # Pause to ensure the click is registered and the box is focused
        time.sleep(2)

        # Paste the content (Ctrl+V)
        pyautogui.hotkey('ctrl', 'v')

        # Pause to ensure the content is pasted
        time.sleep(2)

        # Press Enter
        pyautogui.press('enter')