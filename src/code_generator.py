import random
import hashlib

def generate_code():
	"""
	Generate a unique string code in the format 'adjective-color-animal'.
	
	Returns:
		str: The generated code.
	"""
	adjectives = ['foolhardy', 'discerning', 'brave', 'quick', 'slow', 'small', 'big', 'bright', 'dark', 'happy', 'sad', 'calm', 'busy', 'lazy', 'loud', 'sanguine', 'mercurial', 'senile', 'ephermal']
	colors = ['aquamarine', 'beige', 'red', 'blue', 'green', 'yellow', 'black', 'white', 'pink', 'purple', 'orange', 'brown', 'gray', 'indigo', 'fuchsia', 'vermilion', 'azure', 'cerulean', 'magenta']
	animals = ['capybara', 'manatee', 'cat', 'dog', 'mouse', 'elephant', 'tiger', 'lion', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'monkey', 'cassowary', 'tarsier', 'ibex', 'wombat', 'kangaroo']

	return f"{random.choice(adjectives)}-{random.choice(colors)}-{random.choice(animals)}"

def generate_port(code: str) -> int:
	"""
	Generate a port number from a given code.

	Args:
		code (str): The code to generate the port number from.

	Returns:
		int: The generated port number.
	"""
	hash_obj = hashlib.sha256(code.encode())
	hash_int = int(hash_obj.hexdigest(), 16)
	return 3000 + (hash_int % 27000)

