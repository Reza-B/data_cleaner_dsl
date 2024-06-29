grammar DataCleaner;

start: program EOF;

program: loadStatement statement*;

statement
    : removeRowsMissingStatement
    | fillMissingStatement
    | normalizeStatement
    | standardizeStatement
    | logTransformStatement
    | autoCategorizeStatement
    | splitDataStatement
    | removeDuplicateStatement
    | dropRowStatement
    | dropColumnStatement
    | integrateInconsistentData
    | encodingStatement
    | handleOutliersStatement
    ;

// Statements
loadStatement: 'load' path ;
removeRowsMissingStatement: 'remove_rows_missing' column ;
fillMissingStatement: 'fill_missing' column 'with' fillMethod ;
normalizeStatement: 'normalize' column 'to_range(' min_val ',' max_val ')' ;
standardizeStatement: 'standardize' column ;
logTransformStatement: 'log_transform' column ;
autoCategorizeStatement: 'auto_categorize' column 'n_clusters=' number ;
splitDataStatement: 'split_data' 'train=' number ',' 'validate=' number ',' 'test=' number ;
// new Statements
removeDuplicateStatement: 'remove_duplicates';
dropRowStatement: 'drop_row'  (row )* | ('from' row 'to' row ('exclude' row+)?);
dropColumnStatement: 'drop_column' column+;
integrateInconsistentData: 'integrate' option+ 'to' option 'in' column;
encodingStatement: 'encode' (column+ | 'all' | 'exclude' column+)  'with' method;
handleOutliersStatement: 'delete_outliers' (column+ | 'all' | 'exclude' column+) 'with' method;

// Options
path returns[rule_type="str()"]: STRING;
min_val returns[rule_type="id()"]: NUMBER;
max_val returns[rule_type="id()"]: NUMBER;
column returns[rule_type="id()"]: ID;
option returns[rule_type="id()"]: ID;
row returns[rule_type="int()"]: NUMBER;
method returns[rule_type="id()"]: ID;
number returns[rule_type="int()"]: NUMBER;
fillMethod returns[rule_type="str()"]: 'mean' | 'median' | 'mode';

// Tokens
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+;
STRING: '"' .*? '"' ;
WS: [ \t\r]+ -> skip ;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;
COMMENT: '//' ~[\r\n]* -> skip ;