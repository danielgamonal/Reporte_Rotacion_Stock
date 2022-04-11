{
    'name': 'Rotacion de Stock/Reporte de Movientos de Productos',
    'version': '12.0.1.0',
    'summary': 'Movimiento de Productos',
    'category': 'Stock',
    'description': """
        Este modulo permite imprimir un reporte de rotacion de Stock en PDF o Excel.
    """,
    'author': 'Frindt S.A',
    'website': 'https://www.ferreteriafrindt.cl',
    'depends': ['stock', 'sale_management', 'purchase'],
    'data': [
        'wizard/stock_rotation_report_view.xml',
        'report/report_stock_rotation.xml',
    ],

}
