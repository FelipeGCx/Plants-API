from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        page_number = self.page.number
        items = len(data)
        total_items = self.page.paginator.count
        total_pages = self.page.paginator.num_pages

        return {
            'pagination': {
                'page': page_number,
                'items': items,
                'totalItems': total_items,
                'totalPages': total_pages
            },
            'results': data
        }
