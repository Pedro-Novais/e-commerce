from flask import Blueprint, request

from middleware.webhook_auth_panel import handle_webhook_auth_panel

from controller._OrderController import OrderController

webhook = Blueprint('webhook', __name__)

@webhook.route('', subdomain="<subdomain>", methods=['POST'])
@handle_webhook_auth_panel
def notification_payment(subdomain):
    return OrderController(request=request, shop_name=None).webhook_order()