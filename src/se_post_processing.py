'''
This module contains the following functions for counting certain elements
within Stack Exchange posts:

count_html_tags  - Counts the number of HTML tags with a specified tag name.
find_math        - Finds all displayed math equations.
count_code_lines - Counts the number of lines of code.
count_text_lines - Counts the number of lines, excluding displayed math
                   equations and code.
count_lines      - Counts the total number of lines.
'''
import re
from bs4 import BeautifulSoup as bs

def count_html_tags(post, tag_name):
    '''
    Counts the number of HTML tags in a Stack Exchange post with a given tag
    name.

    Arguments
    ---------
    post - str
        A Stack Exchange post as recorded in the "Body" column of the Stack
        Exchange data dumps.

    Returns
    -------
    num_tags - int
        The number of HTML tags in the post.
    '''
    soup = bs(post, features='lxml')
    html_tags = soup.find_all(tag_name)
    num_tags = len(html_tags)

    return num_tags

def find_math(post):
    '''
    Finds all displayed math equations in a Stack Exchange post.

    Arguments
    ---------
    post - str
        A Stack Exchange post as recorded in the "Body" column of the Stack
        Exchange data dumps.

    Returns
    -------
    math_eqs - list[str]
        A list of the text which renders the displayed math equations in the
        post.
    '''
    soup = bs(post, features='lxml')
    text = soup.get_text()
    
    # Regular expressions to find displayed math equations
    math_pat1 = r'\$\$[^\$]+?\$\$'
    math_pat2 = r'\\begin{equation[*]{0,1}}[\S\s]+?\\end{equation[*]{0,1}}'
    
    # Find all math equations and store them in a list.
    math_eqs1 = re.findall(math_pat1, text)
    math_eqs2 = re.findall(math_pat2, text)
    math_eqs = math_eqs1 + math_eqs2

    return math_eqs
    
def count_code_lines(post):
    '''
    Counts the number of lines of code in a Stack Exchange post.
    
    Arguments
    ---------
    post - str
        A Stack Exchange post as recorded in the "Body" column of the Stack
        Exchange data dumps.
        
    Returns
    -------
    num_lines - int
        The number of lines of code in the post.
    '''
    soup = bs(post, features='lxml')
    
    # Get all blocks of code in the post.
    code_blocks = soup.find_all('code')

    # Count the lines in each code block and add them up.
    num_lines = 0
    for block in code_blocks:
        code = block.get_text().strip()
        lines = re.split('\n+', code)
        num_lines += len(lines)

    return num_lines

def count_text_lines(post):
    '''
    Counts the number of lines in a Stack Exchange post, excluding lines which
    are displayed math equations or in code blocks.
    
    Arguments
    ---------
    post - str
        A Stack Exchange post as recorded in the "Body" column of the Stack
        Exchange data dumps.
        
    Returns
    -------
    num_lines - int
        The number of lines of text in the post.
    '''
    soup = bs(post, features='lxml')
    
    # Remove code blocks from soup.
    code_blocks = soup.find_all('code')
    for block in code_blocks:
        block.decompose()
        
    text = soup.get_text()
    
    # Remove displayed math equations from text
    math_eqs = find_math(post)
    for eq in math_eqs:
        text = text.replace(eq, ' ')

    # Count lines by splitting along consecutive linebreaks.
    text = text.strip()
    num_lines = len(re.split('\n+', text))

    return num_lines
    
def count_lines(post):
    '''
    Counts the number of lines in a Stack Exchange post.
    
    Arguments
    ---------
    post - str
        A Stack Exchange post as recorded in the "Body" column of the Stack
        Exchange data dumps.
        
    Returns
    -------
    num_lines - int
        The number of lines in the post.
    '''
    soup = bs(post, features='lxml')
    text = soup.get_text().strip()
    num_lines = len(re.split('\n+', text))

    return num_lines