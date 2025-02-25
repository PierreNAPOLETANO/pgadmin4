##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2023, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

"""Register preferences for query tool"""
from flask_babel import gettext
from pgadmin.utils.constants import PREF_LABEL_DISPLAY,\
    PREF_LABEL_KEYBOARD_SHORTCUTS, PREF_LABEL_EXPLAIN, PREF_LABEL_OPTIONS,\
    PREF_LABEL_EDITOR, PREF_LABEL_CSV_TXT, PREF_LABEL_RESULTS_GRID,\
    PREF_LABEL_SQL_FORMATTING, PREF_LABEL_GRAPH_VISUALISER
from pgadmin.utils import SHORTCUT_FIELDS as shortcut_fields, \
    ACCESSKEY_FIELDS as accesskey_fields
from config import ON_DEMAND_RECORD_COUNT


def register_query_tool_preferences(self):
    self.explain_verbose = self.preference.register(
        'Explain', 'explain_verbose',
        gettext("Verbose output?"), 'boolean', False,
        category_label=PREF_LABEL_EXPLAIN
    )

    self.explain_costs = self.preference.register(
        'Explain', 'explain_costs',
        gettext("Show costs?"), 'boolean', False,
        category_label=PREF_LABEL_EXPLAIN
    )

    self.explain_buffers = self.preference.register(
        'Explain', 'explain_buffers',
        gettext("Show buffers?"), 'boolean', False,
        category_label=PREF_LABEL_EXPLAIN
    )

    self.explain_timing = self.preference.register(
        'Explain', 'explain_timing',
        gettext("Show timing?"), 'boolean', False,
        category_label=PREF_LABEL_EXPLAIN
    )

    self.explain_summary = self.preference.register(
        'Explain', 'explain_summary',
        gettext("Show summary?"), 'boolean', False,
        category_label=PREF_LABEL_EXPLAIN
    )

    self.explain_settings = self.preference.register(
        'Explain', 'explain_settings',
        gettext("Show settings?"), 'boolean', False,
        category_label=PREF_LABEL_EXPLAIN
    )

    self.auto_commit = self.preference.register(
        'Options', 'auto_commit',
        gettext("Auto commit?"), 'boolean', True,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext('Set auto commit on or off by default in new Query '
                         'Tool tabs.')
    )

    self.auto_rollback = self.preference.register(
        'Options', 'auto_rollback',
        gettext("Auto rollback on error?"), 'boolean', False,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext('Set auto rollback on or off by default in new Query '
                         'Tool tabs.')
    )

    self.show_prompt_save_query_changes = self.preference.register(
        'Options', 'prompt_save_query_changes',
        gettext("Prompt to save unsaved query changes?"), 'boolean', True,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext(
            'Specifies whether or not to prompt user to save unsaved '
            'query on query tool exit.'
        )
    )

    self.table_view_data_by_pk = self.preference.register(
        'Options', 'table_view_data_by_pk',
        gettext("Sort View Data results by primary key columns?"),
        'boolean', True,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext("If set to True, data returned when using the "
                         "View/Edit Data - All Rows option will be sorted by "
                         "the Primary Key columns by default. When using the "
                         "First/Last 100 Rows options, data is always sorted.")
    )

    self.show_prompt_save_data_changes = self.preference.register(
        'Options', 'prompt_save_data_changes',
        gettext("Prompt to save unsaved data changes?"), 'boolean', True,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext(
            'Specifies whether or not to prompt user to save unsaved '
            'data on data grid exit.'
        )
    )

    self.show_prompt_commit_transaction = self.preference.register(
        'Options', 'prompt_commit_transaction',
        gettext("Prompt to commit/rollback active transactions?"), 'boolean',
        True,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext(
            'Specifies whether or not to prompt user to commit or rollback '
            'an active transaction on Query Tool exit.'
        )
    )

    self.copy_sql_to_query_tool = self.preference.register(
        'Options', 'copy_sql_to_query_tool',
        gettext("Copy SQL from main window to query tool?"), 'boolean',
        False,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext(
            'Specifies whether or not to copy SQL to query tool from '
            'main window.'
        )
    )

    self.sql_font_size = self.preference.register(
        'Editor', 'plain_editor_mode',
        gettext("Plain text mode?"), 'boolean', False,
        category_label=PREF_LABEL_EDITOR,
        help_str=gettext(
            'When set to True, keywords won\'t be highlighted and code '
            'folding will be disabled. Plain text mode will improve editor '
            'performance with large files.'
        )
    )

    self.sql_font_size = self.preference.register(
        'Editor', 'code_folding',
        gettext("Code folding?"), 'boolean', True,
        category_label=PREF_LABEL_EDITOR,
        help_str=gettext(
            'Enable or disable code folding. In plain text mode, this will '
            'have no effect as code folding is always disabled in that mode. '
            'Disabling will improve editor performance with large files.'
        )
    )

    self.wrap_code = self.preference.register(
        'Editor', 'wrap_code',
        gettext("Line wrapping?"), 'boolean', False,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext(
            'Specifies whether or not to wrap SQL code in the editor.'
        )
    )

    self.insert_pair_brackets = self.preference.register(
        'Editor', 'insert_pair_brackets',
        gettext("Insert bracket pairs?"), 'boolean', True,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext(
            'Specifies whether or not to insert paired brackets in the '
            'editor.'
        )
    )

    self.brace_matching = self.preference.register(
        'Editor', 'brace_matching',
        gettext("Brace matching?"), 'boolean', True,
        category_label=PREF_LABEL_OPTIONS,
        help_str=gettext(
            'Specifies whether or not to highlight matched braces '
            'in the editor.'
        )
    )

    self.csv_quoting = self.preference.register(
        'CSV_output', 'csv_quoting',
        gettext("CSV quoting"), 'options', 'strings',
        category_label=PREF_LABEL_CSV_TXT,
        options=[{'label': gettext('None'), 'value': 'none'},
                 {'label': gettext('All'), 'value': 'all'},
                 {'label': gettext('Strings'), 'value': 'strings'}],
        control_props={
            'allowClear': False,
            'tags': False
        }
    )

    self.csv_quote_char = self.preference.register(
        'CSV_output', 'csv_quote_char',
        gettext("CSV quote character"), 'options', '"',
        category_label=PREF_LABEL_CSV_TXT,
        options=[{'label': '"', 'value': '"'},
                 {'label': '\'', 'value': '\''}],
        control_props={
            'allowClear': False,
            'tags': False,
            'creatable': True,
            'maxLength': 1
        }
    )

    self.csv_field_separator = self.preference.register(
        'CSV_output', 'csv_field_separator',
        gettext("CSV field separator"), 'options', ',',
        category_label=PREF_LABEL_CSV_TXT,
        options=[{'label': ';', 'value': ';'},
                 {'label': ',', 'value': ','},
                 {'label': '|', 'value': '|'},
                 {'label': gettext('Tab'), 'value': '\t'}],
        control_props={
            'allowClear': False,
            'tags': False,
            'creatable': True,
            'maxLength': 1
        }
    )

    self.replace_nulls_with = self.preference.register(
        'CSV_output', 'csv_replace_nulls_with',
        gettext("Replace null values with"), 'text', 'NULL',
        category_label=PREF_LABEL_CSV_TXT,
        help_str=gettext('Specifies the string that represents a null value '
                         'while downloading query results as CSV. You can '
                         'specify any arbitrary string to represent a '
                         'null value, with quotes if desired.'),
        allow_blanks=True
    )

    self.results_grid_quoting = self.preference.register(
        'Results_grid', 'results_grid_quoting',
        gettext("Result copy quoting"), 'options', 'strings',
        category_label=PREF_LABEL_RESULTS_GRID,
        options=[{'label': gettext('None'), 'value': 'none'},
                 {'label': gettext('All'), 'value': 'all'},
                 {'label': gettext('Strings'), 'value': 'strings'}],
        control_props={
            'allowClear': False,
            'tags': False
        }
    )

    self.results_grid_quote_char = self.preference.register(
        'Results_grid', 'results_grid_quote_char',
        gettext("Result copy quote character"), 'options', '"',
        category_label=PREF_LABEL_RESULTS_GRID,
        options=[{'label': '"', 'value': '"'},
                 {'label': '\'', 'value': '\''}],
        control_props={
            'allowClear': False,
            'tags': False
        }
    )

    self.results_grid_field_separator = self.preference.register(
        'Results_grid', 'results_grid_field_separator',
        gettext("Result copy field separator"), 'options', '\t',
        category_label=PREF_LABEL_RESULTS_GRID,
        options=[{'label': ';', 'value': ';'},
                 {'label': ',', 'value': ','},
                 {'label': '|', 'value': '|'},
                 {'label': gettext('Tab'), 'value': '\t'}],
        control_props={
            'allowClear': False,
            'tags': False
        }
    )

    self.column_data_auto_resize = self.preference.register(
        'Results_grid', 'column_data_auto_resize',
        gettext("Columns sized by"), 'radioModern', 'by_data',
        options=[{'label': gettext('Column data'), 'value': 'by_data'},
                 {'label': gettext('Column name'), 'value': 'by_name'}],
        category_label=PREF_LABEL_RESULTS_GRID,
        help_str=gettext(
            'If set to \'Column data\' columns will auto-size to the maximum '
            'width of the data in the column as loaded in the first batch. If '
            'set to \'Column name\', the column will be sized to the widest '
            'of the data type or column name.'
        ),
        dependents=['column_data_max_width']
    )

    self.column_data_max_width = self.preference.register(
        'Results_grid', 'column_data_max_width',
        gettext("Maximum column width"), 'integer', 0,
        category_label=PREF_LABEL_RESULTS_GRID,
        help_str=gettext(
            'Specify the maximum width of the column in pixels when '
            '\'Columns sized by \' is set to \'Column data\'.'
        ),
    )

    self.on_demand_record_count = self.preference.register(
        'Results_grid', 'on_demand_record_count',
        gettext("On demand record count"), 'integer', ON_DEMAND_RECORD_COUNT,
        min_val=100,
        category_label=PREF_LABEL_RESULTS_GRID,
        help_str=gettext('Specify the number of records to fetch in one batch '
                         'in query tool when query result set is large. '
                         'Changing this value will override '
                         'ON_DEMAND_RECORD_COUNT setting from config file.')
    )

    self.sql_font_size = self.preference.register(
        'Editor', 'sql_font_size',
        gettext("Font size"), 'numeric', '1',
        min_val=0.1,
        max_val=10,
        category_label=PREF_LABEL_DISPLAY,
        help_str=gettext(
            'The font size to use for the SQL text boxes and editors. '
            'The value specified is in "em" units, in which 1 is the '
            'default relative font size. For example, to increase the '
            'font size by 20 percent use a value of 1.2, or to reduce '
            'by 20 percent, use a value of 0.8. Minimum 0.1, maximum 10.'
        )
    )

    self.display_connection_status = self.preference.register(
        'display', 'connection_status',
        gettext("Connection status"), 'boolean', True,
        category_label=PREF_LABEL_DISPLAY,
        help_str=gettext('If set to True, the Query Tool '
                         'will monitor and display the connection and '
                         'transaction status.')
    )

    self.connection_status = self.preference.register(
        'display', 'connection_status_fetch_time',
        gettext("Connection status refresh rate"), 'integer', 2,
        min_val=1, max_val=600,
        category_label=PREF_LABEL_DISPLAY,
        help_str=gettext(
            'The number of seconds between connection/transaction '
            'status polls.'
        )
    )

    self.query_success_notification = self.preference.register(
        'display', 'query_success_notification',
        gettext("Show query success notification?"), 'boolean', True,
        category_label=PREF_LABEL_DISPLAY,
        help_str=gettext('If set to True, the Query Tool '
                         'will show notifications on successful query '
                         'execution.')
    )

    self.preference.register(
        'keyboard_shortcuts',
        'execute_query',
        gettext('Execute query'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': False,
            'control': False,
            'key': {
                'key_code': 116,
                'char': 'F5'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'save_data',
        gettext('Save data changes'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': False,
            'control': False,
            'key': {
                'key_code': 117,
                'char': 'F6'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'explain_query',
        gettext('EXPLAIN query'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': False,
            'control': False,
            'key': {
                'key_code': 118,
                'char': 'F7'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'explain_analyze_query',
        gettext('EXPLAIN ANALYZE query'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': True,
            'control': False,
            'key': {
                'key_code': 118,
                'char': 'F7'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'clear_query',
        gettext('Clear query'),
        'keyboardshortcut',
        {
            'alt': True,
            'shift': False,
            'control': True,
            'key': {
                'key_code': 76,
                'char': 'L'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'download_results',
        gettext('Download Results'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': False,
            'control': False,
            'key': {
                'key_code': 119,
                'char': 'F8'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'move_previous',
        gettext('Previous tab'),
        'keyboardshortcut',
        {
            'alt': True,
            'shift': True,
            'control': False,
            'key': {
                'key_code': 219,
                'char': '['
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'move_next',
        gettext('Next tab'),
        'keyboardshortcut',
        {
            'alt': True,
            'shift': True,
            'control': False,
            'key': {
                'key_code': 221,
                'char': ']'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'switch_panel',
        gettext('Switch Panel'),
        'keyboardshortcut',
        {
            'alt': True,
            'shift': True,
            'control': False,
            'key': {
                'key_code': 9,
                'char': 'Tab'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    # All about access keys
    self.preference.register(
        'keyboard_shortcuts', 'btn_open_file',
        gettext('Accesskey (Open file)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 79,
                'char': 'o'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_save_file',
        gettext('Accesskey (Save file)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 83,
                'char': 's'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_paste_row',
        gettext('Accesskey (Paste rows)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 80,
                'char': 'p'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_delete_row',
        gettext('Accesskey (Delete rows)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 68,
                'char': 'd'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_filter_dialog',
        gettext('Accesskey (Filter dialog)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 70,
                'char': 'f'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_filter_options',
        gettext('Accesskey (Filter options)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 73,
                'char': 'i'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_rows_limit',
        gettext('Accesskey (Rows limit)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 82,
                'char': 'r'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_execute_options',
        gettext('Accesskey (Execute options)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 88,
                'char': 'x'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_cancel_query',
        gettext('Accesskey (Cancel query)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 81,
                'char': 'q'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_conn_status',
        gettext('Accesskey (Connection status)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 84,
                'char': 't'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts', 'btn_find_options',
        gettext('Accesskey (Find options)'), 'keyboardshortcut',
        {
            'key': {
                'key_code': 78,
                'char': 'n'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=accesskey_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'toggle_case',
        gettext('Toggle case of selected text'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': True,
            'control': True,
            'key': {
                'key_code': 85,
                'char': 'u'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'auto_completion', 'keywords_in_uppercase',
        gettext("Keywords in uppercase"), 'boolean', True,
        category_label=gettext('Auto completion'),
        help_str=gettext('If set to True, Keywords will be displayed '
                         'in upper case for auto completion.')
    )

    self.preference.register(
        'auto_completion', 'autocomplete_on_key_press',
        gettext("Autocomplete on key press"), 'boolean', False,
        category_label=gettext('Auto completion'),
        help_str=gettext('If set to True, autocomplete will be available on '
                         'key press along with CTRL/CMD + Space. If set to '
                         'False, autocomplete is only activated when CTRL/CMD '
                         '+ Space is pressed.')
    )

    self.preference.register(
        'keyboard_shortcuts',
        'commit_transaction',
        gettext('Commit'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': True,
            'control': True,
            'key': {
                'key_code': 77,
                'char': 'm'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.preference.register(
        'keyboard_shortcuts',
        'rollback_transaction',
        gettext('Rollback'),
        'keyboardshortcut',
        {
            'alt': False,
            'shift': True,
            'control': True,
            'key': {
                'key_code': 82,
                'char': 'r'
            }
        },
        category_label=PREF_LABEL_KEYBOARD_SHORTCUTS,
        fields=shortcut_fields
    )

    self.keyword_case = self.preference.register(
        'editor', 'keyword_case',
        gettext("Keyword case"), 'radioModern', 'upper',
        options=[{'label': gettext('Upper case'), 'value': 'upper'},
                 {'label': gettext('Lower case'), 'value': 'lower'},
                 {'label': gettext('Capitalized'), 'value': 'capitalize'}],
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext(
            'Convert keywords to upper, lower, or capitalized casing.'
        )
    )

    self.identifier_case = self.preference.register(
        'editor', 'identifier_case',
        gettext("Identifier case"), 'radioModern', 'upper',
        options=[{'label': gettext('Upper case'), 'value': 'upper'},
                 {'label': gettext('Lower case'), 'value': 'lower'},
                 {'label': gettext('Capitalized'), 'value': 'capitalize'}],
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext(
            'Convert identifiers to upper, lower, or capitalized casing.'
        )
    )

    self.strip_comments = self.preference.register(
        'editor', 'strip_comments',
        gettext("Strip comments?"), 'boolean', False,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext('If set to True, comments will be removed.')
    )

    self.reindent = self.preference.register(
        'editor', 'reindent',
        gettext("Re-indent?"), 'boolean', True,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext('If set to True, the indentations of the '
                         'statements are changed.')
    )

    self.reindent_aligned = self.preference.register(
        'editor', 'reindent_aligned',
        gettext("Re-indent aligned?"), 'boolean', False,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext('If set to True, the indentations of the '
                         'statements are changed, and statements are '
                         'aligned by keywords.')
    )

    self.spaces_around_operators = self.preference.register(
        'editor', 'spaces_around_operators',
        gettext("Spaces around operators?"), 'boolean', True,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext('If set to True, spaces are used around all '
                         'operators.')
    )

    self.comma_first = self.preference.register(
        'editor', 'comma_first',
        gettext("Comma-first notation?"), 'boolean', False,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext('If set to True, comma-first notation for column '
                         'names is used.')
    )

    self.wrap_after = self.preference.register(
        'editor', 'wrap_after',
        gettext("Wrap after N characters"), 'integer', 4,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext("The column limit (in characters) for wrapping "
                         "comma-separated lists. If zero, it puts "
                         "every item in the list on its own line.")
    )

    self.tab_size = self.preference.register(
        'editor', 'tab_size',
        gettext("Tab size"), 'integer', 4,
        min_val=2,
        max_val=8,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext(
            'The number of spaces per tab. Minimum 2, maximum 8.'
        )
    )

    self.use_spaces = self.preference.register(
        'editor', 'use_spaces',
        gettext("Use spaces?"), 'boolean', False,
        category_label=PREF_LABEL_SQL_FORMATTING,
        help_str=gettext(
            'Specifies whether or not to insert spaces instead of tabs '
            'when the tab key or auto-indent are used.'
        )
    )

    self.row_limit = self.preference.register(
        'graph_visualiser', 'row_limit',
        gettext("Row Limit"), 'integer',
        10000, min_val=1, category_label=PREF_LABEL_GRAPH_VISUALISER,
        help_str=gettext('This setting specifies the maximum number of rows '
                         'that will be plotted on a chart. Increasing this '
                         'limit may impact performance if charts are plotted '
                         'with very high numbers of rows.')
    )
