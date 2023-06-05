import graphene
from graphene_django import DjangoObjectType
from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

#1
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    league = graphene.Int()
    cup = graphene.Int()
    concacaf = graphene.Int()
    age = graphene.Int()
    stadium = graphene.String()
    state = graphene.String()
    country = graphene.String()
    nameleague = graphene.String()
    image = graphene.String()

#2
    class Arguments:
        name = graphene.String()
        league = graphene.Int()
        cup = graphene.Int()
        concacaf = graphene.Int()
        age = graphene.Int()
        stadium = graphene.String()
        state = graphene.String()
        country = graphene.String()
        nameleague = graphene.String()
        image = graphene.String()
        
#3
    def mutate(self, info, name, league, cup, concacaf, age, stadium, state, country, nameleague, image):
        link = Link(name=name, league=league, cup=cup, concacaf=concacaf, age=age, stadium=stadium, state=state,
            country=country, nameleague=nameleague, image=image)
        link.save()

        return CreateLink(
            id=link.id,
            name=link.name,
            league=link.league,
            cup=link.cup,
            concacaf=link.concacaf,
            age=link.age,
            stadium=link.stadium,
            state=link.state,
            country=link.country,
            nameleague=link.nameleague,
            image=link.image,
        )

#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()