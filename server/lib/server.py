from flask import Flask
from flask_graphql import GraphQLView
from lib.schema.schema import schema

app = Flask("JobMarketAPI")

app.add_url_rule(
    "/api", view_func=GraphQLView.as_view("api", schema=schema, graphiql=True)
)

app.add_url_rule(
    "/api/batch",
    view_func=GraphQLView.as_view("batch", schema=schema, batch=True),
)
