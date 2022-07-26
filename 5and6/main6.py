import random

if __name__ == "__main__":

    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    # Step 1

    word_list = [
        'abruptly',
        'absurd',
        'abyss',
        'affix',
        'askew',
        'avenue',
        'awkward',
        'axiom',
        'azure',
        'bagpipes',
        'bandwagon',
        'banjo',
        'bayou',
        'beekeeper',
        'bikini',
        'blitz',
        'blizzard',
        'boggle',
        'bookworm',
        'boxcar',
        'boxful',
        'buckaroo',
        'buffalo',
        'buffoon',
        'buxom',
        'buzzard',
        'buzzing',
        'buzzwords',
        'caliph',
        'cobweb',
        'cockiness',
        'croquet',
        'crypt',
        'curacao',
        'cycle',
        'daiquiri',
        'dirndl',
        'disavow',
        'dizzying',
        'duplex',
        'dwarves',
        'embezzle',
        'equip',
        'espionage',
        'euouae',
        'exodus',
        'faking',
        'fishhook',
        'fixable',
        'fjord',
        'flapjack',
        'flopping',
        'fluffiness',
        'flyby',
        'foxglove',
        'frazzled',
        'frizzled',
        'fuchsia',
        'funny',
        'gabby',
        'galaxy',
        'galvanize',
        'gazebo',
        'giaour',
        'gizmo',
        'glowworm',
        'glyph',
        'gnarly',
        'gnostic',
        'gossip',
        'grogginess',
        'haiku',
        'haphazard',
        'hyphen',
        'iatrogenic',
        'icebox',
        'injury',
        'ivory',
        'ivy',
        'jackpot',
        'jaundice',
        'jawbreaker',
        'jaywalk',
        'jazziest',
        'jazzy',
        'jelly',
        'jigsaw',
        'jinx',
        'jiujitsu',
        'jockey',
        'jogging',
        'joking',
        'jovial',
        'joyful',
        'juicy',
        'jukebox',
        'jumbo',
        'kayak',
        'kazoo',
        'keyhole',
        'khaki',
        'kilobyte',
        'kiosk',
        'kitsch',
        'kiwifruit',
        'klutz',
        'knapsack',
        'larynx',
        'lengths',
        'lucky',
        'luxury',
        'lymph',
        'marquis',
        'matrix',
        'megahertz',
        'microwave',
        'mnemonic',
        'mystify',
        'naphtha',
        'nightclub',
        'nowadays',
        'numbskull',
        'nymph',
        'onyx',
        'ovary',
        'oxidize',
        'oxygen',
        'pajama',
        'peekaboo',
        'phlegm',
        'pixel',
        'pizazz',
        'pneumonia',
        'polka',
        'pshaw',
        'psyche',
        'puppy',
        'puzzling',
        'quartz',
        'queue',
        'quips',
        'quixotic',
        'quiz',
        'quizzes',
        'quorum',
        'razzmatazz',
        'rhubarb',
        'rhythm',
        'rickshaw',
        'schnapps',
        'scratch',
        'shiv',
        'snazzy',
        'sphinx',
        'spritz',
        'squawk',
        'staff',
        'strength',
        'strengths',
        'stretch',
        'stronghold',
        'stymied',
        'subway',
        'swivel',
        'syndrome',
        'thriftless',
        'thumbscrew',
        'topaz',
        'transcript',
        'transgress',
        'transplant',
        'triphthong',
        'twelfth',
        'twelfths',
        'unknown',
        'unworthy',
        'unzip',
        'uptown',
        'vaporize',
        'vixen',
        'vodka',
        'voodoo',
        'vortex',
        'voyeurism',
        'walkway',
        'waltz',
        'wave',
        'wavy',
        'waxy',
        'wellspring',
        'wheezy',
        'whiskey',
        'whizzing',
        'whomever',
        'wimpy',
        'witchcraft',
        'wizard',
        'woozy',
        'wristwatch',
        'wyvern',
        'xylophone',
        'yachtsman',
        'yippee',
        'yoked',
        'youthful',
        'yummy',
        'zephyr',
        'zigzag',
        'zigzagging',
        'zilch',
        'zipper',
        'zodiac',
        'zombie',
    ]

    # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    number = random.randint(0, len(word_list)-1)
    chosen_word = word_list[number]

    stage = 6
    print(f'Psst, the solution is {chosen_word}.')
    display = []
    for i in chosen_word:
        display.append("_")
    has_won = True
    while has_won:
        guessed = False
        guess = input("Please guess a letter: ").lower()
        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                guessed = True
        for i in range(0, len(display)):
            if display[i] == "_":
                has_won = False
        if not has_won:
            print(display)
            has_won = True
            if not guessed:
                print(stages[stage])
                if stage == 0:
                    print("You lose")
                    break
                else:
                    stage -= 1
        else:
            print("You won!")
            break;