CREATE TABLE book_details (
    bid SERIAL PRIMARY KEY,
    book_name VARCHAR(255),
    description TEXT,
    number_of_pages INT,
    author_name VARCHAR(255),
    publisher_name VARCHAR(255)
);

-- Insert data
INSERT INTO book_details (bid, book_name, description, number_of_pages, author_name, publisher_name)
VALUES
    (1, 'The Great Gatsby', 'A novel by F. Scott Fitzgerald', 218, 'F. Scott Fitzgerald', 'Scribner'),
    (2, 'To Kill a Mockingbird', 'A novel by Harper Lee', 281, 'Harper Lee', 'J. B. Lippincott & Co.'),
    (3, '1984', 'A dystopian novel by George Orwell', 328, 'George Orwell', 'Secker & Warburg'),
    (4, 'Pride and Prejudice', 'A romantic novel by Jane Austen', 279, 'Jane Austen', 'T. Egerton, Whitehall'),
    (5, 'The Catcher in the Rye', 'A novel by J. D. Salinger', 277, 'J. D. Salinger', 'Little, Brown and Company');
