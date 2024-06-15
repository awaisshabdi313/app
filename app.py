import streamlit as st

# In-memory book storage
books = []

# Function to add a book
def add_book(title, author, genre, year):
    book = {
        'Title': title,
        'Author': author,
        'Genre': genre,
        'Year': year
    }
    books.append(book)

# Function to display books
def display_books():
    if books:
        for book in books:
            st.write(f"*Title:* {book['Title']}")
            st.write(f"*Author:* {book['Author']}")
            st.write(f"*Genre:* {book['Genre']}")
            st.write(f"*Year:* {book['Year']}")
            st.write("---")
    else:
        st.write("No books in the library yet.")

# Streamlit interface
st.title("Library Management System")

# Tabs for adding and viewing books
tab1, tab2 = st.tabs(["Add Book", "View Books"])

# Add Book Tab
with tab1:
    st.header("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    year = st.number_input("Year", min_value=0, max_value=9999, step=1, format="%d")
    if st.button("Add Book"):
        if title and author and genre and year:
            add_book(title, author, genre, year)
            st.success("Book added successfully!")
        else:
            st.error("Please fill in all fields.")

# View Books Tab
with tab2:
    st.header("Library Books")
    display_books()

# Run the Streamlit app
if _name_ == "_main_":
    st.run()