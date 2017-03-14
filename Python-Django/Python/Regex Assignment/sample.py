import re

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
	for word in words:
		if re.search(regex,word):
			print word


# all words that contain a "v"
get_matching_words(r"v{1}")

#2. all words that contain a double "s"
#get_matching_words(r"ss+")

#3. all words that end with "e"
#get_matching_words(r"e$")

#4. all words that contain an "b",any character,then another "b"
#get_matching_words(r"[b][^b]{1}[b]")

#5. all words that contain an "b",at least one character,then another "b"
#get_matching_words(r"[b][a-z]+[b]")

#6. all words that contain an "b",any number of characters(including zero),then another "b"
#get_matching_words(r"[b][a-z]*[b]")

#7. all words that include all five vowels in order
#get_matching_words(r"^[^aeiou]*a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u[^aeiou]*$")

#8. all words that only use the letters in "regular expression" (each letter can appear any number of times)
#get_matching_words(r"[regular expressions]")

#9. all words that contain a double letter
#get_matching_words(r"\w*(\w)\1\w*")