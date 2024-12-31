from datetime import datetime

from ._BaseRepository import BaseRepository
from .Conn import ConnDatabase
from model.NotificationsModel import Notification

class NotificationRepository(BaseRepository):
    def __init__(self):
        self.conn = ConnDatabase()

        super().__init__(
            DataModel=Notification,
            conn=self.conn
        )
    
    def create_notification(
            self,
            db,
            shop,
            notification_id,
            data,
            notification_type = "payment",
            processed = 'PENDING',
            processed_at = None
            ):
        
        new_notification = Notification(
            shop_name=shop,
            notification_id=notification_id,
            data=data,
            processed=processed,
            notification_type=notification_type,
            processed_at=processed_at
        )

        db.add(new_notification)
        db.commit()
        db.refresh(new_notification)

        return new_notification
    
    def update_notification(
            self,
            db,
            notification,
            processed,
            processed_at=datetime.now()
            ):
        
        notification.processed = processed
        notification.processed_at = processed_at

        db.commit()
