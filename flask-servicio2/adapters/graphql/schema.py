type_defs = """
type Query {
  searchMovies(query: String!): [Movie!]!
  getFavoriteMovies(user_id: ID!): [FavoriteResponse!]!
}

type Mutation {
  addFavoriteMovie(user_id: ID!, movie_id: ID!): AddFavoriteResponse
  addToWatchLater(user_id: ID!, movie_id: ID!): AddWatchLaterResponse
}

type Movie {
  id: ID!
  title: String!
  overview: String
  release_date: String
  poster: String
}

type AddFavoriteResponse {
  success: Boolean!
  movie_id: ID!
}

type AddWatchLaterResponse { 
  success: Boolean!
  movie_id: ID!
}

type FavoriteResponse { 
  id: ID!
  poster: String!
}
"""
