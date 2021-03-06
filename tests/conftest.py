import pytest
from graphql import build_schema


@pytest.fixture
def sample_schema():
    schema = """
enum Episode { NEWHOPE, EMPIRE, JEDI }

interface Character {
  id: String!
  name: String
  friends: [Character!]!
  appearsIn: [Episode]
}

type Human implements Character {
  id: String!
  name: String
  friends: [Character]
  appearsIn: [Episode]
  homePlanet: String
}

type Droid implements Character {
  id: String!
  name: String
  friends: [Character]
  appearsIn: [Episode]
  primaryFunction: String
}

type Query {
  hero(episode: Episode): Character
  human(id: String!): Human
  droid(id: String!): Droid
}

type Mutation {
    addHuman(id: String!, name: String, homePlanet: String): Human
    addDroid(id: String!, name: String, primaryFunction: String): Droid
}
"""
    return build_schema(schema)
