{
    'name': 'All in One Dashboard Lite',
    'version': '15.0.1.0.0',
    'category': 'Productivity',
    'summery': 'Smart Dashboard',
    'author': 'INKERP',
    'website': "https://www.INKERP.com",
    'depends': ['web'],
    'data': [
        'security/custom_dashboard_security.xml',
        'security/ir.model.access.csv',
        'views/eg_custom_dashboard_item_view.xml',
        'views/custom_dashboard_board.xml',
        'data/custom_dashboard_client_actions.xml',
    ],
    'demo': [
        'demo/dashboard_charts_demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'eg_ai_smart_dashboard_lite/static/src/xml/ColorPickerWidget.xml',
            'eg_ai_smart_dashboard_lite/static/src/xml/DashboardIconPicker.xml',
            'eg_ai_smart_dashboard_lite/static/src/xml/DashboardTilePreview.xml',
            'eg_ai_smart_dashboard_lite/static/src/xml/DashboardTile.xml',
            'eg_ai_smart_dashboard_lite/static/src/xml/custom_dashboard_qweb.xml',
            'eg_ai_smart_dashboard_lite/static/src/xml/custom_dashboard_view.xml',
            'eg_ai_smart_dashboard_lite/static/src/xml/CustomDashboardBoard.xml',
        ],
        'web.assets_backend': [
            'eg_ai_smart_dashboard_lite/static/src/js/ColorPickerWidget.js',
            'eg_ai_smart_dashboard_lite/static/src/js/DashboardIconPicker.js',
            'eg_ai_smart_dashboard_lite/static/src/js/graph_preview.js',
            'eg_ai_smart_dashboard_lite/static/src/js/dashboard_board.js',
            'eg_ai_smart_dashboard_lite/static/src/css/custom_dashboard.css',
        ],
        'web._assets_common_scripts': [
            'eg_ai_smart_dashboard_lite/static/lib/js/spectrum.js',
            'eg_ai_smart_dashboard_lite/static/lib/js/apexcharts.min.js',
            'eg_ai_smart_dashboard_lite/static/lib/js/bootstrap-iconpicker.min.js',
            'eg_ai_smart_dashboard_lite/static/lib/js/jquery.ui.touch-punch.min.js',
            'eg_ai_smart_dashboard_lite/static/lib/js/gridstack.min.js',
            'eg_ai_smart_dashboard_lite/static/lib/js/gridstack.jQueryUI.min.js',
        ],
        'web._assets_common_styles': [
            'eg_ai_smart_dashboard_lite/static/lib/css/spectrum.css',
            'eg_ai_smart_dashboard_lite/static/lib/css/bootstrap-iconpicker.min.css',
            'eg_ai_smart_dashboard_lite/static/lib/css/gridstack.min.css',
            'eg_ai_smart_dashboard_lite/static/lib/css/apexcharts.css',
        ],
    },
    'images': ['static/description/banner.gif'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
    'pre_init_hook': 'pre_init_hook',
    'uninstall_hook': "uninstall_hook",
}
