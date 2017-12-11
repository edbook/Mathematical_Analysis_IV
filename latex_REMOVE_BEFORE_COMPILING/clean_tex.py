#!/usr/bin/python
import re
import sys


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
    '\\begin{frame}': '\subsection',
    '\\end{frame}': '\n\n--------------\n\n',
    '\\begin{block}': '\subsubsection',
    '\\end{block}': '\n\n--------------\n\n',
    '\\begin{se}': '\subsubsection{Setning}',
    '\\end{se}': '\n\n--------------\n\n',
    '\\begin{sex}': '\subsubsection{Setning}',
    '\\end{sex}': '\n\n--------------\n\n',
    '\\begin{sk}': '\subsubsection{Skilgreining}',
    '\\end{sk}': '\n\n--------------\n\n',
    '\\begin{sesk}': '\subsubsection{Setning og skilgreining}',
    '\\end{sesk}': '\n\n--------------\n\n',
    '\\begin{hs}': '\subsubsection{Hjálparsetning}',
    '\\end{hs}': '\n\n--------------\n\n',
    '\\begin{fs}': '\subsubsection{Fylgisetning}',
    '\\end{fs}': '\n\n--------------\n\n',
    '\\begin{sy}': '\subsubsection{Sýnidæmi}',
    '\\end{sy}': '\n\n--------------\n\n',
    '\\begin{fo}': '\subsubsection{Forrit}',
    '\\end{fo}': '\n\n--------------\n\n',
    '\\begin{so}': '\subsubsection{Sönnun}',
    '\\end{so}': '\n\n--------------\n\n',
    '\\begin{sotx}': '\subsubsection{Sönnun}',
    '\\end{sotx}': '\n\n--------------\n\n',
    '\\æfing': '\section{Æfingardæmi}',
    '\\dæmi': '\subsubsection',

    # To fix (some) of the problems with \set
    '\\set\n': '\set ',
    # (Testing, hopefully this will help with stuff like "\set\alpha")
    '\\set\\': '\set \\',

    # To help with fixing the "math within italics" later.
    # We want to change all the "*" used in math (e.g. ^*) to \ast,
    re.compile(r'\^ ?(\n)? ?\*'): r'^\\ast\1',
    re.compile(r'\\sp? ?(\n)? ?\*'): r'^\\ast\1',

    # For labels and references: # >> ToDo: take labels outside equations etc.
    #re.compile(r'\\begin\{equation}\n(.*?)\\label\{(.*?)\}(.*?)\\end\{equation\}'): 'zzzzz',
    #re.compile(r'\\begin\{equation}(.*?)\\label\{(.*?)\}(.*?)\\end\{equation\}'): '\\label\{\\2\}\n\n\\begin\{equation\}\\1\\2\\end\{equation\}',
    
    re.compile(r'((?:\n\\.+)*)\\label\{(.*?)\}'): '\n\n.. _\\2:\n\\1',
    re.compile(r'\\ref\{(.*?)\}'): ':ref:`\\1`',

    # For fixing lists with specified labels, (mostly Roman numerals), prevents Pandoc from changing to "-"
    
    '\\begin{itemize}': '',
    '\\end{itemize}': '',
    re.compile(r'\\item\[(.*?)\]'): '\\item{\\1}',

    # For pictures: "MYND VANTAR HÉR!!!" is the common term to search for when manual work is needed
    '\\begin{picture}': 'MYND VANTAR HÉR!!!\n\\begin{picture}',
    re.compile(r'(.*?)\n\\input fig(.*?)\n'): 'MYND VANTAR HÉR!!!(setja texta undir mynd (finna í .tex) og fjarlægja ónotaðan kóða)\n.. figure:: ./myndir/fig\\2.svg\n\n    :align: center\n\n\\1\n\\input fig\\2\n',
    re.compile(r'\\v?figura ?\{(.*?)\}\{\{?.*?Mynd: ([\s\S]*?)\}?\}'): '.. figure:: ./myndir/\\1.svg\n\n    :align: center\n\n    :alt: \\2\n\n    2BeRemovedMynd: \\2\n',
    #re.compile(r'\\v?figura ?\{([^{].*?)\}\{(.*?)\}'): '.. figure:: ./myndir/\\1.svg\n    :align: center\n\n    :alt: \\2\n\n    2BeRemoved\\2\n',

    # For indexing: (NOTE: MANUAL WORK STILL NEEDED! This just saves *some* work!)
    re.compile(r'\\index\{([\s\S]*?)\}'): ' :hover:`\\1`',
    # 'sub': 'dub'
}


f = open(sys.argv[1], encoding='utf8')
filedata = f.read()
f.close()

newdata = replace_all(filedata, reps)


# A stack for fixing the command "\set{...}".
# It goes throught the entire file searching for "\set{" and when found changes it to "\{" and adds 1 to depth.
# Then, it adds 1 to depth for each additional { and subtracts 1 for each }.
# When the depth goes below zero we have found the matching bracket to "\set{" and we change it also to "\}".
# The rest of the code keeps track of where we are in the file, as the index points to individual characters
# and updates the index and length of the file accordingly when things are deleted and inserted.
working_data = list(newdata)
length_of_opening_tag = len('\set{')
length_of_closing_tag = len('}')
maximum_index = len(working_data) - length_of_opening_tag - length_of_closing_tag
index = 0
depth = 0
while index < maximum_index:
    if working_data[index:index+length_of_opening_tag] == list('\set{'):
    #print(working_data[index:index+length_of_opening_tag], "found!")
        del working_data[index+1:index+4]
        maximum_index -= 3
        index += 2
        depth = 1
        while depth > 0:
            if working_data[index] == '{':
                depth += 1
            if working_data[index] == '}':
                depth -= 1
            index += 1
        working_data.insert(index-1, '\\')
        maximum_index += 1
        index += 1
    index += 1

newdata = ''.join(working_data)



# Add subsections where needed (SOMETIMES BUGGY!!!)
sections = re.split(r'\\section\*?\{([\s\S]+?)\}', newdata)
# sections is an array containing:
# 0: everything before first section
# 1: first section title
# 2: first section content
# 3: second section title
# 4: second section content
# ... and so on.

final_sections = [sections[0]]

sections = sections[1:]

if sections:
    for i in range(len(sections) // 2):
        section_title = sections[2 * i]
        #print(section_title.encode('cp437', 'ignore'))
        final_sections.append('\\section{' + section_title + '}')
        section = sections[2 * i + 1]
        subsection_index = section.find('\\subsection')
        subsubsection_index = section.find('\\subsubsection')
        #print("--- Subsection index", subsection_index)
        #print("--- Subsubsection index", subsubsection_index)
        if subsubsection_index != -1 and (subsection_index == -1 or subsubsection_index < subsection_index):
            # We have a subsubsection without having a subsection first -
            # add a subsection at the beginning of the section.
            final_sections.append('\n\n\\subsection{' + section_title + '}')
        final_sections.append(section)

# Saving the finished product
f = open(sys.argv[2], 'w')
f.write(''.join(final_sections))
f.close()
