def teste(x):
    if x <= 10:
        print(x)
        teste(x + 1)
    else:
        print('acabou')
        
teste(1)
        
