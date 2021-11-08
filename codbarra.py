from barcode import EAN13
from barcode.writer import ImageWriter


prod_cod = {
    "Feijão":"012345678901",
    "Arroz":"123456789012",
    "Macarrão":"234567890123"
}

for produto in prod_cod:
    codigo = prod_cod[produto]
    codbarra = EAN13(codigo, writer=ImageWriter())
    codbarra.save(f'codigodebarra_{produto}')
