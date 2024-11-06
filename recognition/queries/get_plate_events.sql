SELECT 
    plate_events.plate_number,
    plate_events.brand,
    plate_events.color,
    plate_events.recognition_time,
    cameras.name AS camera_name,
    cameras.ip_address,
    cameras.latitude,
    cameras.longitude
FROM 
    plate_events
JOIN 
    cameras ON plate_events.camera_id = cameras.id
WHERE 
    (%s IS NULL OR plate_events.plate_number LIKE %s)
    AND (%s IS NULL OR plate_events.camera_id = %s)
    AND (%s IS NULL OR plate_events.recognition_time >= %s)
    AND (%s IS NULL OR plate_events.recognition_time <= %s);
