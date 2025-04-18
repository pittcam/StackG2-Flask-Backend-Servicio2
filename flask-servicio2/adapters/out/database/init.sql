CREATE TABLE IF NOT EXISTS user_favorites (
    user_id UUID NOT NULL,
    movie_id VARCHAR NOT NULL,
    PRIMARY KEY (user_id, movie_id)
);

CREATE TABLE IF NOT EXISTS user_watchlist (
    user_id UUID NOT NULL,
    movie_id VARCHAR NOT NULL,
    PRIMARY KEY (user_id, movie_id)
);
