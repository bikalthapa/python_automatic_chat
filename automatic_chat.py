import pyautogui # pip install pyautogui
conversation = [
"What song was or do you want to be the your first dance at your wedding?",
"What song would make the best theme music for you?",
"What is the most irrational superstition you have?",
"What is the weirdest food combination you enjoy?",
"What is the stupidest thing you ever did on a dare?",
"What is the worst date you have ever been on?",
"Who is the most embarrassing person you had a crush on?",
"What is your idea of the perfect day?",
"If you could swap lives with one of your friends, who would it be?",
"Who knows the most secrets about you?",
"What are your must-have qualities in a best friend?",
"If you had to get a tattoo today, what would you get?",
"If you could have free meals for life at one fast food chain, which one would you choose?",
"What is the most embarrassing thing your parents have ever done?",
"What is a lie or exaggeration you said to impress a crush?",
"What is the silliest you have ever felt?",
"When was the last time you laughed so hard that you cried?",
"What does your mother yell at you when she’s angry?",
"What is a telltale sign that you are upset?",
"What is your nickname?",
"What is the wackiest thing you ever did to help a friend?",
"What fictional character would you most like to be friends with?",
"What is your favorite topic to talk about?",
"What is your preferred method of communication?",
"Where is your happy place?",
"Where is your secret hideout?",
"What would your dream house look like?",
"Which family member are you closest to?",
"What is a habit you picked up from your parents?",
"What is the meanest thing you ever did to a sibling or that a sibling did to you?",
"What was your best birthday ever?",
"What is your most treasured possession?",
]

for i in conversation:
	pyautogui.write(i, interval=0.2)
	pyautogui.press("enter")
