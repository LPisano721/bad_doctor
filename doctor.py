"""
program: doctor.py
author: Luigi Pisano
date: 10/6/2020
page 160 - 163

Conducts an interactive session of nondirective pyschology"""

import random

hedges = ("Interesting...", "Interesting, please tell me more...", "Please, tell me more.", "Many of my patients tell me the same thing. Please, go on...", "Please continue.", "go on, go on...", "Alright...");

qualifiers = ("Why do you say that ", "You seem to think that ", "Please, explain why ")
replacements = {"i":"you", "I":"you", "you":"me", "me":"you", "my":"your", "we":"you",  "us":"you", "mine":"yours", "am":"are"}

# List that will record the previous user input
history = []

def reply(sentence):
	"""Builds and returns a reply to a sentence. """
	probability = random.randint(1,4)
	if probability == 1:
		return random.choice(hedges)
	elif probability == 2 and len(history) > 3:
		return "Earlier, you said that " + changePerson(random.choice(history))
	else:
		response = random.choice(qualifiers) + changePerson(sentence)
		history.append(response)
		return response

def changePerson(sentence):
	"""Replaces first-person pronouns with second-person pronouns."""
	# Split the original sentence into individual words
	userInput = sentence.split()
	#create an empty list to store the reply words eventually
	replyWords = []
	for eachWord in userInput:
		# each time through the userInput list, add to the reply replyWords list
		replyWords.append(replacements.get(eachWord, eachWord))
	# now that the replyWords have been found, make it a string again
	return " ".join(replyWords)

def main():
	"""Handles the interaction between patient and the doctor."""
	print("Good morning, I hope that you are well today.")
	print("What would you like to discuss today?")
	while True:
		sentence = input("\nPlease, type your response or QUIT to exit our therapy session. >> ")
		# check to see if the user wants to quit or if should continue
		if sentence.upper() == "QUIT":
			print("Have a nice day.")
			break
		print(reply(sentence))

# Call to the main() function for entry into the program
main()
