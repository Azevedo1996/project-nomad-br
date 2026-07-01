# Troubleshooting - Project N.O.M.A.D. Brasil

## Porta 8082 já está em uso

Verifique processos/containers usando a porta:

```bash
docker ps
```

Altere no `docker-compose.br.yml`:

```yaml
ports:
  - "8083:8080"
```

Depois acesse:

```text
http://localhost:8083
```

## Container admin não sobe

Confira logs:

```bash
docker logs nomad_br_admin
```

Ou:

```bash
docker compose -f docker-compose.br.yml logs -f admin
```

Verifique:

- `APP_KEY` com 16+ caracteres;
- MySQL saudável;
- Redis saudável;
- permissões em `/opt/project-nomad-br`.

## MySQL não fica healthy

Ver logs:

```bash
docker logs nomad_br_mysql
```

Possíveis causas:

- diretório sem permissão;
- volume antigo corrompido;
- senha alterada depois da primeira inicialização;
- pouco espaço em disco.

## Redis não fica healthy

Ver logs:

```bash
docker logs nomad_br_redis
```

Possíveis causas:

- permissão no diretório `/opt/project-nomad-br/redis`;
- pouco espaço em disco.

## Dozzle não abre

Acesse:

```text
http://localhost:9998
```

Se não abrir, verifique:

```bash
docker logs nomad_br_dozzle
```

## Erro no GitHub Actions de URLs

O workflow `Validate Collection URLs` no projeto brasileiro deve ser consultivo. URLs externas antigas podem falhar, mas isso não deve bloquear o projeto brasileiro.

## Erro no validador brasileiro

Execute localmente:

```bash
python scripts/validate-br-catalogs.py
```

Corrija os erros críticos antes de commitar.

## Arquivos grandes foram adicionados sem querer

Veja arquivos staged:

```bash
git status
```

Remova do stage:

```bash
git restore --staged caminho/do/arquivo
```

Adicione regra no `.gitignore` se necessário.
