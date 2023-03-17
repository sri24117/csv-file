from app.models import DataModel

def get_sorted_data(sort_by='column1', order='asc', limit=50):
    if order == 'desc':
        sort_by = '-' + sort_by

    sorted_data = DataModel.objects.order_by(sort_by)[:limit]
    return sorted_data