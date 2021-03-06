from ply import lex

tokens = [
    'character',
    'digit',
    'LP',
    'RP',
    'LT',
    'GT',
    'Assign',
    'Separator',
    'Comillas'
]

reserved = {
'ArrayStack': 'AS','SinglyLinkedList': 'SLL','CircularDoublyLinkedList': 'CDLL','ArrayList': 'AL', 'Set': 'Set', 'Bag': 'Bag',
'Map': 'Map','HashTableSC': 'HSSC', 'HashTableOA': 'HSOA','DoublyLinkedQueue': 'DLQ','print': 'print','use': 'use','None': 'None',
'StringComp': 'StringComp', 'NumberComp': 'NumberComp', 'BinarySearchTree': 'Tree', 'SortedArrayList': 'SArrayList','True':'True', 'False':'False',
'add':'add', 'remove':'remove','removeAll':'removeAll', 'contains':'contains','clear':'clear', 'get':'get', 'index':'index'
}

tokens += list(reserved.values())

# Definitions of the tokens
t_character = r'[A-Za-z]' '|' r'\?' '|' r'\_'
t_digit = r'[0-9]'
t_LP = r'\('
t_RP = r'\)'
t_LT = r'\<'
t_GT = r'\>'
t_Assign = r'\=\>'
t_Separator = r'\,'
t_ignore = ' \t'
t_Comillas = r'\"'


def t_reserved(t):
    r'ArrayStack | SinglyLinkedList | CircularDoublyLinkedList | ArrayList | Set | Bag | Map | HashTableSC | HashTableOA | DoublyLinkedQueue | print | use | add | None | StringComp | NumberComp | BinarySearchTree | SortedArrayList | True | False | removeAll | contains| clear | index | remove | get'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()
#
# # Test it out
# data = '''
# ArrayStack Names => <"Francisco","Jorge","Alberto","Andrew">
# '''
#
# # Give the lexer some input
# lex.input(data)
#
# # Tokenize
# while True:
#     tok = lex.token()
#     if not tok:
#         break  # No more input
#     print(tok)