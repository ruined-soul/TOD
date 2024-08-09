-- Example SQL migration script to create the initial tables.
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    coins INTEGER DEFAULT 0,
    is_admin BOOLEAN DEFAULT FALSE,
    is_owner BOOLEAN DEFAULT FALSE
);

CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER,
    mode TEXT DEFAULT 'solo',
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE game_players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER REFERENCES games(id),
    user_id INTEGER REFERENCES users(id),
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    text TEXT NOT NULL,
    is_adult BOOLEAN DEFAULT FALSE
);
