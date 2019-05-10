import graphene
from lib.models.offer import Offer as DBOffer


# class Company(graphene.ObjectType):
#     name = graphene.String()


# class Location(graphene.ObjectType):
#     country = graphene.String()
#     city = graphene.String()


class Offer(graphene.ObjectType):
    title = graphene.String()
    company = graphene.String()
    location = graphene.String()
    link = graphene.String()


class Query(graphene.ObjectType):
    offers = graphene.List(Offer)

    def resolve_offers(self, info):
        return DBOffer.objects()


schema = graphene.Schema(query=Query)
