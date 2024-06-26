from django.conf import settings
from graphene_django import DjangoObjectType
from mainpage import models
from django.contrib.auth import get_user_model
from mainpage.models import Event_item
import graphene

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile


class EventType(DjangoObjectType):
    class Meta:
        model = models.Event_item


class Query(graphene.ObjectType):
    all_events = graphene.List(EventType)
    #event_by_title = graphene.Field(EventType, title=graphene.String())

    def resolve_all_events(root, info):
        return (
            models.Event_item.objects.all()
        )


    # def resolve_event_by_title(root, info, title):
    #     return (
    #         models.Event_item.objects.get(title=title).all()
    #     )

    # all_posts = graphene.List(PostType)
    # author_by_username = graphene.Field(AuthorType, username=graphene.String())
    # post_by_slug = graphene.Field(PostType, slug=graphene.String())
    # posts_by_author = graphene.List(PostType, username=graphene.String())
    # posts_by_tag = graphene.List(PostType, tag=graphene.String())
    #
    # def resolve_all_posts(root, info):
    #     return (
    #         models.Post.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .all()
    #     )
    #
    # def resolve_author_by_username(root, info, username):
    #     return models.Profile.objects.select_related("user").get(
    #         user__username=username
    #     )
    #
    # def resolve_post_by_slug(root, info, slug):
    #     return (
    #         models.Post.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .get(slug=slug)
    #     )
    #
    # def resolve_posts_by_author(root, info, username):
    #     return (
    #         models.Post.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .filter(author__user__username=username)
    #     )
    #
    # def resolve_posts_by_tag(root, info, tag):
    #     return (
    #         models.Post.objects.prefetch_related("tags")
    #         .select_related("author")
    #         .filter(tags__name__iexact=tag)
    #     )


schema = graphene.Schema(query=Query)