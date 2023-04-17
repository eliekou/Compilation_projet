class Visitor:
    def visit_main_class():
        pass
    def visit_class():
        pass
    def visit_method():
        pass
    def visit_var():
        pass
    def visit_type():
        pass
    def visit_binary_expression():
        pass
    def visit_new_expression():
        pass
    def visit_expression_length():
        pass
    def visit_identifier():
        pass
    def visit_bool_expression():
        pass
    def visit_countery_expression():
        pass
    def visit_simple_expression():
        pass
    def visit_this_expression():
        pass
    def visit_array_expression():
        pass
    def visit_method_call():
        pass
    def visit_statement():
        pass
    def visit_if_statement():
        pass
    def visit_while_statement():
        pass
    def visit_print_statement():
        pass
    def visit_assign_statement():
        pass
    def visit_array_assign_statement():
        pass
class PrettyPrinter(Visitor):
    def visit_program(self, program):
        print("class " + program.main_class.name + " {\n public static void main (String[] " + program.main_class.arg + ") {\n" )
    def visit_main_class(self, main_class):
        print("class " + main_class.name + " {\n public static void main (String[] " + main_class.arg + ") {\n" + \
               "    " + main_class.body)
    def visit_class(self, class_):
        print("class " + class_.name + " {\n" + \
               "  " + class_.body + \
               "}\n")
    def visit_method(self, method):
        return "public " + method.type + " " + method.name + "(" + method.args + ") {\n" + \
               "  " + method.body + \
               "}\n"
    def visit_var(self, var):
        return var.type + " " + var.name + ";\n"
    def visit_type(self, type_):
        return type_.name
    def visit_binary_expression(self, binary_expression):
        return binary_expression.left + " " + binary_expression.op + " " + binary_expression.right
    def visit_new_expression(self, new_expression):
        return "new " + new_expression.name + "()"
    def visit_expression_length(self, expression_length):
        return expression_length.name + ".length"
    def visit_identifier(self, identifier):
        return identifier.name
    def visit_bool_expression(self, bool_expression):
        return str(bool_expression.value)
