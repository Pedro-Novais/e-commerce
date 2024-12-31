class StatusCodeResponse(object):
    SUCCESS = {
        "pending": "PENDING",
        "approved": "APPROVED",
        "authorized": "AUTHORIZED",
        "in_process": "PENDING",
        "in_mediation": "PENDING",
        "rejected": "REJECTED",
        "cancelled": "CANCELLED",
        "refunded": "REFUNDED",
        "charged_back": "CHARGE_BACK"
    }

    STATUS_DETAIL = {
        "accredited": "Pedido pago com sucesso",
        "cc_rejected_insufficient_amount": "Saldo insuficiente",
        "cc_rejected_call_for_authorize": "Pendente de autorização",
        "cc_rejected_bad_filled_security_code": "Código de segurança inválido",
        "cc_rejected_bad_filled_date": "Cartão expirado",
        "cc_rejected_bad_filled_other": "Erro com preenchimento de dados do pagamento",
        "cc_rejected_bad_filled_card_number": "Número do cartão inválido",
        "cc_rejected_invalid_installments": "Parcelas inválidas",
        "cc_rejected_duplicated_payment": "Pagamento duplicado",
        "cc_rejected_card_disabled": "Cartão desabilitado",
        "cc_rejected_card_type_not_allowed": "Cartão não permitido",
        "cc_rejected_max_attempts": "Tentativa excedida do PIN do cartão",
        "cc_rejected_blacklist": "Cartão rejeitado",
        "cc_rejected_other_reason": "Cartão rejeitado",
        "rejected_by_regulations": "Pagamento rejeitado",
        "rejected_by_bank": "Pagamento rejeitado",
        "rejected_insufficient_data": "Pagamento rejeitado",
        "cc_amount_rate_limit_exceeded": "Pagamento rejeitado",
        "cc_rejected_high_risk": "Pagamento rejeitado",
        "cc_rejected_card_error": "Pagamento rejeitado",
        "cc_rejected_3ds_mandatory": "Pagamento rejeitado",
        "bank_error": "Pagamento rejeitado"
    }

    ERROR = {
        1: "Caso esse erro apareça, verifique os parâmetros enviados na solicitação.",
        3: "Certifique-se de que está usando um token de teste.",
        4: "O caller não está autorizado a acessar este recurso",
        8: "Este erro é exibido quando o nome de determinado parâmetro é inserido incorretamente. Revise o parâmetro retornado no erro e garanta que a informação inserida esteja correta.",
        23: "Certifique-se de que a data de expiração está no formato correto: yyyy-MM-dd'T'HH:mm:ssz.",
        1000: "Número de linhas excedeu os limites. Reduza o número de linhas na solicitação.",
        2002: "Cliente não encontrado. Verifique os detalhes e tente novamente.",
        2004: "Verifique o endpoint da API e tente novamente.",
        2006: "Token do cartão não encontrado. Certifique-se de que ele é correto e válido.",
        2007: "Verifique sua conexão de rede e tente novamente.",
        2009: "Certifique-se de fornecer o emissor do token do cartão.",
        2034: "Certifique-se de que os usuários envolvidos são todos produtivos ou todos de teste e revise o `sponsor_id` se aplicável.",
        2059: "Não é possível usar `application_fee` com este pagamento. Use um Access Token gerado via OAuth.",
        2062: "Token do cartão inválido. Verifique se ele é correto e válido.",
        2067: "Número de identificação do usuário inválido. Verifique e tente novamente.",
        2072: "Valor de `transaction_amount` inválido. Certifique-se de que é válido.",
        2077: "Captura diferida não suportada. Ajuste sua solicitação.",
        2123: "Operadores inválidos envolvidos na transação.",
        2131: "Verifique o campo `payment_method` e o número de parcelas (`installments`).",
        2198: "Email do teste inválido. Certifique-se de que está utilizando um email correto (@testuser.com).",
        3000: "Inclua `cardholder_name` na solicitação.",
        3001: "Inclua `cardissuer_id` com os dados do cartão.",
        3002: "O caller não está autorizado a realizar esta ação",
        3003: "Certifique-se de que o `card_token_id` é correto e não foi reutilizado.",
        3004: "Certifique-se de que `site_id` está corretamente formatado.",
        3005: "Verifique o estado do recurso antes de realizar essa operação.",
        3006: "Certifique-se de que o `cardtoken_id` é correto.",
        3007: "Inclua um `client_id` válido.",
        3008: "Verifique o `cardtoken` e tente novamente.",
        3009: "Verifique as permissões do `client_id` e tente novamente.",
        3010: "Certifique-se de que o cartão está na whitelist.",
        3011: "Verifique o campo `payment_method` e corrija se necessário.",
        3012: "Certifique-se de que `security_code_length` é válido.",
        3013: "O campo `security_code` é obrigatório e não pode estar vazio.",
        3014: "Certifique-se de que o método de pagamento é válido.",
        3015: "Verifique se `card_number_length` é válido.",
        3016: "Verifique se o número do cartão (`card_number`) é válido.",
        3017: "O `card_number_id` não pode ser nulo ou vazio.",
        3018: "Informe o `expiration_month`.",
        3019: "Informe o `expiration_year`.",
        3020: "Informe o `cardholder.name`.",
        3021: "Informe `cardholder.document.number`.",
        3022: "Informe `cardholder.document.type`.",
        3023: "Informe `cardholder.document.subtype`.",
        3024: "Reembolsos parciais não são suportados para esta transação.",
        3025: "Verifique o código de autenticação e tente novamente.",
        3026: "Certifique-se de que o `card_id` corresponde ao `payment_method_id`.",
        3027: "Verifique e ajuste o valor de `payment_type_id`.",
        3028: "Revise o valor de `payment_method_id`.",
        3029: "Certifique-se de que o mês de expiração do cartão é válido.",
        3030: "Verifique se o ano de expiração do cartão é válido.",
        3031: "O campo `secure_code_id` não pode estar vazio.",
        3032: "Verifique o comprimento do código de segurança e a validação do número do cartão.",
        4000: "O atributo `token` não pode ser nulo.",
        4001: "Inclua o atributo `payment_method_id`.",
        4002: "Inclua o atributo `transaction_amount`.",
        4003: "Certifique-se de que o `transaction_amount` é numérico.",
        4004: "O campo `installments` não pode estar vazio.",
        4005: "O atributo `installments` deve ser numérico.",
        4006: "O campo `payer` está mal formatado.",
        4050: "O campo `payer.email` deve ser um endereço de email válido.",
        4051: "Certifique-se de que o `payer.email` está dentro do limite de 254 caracteres.",
        }