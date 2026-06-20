from django.utils import timezone

def smart_merge(local_data, server_instance):
    """
    Implements field-level smart merge.
    local_data: dict of fields from mobile
    server_instance: existing model instance on server
    """
    updated_fields = []
    for field, value in local_data.items():
        if field in ['id', 'user', 'last_synced_at']:
            continue

        if hasattr(server_instance, field):
            current_server_value = getattr(server_instance, field, None)
            # If local value is different and not null/empty, update server.
            if value is not None and value != "" and value != current_server_value:
                setattr(server_instance, field, value)
                updated_fields.append(field)

    if updated_fields:
        if hasattr(server_instance, 'last_synced_at'):
            server_instance.last_synced_at = timezone.now()
        server_instance.save()
    return server_instance, updated_fields
