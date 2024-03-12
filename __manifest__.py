
{
    'name' : 'stock_cepal_products',
    'version' : '0.1',
    'category': '',
    'website' : '',
    'summary' : 'test',
    'depends': [
        'base',
        'stock'
    ],
    'data': [
      'views/product_qty_stock.xml'
    ],

    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
        
        ],
    },
    'license': 'LGPL-3',
}
