#include "EditLexer.h"
#include "EditStyleX.h"

static KEYWORDLIST Keywords_Ruby = {{
//++Autogenerated -- start of section automatically generated
"BEGIN END __ENCODING__ __FILE__ __LINE__ alias and begin break case class def defined? do else elsif end ensure "
"false for if in module next nil not or redo rescue retry return self super then true undef unless until when while "
"yield "

, // 1 code folding
"begin case class def do for if module unless until while "

, // 2 regex
"and begin break case do else elsif if next not or return unless until when "

, // 3 pre-defined constants
"ARGF ARGV DATA ENV FALSE NIL "
"RUBY_COPYRIGHT RUBY_DESCRIPTION RUBY_ENGINE RUBY_ENGINE_VERSION RUBY_PLATFORM RUBY_RELEASE_DATE RUBY_REVISION "
"RUBY_VERSION "
"SCRIPT_LINES__ STDERR STDIN STDOUT TOPLEVEL_BINDING TRUE "

, // 4 pre-defined variables
"$DEBUG $FILENAME $LOADED_FEATURES $LOAD_PATH $VERBOSE $stderr $stdin $stdout "

, // 5 module
"AbstractSyntaxTree Comparable Constants Continuation Enumerable Errno FileTest Formatter GC GID Kernel Marshal Math "
"ObjectSpace Process Profiler Signal Sys UID UnicodeNormalize WaitReadable WaitWritable Warning "

, // 6 class
"AccessError AllocationError ArgumentError ArithmeticSequence Array Backtrace BasicObject Binding Buffer "
"Chain Class ClosedError ClosedQueueError CompatibilityError Complex ConditionVariable Converter ConverterNotFoundError "
"Dir DomainError "
"EAGAINWaitReadable EAGAINWaitWritable EINPROGRESSWaitReadable EINPROGRESSWaitWritable EOFError "
"EWOULDBLOCKWaitReadable EWOULDBLOCKWaitWritable Encoding EncodingError Enumerator Error Exception "
"FalseClass Fiber FiberError File Float FloatDomainError FrozenError Generator Hash "
"IO IOError IndexError InstructionSequence Integer Interrupt InvalidByteSequenceError InvalidatedError IsolationError "
"KeyError Lazy LoadError LocalJumpError Location LockedError MatchData Method Module MovedError MovedObject Mutex "
"NameError NilClass "
"NoMatchingPatternError NoMatchingPatternKeyError NoMemoryError NoMethodError Node NotImplementedError Numeric "
"Object Pool Proc Producer Queue "
"Ractor Random Range RangeError Rational Refinement RemoteError Ripper RubyVM RuntimeError "
"SchedulerInterface ScriptError SecurityError SignalException SizedQueue "
"StandardError Stat Status StopIteration String Struct Symbol SyntaxError SystemCallError SystemExit SystemStackError "
"Thread ThreadError ThreadGroup Time TracePoint TrueClass TypeError "
"UnboundMethod UncaughtThrowError UndefinedConversionError UnsafeError WeakMap Yielder ZeroDivisionError "

, // 7 built-in function
"__callee__ __dir__ __id__ __method__ __send__ "
"abort alias_method ancestors append_features at_exit attr attr_accessor attr_reader attr_writer autoload autoload? "
"binding block_given? "
"callable_methods callcc caller caller_locations catch chomp chop "
"class_eval class_exec class_variable_defined? class_variable_get class_variable_set class_variables clone "
"const_defined? const_get const_missing const_set const_source_location constants "
"define_method define_singleton_method deprecate_constant display do_until do_while dup "
"enum_for equal? eval exec exit exit! extend extend_object extended fail fork format freeze frozen? "
"gets global_variables gsub hash "
"import_methods include include? included included_modules inspect instance_eval instance_exec "
"instance_method instance_methods instance_of? "
"instance_variable_defined? instance_variable_get instance_variable_set instance_variables is_a? itself "
"kind_of? lambda load local_variables loop "
"matching_methods method method_added method_defined? method_missing method_removed method_undefined methods "
"module_eval module_exec module_function "
"name nesting new nil? object_id open "
"prepend prepend_features prepended print printf "
"private private_class_method private_constant private_instance_methods private_method_defined? private_methods "
"proc protected protected_instance_methods protected_method_defined? protected_methods public "
"public_class_method public_constant public_instance_method public_instance_methods "
"public_method public_method_defined? public_methods public_send putc puts "
"raise rand readline readlines refine remove_class_variable remove_const remove_instance_variable remove_method "
"require require_relative respond_to? respond_to_missing? ruby2_keywords "
"select send set_trace_func shortest_abbreviation singleton_class singleton_class? "
"singleton_method singleton_method_added singleton_method_removed singleton_method_undefined singleton_methods sleep "
"spawn sprintf srand sub syscall system "
"taint tainted? tap test throw to_enum to_s trace_var trap trust "
"undef_method untaint untrace_var untrust untrusted? used_modules using warn yield_self "

, // 8 function
NULL

, NULL, NULL, NULL, NULL, NULL, NULL, NULL
//--Autogenerated -- end of section automatically generated
}};

static EDITSTYLE Styles_Ruby[] = {
	EDITSTYLE_DEFAULT,
	{ MULTI_STYLE(SCE_RB_WORD, SCE_RB_WORD_DEMOTED, 0, 0), NP2StyleX_Keyword, L"bold; fore:#FF8000" },
	{ MULTI_STYLE(SCE_RB_MODULE_NAME, SCE_RB_LIKE_MODULE, 0, 0), NP2StyleX_Module, L"bold; fore:#007F7F" },
	{ MULTI_STYLE(SCE_RB_CLASS_NAME, SCE_RB_LIKE_CLASS, 0, 0), NP2StyleX_Class, L"bold; fore:#007F7F" },
	{ SCE_RB_DEF_NAME, NP2StyleX_FunctionDefinition, L"bold; fore:#A46000" },
	{ SCE_RB_FUNCTION, NP2StyleX_Function, L"fore:#A46000" },
	{ SCE_RB_BUILTIN_CONSTANT, NP2StyleX_BuiltInConstant, L"bold; fore:#008080" },
	{ SCE_RB_BUILTIN_FUNCTION, NP2StyleX_BuiltInFunction, L"fore:#0080C0" },
	{ SCE_RB_NUMBER, NP2StyleX_Number, L"fore:#FF0000" },
	{ SCE_RB_OPERATOR, NP2StyleX_Operator, L"fore:#B000B0" },
	{ SCE_RB_COMMENTLINE, NP2StyleX_Comment, L"fore:#608060" },
	{ MULTI_STYLE(SCE_RB_STRING_DQ, SCE_RB_STRING_SQ, 0, 0), NP2StyleX_String, L"fore:#008000" },
	{ SCE_RB_POD, NP2StyleX_POD, L"fore:#004000; back:#C0FFC0; eolfilled" },
	{ SCE_RB_BACKTICKS, NP2StyleX_Backticks, L"fore:#FF0080" },
	{ SCE_RB_REGEX, NP2StyleX_Regex, L"back:#A0FFA0" },
	{ SCE_RB_SYMBOL, NP2StyleX_Symbol, L"bold; fore:#FF4F0F" },
	{ MULTI_STYLE(SCE_RB_CLASS_VAR, SCE_RB_INSTANCE_VAR, SCE_RB_GLOBAL, 0), NP2StyleX_Variable, L"fore:#003CE6" },
	{ SCE_RB_HERE_DELIM, NP2StyleX_HeredocDelimiter, L"fore:#648000" },
	{ SCE_RB_HERE_Q, NP2StyleX_HeredocSingleQuoted, L"fore:#648000" },
	{ SCE_RB_HERE_QQ, NP2StyleX_HeredocDoubleQuoted,L"fore:#648000" },
	{ SCE_RB_HERE_QX, NP2StyleX_HeredocBackticks, L"fore:#E24000; back:#FFF1A8" },
	{ SCE_RB_STRING_Q, NP2StyleX_SingleQuotedString_q, L"fore:#008000" },
	{ SCE_RB_STRING_QQ, NP2StyleX_DoubleQuotedString_qq, L"fore:#008000" },
	{ SCE_RB_STRING_QX, NP2StyleX_Backticks_qx, L"fore:#E24000; back:#FFF1A8" },
	{ SCE_RB_STRING_QR, NP2StyleX_Regex_qr, L"fore:#006633; back:#FFF1A8" },
	{ SCE_RB_STRING_QW, NP2StyleX_Array_qw, L"fore:#003CE6" },
	{ SCE_RB_DATASECTION, NP2StyleX_DataSection, L"fore:#600000; back:#FFF0D8; eolfilled" },
};

EDITLEXER lexRuby = {
	SCLEX_RUBY, NP2LEX_RUBY,
//Settings++Autogenerated -- start of section automatically generated
	{
		LexerAttr_NoBlockComment |
		LexerAttr_PrintfFormatSpecifier,
		TAB_WIDTH_4, INDENT_WIDTH_4,
		(1 << 0) | (1 << 1) | (1 << 2), // module, class, method
		SCE_RB_DEF_NAME,
		0, '\\', 0,
		SCE_RB_STRING_SQ
		, KeywordAttr32(0, KeywordAttr_PreSorted) // keywords
		| KeywordAttr32(1, KeywordAttr_PreSorted | KeywordAttr_NoAutoComp) // code folding
		| KeywordAttr32(2, KeywordAttr_PreSorted | KeywordAttr_NoAutoComp) // regex
		| KeywordAttr32(3, KeywordAttr_PreSorted) // pre-defined constants
		| KeywordAttr32(4, KeywordAttr_NoLexer) // pre-defined variables
		| KeywordAttr32(5, KeywordAttr_PreSorted) // module
		| KeywordAttr32(6, KeywordAttr_PreSorted) // class
		| KeywordAttr64(7, KeywordAttr_PreSorted) // built-in function
		| KeywordAttr64(8, KeywordAttr_NoLexer) // function
	},
//Settings--Autogenerated -- end of section automatically generated
	EDITLEXER_HOLE(L"Ruby Script", Styles_Ruby),
	L"rb; ruby; rbw; rake; rjs; gemspec; podspec; cr",
	&Keywords_Ruby,
	Styles_Ruby
};
