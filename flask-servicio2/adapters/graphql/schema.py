type_defs = """
type Query {
  searchMovies(query: String!): [Movie!]!
}

type Movie {
  id: ID!
  title: String!
  overview: String
  release_date: String
  poster: String
}
"""