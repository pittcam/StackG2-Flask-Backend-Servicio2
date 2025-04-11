type_defs = """
type Query {
  searchMovies(query: String!): [Movie!]!
}

type Mutation {
  addFavoriteMovie(user_id: ID!, movie_id: Int!): AddFavoriteResponse
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
  movie_id: Int!
}
"""
