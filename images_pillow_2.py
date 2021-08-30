from PIL import Image

words = Image.open('./Images/word_matrix.png')
puzzle = Image.open('./Images/mask.png')
print(words.size)
puzzle = puzzle.resize(words.size)
# puzzle.save('./Images/mask_2.png')
print(puzzle.size)
words = Image.blend(puzzle, words, 7)
# words.paste(puzzle, (0, 0), puzzle)
words.show()