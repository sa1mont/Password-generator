import random

digits = "0123456789"
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

pass_count = input('Введите количество паролей для генерации.')
pass_len = input('Введите необходимую длину паролей.')
pass_is_digit = input('Должны ли быть цифры в пароле?')
pass_is_upper = input('Должны ли быть прописные буквы в пароле?')
pass_is_lower = input('Должны ли быть строчные буквы в пароле?')
pass_is_symb = input('Должны ли быть спец. символы (№, #, $, %, & и т.д.) в пароле?')
pass_is_neodsymb = input('Исключать ли неоднозначные символы(il1Lo0O) в пароле?')

if pass_is_digit.lower() == "да":
    chars += digits
if pass_is_upper.lower() == "да":
    chars += uppercase_letters
if pass_is_lower.lower() == "да":
    chars += lowercase_letters
if pass_is_symb.lower() == "да":
    chars += punctuation
if pass_is_neodsymb.lower() == "да":
    for i in 'il1Lo0O':
        chars.replace(i, '')
