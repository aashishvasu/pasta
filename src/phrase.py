import random

neg_adjectives = [
	"abrasive",
	"bitter",
	"callous",
	"cynical",
	"disagreeable",
	"dull",
	"grouchy",
	"harsh",
	"stoic",
	"irritable",
	"miserable",
	"moody",
	"morose",
	"pessimistic",
	"rude",
	"spiteful",
	"sullen",
	"surly",
	"unfriendly",
	"unsociable"
]

pos_adjectives = [
	"adorable",
	"beautiful",
	"charming",
	"delightful",
	"elegant",
	"fancy",
	"glamorous",
	"handsome",
	"magnificent",
	"playful",
	"precious",
	"quaint",
	"radiant",
	"refined",
	"regal",
	"resplendent",
	"splendid",
	"stunning",
	"sublime",
	"superb"
]

colors = [
	"red",
	"orange",
	"yellow",
	"green",
	"blue",
	"purple",
	"pink",
	"brown",
	"gray",
	"black"
]

animals = [
	"Dog",
	"Cat",
	"Lion",
	"Tiger",
	"Bear",
	"Wolf",
	"Fox",
	"Raccoon",
	"Otter",
	"Giraffe",
	"Elephant",
	"Zebra",
	"Hippopotamus",
	"Gorilla",
	"Chimpanzee",
	"Panda",
	"Kangaroo",
	"Koala",
	"Gorilla",
	"Penguin"
]

def get_random_phrase():
	adj1 = random.choice(neg_adjectives)
	adj2 = random.choice(pos_adjectives)
	color = random.choice(colors)
	animal = random.choice(animals)
	return f"{adj1}-{adj2}-{color}-{animal}".lower()

def get_short_phrase(phrase:str):
	words = phrase.split('-')
	return f"{words[2]}-{words[3]}"