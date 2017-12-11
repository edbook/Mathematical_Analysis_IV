#!/usr/bin/python
import re
import os
import sys
import fileinput



# Replace method 
def replace_all(text, dic):
    for i, j in dic.items():
        if type(i) == str:
            text = text.replace(i, j)
        else:
            text = i.sub(j, text)
    return text
 
# Dictionary with our find:replace values.
reps = {
    '\\sp':'^',
    '\n\n ':'\n\n',
    re.compile(r'\n(.*?)truecm'): '\n',
    '\n\n————–\n\n':'\n\n--------------\n\n',

    # For fixing lists with (lower case) Roman numerals with up to 10 items
    re.compile(r'\n *?\(i\)'): '\n\\(i)',
    re.compile(r'\n *?\(ii\)'): '\n\\(ii)',
    re.compile(r'\n *?\(iii\)'): '\n\\(iii)',
    re.compile(r'\n *?\(iv\)'): '\n\\(iv)',
    re.compile(r'\n *?\(v\)'): '\n\\(v)',
    re.compile(r'\n *?\(vi\)'): '\n\\(vi)',
    re.compile(r'\n *?\(vii\)'): '\n\\(vii)',
    re.compile(r'\n *?\(viii\)'): '\n\\(viii)',
    re.compile(r'\n *?\(ix\)'): '\n\\(ix)',
    re.compile(r'\n *?\(x\)'): '\n\\(x)',

    # For fixing references, removing equation references, etc.
    re.compile(r'\n\n +.. _(.*?)\n\n'): '\n',
    re.compile(r' *?\.\. _.*?:(.*?)\n'): '   \\1\n',


    # To fix a rare error where linebreaks within :math:`` broke stuff
    re.compile(r':math:`([^`]*?)\n([^`]*?)`'): ':math:`\\1 \\2`',

    # For images
    '.svg\n\n:align: center\n\n:alt:':'.svg\n    :align: center\n    :alt:',
    '2BeRemoved':'    ',

    # For references, "Link title" is where the name of the link should be.
    # Naming *every* link "Link title" should make non-fixed links easy to find and fix
    re.compile(r':ref:‘(.*?)‘'): ':ref:`Link title <\\1>`',

    # For hover text
    re.compile(r':hover:‘(.*?)‘'): ':hover:`\\1`',
#	'sub':'dub'
}


f = open(sys.argv[1], encoding="utf-8")
filedata = f.read()
f.close()

# Using "fuppsetning.tex" in its entirity before a chapter generates 10 lines of garbage text
# When replacing we only use lines 11 and up, i.e. we throw away the first 10 and then replace
lines = filedata.split('\n')
newdata = replace_all('\n'.join(lines[11:]), reps)



# For fixing math within italics. 
# WARNING! Only works if the only "*" are those created with Pandoc! 
# That is, if the only "*" are those to indicate opening and closing italics.
#
# To fix math appearing between asterisks, "*", we are going to split the file by the symbol "*",
# then add ALL asterisks as they should be to every other line in the split (i.e. what is between asterisks),
# and finally, we join the splits NOT with the original asterisks, but with a blank character instead.
italics_replacement_rules = {
    # Byrjar ekki á :math:
    re.compile(r'^((?!:math:).*\n*.*)'): r'*\1',

    # Byrjar á :math:, bætir við bil ef þarf og setur stjörnu eftir næsta bil (jafnvel ef hún er á næstu línu)
    re.compile(r'^:math:`(.*?)`( ?)(\n?)( ?)'): r':math:`\1` \3\4*',

    # :math: í miðjunni (með whitespace á undan og annaðhvort whitespace eða "-" á eftir)
    re.compile(r'(\s):math:`(.*?)`(\s|-)'): r'*\1:math:`\2` \3*',

    # :math: inn í :hover: í miðjunni 
    re.compile(r':hover:`\\? ?:math:`(.*?)`(.*?)`'): r'* :hover:`:math:`\1` \2`',

    # Endar ekki á "`" (vonandi frá :math:``!!!)
    # Ef ekki, (t.d. hover``) þá má bæta við bil eftir hover`` þ.a. þetta keyrist ekki))
    re.compile(r'(?<!`)$'): r'*',

    # Endar á (whitespace):math:``, þetta [^`]*? leyfir (ekki greedy) alla stafi nema "`" 
    # þ.a. við tökum ekki óvart annað "math" með að hluta til.
    # (mætti einnig nota look-behind)
    re.compile(r'(\s):math:`([^`]*?)`$'): r'*\1:math:`\2`',

    # Endar á :hover:``, þetta [^`]*? leyfir (ekki greedy) alla stafi nema "`" 
    # þ.a. við tökum ekki óvart annað "hover" með að hluta til.
    # (mætti einnig nota look-behind)
    re.compile(r'(\s):hover:`([^`]*?)`$'): r'*\1:hover:`\2`',
}

# Code that uses the dictionary above to fix italics
split_by_star = newdata.split('*')
for index, _ in enumerate(split_by_star):
    if index % 2 == 1:
        split_by_star[index] = replace_all(split_by_star[index], italics_replacement_rules)

# Our (hopefully) fixed text
fixed_italics = ''.join(split_by_star)


# TODO: make new rules to do "'.. \\_': '.. _',"


# Saving the finished product
f = open(sys.argv[2],'w')
f.write(fixed_italics)
f.close()
