dict = ['GEEKS', 'FOR', 'QUIZ', 'GO']
word_length = 5

def isWord(string):
    if string in dict: return True
    return  False


def checkWord(boggle, visited, i, j, string):
    height = len(boggle)
    width = len(boggle[0])
    string += boggle[i][j]

    if len(string) > word_length:
        return

    if isWord(string):
        print(string)

    if i > 0 and visited[i-1][j] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i-1, j, string)
        visited[i][j] = False

    if i < height-1 and visited[i+1][j] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i+1, j, string)
        visited[i][j] = False

    if j > 0 and visited[i][j-1] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i, j-1, string)
        visited[i][j] = False

    if j < width-1 and visited[i][j+1] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i, j+1, string)
        visited[i][j] = False

    if i > 0 and j > 0 and visited[i-1][j-1] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i-1, j-1, string)
        visited[i][j] = False

    if i > 0 and j < width-1 and visited[i-1][j+1] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i-1, j+1, string)
        visited[i][j] = False

    if i < height-1 and j > 0 and visited[i+1][j-1] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i+1, j-1, string)
        visited[i][j] = False

    if i < height-1 and j < width-1 and visited[i+1][j+1] == False:
        visited[i][j] = True
        checkWord(boggle, visited, i+1, j+1, string)
        visited[i][j] = False


def findAllWords(boggle):
    height = len(boggle)
    width = len(boggle[0])
    for i in range(height):
        for j in range(width):
            visited = [[False for _ in range(width)] for _ in range(height)]
            checkWord(boggle, visited, i, j, "")


boggle = [
    ['F', 'O', 'R'],
    ['G', 'I', 'Z'],
    ['U', 'E', 'K'],
    ['Q', 'S', 'E']
]
findAllWords(boggle)


