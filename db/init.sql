CREATE DATABASE IF NOT EXISTS xkcd;
USE xkcd;

CREATE TABLE IF NOT EXISTS comics (
    num INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    safe_title VARCHAR(255) NOT NULL,
    publication_date VARCHAR(20) NOT NULL,
    transcript TEXT,
    alt_text TEXT,
    image_url VARCHAR(500),
    link VARCHAR(500),
    news TEXT,
    explanation_text TEXT,
    source_url VARCHAR(500),
    retrieved_date DATETIME NOT NULL
);

INSERT INTO comics (
    num,
    title,
    safe_title,
    publication_date,
    transcript,
    alt_text,
    image_url,
    link,
    news,
    explanation_text,
    source_url,
    retrieved_date
)
VALUES (
    2221,
    'Emulation',
    'Emulation',
    '2019-10-28',
    '',
    'I laugh at the software as if I am 100% confident that it is 2019.',
    'https://imgs.xkcd.com/comics/emulation.png',
    '',
    '',
    'A comic about software emulation and uncertainty about the current year.',
    'https://xkcd.com/2221/',
    NOW()
);