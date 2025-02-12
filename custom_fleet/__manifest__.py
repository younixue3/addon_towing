{
    'name': 'Fleet Vehicle Towing Info',
    'version': '1.0',
    'category': 'Fleet',
    'depends': ['fleet', 'sale', 'hr'],  # Tambahkan dependensi ke modul fleet
    'data': [
        'views/fleet_vehicle_towing_views.xml',  # Tambahkan file view XML
        'views/sale_order_view.xml',  # File view
        'views/sale_order_report_inherit_fleet.xml',
        'views/hr_employee_view_inherit.xml',
        'views/report_invoice.xml',
        'views/account_move_view.xml',
        'views/move_view_form_inherit.xml',

    ],
    'installable': True,
    'application': False,
}
