from langchain_text_splitters import RecursiveCharacterTextSplitter

content = '''
# Bengaluru Overview

## Tech Industry
Bengaluru is known as India's Silicon Valley. Tech parks like Electronic City and Whitefield host thousands of tech companies. Major firms include Infosys, Wipro, and TCS.

## Climate
The city sits at 920 meters altitude. This gives it pleasantly cool weather year-round. Average temperatures rarely exceed 30 degrees.

## Food
Bengaluru's food scene is legendary. South Indian classics like masala dosa and idli thrive here. Filter coffee shops dot every street corner.
'''

# Recursive chunking --> this chunking method splits content into paragraph and checks for chunk size, if chunk size exceeds then
# splits into sentence and to words till chunk size is met.
# paragraph --> sentences --> words --> character
# intialize the chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=40, 
    chunk_overlap=3 # number of overlap of characters Eg: ['temperatu', 'atures'] --> 'atu' is overlap between chunks
)

# splitting data into chunks
chunks = splitter.split_text(content)
print(len(chunks))
print(chunks)