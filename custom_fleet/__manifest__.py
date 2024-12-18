{
    'name': 'Fleet Vehicle Towing Info',
    'version': '1.0',
    'category': 'Fleet',
    'depends': ['fleet', 'sale', 'hr'],  # Tambahkan dependensi ke modul fleet
    'data': [
        'views/fleet_vehicle_towing_views.xml',  # Tambahkan file view XML
        'views/sale_order_view.xml',  # File view
        'views/hr_employee_view_inherit.xml',
    ],
    'installable': True,
    'application': False,
}
