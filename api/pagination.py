from django.core.paginator import EmptyPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    """
    Pagination for clips
    """

    page_size_query_param = "page_size"
    max_page_size = 50
    page_size = 10

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "pages": self.page.paginator.num_pages,
                "next": self.get_next_link(),
                "next_page_number": self.page.next_page_number()
                if self.page.has_next()
                else None,
                "previous": self.get_previous_link(),
                "results": data,
            }
        )

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a page object,
        or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param) or 1

        try:
            self.page = paginator.page(page_number)
        except EmptyPage:
            raise NotFound("Invalid page.")

        self.request = request
        return list(self.page)
