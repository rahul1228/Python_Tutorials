story = '''
{}, But! {} only if ye be {} of valor!
For {} is guaranteed by a {} so {},
so {}, that no {} yet has {}
with it... and {}!
'''

def main():
	player_name = raw_input('What is your name? ')
	print 'Hello, ',player_name,'!'
	print 'Welcome to MAD LIBS'
	print '----------------------------------------------------'
	command = raw_input('Enter a command (e.g., Eat): ')
	plural_noun = raw_input('Enter a plural noun (e.g., trees): ')
	animal = raw_input('Enter an animal (e.g., Kangaroo): ')
	location = raw_input('Enter a location (e.g., St.thomas or SkyLine Courts): ')
	singular_noun = raw_input('Enter a singular noun (e.g., tree): ')

	adjectives = []
	adjectives.append(raw_input('Enter an adjective (e.g., big): '))
	adjectives.append(raw_input('Enter another adjective: '))

	past_participles = []
	past_participles.append(raw_input('Enter a past participle (e.g., played or fucked): '))
	past_participles.append(raw_input('Enter another past participle: '))

	# Below calls format() function on story and stores in mad_lib
	# var parameters/arguments in format() function replace {} in the string stored in story abovr.
	mad_lib = story.format(command,command,plural_noun,
							location,animal,adjectives[0],
							adjectives[1],singular_noun,
							past_participles[0],past_participles[1])

	print mad_lib

main()