#SQL DATABASE CREATION FOR 
#LIBRARY MANAGEMENT SYSTEM

CREATE DATABASE LibraryManagement;

USE LibraryManagement;

CREATE TABLE Books
(
    BookID int NOT NULL,
    Title varchar(255) NOT NULL,
    Author varchar(255) NOT NULL,
    Genre varchar(255) NOT NULL,
    NumberOfPages int NOT NULL,
    PRIMARY KEY (BookID)
);

CREATE TABLE Members
(
    MemberID int NOT NULL,
    Name varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    PhoneNumber int NOT NULL,
    PRIMARY KEY (MemberID)
);

CREATE TABLE Borrows
(
    MemberID int NOT NULL,
    BookID int NOT NULL,
    DateBorrowed date NOT NULL,
    DateReturned date NOT NULL,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);