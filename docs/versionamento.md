# Versionamento do Project N.O.M.A.D. Brasil

O Project N.O.M.A.D. Brasil usa versões com sufixo `-br` para diferenciar as entregas brasileiras das versões do projeto original.

## Formato

```text
vMAJOR.MINOR.PATCH-br
```

Exemplo:

```text
v0.1.0-br
```

## Critério simples

### PATCH

Correções pequenas:

```text
v0.1.1-br
```

Exemplos:

- correção de documentação;
- ajuste pequeno em script;
- correção de link;
- correção de workflow.

### MINOR

Novas funcionalidades brasileiras:

```text
v0.2.0-br
```

Exemplos:

- primeiro mapa PMTiles publicado;
- catálogo Kiwix preenchido;
- novo workflow;
- instalador simplificado.

### MAJOR

Mudanças grandes:

```text
v1.0.0-br
```

Exemplos:

- interface traduzida;
- imagem Docker brasileira própria;
- catálogo brasileiro integrado ao painel;
- versão considerada pronta para público geral.

## Tags no GitHub

Criar tag:

```bash
git tag v0.1.0-br
git push origin v0.1.0-br
```

Criar release via GitHub CLI:

```bash
gh release create v0.1.0-br --title "Project N.O.M.A.D. Brasil v0.1.0-br" --notes-file docs/releases/v0.1.0-br.md
```
