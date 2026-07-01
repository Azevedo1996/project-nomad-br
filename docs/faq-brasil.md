# FAQ Brasil - Project N.O.M.A.D. Brasil

## O painel já está em português?

Ainda não totalmente. A primeira fase do projeto brasileiro prioriza documentação, conteúdos, catálogos e mapas. A tradução completa da interface será uma fase futura.

## Posso usar conteúdos em português mesmo com a interface em inglês?

Sim. A interface pode estar em inglês, mas os conteúdos baixados, documentos, mapas e prompts de IA podem ser voltados ao português brasileiro.

## Por que os mapas do Brasil ainda aparecem como planejados?

Porque os arquivos `.pmtiles` precisam ser gerados, validados e publicados em GitHub Releases ou outro storage antes de entrarem como disponíveis no catálogo.

## Posso rodar no Windows?

Sim, preferencialmente com Docker Desktop usando WSL2.

## Posso rodar no Linux?

Sim. O ambiente é mais natural em Linux, especialmente Ubuntu/Debian ou servidores com Docker instalado.

## Preciso de GPU?

Não para usar biblioteca, mapas e conteúdos offline. GPU só é recomendada para IA local com modelos maiores.

## Quanto espaço em disco preciso?

Depende do uso:

```text
Uso básico: 100 GB+
IA local: 250 GB+
Biblioteca grande e mapas: 500 GB+
```

## Posso colocar os dados em HD externo?

Sim, desde que o caminho seja montado corretamente no host e o `docker-compose.br.yml` aponte para esse caminho.

## O que não devo commitar no GitHub?

Não commite:

```text
arquivos .pmtiles grandes
arquivos .zim grandes
banco de dados
storage local
senhas reais
```

## O projeto substitui o original?

Não. Este é um projeto paralelo brasileiro, mantendo créditos ao Project N.O.M.A.D. original.
