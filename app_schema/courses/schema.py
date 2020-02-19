import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from app_models.graphql.bikes.models import Shop
from app_types.bikes.types import BikeType, ShopType
from app_mutations.bikes.mutations import CreateBikeMutation, UpdateBikeMutation, DeleteBikeMutation

class Mutations(graphene.ObjectType):
    create_bike = CreateBikeMutation.Field()
    update_bike = UpdateBikeMutation.Field()
    delete_bike = DeleteBikeMutation.Field()


class Query(graphene.ObjectType):
    node = Node.Field()
    bikes = MongoengineConnectionField(BikeType)
    shop_list = graphene.List(ShopType)

    def resolve_shop_list(self, info):
        return Shop.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations, types=[BikeType, ShopType])