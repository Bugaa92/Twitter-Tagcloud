"""
	This file holds some resources
"""

from sets import Set


"""
	OAuth Authentication Credentials
	You have to complete this dictionary with the credentials you get
	from twitter after you:
	- authenticate on https://twitter.com/
	- create a new app on: https://apps.twitter.com/
"""
creds = dict(
	consumer_key 		= "vI0LC9y9x6VIsHbo9L8ElkdUn",
	consumer_secret 	= "kbubkIgysn1qzzW5vQVTmRtwPVHMncmp6rkukobgP5LhW8LPeG",
	access_token 		= "3163644827-RDs4DL5icuU9YCLBiOVNwzOnwD0Btk90I9pVpjg",
	access_token_secret	= "FPSGLbxgxFKLovIIiDM96P7dcDz0gLSRrlUzXgdvsmnkv"
)


"""
	A list of stopwords`
"""
stopwords = Set([
	"a",
	"about",
	"above",
	"after",
	"again",
	"against",
	"all",
	"am",
	"an",
	"and",
	"any",
	"are",
	"as",
	"at",
	"b",
	"be",
	"because",
	"been",
	"before",
	"being",
	"below",
	"between",
	"both",
	"but",
	"by",
	"c",
	"can",
	"co",
	"could",
	"did",
	"d",
	"do",
	"does",
	"doing",
	"down",
	"during",
	"e",
	"each",
	"f",
	"few",
	"for",
	"from",
	"further",
	"g",
	"give",
	"h",
	"had",
	"has",
	"have",
	"having",
	"he",
	"he'd",
	"he'll",
	"he's",
	"her",
	"here",
	"here's",
	"hers",
	"herself",
	"him",
	"himself",
	"his",
	"how",
	"how's",
	"http",
	"https",
	"i",
	"i'd",
	"i'll",
	"i'm",
	"i've",
	"if",
	"in",
	"into",
	"is",
	"it",
	"it's",
	"its",
	"itself",
	"j",
	"just",
	"k",
	"l",
	"let's",
	"like",
	"m",
	"me",
	"more",
	"most",
	"must",
	"my",
	"myself",
	"n",
	"new",
	"no",
	"nor",
	"not",
	"o",
	"of",
	"off",
	"on",
	"once",
	"only",
	"or",
	"other",
	"ought",
	"our",
	"ours",
	"ourselves",
	"out",
	"over",
	"own",
	"p",
	"q",
	"r",
	"rt",
	"s",
	"same",
	"she",
	"she'd",
	"she'll",
	"she's",
	"should",
	"so",
	"some",
	"such",
	"t",
	"than",
	"that",
	"that's",
	"the",
	"their",
	"theirs",
	"them",
	"themselves",
	"then",
	"there",
	"there's",
	"these",
	"they",
	"they'd",
	"they'll",
	"they're",
	"they've",
	"this",
	"those",
	"through",
	"to",
	"too",
	"u",
	"under",
	"until",
	"up",
	"v",
	"very",
	"w",
	"was",
	"we",
	"we'd",
	"we'll",
	"we're",
	"we've",
	"were",
	"what",
	"what's",
	"when",
	"when's",
	"where",
	"where's",
	"which",
	"while",
	"who",
	"who's",
	"whom",
	"why",
	"why's",
	"with",
	"won't",
	"would",
	"x",
	"y",
	"you",
	"you'd",
	"you'll",
	"you're",
	"you've",
	"your",
	"yours",
	"yourself",
	"yourselves",
	"z",
])