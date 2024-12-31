class I18n(object):
    STATUS_ORDER_NEW = "NEW"
    STATUS_ORDER_ACCEPTED = "ACCEPTED"
    STATUS_ORDER_SHIPPED = "SHIPPED"
    STATUS_ORDER_DELIVERED = "DELIVERED"
    STATUS_ORDER_CANCELLED = "CANCELLED"

    SUCCESS_CREATE_ORDER = "Pedido criado com sucesso"
    SUCCESS_CREATE_ORDER_PIX = "Pedido criado com sucesso, pagamento pix pendente"

    NOT_FOUND_PRODUCTS_FROM_ORDER = "Itens adicionados no pedido não foram encontrados na loja"
    
    ERROR_PROCESSING_PAYMENT = "Pagamento não foi concluido, motivo: {reason}"
    
    ERROR_CREATE_PAYMENT = "Erro ao criar pagamento"