"""
Homework 4.

The English language has five vowels: A, E, I, O, and U
Please count each vowel occurrence in text bellow (total sum of lower and
capital cases) and write output as table smth

then modify text where each vowel replaced with
A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
ex. "Í wàndéréd lónély...."   and print it.
"""

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.
Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

poem_low = poem_text.lower()

dict_poem = {'a': poem_low.count('a'), 'e': poem_low.count('e'),
             'i': poem_low.count('i'), 'o': poem_low.count('o'),
             'u': poem_low.count('u')}

sep_num = 25
print('-' * sep_num)
print(f"| {'vowel':^10} | {'count': ^8} |")
print('-' * sep_num)

for vowel, count in dict_poem.items():
    print(f'| {vowel:^10} | {count:^8} |')
print('-' * sep_num)

translation_table = str.maketrans('AaEeIiOoUu', 'ÀàÉéÍíÓóÚú')
modified_text = poem_text.translate(translation_table)
print(modified_text)
