"""
Lexer Configuration Property

tab_settings: scheme default tab and indentation settings.
	tab_width: tab width, default is 4.
	indent_width: indentation width, default is 4.
	tab_as_spaces: insert tab as spaces, default is False.
	use_global_tab_settings: use global tab settings, default is True.
default_encoding: scheme default encoding, default is not set.
default_line_ending: scheme default line ending, default is not set.

line_comment_string: line comment start string, default is None.
line_comment_at_line_start: put start string at line start, default is False.
block_comment_string: block comment start and end string, default is None.
block_comment_on_new_line: put start and end string on new line, default is False.
cpp_style_comment: shortcut to use C++ style line and block comment, default is False.
shebang_exe_name: executable name for shebang, default is None.

indent_based_folding: code folding is indentation based, default is False.
indent_guide_style: indentation guide view style, default is SC_IV_LOOKBOTH.
				for indentation based folding, SC_IV_LOOKFORWARD may looks better.
default_fold_level: level list for toggle default code folding.
				level name enclosed with `[]` will be ignored.
default_fold_ignore_inner: inner style to be ignored for toggle default code folding.
				normally this is function definition style.

printf_format_specifier: has C printf like format specifier, default is False.
format_specifier_style: style for format specifier, default is zero.
escape_char_start: character used to escape special characters, default is backslash.
escape_char_style: style for escape character, default is zero.
raw_string_style: styles where backslash is treated literally, default are zeros.
character_style: styles for character literal, default are zeros.
none_quote_style: style for single quote not used for quotation, default is zero.

angle_bracket_generic: has C++ like template or generic with angle bracket, default is False.
operator_style:	styles for operator punctuation, default are zeros.
"""

from enum import IntFlag

class LexerAttr(IntFlag):
	Default = 0
	TabAsSpaces = 1 << 0			# tab_as_spaces
	NoGlobalTabSettings = 1 << 1	# use_global_tab_settings
	NoLineComment = 1 << 2			# line_comment_string
	NoBlockComment = 1 << 3			# block_comment_string
	IndentBasedFolding = 1 << 4		# indent_based_folding
	IndentLookForward = 1 << 5		# indent_guide_style
	PrintfFormatSpecifier = 1 << 6	# printf_format_specifier
	AngleBracketGeneric = 1 << 7	# angle_bracket_generic

class KeywordAttr(IntFlag):
	Default = 0
	MakeLower = 1	# need convert to lower case for lexer.
	PreSorted = 2	# word list is presorted.
	NoLexer = 4		# not used by lexer, listed for auto-completion.
	NoAutoComp = 8	# don't add to default auto-completion list.
	Special = 256	# used by context based auto-completion.

TabSettings_Default = {
	'tab_width': 4,
	'indent_width': 4,
	'tab_as_spaces': False,
	'use_global_tab_settings': True,
}
TabSettings_Tab4 = {
	'tab_width': 4,
	'indent_width': 4,
	'tab_as_spaces': False,
	'use_global_tab_settings': False,
}
TabSettings_Space4 = {
	'tab_width': 4,
	'indent_width': 4,
	'tab_as_spaces': True,
	'use_global_tab_settings': False,
}
TabSettings_Space2 = {
	'tab_width': 2,
	'indent_width': 2,
	'tab_as_spaces': True,
	'use_global_tab_settings': False,
}

DefaultFoldLevel = ['level1', 'level2']
NoEscapeCharacter = '\0'

LexerConfigMap = {
	'NP2LEX_TEXTFILE': {
		'indent_based_folding': True,
		'indent_guide_style': 'forward',
		'escape_char_start': NoEscapeCharacter,
	},
	'NP2LEX_2NDTEXTFILE': {
		'indent_based_folding': True,
		'indent_guide_style': 'forward',
		'escape_char_start': NoEscapeCharacter,
	},
	'NP2LEX_ANSI': {
		'default_encoding': 'DOS-437',
		'default_line_ending': 'CRLF',
		'indent_based_folding': True,
		'indent_guide_style': 'forward',
		'escape_char_start': NoEscapeCharacter,
	},

	'NP2LEX_ABAQUS': {
		'line_comment_string': '**',
		'operator_style': ['SCE_APDL_OPERATOR'],
	},
	'NP2LEX_ACTIONSCRIPT': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'anonymous object', 'method'],
		'default_fold_ignore_inner': 'SCE_JS_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_JS_ESCAPECHAR',
		'angle_bracket_generic': True,
		'operator_style': ['SCE_JS_OPERATOR', 'SCE_JS_OPERATOR2', 'SCE_JS_OPERATOR_PF'],
	},
	'NP2LEX_APDL': {
		'line_comment_string': '!',
		'operator_style': ['SCE_APDL_OPERATOR'],
	},
	'NP2LEX_ASM': {
		'line_comment_string': [';', '# ', '//', '@ '],
		'block_comment_string': ('/*', '*/'),
		'operator_style': ['SCE_ASM_OPERATOR'],
	},
	'NP2LEX_ASYMPTOTE': {
		'cpp_style_comment': True,
		'default_fold_level': ['struct', 'function'],
		'default_fold_ignore_inner': 'SCE_ASY_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_ASY_ESCAPECHAR',
		'operator_style': ['SCE_ASY_OPERATOR'],
	},
	'NP2LEX_AUTOHOTKEY': {
		'line_comment_string': ';',
		'block_comment_string': ('/*', '*/'),
		#'block_comment_on_new_line': True,
		'default_fold_level': ['class', 'function'],
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_AHK_FORMAT_SPECIFIER',
		'escape_char_start': '`',
		'escape_char_style': 'SCE_AHK_ESCAPECHAR',
		'operator_style': ['SCE_AHK_OPERATOR'],
	},
	'NP2LEX_AUTOIT3': {
		'line_comment_string': ';',
		'block_comment_string': ('#cs', '#ce'),
		'block_comment_on_new_line': True,
		'operator_style': ['SCE_AU3_OPERATOR'],
	},
	'NP2LEX_AVISYNTH': {
		'line_comment_string': '#',
		'block_comment_string': ('/*', '*/'),
		'default_fold_level': ['function'],
		'escape_char_style': 'SCE_AVS_ESCAPECHAR',
		'operator_style': ['SCE_AVS_OPERATOR'],
	},
	'NP2LEX_AWK': {
		'line_comment_string': '#',
		'shebang_exe_name': 'awk',
		'default_fold_level': ['namespace', 'function'],
		'default_fold_ignore_inner': 'SCE_AWK_FUNCTION_DEFINITION',
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_AWK_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_AWK_ESCAPECHAR',
		'operator_style': ['SCE_AWK_OPERATOR'],
	},

	'NP2LEX_BASH': {
		'default_encoding': 'utf-8',
		'default_line_ending': 'LF',
		'line_comment_string': ['#', 'dnl '],
		'shebang_exe_name': ['bash', 'm4', 'csh'],
		'raw_string_style': ['SCE_SH_STRING_SQ'],
		'operator_style': ['SCE_SH_OPERATOR'],
	},
	'NP2LEX_BATCH': {
		'default_encoding': 'ANSI',
		'default_line_ending': 'CRLF',
		'line_comment_string': '@rem ',
		'line_comment_at_line_start': True,
		'escape_char_start': '^',
		'escape_char_style': 'SCE_BAT_ESCAPECHAR',
		'operator_style': ['SCE_BAT_OPERATOR'],
	},
	'NP2LEX_BLOCKDIAG': {
		'line_comment_string': '//',
		'block_comment_string': [('/*', '*/'), ('<!--', '-->')],
		'default_fold_level': ['graph', 'subgraph'],
		'escape_char_style': 'SCE_GRAPHVIZ_ESCAPECHAR',
		'operator_style': ['SCE_GRAPHVIZ_OPERATOR'],
	},

	'NP2LEX_CIL': {
		'cpp_style_comment': True,
		'operator_style': ['SCE_C_OPERATOR'],
	},
	'NP2LEX_CMAKE': {
		'line_comment_string': '#',
		'block_comment_string': ('#[[', ']]'),
		'escape_char_style': 'SCE_CMAKE_ESCAPECHAR',
		'angle_bracket_generic': True, # for bracket argument $<>
		'operator_style': ['SCE_CMAKE_OPERATOR'],
	},
	'NP2LEX_COFFEESCRIPT': {
		'line_comment_string': '#',
		'block_comment_string': ('###', '###'),
		'indent_based_folding': True,
		'indent_guide_style': 'forward',
		'default_fold_level': ['class', 'function'],
		'escape_char_style': 'SCE_COFFEESCRIPT_ESCAPECHAR',
		'operator_style': ['SCE_COFFEESCRIPT_OPERATOR', 'SCE_COFFEESCRIPT_OPERATOR2', 'SCE_COFFEESCRIPT_OPERATOR_PF'],
	},
	'NP2LEX_CONFIG': {
		'line_comment_string': '#',
		'operator_style': ['SCE_CONF_OPERATOR'],
	},
	'NP2LEX_CPP': {
		'cpp_style_comment': True,
		'default_fold_level': ['preprocessor', 'namespace', 'class', 'method'],
		'printf_format_specifier': True,
		'raw_string_style': ['SCE_C_STRINGRAW'],
		'character_style': ['SCE_C_CHARACTER'],
		'none_quote_style': 'SCE_C_NUMBER',
		'angle_bracket_generic': True,
		'operator_style': ['SCE_C_OPERATOR'],
	},
	'NP2LEX_CSHARP': {
		'cpp_style_comment': True,
		'default_fold_level': ['namespace', 'class', 'method'],
		'default_fold_ignore_inner': 'SCE_CSHARP_FUNCTION_DEFINITION',
		'format_specifier_style': 'SCE_CSHARP_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_CSHARP_ESCAPECHAR',
		'raw_string_style': ['SCE_CSHARP_VERBATIM_STRING', 'SCE_CSHARP_INTERPOLATED_VERBATIM_STRING',
			'SCE_CSHARP_RAWSTRING_SL', 'SCE_CSHARP_INTERPOLATED_RAWSTRING_SL',
			'SCE_CSHARP_RAWSTRING_ML', 'SCE_CSHARP_INTERPOLATED_RAWSTRING_ML',
		],
		'character_style': ['SCE_CSHARP_CHARACTER'],
		'angle_bracket_generic': True,
		'operator_style': ['SCE_CSHARP_OPERATOR', 'SCE_CSHARP_OPERATOR2'],
	},
	'NP2LEX_CSS': {
		'cpp_style_comment': True,
		'escape_char_style': 'SCE_CSS_ESCAPECHAR',
		'operator_style': ['SCE_CSS_OPERATOR'],
	},

	'NP2LEX_DLANG': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'function'],
		'default_fold_ignore_inner': 'SCE_D_FUNCTION_DEFINITION',
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_D_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_D_ESCAPECHAR',
		'raw_string_style': ['SCE_D_RAWSTRING', 'SCE_D_STRING_BT'],
		'character_style': ['SCE_D_CHARACTER'],
		'operator_style': ['SCE_D_OPERATOR'],
	},
	'NP2LEX_DART': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'method'],
		'default_fold_ignore_inner': 'SCE_DART_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_DART_ESCAPECHAR',
		'raw_string_style': ['SCE_DART_RAWSTRING_SQ', 'SCE_DART_RAWSTRING_DQ',
			'SCE_DART_TRIPLE_RAWSTRING_SQ', 'SCE_DART_TRIPLE_RAWSTRING_DQ',
		],
		'angle_bracket_generic': True,
		'operator_style': ['SCE_DART_OPERATOR', 'SCE_DART_OPERATOR2'],
	},
	'NP2LEX_DIFF': {
		'default_fold_level': ['command', '[file]', 'diff'],
		'escape_char_start': NoEscapeCharacter,
	},

	'NP2LEX_FORTRAN': {
		'line_comment_string': ['!'], # omited '*'
		'block_comment_string': ('#if 0', '#endif'),
		'block_comment_on_new_line': True,
		'operator_style': ['SCE_F_OPERATOR', 'SCE_F_OPERATOR2'],
	},
	'NP2LEX_FSHARP': {
		'line_comment_string': '//',
		'block_comment_string': ('(*', '*)'),
		'operator_style': ['SCE_FSHARP_OPERATOR'],
	},

	'NP2LEX_GN': {
		'line_comment_string': '#',
		'escape_char_style': 'SCE_GN_ESCAPECHAR',
		'operator_style': ['SCE_GN_OPERATOR', 'SCE_GN_OPERATOR2'],
	},
	'NP2LEX_GO': {
		'cpp_style_comment': True,
		'default_fold_level': ['struct', 'function'],
		'default_fold_ignore_inner': 'SCE_GO_FUNCTION_DEFINITION',
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_GO_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_GO_ESCAPECHAR',
		'raw_string_style': ['SCE_GO_RAW_STRING'],
		'character_style': ['SCE_GO_CHARACTER'],
		'operator_style': ['SCE_GO_OPERATOR', 'SCE_GO_OPERATOR2'],
	},
	'NP2LEX_GRADLE': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'method'],
		'default_fold_ignore_inner': 'SCE_GROOVY_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_GROOVY_ESCAPECHAR',
		'angle_bracket_generic': True,
		'operator_style': ['SCE_GROOVY_OPERATOR', 'SCE_GROOVY_OPERATOR2', 'SCE_GROOVY_OPERATOR_PF'],
	},
	'NP2LEX_GRAPHVIZ': {
		'line_comment_string': '//',
		'block_comment_string': [('/*', '*/'), ('<!--', '-->')],
		'default_fold_level': ['graph', 'subgraph'],
		'escape_char_style': 'SCE_GRAPHVIZ_ESCAPECHAR',
		'operator_style': ['SCE_GRAPHVIZ_OPERATOR'],
	},
	'NP2LEX_GROOVY': {
		'cpp_style_comment': True,
		'shebang_exe_name': 'groovy',
		'default_fold_level': ['class', 'method'],
		'default_fold_ignore_inner': 'SCE_GROOVY_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_GROOVY_ESCAPECHAR',
		'angle_bracket_generic': True,
		'operator_style': ['SCE_GROOVY_OPERATOR', 'SCE_GROOVY_OPERATOR2', 'SCE_GROOVY_OPERATOR_PF'],
	},

	'NP2LEX_HAXE': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'method'],
		'default_fold_ignore_inner': 'SCE_HAXE_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_HAXE_ESCAPECHAR',
		'angle_bracket_generic': True,
		'operator_style': ['SCE_HAXE_OPERATOR', 'SCE_HAXE_OPERATOR2'],
	},
	'NP2LEX_HTML': {
		'tab_settings': TabSettings_Space2,
		'line_comment_string': ['//', "'", '#'],
		'block_comment_string': [('<!--', '-->'), ('/*', '*/'), ('--', '--')],
		'default_fold_level': ['level1', 'level2', 'level13', 'level4'],
		#'escape_char_start': NoEscapeCharacter, # backslash for embedded script or style
	},

	'NP2LEX_INI': {
		'line_comment_string': ';',
		'default_fold_level': ['section', 'comment'],
		'escape_char_start': NoEscapeCharacter,
	},
	'NP2LEX_INNOSETUP': {
		'line_comment_string': [';', '//'],
		'block_comment_string': [('/*', '*/'), ('{', '}'), ('(*', '*)')],
		'default_fold_level': ['section', 'code'],
		'escape_char_start': NoEscapeCharacter,
		'operator_style': ['SCE_INNO_OPERATOR'],
	},

	'NP2LEX_JAMFILE': {
		'line_comment_string': '#',
		'block_comment_string': ('#|', '|#'),
		'escape_char_style': 'SCE_JAM_ESCAPECHAR',
		'operator_style': ['SCE_JAM_OPERATOR'],
	},
	'NP2LEX_JAVA': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'inner class', 'method'],
		'default_fold_ignore_inner': 'SCE_JAVA_FUNCTION_DEFINITION',
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_JAVA_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_JAVA_ESCAPECHAR',
		'character_style': ['SCE_JAVA_CHARACTER'],
		'angle_bracket_generic': True,
		'operator_style': ['SCE_JAVA_OPERATOR'],
	},
	'NP2LEX_JAVASCRIPT': {
		'cpp_style_comment': True,
		'shebang_exe_name': 'node',
		'default_fold_level': ['class', 'anonymous object', 'method'],
		'default_fold_ignore_inner': 'SCE_JS_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_JS_ESCAPECHAR',
		'operator_style': ['SCE_JS_OPERATOR', 'SCE_JS_OPERATOR2', 'SCE_JS_OPERATOR_PF'],
	},
	'NP2LEX_JSON': {
		'cpp_style_comment': True,
		'default_fold_level': ['level1', 'level2', 'level13', 'level4'],
		'escape_char_style': 'SCE_JSON_ESCAPECHAR',
		'operator_style': ['SCE_JSON_OPERATOR'],
	},
	'NP2LEX_JULIA': {
		'line_comment_string': '#',
		'block_comment_string': ('#=', '=#'),
		'default_fold_level': ['struct', 'method'],
		'default_fold_ignore_inner': 'SCE_JULIA_FUNCTION_DEFINITION',
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_JULIA_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_JULIA_ESCAPECHAR',
		'raw_string_style': ['SCE_JULIA_RAWSTRING', 'SCE_JULIA_TRIPLE_RAWSTRING'],
		'character_style': ['SCE_JULIA_CHARACTER'],
		'operator_style': ['SCE_JULIA_OPERATOR', 'SCE_JULIA_OPERATOR2'],
	},

	'NP2LEX_KOTLIN': {
		'cpp_style_comment': True,
		#'shebang_exe_name': 'kotlin',
		'default_fold_level': ['class', 'inner class', 'method'],
		'default_fold_ignore_inner': 'SCE_KOTLIN_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_KOTLIN_ESCAPECHAR',
		'raw_string_style': ['SCE_KOTLIN_RAWSTRING'],
		'character_style': ['SCE_KOTLIN_CHARACTER'],
		'angle_bracket_generic': True,
		'operator_style': ['SCE_KOTLIN_OPERATOR', 'SCE_KOTLIN_OPERATOR2'],
	},

	'NP2LEX_LATEX': {
		'line_comment_string': '%',
		'block_comment_string': ('\\begin{comment}', '\\end{comment}'),
		'block_comment_on_new_line': True,
		'escape_char_start': '^',
		'escape_char_style': 'SCE_L_SPECIAL',
		'operator_style': ['SCE_L_OPERATOR'],
	},
	'NP2LEX_LISP': {
		'line_comment_string': ';',
		'block_comment_string': ('#|',  '|#'),
		'operator_style': ['SCE_C_OPERATOR'],
	},
	'NP2LEX_LLVM': {
		'line_comment_string': ';',
		'escape_char_style': 'SCE_LLVM_ESCAPECHAR',
		'operator_style': ['SCE_LLVM_OPERATOR'],
	},
	'NP2LEX_LUA': {
		'line_comment_string': '--',
		'block_comment_string': ('--[[', '--]]'),
		'shebang_exe_name': 'lua',
		'default_fold_level': ['class', 'function'],
		'printf_format_specifier': True,
		'operator_style': ['SCE_LUA_OPERATOR'],
	},

	'NP2LEX_MAKEFILE': {
		'tab_settings': TabSettings_Tab4,
		'line_comment_string': '#',
		'escape_char_start': NoEscapeCharacter,
		'operator_style': ['SCE_MAKE_OPERATOR'],
	},
	'NP2LEX_MARKDOWN': {
		'block_comment_string': ('<!--', '-->'),
		'default_fold_level': ['header1', 'header2'],
		'escape_char_style': 'SCE_MARKDOWN_ESCAPECHAR',
	},
	'NP2LEX_MATLAB': {
		'line_comment_string': ['%', '//'],
		'block_comment_string': [('%{', '}%'), ('/*', '*/')],
		'block_comment_on_new_line': True,
		'printf_format_specifier': True,
		#'escape_char_start': NoEscapeCharacter, # backslash for Octave escape character
		'operator_style': ['SCE_MAT_OPERATOR'],
	},

	'NP2LEX_NSIS': {
		'line_comment_string': ['#'], # omited ';'
		'block_comment_string': ('/*', '*/'),
		'default_fold_level': ['section', 'function'],
		'escape_char_style': 'SCE_NSIS_ESCAPECHAR',
		'operator_style': ['SCE_NSIS_OPERATOR'],
	},

	'NP2LEX_PASCAL': {
		'line_comment_string': '//',
		'block_comment_string': [('{', '}')], # omited ('(*', '*)')
		'operator_style': ['SCE_PAS_OPERATOR'],
	},
	'NP2LEX_PERL': {
		'line_comment_string': '#',
		'shebang_exe_name': 'perl',
		'printf_format_specifier': True,
		'raw_string_style': ['SCE_PL_STRING_SQ'],
		'operator_style': ['SCE_PL_OPERATOR'],
	},
	'NP2LEX_PHP': {
		'line_comment_string': ['//', '#'],
		'block_comment_string': [('/*', '*/'), ('<!--', '-->'), ('--', '--')],
		'shebang_exe_name': 'php',
		'default_fold_level': ['[php tag]', 'class', 'method'],
		'default_fold_ignore_inner': 'SCE_PHP_FUNCTION_DEFINITION',
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_PHP_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_PHP_ESCAPECHAR',
		'raw_string_style': ['SCE_PHP_STRING_SQ', 'SCE_PHP_NOWDOC'],
		'operator_style': ['SCE_PHP_OPERATOR', 'SCE_PHP_OPERATOR2'],
	},
	'NP2LEX_POWERSHELL': {
		'line_comment_string': '#',
		'block_comment_string': ('<#', '#>'),
		'escape_char_start': '`',
		'raw_string_style': ['SCE_POWERSHELL_STRING_SQ'],
		'operator_style': ['SCE_POWERSHELL_OPERATOR'],
	},
	'NP2LEX_PYTHON': {
		'line_comment_string': '#',
		'shebang_exe_name': 'python3',
		'indent_based_folding': True,
		'indent_guide_style': 'forward',
		'default_fold_level': ['class', 'function'],
		'default_fold_ignore_inner': 'SCE_PY_FUNCTION_DEFINITION',
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_PY_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_PY_ESCAPECHAR',
		'raw_string_style': ['SCE_PY_RAWSTRING_SQ', 'SCE_PY_RAWSTRING_DQ',
			'SCE_PY_TRIPLE_RAWSTRING_SQ', 'SCE_PY_TRIPLE_RAWSTRING_DQ',
			'SCE_PY_RAWFMTSTRING_SQ', 'SCE_PY_RAWFMTSTRING_DQ',
			'SCE_PY_TRIPLE_RAWFMTSTRING_SQ', 'SCE_PY_TRIPLE_RAWFMTSTRING_DQ',
			'SCE_PY_RAWBYTES_SQ', 'SCE_PY_RAWBYTES_DQ',
			'SCE_PY_TRIPLE_RAWBYTES_SQ', 'SCE_PY_TRIPLE_RAWBYTES_DQ',
		],
		'operator_style': ['SCE_PY_OPERATOR', 'SCE_PY_OPERATOR2'],
	},

	'NP2LEX_RLANG': {
		'line_comment_string': '#',
		'block_comment_string': ('if (FALSE) {', '}'),
		'block_comment_on_new_line': True,
		'default_fold_level': ['function'],
		'printf_format_specifier': True,
		'format_specifier_style': 'SCE_R_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_R_ESCAPECHAR',
		'operator_style': ['SCE_R_OPERATOR', 'SCE_R_INFIX'],
	},
	'NP2LEX_REBOL': {
		'line_comment_string': ';',
		'block_comment_string': ('comment {', '}'),
		'block_comment_on_new_line': True,
		'escape_char_start': '^',
		'escape_char_style': 'SCE_REBOL_ESCAPECHAR',
		'none_quote_style': 'SCE_REBOL_SYMBOL',
		'operator_style': ['SCE_REBOL_OPERATOR'],
	},
	'NP2LEX_RESOURCESCRIPT': {
		'cpp_style_comment': True,
		'default_fold_level': ['preprocessor', 'resource'],
		'printf_format_specifier': True,
		'character_style': ['SCE_C_CHARACTER'],
		'none_quote_style': 'SCE_C_NUMBER',
		'operator_style': ['SCE_C_OPERATOR'],
	},
	'NP2LEX_RUBY': {
		'line_comment_string': '#',
		'shebang_exe_name': 'ruby',
		'default_fold_level': ['module', 'class', 'method'],
		'default_fold_ignore_inner': 'SCE_RB_DEF_NAME',
		'printf_format_specifier': True,
		'raw_string_style': ['SCE_RB_STRING_SQ'],
		'operator_style': ['SCE_RB_OPERATOR'],
	},
	'NP2LEX_RUST': {
		'cpp_style_comment': True,
		#'shebang_exe_name': 'rust',
		'default_fold_level': ['struct', 'function'],
		'default_fold_ignore_inner': 'SCE_RUST_FUNCTION_DEFINITION',
		'format_specifier_style': 'SCE_RUST_FORMAT_SPECIFIER',
		'escape_char_style': 'SCE_RUST_ESCAPECHAR',
		'raw_string_style': ['SCE_RUST_RAW_STRING', 'SCE_RUST_RAW_BYTESTRING'],
		'character_style': ['SCE_RUST_CHARACTER', 'SCE_RUST_BYTE_CHARACTER'],
		'none_quote_style': 'SCE_RUST_LIFETIME',
		'operator_style': ['SCE_RUST_OPERATOR'],
	},

	'NP2LEX_SCALA': {
		'cpp_style_comment': True,
		'shebang_exe_name': 'scala',
		'default_fold_level': ['class', 'inner class', 'method'],
		'character_style': ['SCE_C_CHARACTER'],
		'operator_style': ['SCE_C_OPERATOR'],
	},
	'NP2LEX_SMALI': {
		'line_comment_string': '#',
		'default_fold_level': ['.method', '.switch'],
		'operator_style': ['SCE_SMALI_OPERATOR'],
	},
	'NP2LEX_SQL': {
		'line_comment_string': '-- ', # extra space
		'block_comment_string': ('/*', '*/'),
		'default_fold_level': ['function'],
		'escape_char_style': 'SCE_SQL_ESCAPECHAR',
		'operator_style': ['SCE_SQL_OPERATOR'], # ignore q'{SCE_SQL_QOPERATOR}'
	},
	'NP2LEX_SWIFT': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'function'],
		'default_fold_ignore_inner': 'SCE_SWIFT_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_SWIFT_ESCAPECHAR',
		'angle_bracket_generic': True,
		'operator_style': ['SCE_SWIFT_OPERATOR', 'SCE_SWIFT_OPERATOR2'],
	},

	'NP2LEX_TCL': {
		'line_comment_string': '#',
		'block_comment_string': ('if (0) {', '}'),
		'block_comment_on_new_line': True,
		'shebang_exe_name': 'wish',
		'printf_format_specifier': True,
		'operator_style': ['SCE_TCL_MODIFIER'],
	},
	'NP2LEX_TEXINFO': {
		'line_comment_string': '@c ',
		'escape_char_start': '@',
		'escape_char_style': 'SCE_L_SPECIAL',
		'operator_style': ['SCE_L_OPERATOR'],
	},
	'NP2LEX_TOML': {
		'line_comment_string': '#',
		'default_fold_level': ['table', 'comment'],
		'escape_char_style': 'SCE_TOML_ESCAPECHAR',
		'operator_style': ['SCE_TOML_OPERATOR'],
	},
	'NP2LEX_TYPESCRIPT': {
		'cpp_style_comment': True,
		'default_fold_level': ['class', 'anonymous object', 'method'],
		'default_fold_ignore_inner': 'SCE_JS_FUNCTION_DEFINITION',
		'escape_char_style': 'SCE_JS_ESCAPECHAR',
		'angle_bracket_generic': True,
		'operator_style': ['SCE_JS_OPERATOR', 'SCE_JS_OPERATOR2', 'SCE_JS_OPERATOR_PF'],
	},

	'NP2LEX_VBSCRIPT': {
		'line_comment_string': "'",
		'default_fold_level': ['function'],
		'escape_char_start': NoEscapeCharacter,
		'none_quote_style': 'SCE_B_COMMENT',
		'operator_style': ['SCE_B_OPERATOR'],
	},
	'NP2LEX_VERILOG': {
		'cpp_style_comment': True,
		'none_quote_style': 'SCE_V_NUMBER',
		'operator_style': ['SCE_V_OPERATOR'],
	},
	'NP2LEX_VHDL': {
		'line_comment_string': '--',
		'block_comment_string': ('/*', '*/'),
		'operator_style': ['SCE_VHDL_OPERATOR'],
	},
	'NP2LEX_VIM': {
		'line_comment_string': '"',
		'escape_char_style': 'SCE_YAML_ESCAPECHAR',
		'raw_string_style': ['SCE_VIM_STRING_SQ'],
		'operator_style': ['SCE_VIM_OPERATOR'],
	},
	'NP2LEX_VISUALBASIC': {
		'line_comment_string': "'",
		'default_fold_level': ['class', 'function'],
		'escape_char_start': NoEscapeCharacter,
		'none_quote_style': 'SCE_B_COMMENT',
		'operator_style': ['SCE_B_OPERATOR'],
	},

	'NP2LEX_WASM': {
		'line_comment_string': ';;',
		'block_comment_string': ('(;', ';)'),
		'escape_char_style': 'SCE_WASM_ESCAPECHAR',
		'operator_style': ['SCE_WASM_OPERATOR'],
	},
	'NP2LEX_XML': {
		'line_comment_string': ['//', "'", '#'],
		'block_comment_string': [('<!--', '-->'), ('/*', '*/'), ('--', '--')],
		'default_fold_level': ['level1', 'level2', 'level13', 'level4'],
		'escape_char_start': NoEscapeCharacter,
	},
	'NP2LEX_YAML': {
		'tab_settings': TabSettings_Space2,
		'line_comment_string': '#',
		'indent_based_folding': True,
		'indent_guide_style': 'forward',
		'default_fold_level': ['level1', 'level2', 'level13', 'level4'],
		'escape_char_style': 'SCE_YAML_ESCAPECHAR',
		'operator_style': ['SCE_YAML_OPERATOR'],
	},
}

def get_enum_flag_expr(flag, merge=True, separator='_'):
	cls = flag.__class__
	prefix = cls.__name__ + separator
	if flag.name:
		return prefix + flag.name

	result = []
	values = cls.__members__.values()
	for value in values:
		if flag & value:
			result.append(prefix + value.name)
	if merge:
		return ' | '.join(result)
	return result

def dump_enum_flag(cls, indent='', anonymous=True, as_shift=False, max_value=None, separator='_'):
	prefix = cls.__name__ + separator
	values = cls.__members__.values()
	name = '' if anonymous else cls.__name__ + ' '
	output = [f'{indent}enum {name}{{']
	for flag in values:
		value = int(flag)
		if not max_value or value < max_value:
			if value and as_shift:
				assert value.bit_count() == 1, flag
				value = f'1 << {value.bit_length() - 1}'
			output.append(f'{indent}\t{prefix}{flag.name} = {value},')
	output.append(f'{indent}}};')
	return output

CEscapeMap = {
	'\0': r'\0',
	'\a': r'\a',
	'\b': r'\b',
	'\n': r'\n',
	'\r': r'\r',
	'\f': r'\f',
	'\v': r'\v',
	'\\': r'\\',
	'\'': r'\'',
	'\"': r'\"',
}

def escape_c_char(ch):
	if ch in CEscapeMap:
		return CEscapeMap[ch]
	if ch < ' ' or ord(ch) >= 127:
		return f'\\x{ord(ch):02x}'
	return ch

def escape_c_string(s):
	return ''.join(escape_c_char(ch) for ch in s)

def quote_c_char(ch):
	return "'" + escape_c_char(ch) + "'"

def MergeSwitchCaseList(caseList):
	codeMap = {}
	for label, code in sorted(caseList.items()):
		if code in codeMap:
			codeMap[code].append(label)
		else:
			codeMap[code] = [label]

	output = []
	indent = '\t'
	for code, label in codeMap.items():
		output.extend(f'{indent}case {key}:' for key in label)
		output.extend(code)
	return output


def BuildLexerConfigContent(rid, keywordAttr):
	config = LexerConfigMap.get(rid, {})
	if rid and not (config or keywordAttr):
		return ['\tSCHEME_SETTINGS_DEFAULT,']

	tab_settings = config.get('tab_settings', TabSettings_Default)
	# lexer attribute
	flag = LexerAttr.Default
	if tab_settings['tab_as_spaces']:
		flag |= LexerAttr.TabAsSpaces
	if not tab_settings['use_global_tab_settings']:
		flag |= LexerAttr.NoGlobalTabSettings

	# line comment, block comment
	if not config.get('cpp_style_comment', False):
		if not config.get('line_comment_string', ''):
			flag |= LexerAttr.NoLineComment
		if not config.get('block_comment_string', ''):
			flag |= LexerAttr.NoBlockComment

	# indentation guide
	indent_based_folding = config.get('indent_based_folding', False)
	if indent_based_folding:
		flag |= LexerAttr.IndentBasedFolding
	style = config.get('indent_guide_style', '')
	if style == 'forward':
		flag |= LexerAttr.IndentLookForward

	# styles
	if config.get('printf_format_specifier', False):
		flag |= LexerAttr.PrintfFormatSpecifier
	if config.get('angle_bracket_generic', False):
		flag |= LexerAttr.AngleBracketGeneric

	output = ['\t{']
	indent = '\t\t'
	expr = get_enum_flag_expr(flag, merge=False)
	if isinstance(expr, str):
		output.append(f'{indent}{expr},')
	else:
		output.extend(f'{indent}{item} |' for item in expr)
		output[-1] = output[-1][:-2] + ','

	# tab width, indent width
	output.append(f"{indent}TAB_WIDTH_{tab_settings['tab_width']}, INDENT_WIDTH_{tab_settings['indent_width']},")

	# default fold level, default fold ignore inner
	foldLevel = config.get('default_fold_level', DefaultFoldLevel)
	levelList = []
	for index, comment in enumerate(foldLevel):
		if comment[0] != '[': # omit this level
			levelList.append(f'(1 << {index + indent_based_folding})')
	expr = ' | '.join(levelList)
	comment = ', '.join(foldLevel)
	if rid:
		output.append(f'{indent}{expr}, // {comment}')
	else:
		output.append(f'{indent}{expr}, /* {comment} */')
	output.append(f"{indent}{config.get('default_fold_ignore_inner', '0')},")

	# escape character, format specifier
	start = config.get('escape_char_start', '\\')
	style = config.get('escape_char_style', '0')
	assert len(start) == 1, (rid, style, start)
	output.append(f"{indent}'{escape_c_char(start)}', {style}, {config.get('format_specifier_style', '0')},")
	# raw string styles
	styles = config.get('raw_string_style', ['0'])
	output.append(f"{indent}{styles[0]},")
	# character style, none single quoted style
	styles = config.get('character_style', ['0'])
	output.append(f"{indent}{styles[0]}, {config.get('none_quote_style', '0')},")
	# operator styles
	styles = config.get('operator_style', []) + ['0', '0']
	output.append(f"{indent}{styles[0]}, {styles[1]},")

	# keyword attribute
	if keywordAttr:
		output[-1] = output[-1][:-1] # remove extra comma
		prefix = ','
		for index, attr, comment in keywordAttr:
			expr = get_enum_flag_expr(attr)
			bit = 64 if index >= 7 else 32
			output.append(f'{indent}{prefix} KeywordAttr{bit}({index}, {expr}) // {comment}')
			prefix = '|'
	else:
		expr = get_enum_flag_expr(KeywordAttr.Default)
		output.append(indent + expr)

	suffix = '\t},'
	if not rid:
		# right align continuation backslash in multi-line macro
		indent_count = len(indent)
		max_width = max(len(line) for line in output) - indent_count
		max_width = (max_width + 8) & ~3
		result = ['#define SCHEME_SETTINGS_DEFAULT\t\\']
		for index, line in enumerate(output):
			width = len(line) - indent_count
			width = (width + 4) & ~3
			padding = (max_width - width) // 4
			padding += index == 0
			result.append(line + '\t'*padding + '\\')
		output = result
		suffix = suffix[:-1]
	output.append(suffix)
	return output

def BuildLexerCommentString():
	scriptShebang = {}
	complexShebang = []
	commentLine = {}
	complexLine = []
	commentBlock = {}
	complexBlock = []
	indent = '\t\t'

	for rid, config in LexerConfigMap.items():
		if name := config.get('shebang_exe_name', None):
			if isinstance(name, str):
				code = (f'{indent}name = "{escape_c_string(name)}";', indent + 'break;', '')
				scriptShebang[rid] = code
			else:
				complexShebang.append(rid)

		if config.get('cpp_style_comment', False):
			line_comment_string = '//'
			block_comment_string = ('/*', '/*')
		else:
			line_comment_string = config.get('line_comment_string', None)
			block_comment_string = config.get('block_comment_string', None)

		if line_comment_string:
			if isinstance(line_comment_string, list) and len(line_comment_string) == 1:
				line_comment_string = line_comment_string[0]
			if isinstance(line_comment_string, str):
				start = config.get('line_comment_at_line_start', False)
				argument = 'TRUE' if start else 'FALSE'
				start = escape_c_string(line_comment_string)
				code = (f'{indent}EditToggleLineComments(L"{start}", {argument});', indent + 'break;', '')
				commentLine[rid] = code
			else:
				complexLine.append(rid)

		if block_comment_string:
			if isinstance(block_comment_string, list) and len(block_comment_string) == 1:
				block_comment_string = block_comment_string[0]
			if isinstance(block_comment_string, tuple):
				assert len(block_comment_string) == 2, (rid, block_comment_string)
				newline = config.get('block_comment_on_new_line', False)
				suffix = 'NewLine' if newline else ''
				start, end = escape_c_string(block_comment_string[0]), escape_c_string(block_comment_string[1])
				code = (f'{indent}EditEncloseSelection{suffix}(L"{start}", L"{end}");', indent + 'break;', '')
				commentBlock[rid] = code
			else:
				complexBlock.append(rid)

	commentLine = MergeSwitchCaseList(commentLine)
	commentBlock = MergeSwitchCaseList(commentBlock)
	scriptShebang = MergeSwitchCaseList(scriptShebang)
	if complexLine:
		print('complex line comment:', ', '.join(sorted(complexLine)))
	if complexBlock:
		print('complex block comment:', ', '.join(sorted(complexBlock)))
	if complexShebang:
		print('complex script shebang:', ', '.join(sorted(complexShebang)))
	return commentLine, commentBlock, scriptShebang
