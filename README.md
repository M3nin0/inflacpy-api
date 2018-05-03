# Inflacpy-API

API para a consulta de inflações de diversos países. Este projeto usa como base o [Inflacpy](https://github.com/M3nin0/inflacpy)

## Consultar

A consulta disponível pode ser vista abaixo

```
/search?initial=ANO_INICIAL&final=ANO_FINAL&country=PAIS
```

Por exemplo:

```
/search?initial=2015&final=2018&country=brasil
```

## Live

Há um exemplo desta aplicação rodando em: https://inflacpy-api.herokuapp.com/

Lembre-se, todos os parâmetros devem ser passados para a API, caso contrário a pesquisa não será feita.

### Sobre

Os dados são providos do [Inflaction](http://pt.inflation.eu/). Todos os direitos reservados a eles. Projeto criado para facilitar o acesso a informação através de diversos aplicativos.
