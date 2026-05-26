from django.utils import timezone

def smart_merge(local_data, server_instance):
    """
    Implements field-level smart merge.
    local_data: dict of fields from mobile
    server_instance: existing model instance on server
    """
    updated_fields = []
    for field, value in local_data.items():
        # Simple logic: if server field is null or empty, and local has data, update it.
        # If both have data, we could use a timestamp-based approach if available.
        current_server_value = getattr(server_instance, field, None)
        if value and value != current_server_value:
            setattr(server_instance, field, value)
            updated_fields.append(field)

    if updated_fields:
        server_instance.save()
    return server_instance, updated_fields
