from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from goals.models import GoalCategory, Goal, GoalComment
from goals.serializer import GoalCategoryCreateSerializer, GoalCategorySerializer, GoalCreateSerializer, GoalSerializer, \
    GoalCommentSerializer, GoalCommentCreateSerializer


class GoalCategoryCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategoryCreateSerializer


class GoalCategoryListView(ListAPIView):
    model = GoalCategory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategorySerializer

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend]

    ordering_fields = ['title', 'created']
    ordering = ['title']
    search_fields = ['title']

    def get_queryset(self):
        return GoalCategory.objects.prefetch_related('board__participants').filter(
            board__participants__user_id=self.request.user.id,
            is_deleted=False
        )

    def get_queryset(self):
        return GoalCategory.objects.filter(
            user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GoalCategory.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance: GoalCategory):
        instance.is_deleted = True
        instance.save(update_fields=('is_deleted',))

        return instance


class GoalCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCreateSerializer


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCreateSerializer
    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title", "description"]

    def get_queryser(self):
        return Goal.objects.filter(
            Q(user_id=self.request.user.id)  # Это условие, которое говорит, что мы хотим выбрать объекты, у которых user_id равен self.request.user.id. Здесь self.request.user - это текущий аутентифицированный пользователь, и мы хотим выбрать только те цели, которые принадлежат этому пользователю
            & ~Q(status=Goal.Status.archived)
            # Это условие, которое использует тильду (~), чтобы инвертировать результат. Таким образом, мы выбираем объекты, у которых status не равен Goal.Status.archived. Мы хотим исключить из результатов цели, которые находятся в архиве
        )


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(Q(user_id=self.request.user.id)
                                   & ~Q(status=Goal.Status.archived)
                                   )


class GoalCommentCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentCreateSerializer


class GoalCommentListView(ListAPIView):
    model = GoalComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['goal']
    ordering = [
        "-created"]  # Устанавливает порядок сортировки результатов запроса по убыванию времени создания комментария

    def get_queryset(self):
        return GoalComment.objects.filter(user_id=self.request.user.id)


class GoalCommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCommentSerializer

    def get_queryset(self):
        return GoalComment.object.filter(
            Q(user_id=self.request.user.id)
            & ~ Q(status=Goal.Status.archived)
        )


class BoardCreateView(CreateAPIView):
    permission_classes = [BoardPermissions]
    serializer_class = BoardCreateSerializer


class BoardListView(ListAPIView):
    model = Board
    permission_classes = [BoardPermissions]
    serializer_class = BoardListSerializer
    ordering = ["title"]

    # pagination_class = LimitOffsetPagination
    # filter_backends = [filters.OrderingFilter]
    def get_queryset(self):
        return Board.objects.prefetch_related('participants').filter(
            participants__user_id=self.request.user.id, is_deleted=False)


class BoardView(RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.prefetch_related('participants').filter(
            participants__user_id=self.request.user.id, is_deleted=False)

    def perform_destroy(self, instance: GoalCategory):
        instance.is_deleted = True
        instance.save(update_fields=('is_deleted',))
        return instance
