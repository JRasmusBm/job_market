import graphene
from lib.models.offer import Offer as DBOffer
from lib.scrape import scrape, clear_scrapes


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


class Queries(graphene.ObjectType):
    offers = graphene.List(Offer)

    def resolve_offers(self, info):
        return DBOffer.objects()


class ClearScrapes(graphene.Mutation):
    ok = graphene.Boolean()
    offers = graphene.List(Offer)

    def mutate(self, info):
        try:
            clear_scrapes()
            ok = True
            offers = DBOffer.objects()
        except:
            ok = False
            offers = []
        return Scrape(ok=ok, offers=offers)

class Scrape(graphene.Mutation):
    ok = graphene.Boolean()
    offers = graphene.List(Offer)

    def mutate(self, info):
        try:
            asyncio.run(scrape())
            offers = DBOffer.objects()
            ok = True
        except:
            ok = False
            offers = []
        return Scrape(ok=ok, offers=offers)


class Mutations(graphene.ObjectType):
    scrape = Scrape.Field()
    clear_scrapes = ClearScrapes.Field()


schema = graphene.Schema(query=Queries, mutation=Mutations)
