import builtins
for i in dir(builtins):
    if i[0].isupper():
        if i not in ['None', 'False', 'True', 'Ellipsis']:
            print(i,'-->',getattr(builtins,i).__doc__)
            print('-'*80)