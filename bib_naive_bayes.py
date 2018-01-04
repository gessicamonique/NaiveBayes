# Python 3.6

# File Manipulation
# Manipulação de arquivos
    
# Function that reads the file and returns a vector
# função que lê o arquivo e retorna um vetor
def file_read(file): 
    file = open(file,"r") 
    lines = file.readlines()
    file.close()
    for line in range(len(lines)):
        lines[line] = lines[line][:-1].upper()
    return lines 

# Without smoothing
# Sem suavização

# Probability of being popular and unpopular Without smoothing
# probabilidade de ser popular e não popular Sem suavização
def p_popular_and_unpopular(size_popular, size_not_popular):
    return [(size_popular / (size_popular + size_not_popular)), (size_not_popular / (size_popular + size_not_popular))]

# Probability of being popular and unpopular With smoothing
# probabilidade de ser popular e não popular com suavização
def p_popular_and_unpopular_smoothing(size_popular, size_not_popular, k):
    return [((size_popular + k) / (size_popular + size_not_popular + (k * 2))), ((size_not_popular + k) / (size_popular + size_not_popular + (k * 2)))]

# Number of status words
# Quantidade de palavras status
def number_of_words_status(vector_status): 
    sum_words = 0
    for line in vector_status:
        sum_words += len(line.split(" "))
    return sum_words

# Returns the amount of occurrences of a word in status
# retorna a quantidade de ocorrencias de uma palavra em status
def amount_of_occurrences_in_status(word, vector_status):
    occurrences = 0
    for line in vector_status:
        line_vector = line.split(" ")
        occurrences += line_vector.count(word)
    return occurrences

# Returns the number of different words in the dictionary
# retorna a quantidade de palavras distintas no dicionario
def number_of_different_words(dictionary):
    different = []
    for line in dictionary:
        line_vector = line.split(" ")
        for word in line_vector:
            if(word not in different):
                different.append(word)
    return len(different)

# Calculates the likelihood of a news being status Without smoothing
# calcula a probabilidade de uma noticia ser status sem suavização
def p_status_news(news, vector_status, number_of_words_status):
    news_vector = news.split(" ")
    p_status = (amount_of_occurrences_in_status(news_vector[0], vector_status)/number_of_words_status)
    for lines in range(1,len(news_vector)):
##        print(p_status)
        p_status *= (amount_of_occurrences_in_status(news_vector[lines], vector_status)/number_of_words_status)
    return p_status

# Calculates the likelihood of a news being status With smoothing
# calcula a probabilidade de uma noticia ser status com suavização
def p_status_news_smoothing(news, vector_status, number_of_words_status, k, dictionary):
    news_vector = news.split(" ")
    p_status = ((amount_of_occurrences_in_status(news_vector[0], vector_status) + k) / (number_of_words_status + (k * number_of_different_words(dictionary))))
    for lines in range(1,len(news_vector)):
##        print(p_status)
        p_status *= ((amount_of_occurrences_in_status(news_vector[lines], vector_status) + k) / (number_of_words_status + (k * number_of_different_words(dictionary))))
    return p_status

# Naive Bayes popular
def naive_bayes(news):

##    novaLista1 = ["O filme é divertido", "Gosto de filme de ação", "Gosto muito de ação"]
##    novaLista2 = ["É muito violento", "O filme é triste"]

    vector_popular = file_read("popular.txt")
    vector_not_popular = file_read("not-popular.txt")
    
    number_of_words_popular = number_of_words_status(vector_popular)
    number_of_words_not_popular = number_of_words_status(vector_not_popular)
    
    try:
        p_popular_unpopular = p_popular_and_unpopular(len(vector_popular), len(vector_not_popular))
        
        p_popular_news = p_status_news(news, vector_popular, number_of_words_popular)
        p_not_popular_news = p_status_news(news, vector_not_popular, number_of_words_not_popular)
        number_p_popular_news = [(p_popular_news * p_popular_unpopular[0]) / ((p_popular_news * p_popular_unpopular[0]) + (p_not_popular_news * p_popular_unpopular[1])), "Não Suavizou"]
    
    except:
##        print("suavizei")
        k = 1
        dictionary = vector_popular + vector_not_popular
        
        p_popular_unpopular = p_popular_and_unpopular_smoothing(len(vector_popular), len(vector_not_popular), k)
        
        p_popular_news = p_status_news_smoothing(news, vector_popular, number_of_words_popular, k, dictionary)
        p_not_popular_news = p_status_news_smoothing(news, vector_not_popular, number_of_words_not_popular, k, dictionary)
        number_p_popular_news = [(p_popular_news * p_popular_unpopular[0]) / ((p_popular_news * p_popular_unpopular[0]) + (p_not_popular_news * p_popular_unpopular[1])), "Suavizou"]                                 
    return number_p_popular_news

# O filme não é divertido  (precisa de suavização)
# O filme é de ação  (não precisa de suavização)


##print(naive_bayes("O filme não é divertido".upper()))










        
        
