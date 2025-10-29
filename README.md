# TCAdmin Bot - Railway

Bot Python para processar pedidos TCAdmin hospedado no Railway.

## Configuração

### Variáveis de Ambiente

Configure as seguintes variáveis no Railway:

- `SUPABASE_URL`: URL do Supabase
- `SUPABASE_KEY`: Chave do Supabase
- `TCADMIN_USERNAME`: Usuário do TCAdmin
- `TCADMIN_PASSWORD`: Senha do TCAdmin

### Endpoints

- `GET /`: Status do serviço
- `GET /health`: Health check
- `POST /process-order`: Processar pedido

### Exemplo de uso

```bash
curl -X POST https://seu-app.railway.app/process-order \
  -H "Content-Type: application/json" \
  -d '{"order_id": "123"}'
```

## Deploy

1. Conecte o repositório no Railway
2. Configure as variáveis de ambiente
3. Deploy automático via GitHub
