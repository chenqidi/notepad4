#include "EditLexer.h"
#include "EditStyleX.h"

static KEYWORDLIST Keywords_Haxe = {{
//++Autogenerated -- start of section automatically generated
"abstract break callback case cast catch class continue default do dynamic else enum extends extern "
"false final for from function here if implements import in inline interface macro never new null "
"operator overload override package private public return static super switch this throw to trace true try typedef "
"untyped using var while "

, // 1 preprocessor
"else elseif end error if "

, // 2 class
"Any Array Bool Class Date Dynamic EReg Enum EnumValue Exception Float GenericStack HashMap "
"Int Int32 Int64 IntIterator IntMap Iterable Iterator Json Lambda List Map Math Null ObjectMap Reflect Resource "
"Serializer Single Std String StringBuf StringMap Sys Template Timer Type UInt UnicodeString Unserializer Vector Void "
"WeakMap Xml "

, // 3 interface
"ArrayAccess "

, // 4 enumeration
"Option ValueType XmlType "

, // 5 constant
NULL

, // 6 metadata
NULL

, // 7 function
NULL

, // 8 comment tag
"see "

, NULL, NULL, NULL, NULL, NULL, NULL
//--Autogenerated -- end of section automatically generated

, // 15 Code Snippet
"for^() if^() switch^() while^() else^if^() else^{} "
}};

static EDITSTYLE Styles_Haxe[] = {
	EDITSTYLE_DEFAULT,
	{ SCE_HAXE_WORD, NP2StyleX_Keyword, L"fore:#0000FF" },
	{ SCE_HAXE_PREPROCESSOR, NP2StyleX_Preprocessor, L"fore:#FF8000" },
	{ SCE_HAXE_CLASS, NP2StyleX_Class, L"fore:#0080FF" },
	{ SCE_HAXE_INTERFACE, NP2StyleX_Interface, L"bold; fore:#1E90FF" },
	{ SCE_HAXE_ENUM, NP2StyleX_Enumeration, L"fore:#FF8000" },
	{ SCE_HAXE_MATADATA, NP2StyleX_Metadata, L"fore:#FF8000" },
	{ SCE_HAXE_FUNCTION_DEFINITION, NP2StyleX_FunctionDefinition, L"bold; fore:#A46000" },
	{ SCE_HAXE_FUNCTION, NP2StyleX_Function, L"fore:#A46000" },
	{ SCE_HAXE_CONSTANT, NP2StyleX_Constant, L"fore:#B000B0" },
	{ MULTI_STYLE(SCE_HAXE_COMMENTLINE, SCE_HAXE_COMMENTBLOCK, 0, 0), NP2StyleX_Comment, L"fore:#608060" },
	{ MULTI_STYLE(SCE_HAXE_COMMENTLINEDOC, SCE_HAXE_COMMENTBLOCKDOC, 0, 0), NP2StyleX_DocComment, L"fore:#408040" },
	{ SCE_HAXE_COMMENTTAGAT, NP2StyleX_DocCommentTag, L"fore:#408080" },
	{ SCE_HAXE_TASKMARKER, NP2StyleX_TaskMarker, L"bold; fore:#408080" },
	{ MULTI_STYLE(SCE_HAXE_STRINGDQ, SCE_HAXE_STRINGSQ, 0, 0), NP2StyleX_String, L"fore:#008000" },
	{ SCE_HAXE_ESCAPECHAR, NP2StyleX_EscapeSequence, L"fore:#0080C0" },
	{ SCE_HAXE_REGEX, NP2StyleX_Regex, L"fore:#006633; back:#FFF1A8" },
	{ SCE_HAXE_NUMBER, NP2StyleX_Number, L"fore:#FF0000" },
	{ MULTI_STYLE(SCE_HAXE_VARIABLE, SCE_HAXE_VARIABLE2, 0, 0), NP2StyleX_Variable, L"fore:#9E4D2A" },
	{ MULTI_STYLE(SCE_HAXE_OPERATOR, SCE_HAXE_OPERATOR2, 0, 0), NP2StyleX_Operator, L"fore:#B000B0" },
};

EDITLEXER lexHaxe = {
	SCLEX_HAXE, NP2LEX_HAXE,
//Settings++Autogenerated -- start of section automatically generated
	{
		LexerAttr_Default,
		TAB_WIDTH_4, INDENT_WIDTH_4,
		(1 << 0) | (1 << 1), // class, method
		SCE_HAXE_FUNCTION_DEFINITION,
		0, '\\', SCE_HAXE_ESCAPECHAR,
		0
		, KeywordAttr32(0, KeywordAttr_PreSorted) // keywords
		| KeywordAttr32(1, KeywordAttr_PreSorted | KeywordAttr_NoAutoComp) // preprocessor
		| KeywordAttr32(2, KeywordAttr_PreSorted) // class
		| KeywordAttr32(3, KeywordAttr_PreSorted) // interface
		| KeywordAttr32(4, KeywordAttr_PreSorted) // enumeration
		| KeywordAttr64(8, KeywordAttr_NoLexer | KeywordAttr_NoAutoComp) // comment tag
	},
//Settings--Autogenerated -- end of section automatically generated
	EDITLEXER_HOLE(L"Haxe Script", Styles_Haxe),
	L"hx",
	&Keywords_Haxe,
	Styles_Haxe
};
