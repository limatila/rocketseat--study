

def print_sequencially(*args, inicial="---\n", separator="\n\n---\n", early_breakline=False):
    """ Prints sequencially, for n args that is inserted in.
    
    :param args: Arguments to be printed.
    :type args: Any
    :param separator: Separator between each argument printed.
    :type separator: str
    """
    lista_args = list(args)
    
    lista_args[0] = inicial + str(lista_args[0])
    if early_breakline: 
        lista_args[0] = f"\n{lista_args[0]}"

    print(
        *lista_args,
        sep=separator,
    )